import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgChartsModule } from 'ng2-charts'; // ADICIONE ESTA LINHA

@Component({
  selector: 'app-dashboard-chart3',
  templateUrl: './dashboard-chart3.component.html',
  styleUrls: ['./dashboard-chart3.component.css'],
  standalone: true,
  imports: [NgChartsModule],
})
export class DashboardChart3Component implements OnInit {
  public barChartLabels: string[] = [];
  public barChartData: any[] = [];
  public barChartOptions = { responsive: true, indexAxis: 'y' }; // Barra horizontal
  public barChartType: any = 'bar';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http
      .get<any>('http://localhost:8000/api/v1/dashboard/chart/data/3')
      .subscribe((res) => {
        this.barChartLabels = res.data.map((d: any) => d.category);
        this.barChartData = [
          {
            label: 'Reservas por Rota (Origem-Destino)',
            data: res.data.map((d: any) => d.value),
            backgroundColor: 'rgba(255, 206, 86, 0.5)',
          },
        ];
      });
  }
}
