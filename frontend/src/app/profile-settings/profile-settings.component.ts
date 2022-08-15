import { Component, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';
import { of } from 'rxjs';
import {ProfileService} from '../service/profile.service';
@Component({
  selector: 'app-profile-settings',
  templateUrl: './profile-settings.component.html',
  styleUrls: ['./profile-settings.component.css']
})
export class ProfileSettingsComponent implements OnInit {
  UserProfile: FormGroup;
   name: string;
   profileName: string;
   profileEmail: string;
   profileMobileNo: string;
   profilePassword: string;
   profileNewPassword: string;
   profileChangePassword: string;
   changePasswordClicked : boolean = false;

   @ViewChild('f') form: any;

   //password:FormControl;

  constructor(private profileService : ProfileService) { }

  ngOnInit(): void {
    this.getProfileData();

  }

  getProfileData(){
    if(localStorage.getItem('farmerId')){
      this.profileService.getFarmerProfile()
    .subscribe((response) => {
      this.profileName = response.username;
      this.profileEmail = response.email;
      this.profileMobileNo=response.mobileNumber;


    },(error) => {
      console.log()
    });
    } else if(localStorage.getItem('adminId')){
        this.profileService.getAdminProfile()
      .subscribe((response) => {
        this.profileName = response.username;
        this.profileEmail = response.email;
        this.profileMobileNo=response.mobileNumber;


      },(error) => {
        console.log()
      });
    } else if(localStorage.getItem('customerId')){
      this.profileService.getCustomerProfile()
      .subscribe((response) => {
        this.profileName = response.username;
        this.profileEmail = response.email;
        this.profileMobileNo=response.mobileNumber;


      },(error) => {
        console.log()
      });
    }
    
    

  }

  changePassword(){
    this.changePasswordClicked = true;
    console.log("Change Password method called");
  }
  
  saveChanges(){
    let userPassword = this.profilePassword;
    if(this.changePasswordClicked){
      if(this.profileNewPassword != this.profileChangePassword){
        console.log("password is not matching");
        return;
      }
      userPassword = this.profileNewPassword;
    }
    let userId: String = localStorage.getItem('farmerId') ? localStorage.getItem('farmerId') : 
    localStorage.getItem('adminId') ? localStorage.getItem('adminId') : localStorage.getItem('customerId');
    
    let outputObj = {
      username: this.profileName,
      password: userPassword,
      id:userId,
      email: this.profileEmail,
      mobile: this.profileMobileNo
    }
    if(localStorage.getItem('farmerId')){
      this.profileService.updateFarmerProfile(outputObj)
    .subscribe((response) => {

    })
    } else if(localStorage.getItem('customerId')){
      this.profileService.updateFarmerProfile(outputObj)
    .subscribe((response) => {

    })
    } else if(localStorage.getItem('adminId')){
      this.profileService.updateFarmerProfile(outputObj)
    .subscribe((response) => {

    })
  }
    

    console.log("changes saved successfully");
  }


}

