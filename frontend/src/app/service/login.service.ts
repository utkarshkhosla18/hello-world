import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { LoginDetails } from '../data-types/login-details';
import { Observable } from 'rxjs';
import { map, catchError} from 'rxjs/operators'
@Injectable({
  providedIn: 'root'
})
export class LoginService {
  baseURL = 'http://127.0.0.1:8000/api'
  constructor(private http: HttpClient) { }
  
  login(user:LoginDetails): Observable<any> {
    const headers = { 'content-type': 'application/json'}  
    const body=JSON.stringify(user);
    console.log(body)
    return this.http.post(this.baseURL + '/login', body,{'headers':headers})
  }
}
