import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Navbar } from "./components/navbar";
import { Cart } from './pages/cart/cart';
import { Shop } from "./pages/shop/shop";
import { ShopContextProvider } from "./context/shop-context";
import { Build } from "./pages/build/build"
import Login from './pages/Login';
import { Viewproduct } from "./pages/viewProductPages/viewproduct";


function App() {
  return (
    <div className="App">
      <ShopContextProvider>
        <Router>  
          <Navbar />
          <Routes>
            <Route path='build' element={<Build/>}/>
            <Route path="/" element={<Shop />} />
            <Route path="cart" element={<Cart />} />
            <Route path='pages/Login' element={<Login/>} />
            <Route path='/:productlink' element={<Viewproduct/>}/>  
          </Routes>
        </Router>
      </ShopContextProvider>

    </div>
  );
}

export default App;