// src/app/components/booking-table/booking-table.component.ts

import { Component, OnInit, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { MatTableModule } from '@angular/material/table';
import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';
import { MatSort, MatSortModule } from '@angular/material/sort';
import { MatInputModule } from '@angular/material/input';
import { MatTableDataSource } from '@angular/material/table';
import { BookingService } from '../../services/booking.service';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-booking-table',
  standalone: true,
  imports: [
    CommonModule,
    HttpClientModule,
    MatTableModule,
    MatPaginatorModule,
    MatSortModule,
    MatInputModule,
    MatFormFieldModule,
    MatButtonModule
  ],
  template: `
    <div class="booking-table-container">
      <h2>Reservas</h2>

      <mat-form-field class="filter">
        <input matInput (keyup)="applyFilter($event)" placeholder="Filtrar reservas">
      </mat-form-field>

      <table mat-table [dataSource]="dataSource" matSort class="mat-elevation-z8">
        <ng-container matColumnDef="id">
          <th mat-header-cell *matHeaderCellDef mat-sort-header>ID</th>
          <td mat-cell *matCellDef="let booking">{{ booking.id }}</td>
        </ng-container>

        <ng-container matColumnDef="passenger">
          <th mat-header-cell *matHeaderCellDef mat-sort-header>Passageiro</th>
          <td mat-cell *matCellDef="let booking">{{ booking.first_name }} {{ booking.last_name }}</td>
        </ng-container>

        <ng-container matColumnDef="document">
          <th mat-header-cell *matHeaderCellDef mat-sort-header>Documento</th>
          <td mat-cell *matCellDef="let booking">{{ booking.document }}</td>
        </ng-container>

        <ng-container matColumnDef="departure_date">
          <th mat-header-cell *matHeaderCellDef mat-sort-header>Data de Partida</th>
          <td mat-cell *matCellDef="let booking">{{ booking.departure_date | date: 'dd-MM-yyyy' }}</td>
        </ng-container>

        <ng-container matColumnDef="arrival_date">
          <th mat-header-cell *matHeaderCellDef mat-sort-header>Data de Chegada</th>
          <td mat-cell *matCellDef="let booking">{{ booking.arrival_date | date: 'dd-MM-yyyy' }}</td>
        </ng-container>

        <ng-container matColumnDef="departure_iata">
          <th mat-header-cell *matHeaderCellDef mat-sort-header>Origem</th>
          <td mat-cell *matCellDef="let booking">{{ booking.departure_iata }}</td>
        </ng-container>

        <ng-container matColumnDef="arrival_iata">
          <th mat-header-cell *matHeaderCellDef mat-sort-header>Destino</th>
          <td mat-cell *matCellDef="let booking">{{ booking.arrival_iata }}</td>
        </ng-container>

        <tr mat-header-row *matHeaderRowDef="displayedColumns"></tr>
        <tr mat-row *matRowDef="let row; columns: displayedColumns;"></tr>
      </table>

      <mat-paginator [pageSizeOptions]="[5, 10, 20]" showFirstLastButtons></mat-paginator>
    </div>
  `,
  styles: [`
    .booking-table-container {
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 8px;
      background-color: #f4f4f4;
      margin: 20px;
    }

    mat-form-field {
      width: 100%;
      margin-bottom: 20px;
    }

    table {
      width: 100%;
      margin-top: 20px;
    }

    th {
      background-color: #333;
      color: #fff;
    }

    tr:nth-child(even) {
      background-color: #f9f9f9;
    }
  `]
})
export class BookingTableComponent implements OnInit {
  displayedColumns: string[] = ['id', 'passenger', 'document', 'departure_date', 'arrival_date', 'departure_iata', 'arrival_iata'];
  dataSource = new MatTableDataSource<any>([]);

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(private bookingService: BookingService) {}

  ngOnInit(): void {
    this.loadBookings();
  }

  loadBookings(): void {
    this.bookingService.getAllBookings().subscribe(
      (data: any[]) => {
        this.dataSource.data = data;
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;
      },
      (error: any) => console.error('Erro ao carregar reservas:', error)
    );
  }

  applyFilter(event: Event): void {
    const filterValue = (event.target as HTMLInputElement).value.trim().toLowerCase();
    this.dataSource.filter = filterValue;
  }
}
