import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UserDetail } from '../data-types/user-details';
import { Observable } from 'rxjs';
import { map, catchError} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class RegisterService {
  baseURL = 'http://127.0.0.1:8000/api'
  constructor(private http: HttpClient) { }

  getFarmer(): Observable<any> {
    return this.http.get(this.baseURL + '/farmer')
  }
  getAdmin(): Observable<any> {
    return this.http.get(this.baseURL + '/admin')
  }
  getCustomer(): Observable<any> {
    return this.http.get(this.baseURL + '/customer')
  }
  
  registerUser(User:UserDetail): Observable<any> {
    const headers = { 'content-type': 'application/json'}  
    const body=JSON.stringify(User);
    console.log(body)
    return this.http.post(this.baseURL + '/register', body,{'headers':headers})
  }
}
