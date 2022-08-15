import { Component, OnInit } from '@angular/core';
import {FarmerProductsService} from '../service/farmer-products.service';
import {FarmerHomeService} from '../service/farmer-home.service';
@Component({
  selector: 'app-farmers-homepage',
  templateUrl: './farmers-homepage.component.html',
  styleUrls: ['./farmers-homepage.component.css'],
  providers: [FarmerProductsService]
})
export class FarmersHomepageComponent implements OnInit {


  constructor(private service: FarmerProductsService, private farmerHomeService:FarmerHomeService) { }
  foodData:any = [];
  productData: any;
  ngOnInit(): void {
    // this.foodData = this.service.foodDetails;
    this.getProductDetails();
  }
getProductDetails(){
  this.farmerHomeService.getProducts(localStorage.getItem('farmerId'))
  .subscribe((data: {}) => {
    // console.log(data)
    this.productData = data
    console.log(this.productData)
    // response.name; 
    // response.category_name;
    //  response.image;
    //  response.description;
    //  response.price;
    //  response.stock;
    //console.log(response)
    // this.foodData = respose.body 


  },(error) => {
    console.log()
  });
};

deleteProduct(productId: number) {
  console.log(productId)
  return this.farmerHomeService.deleteProduct(productId).subscribe(
  (response) => {
    // console.log(response)
    alert(response.info)
    // alert(response.info);
    this.getProductDetails()
  },
  (error) =>{
    console.log(error);
    // console.error(error);
  });
}





}
