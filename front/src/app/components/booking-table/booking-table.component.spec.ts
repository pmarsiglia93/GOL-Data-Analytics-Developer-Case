import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BookingTableComponent } from './booking-table.component';

describe('BookingTableComponent', () => {
  let component: BookingTableComponent;
  let fixture: ComponentFixture<BookingTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BookingTableComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BookingTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
