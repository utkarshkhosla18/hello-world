import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import {ProductDetails} from './product';

@Injectable({
  providedIn: 'root'
})
export class FarmerHomeService {


  baseURL = 'http://127.0.0.1:8000/api/farmer/'
  constructor(private http:HttpClient) { }
  // getProduct(): Observable<any> {
     
  //   return this.http.get(this.baseURL + '/product/' + localStorage.getItem('farmerId'));
  // }
  getProducts(farmerId: string | null): Observable<ProductDetails> {
    return this.http.get<ProductDetails>(this.baseURL + farmerId + '/product');
  }

  deleteProduct(productId : number): Observable<any> {
    return this.http.delete('http://127.0.0.1:8000/api/product/' + productId)
  }


 
}
