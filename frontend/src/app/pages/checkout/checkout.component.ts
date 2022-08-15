import { Component, OnInit } from '@angular/core';
import { CheckoutService } from 'src/app/services/checkout.service';

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.css']
})
export class CheckoutComponent implements OnInit {

  constructor(private CheckoutService: CheckoutService) { }
  url="";
  ngOnInit(): void {
    this.checkout(localStorage.getItem("total_price"))
  }

  checkout(str: string | null) {
    return this.CheckoutService.postTocheck(str).subscribe((data: string) => {
      console.log(data)
      console.log(typeof data)
      this.url = data
        
    });
  }
 
}
