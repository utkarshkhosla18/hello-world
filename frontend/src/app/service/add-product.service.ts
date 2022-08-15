import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AddProductService {
baseURL = 'http://127.0.0.1:8000/api/farmer/'
  constructor(private http:HttpClient) { }

  addProduct(farmerId, data): Observable<any> {
    const headers = { 'content-type': 'application/json'} 
    return this.http.post(this.baseURL + farmerId + "/product" ,data,{'headers':headers});
  }

  addProductList(farmerId, data): Observable<any> {
    const headers = { 'content-type': 'application/json'} 
    return this.http.post(this.baseURL + farmerId + "/product" ,data,{'headers':headers});
  }
    
}
