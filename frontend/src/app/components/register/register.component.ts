import { Component, OnInit } from '@angular/core';
import { RegisterService } from "../../service/register.service";
import { UserDetail } from "../../data-types/user-details";
import { ViewChild } from '@angular/core';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
  providers: [RegisterService]
})

export class RegisterComponent implements OnInit {
  public showPassword: boolean = false;
  @ViewChild('f') form: any;
  userType: any = ['admin', 'farmer', 'customer'];
  userData: UserDetail = {
    username: '',
    password: '',
    email: '',
    usertype: ''

  }

  constructor(
    private userRegister: RegisterService
  ) { }

  ngOnInit() {

  }

  registerUsers() {
    console.log(this.userData);
    const userData = this.userData;
    console.log(userData);
    this.userRegister.registerUser(userData).subscribe(
      (response) => {
        console.log(response);
        if(response){
          alert("Welcome aboard ");
        }
      }, 
      (error) =>{
        console.error(error);
      })
  }
  public togglePasswordVisibility(): void {
    this.showPassword = !this.showPassword;
  }

}