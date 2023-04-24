import React from 'react'

export const Product = (props) => {
  const { id, productName, price, productImage} = props.data;
  return (
    <div className="product">
      <img src={productImage} alt="" />
      <div className='description'>
        <b>{productName}</b>
        <p>${price}</p>
        <button className='addToCartBttn'>Add To Cart</button>
      </div>

    </div>
  )
}

