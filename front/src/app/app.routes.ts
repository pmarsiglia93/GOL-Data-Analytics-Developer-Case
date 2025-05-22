import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { BookingTableComponent } from './components/booking-table/booking-table.component';
import { BookingFormComponent } from './components/booking-form/booking-form.component';
import { FileUploadComponent } from './components/file-upload/file-upload.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'booking', component: BookingTableComponent },
  { path: 'new-booking', component: BookingFormComponent },
  { path: 'upload', component: FileUploadComponent },
  { path: 'dashboard', component: DashboardComponent },
  { path: '**', redirectTo: '' }
];
