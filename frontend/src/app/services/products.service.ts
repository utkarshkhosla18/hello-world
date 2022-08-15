import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { ProductDetails } from '../shared/products';

@Injectable({providedIn: 'root'})

export class ProductsService {
  [x: string]: any;

  private baseURL = 'http://127.0.0.1:8000/api';
  constructor(private http: HttpClient) { }
  httpOptions = {
    headers: new HttpHeaders({'Content-Type': 'application/json',}),
  };

  getProducts(): Observable<ProductDetails> {
    return this.http.get<ProductDetails>(this.baseURL + '/product');
  }

  getProduct(id: any): Observable<ProductDetails> {
    return this.http.get<ProductDetails>(this.baseURL + '/product/' + id);
      // .pipe(retry(1), catchError(this.handleError));
  }

  searchProducts(str: string): Observable<ProductDetails> {
    return this.http.get<ProductDetails>(this.baseURL + '/product/' + str);
  }
}
