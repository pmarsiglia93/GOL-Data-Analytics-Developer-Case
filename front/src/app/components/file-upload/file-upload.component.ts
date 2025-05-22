// src/app/components/file-upload/file-upload.component.ts

import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { BookingService } from '../../services/booking.service';

@Component({
  selector: 'app-file-upload',
  standalone: true,
  imports: [CommonModule, MatButtonModule],
  template: `
    <div class="file-upload-container">
      <h2>Upload de Reservas</h2>
      <input type="file" accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" (change)="onFileSelected($event)">
      <button mat-raised-button color="primary" (click)="onUpload()">Upload de Reservas</button>
      <button mat-raised-button color="accent" (click)="onDownload()">Download de Reservas</button>
    </div>
  `,
  styles: [`
    .file-upload-container {
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 8px;
      background-color: #f4f4f4;
      margin: 20px;
      max-width: 600px;
    }

    button {
      margin-top: 15px;
      width: 100%;
    }
  `]
})
export class FileUploadComponent {
  selectedFile: File | null = null;

  constructor(private bookingService: BookingService) {}

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files[0]) {
      this.selectedFile = input.files[0];
      this.onUpload();
    }
  }

  onUpload(): void {
    if (this.selectedFile) {
      const formData = new FormData();
      formData.append('file', this.selectedFile);

      this.bookingService.uploadBookings(formData).subscribe(
        response => {
          console.log('Upload realizado com sucesso!', response);
          alert('Upload realizado com sucesso!');
        },
        error => console.error('Erro ao fazer upload:', error)
      );
    }
  }



  onDownload(): void {
    this.bookingService.downloadBookings().subscribe(
      (blob) => {
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'booking.xlsx';  // Ajustar extensão!
        link.click();
        window.URL.revokeObjectURL(url);
      },
      error => console.error('Erro ao fazer download:', error)
    );
  }

}
