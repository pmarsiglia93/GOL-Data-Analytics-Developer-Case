// src/app/services/test.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class TestService {
  private apiUrl = `${environment.apiUrl}/api/v1/booking`;

  constructor(private http: HttpClient) {}

  getBookings() {
    return this.http.get(this.apiUrl);
  }
}
