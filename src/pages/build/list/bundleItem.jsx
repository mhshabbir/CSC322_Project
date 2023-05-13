import React, {useContext} from 'react'
import { Link } from "react-router-dom";
import { ShopContext } from '../../../context/shop-context';

export const BundleItem = (props) => {
    const { id, productName, price, productImage, productlink, category} = props.data;
    const {addToBundle} = useContext(ShopContext);
    const {bundleItems} = useContext(ShopContext);
    const {removeFromBundle} = useContext(ShopContext);
    const {addBundleCategory, removeBundleCategory} = useContext(ShopContext);
    const bundleAmount = bundleItems[id];

  const handleAddToBundleClick = () => {
      addToBundle(id)
      addBundleCategory(category)
    }

  const handleRemoveFromBundleClick = () => {
    removeFromBundle(id)
    removeBundleCategory(category)
  }


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
        <button className='add-to-bundle' onClick={ () => handleAddToBundleClick()}>Add to Bundle</button>
        <button className='add-to-bundle' onClick={ () => handleRemoveFromBundleClick()}>Remove From Bundle</button>
        </div>
    </div>
  )
}

