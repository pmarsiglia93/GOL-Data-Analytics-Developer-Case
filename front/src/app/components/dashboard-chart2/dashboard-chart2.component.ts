import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgChartsModule } from 'ng2-charts'; // ADICIONE ESTA LINHA

@Component({
  selector: 'app-dashboard-chart2',
  templateUrl: './dashboard-chart2.component.html',
  styleUrls: ['./dashboard-chart2.component.css'],
  standalone: true,
  imports: [NgChartsModule],
})
export class DashboardChart2Component implements OnInit {
  public barChartLabels: string[] = [];
  public barChartData: any[] = [];
  public barChartOptions = { responsive: true, indexAxis: 'x' };
  public barChartType: any = 'bar';

  constructor(private http: HttpClient) {}

  private formatDateLabel(date: string): string {
    // Converte "2025-06-01" para "01-06"
    const [year, month, day] = date.split('-');
    return `${day}-${month}`;
  }

  ngOnInit() {
    this.http
      .get<any>('http://localhost:8000/api/v1/dashboard/chart/data/2')
      .subscribe((res) => {
        this.barChartLabels = res.data.map((d: any) => d.category);
        this.barChartData = [
          {
            label: 'Reservas por Data de Chegada',
            data: res.data.map((d: any) => d.value),
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
          },
        ];
      });
  }
}
