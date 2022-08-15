import { TestBed } from '@angular/core/testing';

import { FarmerHomeService } from './farmer-home.service';

describe('FarmerHomeService', () => {
  let service: FarmerHomeService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FarmerHomeService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
