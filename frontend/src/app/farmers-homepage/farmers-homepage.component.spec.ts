import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FarmersHomepageComponent } from './farmers-homepage.component';

describe('FarmersHomepageComponent', () => {
  let component: FarmersHomepageComponent;
  let fixture: ComponentFixture<FarmersHomepageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FarmersHomepageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FarmersHomepageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
