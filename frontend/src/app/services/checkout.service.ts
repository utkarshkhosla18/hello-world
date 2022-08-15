import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CheckoutService {
  private baseURL = 'http://127.0.0.1:8000/api/customer/';
  constructor(private http: HttpClient) { }
  postTocheck(str : string | null) : Observable<any> {
    // let price = + str
    console.log(str)
    let data = {'total': str,
                'currency': 'GBP'}
    console.log(data)
    return this.http.post(this.baseURL + "paypal", data);
  }
}
