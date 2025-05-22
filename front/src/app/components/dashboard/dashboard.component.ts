import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DashboardChart1Component } from '../dashboard-chart1/dashboard-chart1.component';
import { DashboardChart2Component } from '../dashboard-chart2/dashboard-chart2.component';
import { DashboardChart3Component } from '../dashboard-chart3/dashboard-chart3.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    CommonModule,
    DashboardChart1Component,
    DashboardChart2Component,
    DashboardChart3Component,
  ],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {

}
