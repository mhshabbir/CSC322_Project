import React, { useContext } from 'react'
import { Link } from "react-router-dom";
import { ShopContext } from '../../../context/shop-context';

export const BuildProduct = (props) => {
    const { id, productName, price, productImage, productlink} = props.data;
    const {addToBundle} = useContext(ShopContext);
    const {bundleItems} = useContext(ShopContext);
    const {removeFromBundle} = useContext(ShopContext);
    const bundleAmount = bundleItems[id];


  return (
    <div className="build-Product-Card" >
      <Link to={productlink}>
        <img src={productImage} alt="" />
      </Link>
      <div className='build-pc-description'>
        <p>
          <b>{productName}</b>
        </p>
        <p>${price}</p>
        <p>Bundle {bundleAmount}</p>
        <button className='add-to-bundle' onClick={ () => addToBundle(id)}>Add to Bundle</button>
        <button className='add-to-bundle' onClick={ () => removeFromBundle(id)}>Remove From Bundle</button>
        </div>
    </div>
  )
}
