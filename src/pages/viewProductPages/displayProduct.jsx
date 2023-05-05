import React, { useContext } from 'react'
import { ShopContext } from '../../context/shop-context';

export const DisplayProduct = (props) => {
const {id, productName, price, productImage, reviews} = props.data;
const {addToCart} = useContext(ShopContext);
const {cartItems} = useContext(ShopContext);
const cartItemAmount = cartItems[id];


  return (
    <div className="showProduct">
      <img src={productImage} alt="" />
      <div className='description'>
        <p>
          <b>{productName}</b>
        </p>
        <p>${price}</p>
        <button className='addToCartBttn' onClick={()=> addToCart(id)}>
          Add To Cart {cartItemAmount > 0 && <> ({cartItemAmount})</>}
        </button>
      </div>
      <div className='reviewbox'>
        <p>{reviews}</p>
      </div>
    </div>
  )
}
