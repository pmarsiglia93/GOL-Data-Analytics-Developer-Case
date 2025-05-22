// src/app/components/booking-form/booking-form.component.ts

import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { BookingService } from '../../services/booking.service';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-booking-form',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule
  ],
  template: `
    <div class="booking-form-container">
      <h2>Nova Reserva</h2>
      <form [formGroup]="bookingForm" (ngSubmit)="onSubmit()">
        <mat-form-field appearance="fill">
          <mat-label>Primeiro Nome</mat-label>
          <input matInput formControlName="first_name">
        </mat-form-field>

        <mat-form-field appearance="fill">
          <mat-label>Último Nome</mat-label>
          <input matInput formControlName="last_name">
        </mat-form-field>

        <mat-form-field appearance="fill">
          <mat-label>Data de Nascimento</mat-label>
          <input matInput type="date" formControlName="birthday">
        </mat-form-field>

        <mat-form-field appearance="fill">
          <mat-label>Documento</mat-label>
          <input matInput formControlName="document">
        </mat-form-field>

        <mat-form-field appearance="fill">
          <mat-label>Data de Partida</mat-label>
          <input matInput type="date" formControlName="departure_date">
        </mat-form-field>

        <mat-form-field appearance="fill">
          <mat-label>Data de Chegada</mat-label>
          <input matInput type="date" formControlName="arrival_date">
        </mat-form-field>

        <mat-form-field appearance="fill">
          <mat-label>Origem (IATA)</mat-label>
          <input matInput formControlName="departure_iata" maxlength="3">
        </mat-form-field>

        <mat-form-field appearance="fill">
          <mat-label>Destino (IATA)</mat-label>
          <input matInput formControlName="arrival_iata" maxlength="3">
        </mat-form-field>

        <button mat-raised-button color="primary" type="submit" [disabled]="bookingForm.invalid">Cadastrar Reserva</button>
      </form>
    </div>
  `,
  styles: [`
    .booking-form-container {
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 8px;
      background-color: #f4f4f4;
      margin: 20px;
      max-width: 600px;
    }

    mat-form-field {
      width: 100%;
      margin-bottom: 15px;
    }

    button {
      width: 100%;
    }
  `]
})
export class BookingFormComponent {
  bookingForm: FormGroup;

  constructor(private fb: FormBuilder, private bookingService: BookingService) {
    this.bookingForm = this.fb.group({
      first_name: ['', [Validators.required, Validators.pattern(/^[a-zA-Z\s]+$/)]],
      last_name: ['', [Validators.required, Validators.pattern(/^[a-zA-Z\s]+$/)]],
      birthday: ['', Validators.required],  // Adicionando o campo birthday
      document: ['', [Validators.required, Validators.pattern(/^\d+$/)]],
      departure_date: ['', Validators.required],
      arrival_date: ['', Validators.required],
      departure_iata: ['', [Validators.required, Validators.pattern(/^[A-Z]{3}$/)]],
      arrival_iata: ['', [Validators.required, Validators.pattern(/^[A-Z]{3}$/)]],
    });
  }

  onSubmit(): void {
    if (this.bookingForm.valid) {
      const bookingData = {
        first_name: this.bookingForm.value.first_name.trim(),
        last_name: this.bookingForm.value.last_name.trim(),
        birthday: this.bookingForm.value.birthday, // já está no formato correto
        document: this.bookingForm.value.document.trim(),
        departure_date: this.bookingForm.value.departure_date, // já está ok
        arrival_date: this.bookingForm.value.arrival_date, // já está ok
        departure_iata: this.bookingForm.value.departure_iata.trim().toUpperCase(),
        arrival_iata: this.bookingForm.value.arrival_iata.trim().toUpperCase(),
      };

      console.log('Enviando dados para a API:', bookingData);

      this.bookingService.createBooking(bookingData).subscribe(
        response => {
          console.log('Reserva criada com sucesso!', response);
          this.bookingForm.reset();
        },
        error => console.error('Erro ao criar reserva:', error)
      );
    }
  }


  private formatDate(date: string): string {
    const parsedDate = new Date(date);
    const year = parsedDate.getFullYear();
    const month = String(parsedDate.getMonth() + 1).padStart(2, '0');
    const day = String(parsedDate.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
  }
}
