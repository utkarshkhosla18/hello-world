
export interface ICart {
    // id: string;
    items:ICartItem[];
    // product: number;
    // quantity: number;
    // customer: number;
}

export interface ICartItem{
    // id: number,
    // category_name: string,
    // farmer_name: string,
    // image: string,
    // name: string,
    // description: string,
    // price: string,
    // stock: number,
    // status: number,
    // category: number,
    // farmer: number
    // customer: number;
    product: number;
    quantity: number;
    // price:string;
}

// export interface ICartTotal{
//     total: number;
// }

// export class Cart implements ICart {
//     // id = uuid();
//     items: ICartItem[] = [];
//    }
