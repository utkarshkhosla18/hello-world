import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LogInComponent } from './components/log-in/log-in.component';
import { RegisterComponent } from './components/register/register.component';
import{FarmersHomepageComponent} from './farmers-homepage/farmers-homepage.component'
import {AddProductComponent} from './add-product/add-product.component'

import {ProfileSettingsComponent} from './profile-settings/profile-settings.component'
import { AdminDashboardComponent } from './components/admin-dashboard/admin-dashboard.component'
import { CartComponent } from './pages/cart/cart.component';
import { CheckoutComponent } from './pages/checkout/checkout.component';
import { HomeComponent } from './pages/home/home.component';
import { OrderComponent } from './pages/order/order.component';
import { ProductListComponent } from './pages/product-list/product-list.component';
import { ProductlistpageComponent } from './pages/productlistpage/productlistpage.component';
import { AdminProductsListComponent } from './components/admin-products-list/admin-products-list.component';
import { AdminProductsUpdateComponent } from './components/admin-products-update/admin-products-update.component';

const routes: Routes = [
  
  { path: '', pathMatch: 'full', redirectTo: 'login' },
  { path: 'login', component: LogInComponent },
  { path: 'register', component: RegisterComponent },
  {path:'farmershome', component : FarmersHomepageComponent},
   {path: 'addnewproduct',  component : AddProductComponent},
  {path : 'yourprofile' , component : ProfileSettingsComponent},
  {path:'adminDashboard' , component:AdminDashboardComponent},
  { path: 'adminProductUpdate', component: AdminProductsUpdateComponent},
  { path: 'adminProducts', component: AdminProductsListComponent},
  {path:'customerHome', component:HomeComponent},
  {path:'cart',component:CartComponent},
  {path:'order', component:OrderComponent},
  {path:'product-list', component:ProductListComponent},
  {path:'product-list/:id',component:ProductlistpageComponent},
  {path:'checkout', component:CheckoutComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
