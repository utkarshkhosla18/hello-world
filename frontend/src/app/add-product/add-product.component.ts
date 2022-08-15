import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';
import {AddProductService} from '../service/add-product.service'

@Component({
  selector: 'app-add-product',
  templateUrl: './add-product.component.html',
  styleUrls: ['./add-product.component.css'],

})
export class AddProductComponent implements OnInit {

  fileName = '';

  onFileSelected(event: any) {
    console.log(event.target.files[0])
    let reader = new FileReader();
    const appThis = this;
    reader.readAsText(event.target.files[0]);
    reader.onload = function () {
      let text = String(reader.result);
      let lines = text.split(/\r?\n/);
      lines.forEach(line => {
        let vars = line.split(',');
        if (vars[0] != 'category') {
          appThis.productList.push(vars)
        }
      });
    }
  }

  addProducList() {
    // console.log(this.productList)
    let data = {}
    for (var i = 0 ; i<this.productList.length; i++) {
      data[i] = {
        category_name: this.productList[i][0],
        name: this.productList[i][1],
        description: this.productList[i][2],
        price: Number(this.productList[i][3]), 
        stock: Number(this.productList[i][4])
      }
    }
    console.log(data)

    this.addProductService.addProductList(this.farmerId,data).subscribe(
      (response) => {
        console.log(response);
        alert('Add products success')
      },
      (error) =>{
        console.error(error);
      })
  }

    
category:Array<string> = ['vegetable', 'fruit',  'meat'];
modelProductDescription:String;
modelCategory:String;
modelPrice:String;
modelStock: String;
modelName: String;
farmerId: number;

productList=[];


  imageBase64: any;
  isImageSaved: boolean;
  constructor(private addProductService:AddProductService) { }

  CreateBase64String(Inputfile: any) {
    if (Inputfile.target.files && Inputfile.target.files[0]) {
      const reader = new FileReader();
      reader.onload = (e: any) => {
        const image = new Image();
        image.src = e.target.result;
        image.onload = rs => {
          const imgBasePath = e.target.result;
          this.imageBase64 = imgBasePath;
          this.isImageSaved = true;
          console.log(imgBasePath);
        };
      };
      reader.readAsDataURL(Inputfile.target.files[0]);
    }
}
addProduct(){
  // if(!sessionStorage.getItem('farmerId')) return;
  let data = {
    category_name:this.modelCategory,
    name:this.modelName,
    description:this.modelProductDescription,
    stock:this.modelStock,
    image:this.imageBase64,
    price:this.modelPrice
  };
  console.log(data);
  this.addProductService.addProduct(this.farmerId,data).subscribe(
    (response) => {
      alert('Add product success')
      console.log(response);
    },
    (error) =>{
      console.error(error);
    })
}
  ngOnInit(): void {
    this.farmerId = Number(localStorage.getItem('farmerId'))
  }

}
