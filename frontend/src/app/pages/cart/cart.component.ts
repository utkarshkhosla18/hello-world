import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { CartService } from 'src/app/services/cart.service';
import { ICart, ICartItem } from 'src/app/shared/cart';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {
  // cart$:Observable<ICart>;
  // cartTotals$: Observable<ICartTotal>;

  constructor(private param:ActivatedRoute, private CartService: CartService) { }
  // CartData: CartDetails = {
  //   customer: '',
  //   product: '',
  //   quantity: ''

  // }
  cartList:any;
  total_price=0;
  customerId: number;
  ngOnInit() {
      // this.cart$ = this.cartService.cart$;
      // this.cartTotals$ = this.cartService.cartTotal$;
      this.customerId = Number(localStorage.getItem("customerId"));
      this.loadCart(localStorage.getItem("customerId"))
    }


  loadCart(id: string | null) {
    return this.CartService.getCarts(id).subscribe((data: {}) => {
      var arr = Object.keys(data);
      console.log(arr.length)
      var obj = []
      let c_number = arr.length / 2;
      for(var i = 0; i < c_number; i++) {
        console.log((data as any)[i])
        let newdata = {'product' : (data as any)[i],
                        'cart': (data as any)[c_number+i]}
        obj.push(newdata)
        let p = (+(data as any)[i].price)
        let q = (+(data as any)[c_number+i].quantity)
        let pr = p * q
        this.total_price += pr
        // this.total_price += (+(data as any)[i].price) * (data as any)[c_number+i].quantity
      }
      // console.log(data.length)
      console.log(this.total_price)
      console.log(obj)
      this.cartList = obj;
      console.log(this.cartList)
      localStorage.setItem("total_price",String(this.total_price));
    });
  }

  deleteCart(cartId: number) {
    console.log(cartId)
    return this.CartService.deleteCart(this.customerId, cartId).subscribe(
    (response) => {
      // console.log(response)
      alert(response.info)
      // alert(response.info);
      this.loadCart(localStorage.getItem("customerId"))
    },
    (error) =>{
      console.log(error);
      // console.error(error);
    });
  }
    // removeBasketItem(item: ICartItem) {
    //   this.cartService.removeItemFromCart(item);
    // }
  
    // incrementItem(item: ICartItem) {
    //   this.cartService.incrementItemQuantity(item);
    // }
  
    // decrementItem(item: ICartItem) {
    //   this.cartService.decrementItemQuantity(item);
    // }

}
