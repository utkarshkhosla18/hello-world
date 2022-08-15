import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ProductsService } from 'src/app/services/products.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  providers: [ProductsService ],
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  
  constructor(private ProductsService:ProductsService, private router: Router) { }
  productData:any;
  
  ngOnInit() {
    this.loadproducts();
  }

  loadproducts() {
    return this.ProductsService.getProducts().subscribe((data: {}) => {
      this.productData = data;
      console.log(this.productData)
    });
  }

}
