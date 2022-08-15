import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-admin-products-list',
  templateUrl: './admin-products-list.component.html',
  styleUrls: ['./admin-products-list.component.css']
})
export class AdminProductsListComponent implements OnInit {

  constructor() { }
  products = [{
    "item":"1",
    "orderno":"1234",
    "ppu":"1",
    "quantity":"5",
    "price":"5",
    "farmer":"Agri"
  },
    {
    "item":"2",
    "orderno":"1235",
    "ppu":"5",
    "quantity":"5",
    "price":"25",
    "farmer":"Agri"
  },
    {
    "item":"3",
    "orderno":"1236",
    "ppu":"10",
    "quantity":"5",
    "price":"50",
    "farmer":"Agri"
  },
    {
    "item":"4",
    "orderno":"1237",
    "ppu":"15",
    "quantity":"10",
    "price":"150",
    "farmer":"Agri"
  },
    {
    "item":"5",
    "orderno":"1238",
    "ppu":"20",
    "quantity":"5",
    "price":"100",
    "farmer":"Agri"
  }];
  ngOnInit(): void {
  }

}
