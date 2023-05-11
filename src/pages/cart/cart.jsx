import React, { useContext} from 'react';
import { PRODUCTS } from "../../products";
import { ShopContext } from "../../context/shop-context";
import { CartItem } from "./cart-item";
import { Product } from '../shop/product';
import { BundleItem } from '../build/list/bundleItem';

import { useNavigate } from "react-router-dom";


export const Cart = () => {
    const { cartItems, getTotalCartAmount } = useContext(ShopContext)
    const { bundleItems, getTotalBundleAmount } = useContext(ShopContext)
    const totalAmount = getTotalCartAmount()

  const navigate = useNavigate()
  return (
    <div className='cart'>
      <div>
        <h1>Your Cart Items</h1>
      </div>
      <div className='cartItems'>
          {PRODUCTS.map((product) => {
            if (cartItems[product.id] !== 0) {
              return <CartItem data ={product}/>;
            }
          })}
      </div>
      <div classname="products-view-build-page">
        <h1>Your Bundle Iteams</h1>
      </div>
      <div className='buildPC-Product-cartpage'>
          {PRODUCTS.map((product) => {
            if (bundleItems[product.id] !== 0) {
              return <BundleItem data ={product}/>;
            }
          })}
      </div>

      {totalAmount > 0 ? (
      <div className='checkout'>
        
        <p>
          <b>Single Product Subtotal: ${totalAmount}</b>
        </p>
        <button onClick={() => navigate("/")}>Continue Shopping</button>
        <button>Checkout</button>
      </div>
      ) : (
        <h1> Your Cart is Empty</h1>
      )}
    </div>
  )
}
