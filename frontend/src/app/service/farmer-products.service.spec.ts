import { TestBed } from '@angular/core/testing';

import { FarmerProductsService } from './farmer-products.service';

describe('FarmerProductsService', () => {
  let service: FarmerProductsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FarmerProductsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
