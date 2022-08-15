import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-admin-products-update',
  templateUrl: './admin-products-update.component.html',
  styleUrls: ['./admin-products-update.component.css']
})
export class AdminProductsUpdateComponent implements OnInit {

  constructor() { }
  products = [{
    "image":"",
    "price":45,
    "storage":3
  },
    {
    "image":"",
    "price":23,
    "storage":1
  },
    {
    "image":"",
    "price":212,
    "storage":2
  },
    {
    "image":"",
    "price":29,
    "storage":21
  },
    {
    "image":"",
    "price":32,
    "storage":65
  }];
  ngOnInit(): void {
  }

}
