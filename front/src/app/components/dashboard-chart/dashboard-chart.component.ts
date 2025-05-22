import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgChartsModule } from 'ng2-charts';
import { ChartConfiguration } from 'chart.js';

@Component({
  selector: 'app-dashboard-chart',
  standalone: true,
  imports: [CommonModule, NgChartsModule],
  templateUrl: './dashboard-chart.component.html',
  styleUrls: ['./dashboard-chart.component.css']
})
export class DashboardChartComponent {
  @Input() data: { label: string, value: number }[] = [];

  public barChartOptions: ChartConfiguration<'bar'>['options'] = {
    responsive: true,
    indexAxis: 'x'
  };

  public barChartType: 'bar' = 'bar'; // <- ESSA LINHA!

  public get barChartData() {
    return {
      labels: this.data.map(d => d.label),
      datasets: [{
        data: this.data.map(d => d.value),
        label: 'Valores'
      }]
    };
  }
}
