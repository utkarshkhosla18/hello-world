import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule} from '@angular/common/http';
/* Routing */
import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';

/* Angular Material */
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AngularMaterialModule } from './angular-material.module';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';


/* FormsModule */
import { FormsModule, ReactiveFormsModule} from '@angular/forms';

/* Angular Flex Layout */
import { FlexLayoutModule } from "@angular/flex-layout";

/* Components */
import { LogInComponent } from './components/log-in/log-in.component';
import { RegisterComponent } from './components/register/register.component';
import { FarmersHomepageComponent } from './farmers-homepage/farmers-homepage.component';
import { AddProductComponent } from './add-product/add-product.component';
import { ProfileSettingsComponent } from './profile-settings/profile-settings.component';
import { AdminDashboardComponent } from './components/admin-dashboard/admin-dashboard.component'
import { CartComponent } from './pages/cart/cart.component';
import { CheckoutComponent } from './pages/checkout/checkout.component';
import { HomeComponent } from './pages/home/home.component';
import { OrderComponent } from './pages/order/order.component';
import { ProductListComponent } from './pages/product-list/product-list.component';
import { SearchBarComponent } from './sharepage/search-bar/search-bar.component';
import { RouterModule } from '@angular/router';
import { ProductlistpageComponent } from './pages/productlistpage/productlistpage.component';
import { AdminProductsListComponent } from './components/admin-products-list/admin-products-list.component';
import { AdminProductsUpdateComponent } from './components/admin-products-update/admin-products-update.component';

@NgModule({
  declarations: [
    AppComponent,
    RegisterComponent,
    LogInComponent,
    FarmersHomepageComponent,
    AddProductComponent,
    ProfileSettingsComponent,
    AdminDashboardComponent,
    CartComponent,
    HomeComponent,
    OrderComponent,
    ProductListComponent,
    SearchBarComponent,
    CheckoutComponent,
    SearchBarComponent,
    ProductlistpageComponent,
    CheckoutComponent,
    SearchBarComponent,
    AdminProductsListComponent,
    AdminProductsUpdateComponent
    

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    AngularMaterialModule,
    ReactiveFormsModule,
    FormsModule,
    FlexLayoutModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule,
    HttpClientModule,
    RouterModule.forRoot([
      { path: '', component: ProductListComponent },
      { path: 'products/:productId', component: ProductlistpageComponent },
      { path: 'cart', component: CartComponent },
      { path: 'adminProductUpdate', component: AdminProductsUpdateComponent },
      { path: 'adminProducts', component: AdminProductsListComponent },
    ]),
  ],
  providers: [],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})

export class AppModule { }
