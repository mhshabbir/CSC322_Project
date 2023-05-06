import React, { useContext } from 'react'
import { ShopContext } from '../../context/shop-context';


export const DisplayProduct = (props) => {
const {id, productName, price, productImage, reviews} = props.data;
const {addToCart} = useContext(ShopContext);
const {cartItems} = useContext(ShopContext);
const cartItemAmount = cartItems[id];


  return (
    <div className="product-listing">
      <div className="product-img">
        <img src={productImage} alt="" height="420" width="327"/>
      </div>
      <div className='description'>
        <h1>
          <b>{productName}</b>
        </h1>
        <p><span>${price}</span></p>
        <button className='addToCartBttn' onClick={()=> addToCart(id)}>
          Add To Cart {cartItemAmount > 0 && <> ({cartItemAmount})</>}
        </button>
      </div>
      <div className='reviewbox'>
        <p>
          {reviews[0]}
        </p>
      </div>
    </div>
  )
}
