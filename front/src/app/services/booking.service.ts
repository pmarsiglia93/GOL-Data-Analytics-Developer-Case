// src/app/services/booking.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable, map } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class BookingService {
  private apiUrl = `${environment.apiUrl}/booking`;

  constructor(private http: HttpClient) {}

  getAllBookings(): Observable<any[]> {
    return this.http.get<any>(this.apiUrl).pipe(
      map(response => response.data)
    );
  }

  createBooking(booking: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, booking);
  }

  uploadBookings(formData: FormData): Observable<any> {
    return this.http.post(`${this.apiUrl}/file/upload`, formData);
  }

  downloadBookings(): Observable<Blob> {
    return this.http.get(`${this.apiUrl}/file/download`, { responseType: 'blob' });
  }
}
