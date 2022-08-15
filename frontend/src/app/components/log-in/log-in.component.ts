import { Component, OnInit } from '@angular/core';
import { LoginDetails } from "../../data-types//login-details";
import{LoginService} from "../../service/login.service"
import { ViewChild } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css'],
  providers: [LoginService]
})
export class LogInComponent implements OnInit {
  public showPassword: boolean = false;
  userType: any = ['admin', 'farmer', 'customer'];
  loginData: LoginDetails = {
   
    
    email: '',
    password: '',
    usertype: ''

  }
  constructor(private userLogin: LoginService,private router: Router) { }

  ngOnInit(): void {
  }
  loginUsers() {
    console.log(this.loginData);
    const userData = this.loginData;
    console.log(this.loginData);
   
   
    this.userLogin.login(this.loginData).subscribe(
      (response) => {
        console.log(response);
        if(response && response.id){
          alert("You are logged in ");
          if(response.usertype == "farmer"){
            localStorage.setItem("farmerId",response.id);
            localStorage.removeItem('customerId');
            localStorage.removeItem('adminId');
            this.router.navigate(['/farmershome']);
          } else if (response.usertype == "admin"){
            localStorage.setItem("adminId",response.id);
            localStorage.removeItem('customerId');
            localStorage.removeItem('farmerId');
            this.router.navigate(['/adminDashboard']);
          } else if(response.usertype == 'customer'){
            localStorage.setItem("customerId",response.id);
            localStorage.removeItem('adminId');
            localStorage.removeItem('farmerId');
            this.router.navigate(['/customerHome']);
          }
          
        }
        console.log(sessionStorage.getItem("farmerId"));
        
        if(response && response.usertype == "farmer" && (sessionStorage.getItem("farmerId")!= null)){
          
        }
        // else if(response && response.usertype == "farmer" && (sessionStorage.getItem("AdminId")!= null)
        // {
        //   this.router.navigate(['/adminDashboard']);
        // }

      }, 
      (error) =>{
        sessionStorage.removeItem("farmerId");
        console.error(error);
      })
  }

  public togglePasswordVisibility(): void {
    this.showPassword = !this.showPassword;
  }
  
}
