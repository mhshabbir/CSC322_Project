import { createContext, useEffect, useState } from "react";
import { PRODUCTS } from "../products";
import { SUGGESTEDCOFIGS } from "../pages/build/SuggestedConfigData";
import { CornersIn } from "phosphor-react";

export const ShopContext = createContext(null);

const getDefaultCart = () => {
  let cart = {};
  for (let i = 1; i < PRODUCTS.length + 1; i++) {
    cart[i] = 0;
  }
  return cart;
};

const getDefaultBundle = () => {
  let bundle = {};
  for (let i = 1; i < PRODUCTS.length + 1; i++) {
    bundle[i] = 0;
  }
  return bundle;
};


export const ShopContextProvider = (props) => {
  const [cartItems, setCartItems] = useState(getDefaultCart());
  const [bundleItems, setBundleItems] = useState(getDefaultBundle());
  const [currentcat, setcurrentcat] = useState([""]);
  const [suggestionRating, setSuggestionRating] = useState(0);


  const getTotalCartAmount = () => {
    let totalAmount = 0;
    for (const item in cartItems) {
      if (cartItems[item] > 0) {
        let itemInfo = PRODUCTS.find((product) => product.id === Number(item));
        totalAmount += cartItems[item] * itemInfo.price;
      }
    }
    return totalAmount;
  };

  const getTotalBundleAmount = () => {
    let totalBundleAmount = 0;
    for (const item in bundleItems) {
      if (bundleItems[item] > 0) {
        let itemInfo = PRODUCTS.find((product) => product.id === Number(item));
        totalBundleAmount += bundleItems[item] * itemInfo.price;
      }
    }
    return totalBundleAmount;
  };

  const setBundleThroughSuggestions = (SuggestList,rating,bundledproducts) =>{
    //clear the current bundle
    //setBundleItems({});
    //replace the with the current distionary according to id of the review.
    setBundleItems(SuggestList);
    setSuggestionRating(rating);
    const catergorylist = [];

  for (let i = 0; i < PRODUCTS.length ; i++) {
      const product = PRODUCTS[i];
      console.log(product.id)
      console.log(bundledproducts)
      if (bundledproducts.includes(product.id)) {
        catergorylist.push(product.category);
        //addBundleCategory(product.category);
      }
    }
    setcurrentcat([])
    setcurrentcat(catergorylist)

      // for (const id in bundledproducts){
      //   const findid = bundledproducts[id];
      //   const Sproduct = PRODUCTS.find(p => p.id === findid);
      //   const category = Sproduct.category;
      //   addBundleCategory(category);
      //   console.log(category);
      // }

  }

  const addBundleCategory = (category) => {
    setcurrentcat([...currentcat,category])
  }

  const removeBundleCategory = (category) => {
    const filteredArray = currentcat.filter((value) => value !== category);
    setcurrentcat(filteredArray);
  }

  const resetBundleItem = () => {
    setcurrentcat([])
    setBundleItems(getDefaultBundle())
    
  }

  

  const addToBundle = (itemId) => {
    setBundleItems((prev) => ({ ...prev, [itemId]: 1}))
  }
  const removeFromBundle = (itemId) => {
    setBundleItems((prev) => ({ ...prev, [itemId]: 0}))
  }

  const addToCart = (itemId) => {
    setCartItems((prev) => ({ ...prev, [itemId]: prev[itemId] + 1 }));
  };

  const removeFromCart = (itemId) => {
    setCartItems((prev) => ({ ...prev, [itemId]: prev[itemId] - 1 }));
  };

  const updateCartItemCount = (newAmount, itemId) => {
    setCartItems((prev) => ({ ...prev, [itemId]: newAmount }));
  };

  const checkout = () => {
    setCartItems(getDefaultCart());
  };


  const contextValue = {
    getDefaultBundle,
    cartItems,
    addToCart,
    updateCartItemCount,
    removeFromCart,
    getTotalCartAmount,
    checkout,
    bundleItems,
    getTotalBundleAmount,
    addToBundle,
    removeFromBundle,
    addBundleCategory,
    currentcat,
    removeBundleCategory,
    resetBundleItem,
    setBundleThroughSuggestions,
    suggestionRating,
  };

  return (
    <ShopContext.Provider value={contextValue}>
      {props.children}
    </ShopContext.Provider>
  );
};
