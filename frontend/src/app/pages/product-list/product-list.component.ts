import { Component, OnInit } from '@angular/core';
// import { Router } from '@angular/router';
// import { ActivatedRoute } from '@angular/router';
import { ProductsService } from 'src/app/services/products.service';
// import { CartService } from 'src/app/services/cart.service';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  providers: [ProductsService],
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  constructor(private ProductsService:ProductsService) { }
  productData:any;
  input:string;

  ngOnInit() {
    this.loadproducts();
  }

  loadproducts() {
    return this.ProductsService.getProducts().subscribe((data: {}) => {
      this.productData = data;
      console.log(this.productData)
    });
  }

  searchProducts() {
    return this.ProductsService.searchProducts(this.input).subscribe((data: {}) => {
      this.productData = data;
      console.log(this.productData)
    });
  }
}
