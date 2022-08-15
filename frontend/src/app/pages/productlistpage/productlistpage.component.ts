import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ProductsService } from 'src/app/services/products.service';
import { CartService } from 'src/app/services/cart.service';

@Component({
  selector: 'app-productlistpage',
  templateUrl: './productlistpage.component.html',
  providers: [ProductsService],
  styleUrls: ['./productlistpage.component.css']
})
export class ProductlistpageComponent implements OnInit {

  quantity : number | undefined;
  constructor(private param:ActivatedRoute, private service:ProductsService, 
    private route: ActivatedRoute, private cartService: CartService, private router: Router) { }
  getProductId:any;
  productData:any;

  ngOnInit() {
    this.getProductId = this.param.snapshot.paramMap.get('id');
    this.loadproduct(this.getProductId);
  }

  loadproduct(id: any) {
    return this.service.getProduct(id).subscribe((data: {}) => {
      this.productData = data;
      console.log(this.productData)
    });
  }

  addToCart() {
    let data = {
      product: this.productData.id,
      quantity: this.quantity
    };
    console.log(data);
    this.cartService.addToCart(localStorage.getItem("customerId"), data).subscribe(
      (response) => {
        console.log(response);
        this.router.navigate(['/cart']);
      },
      (error) =>{
        console.error(error);
      })
  }

 

  // addItemToCart() {
  //   this.cartService.addItemToCart(this.productData.id, this.quantity);
  // }

  // incrementQuantity() {
  //   this.quantity++;
  // }

  // decrementQuantity() {
  //   if (this.quantity > 1) {
  //   this.quantity--;
  //   }
  // }
}


