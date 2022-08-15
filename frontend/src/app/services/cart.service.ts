import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { ProductDetails } from '../shared/products';
import { ICart, ICartItem } from '../shared/cart';

@Injectable({ providedIn: 'root' }) 

export class CartService {
  private baseURL = 'http://127.0.0.1:8000/api/customer/';
//   items: ProductDetails[] = [];
//   private cartSource = new BehaviorSubject<ICart>(null);
//   cart$ = this.cartSource.asObservable();
//   private cartTotalSource = new BehaviorSubject<ICartTotal>(null);
//   cartTotal$ = this.cartTotalSource.asObservable();

//   customerId=7;
  constructor(private http: HttpClient) { }
  addToCart(customerId: string | null, data: any): Observable<any> {
    // console.log(data)
    // let customer = parseInt(customerId)
    let newdata = {
        customer: Number(customerId),
        product: data.product,
        quantity: Number(data.quantity)
    }
    console.log(newdata)
    return this.http.post(this.baseURL+ customerId + "/cart" ,newdata);
  }


  getCarts(id: string | null) : Observable<any> {
    return this.http.get(this.baseURL+ id + "/cart");
  }

  deleteCart(customerId: number, cartId:number): Observable<any> {
    // console.log(data)
    return this.http.delete(this.baseURL + customerId+ "/cart/" + cartId)
  }
//   httpOptions = {headers: new HttpHeaders({'Content-Type': 'application/json',}),};

//   addItemToCart(product: ProductDetails) {
//     this.items.push(product);
//   }

//   getItems() {
//     return this.items;
//   }

//   clearCart() {
//     this.items = [];
//     return this.items;
//   }}





//   addItemToCart(item: ProductDetails, quantity = 1){
//     const itemToAdd: ICartItem = this.mapProductToCartItem(item, quantity);
//     const cart = this.getCurrentCartValue() ?? this.createCart();
//     cart.items = this.addOrUpdateItem(cart.items, itemToAdd, quantity);
//     this.setCart(cart);
//   }
//   getCurrentCartValue() {
//     return this.cartSource.value;
//   }
//   setCart(basket: ICart) {
//     return this.http.post(this.baseURL + '/customer/' + 7 + '/cart', basket)
//       .subscribe((response: ICart) => {
//         // This will update the BehaviorSubject withnew value
//         this.cartSource.next(response);
//         this.calculateTotals();
//       }, (error) => console.log(error));
//   }
//   incrementItemQuantity(item: ICartItem) {
//     const cart = this.getCurrentCartValue();
//     const foundItemIndex = cart.items.findIndex(x => x.product === item.product);
//     cart.items[foundItemIndex].quantity++;
//     this.setCart(cart);
//   }

//   decrementItemQuantity(item: ICartItem) {
//     const cart = this.getCurrentCartValue();
//     const foundItemIndex = cart.items.findIndex(x => x.product === item.product);
//     if (cart.items[foundItemIndex].quantity > 1) {
//       cart.items[foundItemIndex].quantity--;
//       this.setCart(cart);
//     } else {
//       this.removeItemFromCart(item);
//     }
//   }
//   removeItemFromCart(item: ICartItem) {
//     const cart = this.getCurrentCartValue();
//     if (cart.items.some(x => x.product === item.product)) {
//       cart.items = cart.items.filter(x => x.product !== item.product)
//       if (cart.items.length > 0) {
//         this.setCart(cart);
//       } else {
//         this.deleteCart(cart);
//       }
//     }
//   }
//   deleteCart(basket: ICart) {
//     return this.http.delete(this.baseURL + '/customer/' + 7 + '/cart').subscribe (() => {
//       this.cartSource.next(null);
//       this.cartTotalSource.next(null);
//     //   localStorage.removeItem('basket_id');
//     }, error => {
//       console.log(error);
//     });
//   }

//   private calculateTotals() {
//     const cart = this.getCurrentCartValue();
//     const total = cart.items.reduce((a, b) => ((+b.price)* b.quantity) + a, 0);
//     this.cartTotalSource.next({total});
//   }
//   private addOrUpdateItem(items: ICartItem[], itemToAdd: ICartItem, quantity: number): ICartItem[] {
//     const index = items.findIndex(i => i.product === itemToAdd.product);
//     if (index === -1) {
//       itemToAdd.quantity = quantity;
//       items.push(itemToAdd);
//     } else {
//       items[index].quantity += quantity;
//     }
//     return items;
//   }
//   private createCart(): ICart {
//     const cart = new Cart();
//     // localStorage.setItem('cart_id', cart.id);
//     return cart;
//   }
//   private mapProductToCartItem(item: ProductDetails, quantity: number): ICartItem {
//     return {
//       // customer: ,
//       product: item.id,
//       quantity,
//       price: item.price,
//       // name: item.name,
//       // price: item.price,
//       // image: item.image,
//       // quantity,
//       // category: item.category,
//     };
//   }
}








// //   items: Product[] = [];
// // /* . . . */

// //   addToCart(product: Product) {
// //     this.items.push(product);
// //   }

// //   getItems() {
// //     return this.items;
// //   }

// //   clearCart() {
// //     this.items = [];
// //     return this.items;
// //   }
// /* . . . */
// // }