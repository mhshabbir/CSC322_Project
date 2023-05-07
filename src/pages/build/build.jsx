import React from 'react'
import { PRODUCTS } from "../../products";
import { Product } from "../shop/product";
import { List } from 'phosphor-react';
import { EmptyView } from './emptyView/emptyView';
import { BuildList } from './list/buildList';
import { Filterpanel } from './filterpanel/filterpanel';
import './build.css';


export const Build = () => {
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
            <BuildList />
          </div>
        </div>
    </div>
  )
}


// {PRODUCTS.map((product) => (
//   <Product data = {product} /> 
//   ))}