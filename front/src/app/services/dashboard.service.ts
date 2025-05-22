import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class DashboardService {
  private apiUrl = `${environment.apiUrl}/dashboard`;

  constructor(private http: HttpClient) {}

  getChartData(type: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/chart/data/${type}`);
  }

  getTableData(): Observable<any> {
    return this.http.get(`${this.apiUrl}/data`);
  }
}
