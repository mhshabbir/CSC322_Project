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

export const ShpoContextProvider = (props) => {
    const [cartItems,setCartItems] = useState();
    return <ShpoContext.Provider>{props.children}</ShpoContext.Provider>;
  };

