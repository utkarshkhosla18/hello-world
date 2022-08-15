import { Component, OnInit } from '@angular/core';
import { NumberValueAccessor } from '@angular/forms';
import { Router } from '@angular/router';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  userLoggedIn: boolean = false;
  userType : String = '';
  ngOnInit(): void {
    
      this.userLoggedIn = localStorage.getItem('adminId') != null || localStorage.getItem('customerId') != null || localStorage.getItem('farmerId') != null;
      if(this.userLoggedIn){
        if(localStorage.getItem('farmerId') != null) this.userType = 'farmer'
        else if(localStorage.getItem('customerId') != null) this.userType = 'customer';
        else if (localStorage.getItem('adminId')) this.userType  = 'admin';
      }
      console.log(this.userType);
<<<<<<< HEAD
=======
    
>>>>>>> a81fb7c68c60516c9e86e091a95c1870a298814c
  }
constructor(private router: Router) { }
  
  title = 'FarmersMarket';
   isImageSaved: boolean = false;
    imageBase64: string = '';

    CreateBase64String(Inputfile: any) {
        if (Inputfile.target.files && Inputfile.target.files[0]) {
          const reader = new FileReader();
          reader.onload = (e: any) => {
            const image = new Image();
            image.src = e.target.result;
            image.onload = rs => {
              const imgBasePath = e.target.result;
              this.imageBase64 = imgBasePath;
              this.isImageSaved = true;
              console.log(imgBasePath);
            };
          };
          reader.readAsDataURL(Inputfile.target.files[0]);
        }
    }
    logOut():void{

      localStorage.removeItem('farmerId');
      localStorage.removeItem('customerId');
      localStorage.removeItem('adminId');
      
      alert("You have been signed out of the application");
      this.router.navigate(['/login']);
      
    }
    
}
