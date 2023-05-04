
import './App.css';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Navbar } from "./components/navbar";
import { Cart } from './pages/cart/cart';
import { Shop } from "./pages/shop/shop";
import { ShopContextProvider } from "./context/shop-context";
import { Login } from "./pages/login/login";


function App() {
  return (
    <div className="App">
      <ShopContextProvider>
        <Router>  
          <Navbar />
          <Routes>

            <Route path="/" element={<Shop />} />
            <Route path="/cart" element={<Cart />} />
            <Route path="pages/login" element={<Login/>} />
          </Routes>
        </Router>
      </ShopContextProvider>
    </div>
  );
}

export default App;