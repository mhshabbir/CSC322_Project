import React, { createContext, useState } from "react";
import { PRODUCTS } from "../products";

export const ShpoContext = createContext(null);

//loop to correct 
const getDefaultCart = () => {
    let cart = {}
    for (let i = 0; i < array.length; i++) {
        const element = array[i];
        
    }
}

export const ShopContextProvider = (props) => {
    const [cartItems,setCartItems] = useState();
    return <ShopContext.Provider>{props.children}</ShopContext.Provider>;
  };

