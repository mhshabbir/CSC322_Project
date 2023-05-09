import React from 'react'
import { PRODUCTS } from '../../../products'
import { BuildProduct } from './buildProductList'
import "./buildList.css"

export const BuildList = () => {
  return (
    <div className="BuildListpage">
      <div className="buildListHeader">
        <h1><b>List</b></h1>
      </div>
      <div className='Motherboard'>
        <h2><b>Motherboard</b></h2>
      </div>
          <div className="buildPC-product">
          {PRODUCTS.map((product) => (
            product.category === "Motherboard" ? (
                    <BuildProduct data = {product} key = {product.category} data = {product} /> 
            ) :(
              <React.Fragment key={product.category}></React.Fragment>
            )
 
            ))}
                
          </div>
      <div className='Motherboard'>
        <h2><b>CPU</b></h2>
        <div className="buildPC-product">
          {PRODUCTS.map((product) => (
            product.category === "CPU" ? (
                    <BuildProduct data = {product} key = {product.category} data = {product} /> 
            ) :(
              <React.Fragment key={product.category}></React.Fragment>
            )
 
            ))}
                
          </div>
      </div>
      <div className='Motherboard'>
        <h2><b>Case</b></h2>
        <div className="buildPC-product">
          {PRODUCTS.map((product) => (
            product.category === "Case" ? (
                    <BuildProduct data = {product} key = {product.category} data = {product} /> 
            ) :(
              <React.Fragment key={product.category}></React.Fragment>
            )
 
            ))}
                
          </div>
      </div>
    </div>
  )
}
