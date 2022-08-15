import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {
  baseURL = 'http://127.0.0.1:8000/api'
  constructor(private http: HttpClient) { }

  getFarmerProfile(): Observable<any> {
    return this.http.get(this.baseURL +'/farmer/' + localStorage.getItem('farmerId'));
  }

  updateFarmerProfile(obj): Observable<any> {

    return this.http.put(this.baseURL +'/farmer/' + localStorage.getItem('farmerId'),obj);
  }
  getCustomerProfile(): Observable<any> {
    return this.http.get(this.baseURL +'/customer/' + localStorage.getItem('customerId'));
  }

  updateCustomerProfile(obj): Observable<any> {

    return this.http.put(this.baseURL +'/customer/' + localStorage.getItem('customerId'),obj);
  }
  getAdminProfile(): Observable<any> {
    return this.http.get(this.baseURL +'/admin/' + localStorage.getItem('adminId'));
  }

  updatAdminProfile(obj): Observable<any> {

    return this.http.put(this.baseURL +'/admin/' + localStorage.getItem('adminId'),obj);
  }
}
