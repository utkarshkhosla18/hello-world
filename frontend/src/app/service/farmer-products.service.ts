import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class FarmerProductsService {

  constructor() { }
  foodDetails = [
    {
      id:1,
      foodName:"Lettuce",
      foodDetails:"Wash before use.",
      foodPrice:0.8,
      foodQuantity:"1 package",
      foodImg:"https://www.collinsdictionary.com/images/full/lettuce_124415023.jpg"
    },
    {
      id:2,
      foodName:"Blueberries",
      foodDetails:"300g. Wash before use",
      foodPrice:2.8,
      foodQuantity:"2 boxes",
      foodImg:"https://www.athinaion-land.gr/wp-content/uploads/2020/07/mirtilo-1024x892.jpg"
    },
    {
      id:3,
      foodName:"Beef Steak",
      foodDetails:"500g.",
      foodPrice:5,
      foodQuantity:"1 piece",
      foodImg:"https://www.foodsafetynews.com/files/2020/06/raw-sirloin-steak-beef.jpg"
    },
    {
      id:4,
      foodName:"Baked Chicken Legs",
      foodDetails:"800g. with barbecue sauce.",
      foodPrice:3,
      foodQuantity:"1 package",
      foodImg:"https://www.kosher.com/resized/details.slide/s/t/Stock_Chicken_Legs.jpg"
    },
    {
      id:5,
      foodName:"Celery",
      foodDetails:"500g. Wash before use.",
      foodPrice:1.5,
      foodQuantity:"2 packages",
      foodImg:"https://www.collinsdictionary.com/images/full/celery_259956566.jpg"
    },
    {
      id:6,
      foodName:"Cup mushroom",
      foodDetails:"300g. Wash before use.",
      foodPrice:2,
      foodQuantity:"1 box",
      foodImg:"https://www.mr-fruity.co.uk/wp-content/uploads/2019/04/202209011_2_640x640.jpg"
    }
  ]





}

