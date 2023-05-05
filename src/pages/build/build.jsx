import React from 'react'
import { PRODUCTS } from "../../products";
import { Product } from "../shop/product";

export const Build = () => {
  return (
    <div className="build-page">
        <div className="build-header">
            <h1>Build Your PC</h1>
        </div>
        <div className="build-products">
            {PRODUCTS.map((product) => (
            <Product data = {product} /> 
            ))}
        </div>
    </div>
  )
}
