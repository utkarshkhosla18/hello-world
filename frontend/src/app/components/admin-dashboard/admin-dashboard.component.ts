import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-admin-dashboard',
  templateUrl: './admin-dashboard.component.html',
  styleUrls: ['./admin-dashboard.component.css']
})
export class AdminDashboardComponent implements OnInit {

  constructor() { }
  admins = [{
    "username":"Bowen Zhang",
    "password":"12345678",
    "email":"bzhang73@sheffield.ac.uk"
  },
    {
    "username":"Utkarsh khosla",
    "password":"987654",
    "email":"ukhosla1@sheffiled.ac.uk"
  },
    {
    "username":"Subashree Mahendra Selvakumar",
    "password":"8765432",
    "email":"smahendraselvakumar1@sheffield.ac.uk"
  },
    {
    "username":"Mian Kou ",
    "password":"567891",
    "email":"mkou1@sheffield.ac.uk"
  },
  {
    "username":"Chaoda Song ",
    "password":"3456781",
    "email":"csong1@sheffield.ac.uk"
  },
    {
    "username":"Ying Ouyang ",
    "password":"2345678",
    "email":"youyang1@sheffield.ac.uk"
  }]
  ngOnInit(): void {
  }

}
