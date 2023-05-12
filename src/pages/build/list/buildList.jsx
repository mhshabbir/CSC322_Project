import React, { useContext } from 'react'
import { PRODUCTS } from '../../../products'
import { BuildProduct } from './buildProuctList'
import { ShopContext } from '../../../context/shop-context'
import "./buildList.css"



export const BuildList = () => {

  const {currentcat} = useContext(ShopContext);
  const currentCategoryList = currentcat;
  
  const checkCurrent = (catogoryName) => {
    if (currentCategoryList.includes(catogoryName)) {
      return true;
    } 
  };

  return (

    <div className="BuildListpage">
      <div className="buildListHeader">
        <h1><b>List</b></h1>
      </div>
      {!checkCurrent("Motherboard") && (
        <div className='category'>
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
          </div>
        )} 
          
      {!checkCurrent("CPU") && (
        <div className='category'>
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
        </div>
   )} 
                        
    {!checkCurrent("Case") && (
      <div className='category'>
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
  )} 
  </div>
  )
}