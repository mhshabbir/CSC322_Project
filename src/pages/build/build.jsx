import React, { useContext} from 'react'
import { PRODUCTS } from "../../products";
import { Product } from "../shop/product";
import { List } from 'phosphor-react';
import { EmptyView } from './emptyView/emptyView';
import { BuildList } from './list/buildList';
import { Filterpanel } from './filterpanel/filterpanel';
import { ShopContext } from "../../context/shop-context";
import { BundleItem } from './list/bundleItem';
import './build.css';


export const Build = () => {
  const { bundleItems, getTotalBundleAmount, suggestionRating } = useContext(ShopContext)
  const totalBundleAmount = getTotalBundleAmount()

  return (
    <div className="build-page">
        <div className="build-header">
            <h1>Build Your PC</h1>
        </div>
        {/* Side panel */}
        <div className='buildPage-wrap'>
          <div className="filtering-side-panel">
            <Filterpanel />
          </div>
          {/* List view & emptyView */}

          <div className='products-view-build-page'>
            {totalBundleAmount > 0 ? (
              <div>
              <div>
                <h1>Your Bundle Items</h1>
                <h1>Hello{suggestionRating}</h1>
              </div>
              <div className='buildPC-Product-buildpage'>
                  {PRODUCTS.map((product) => {
                    if (bundleItems[product.id] !== 0) {
                      return <BundleItem data ={product}/>;
                    }
                  })}
              </div>
              </div>
              ) : (
                <h1>Your Bundle is Empty</h1>
              )}
            <BuildList />
          </div>
        </div>
    </div>
  )
}


// {PRODUCTS.map((product) => (
//   <Product data = {product} /> 
//   ))}