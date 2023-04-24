import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './index.css';
import App from './App';
import Login from './pages/LoginPage';
import SignUp from './pages/SignUp';
import Cart from './pages/ShoppingCart';
import reportWebVitals from './reportWebVitals';
import Search from './pages/SearchResults';
import Checkout from './pages/CheckoutPage';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
   <BrowserRouter>
   <Routes>
    <Route path="/" element={<App/>} />
    <Route path="SearchResults" element={<Search/>}/>
    <Route path="LoginPage" element={<Login/>}/>
    <Route path="SignUpPage" element={<SignUp/>}/>
    <Route path="ShoppingCart" element={<Cart/>}/>
    <Route path="CheckoutPage" element={<Checkout/>}/>
   </Routes>
   </BrowserRouter>
  </React.StrictMode>
);


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
