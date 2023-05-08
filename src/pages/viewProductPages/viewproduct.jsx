import React from 'react'
import { PRODUCTS } from "../../products";
//import { Product } from "../shop/product";
import { DisplayProduct } from './displayProduct';
import { useParams } from 'react-router-dom';
import "./viewproduct.css";


export const Viewproduct = () => {
  const {productlinkID} = useParams()
  const viewProductURL = "/product/" + productlinkID

  return (
    <div className='individual-shop-card'>
      <div className='shop_page'>
          <h1>Product Page </h1>
      </div>
      <div>
          <div className="wrapper">
              {PRODUCTS.map((product) => (
                product.productlink === viewProductURL ? ( 
                  <DisplayProduct key = {product.productlink} data = {product} />
                ) : (
                  <React.Fragment key={product.productlink}></React.Fragment>
                )
              ))}
          </div>
      </div>
      <div className='comments'>
        
      </div>
    </div>
  )
}
