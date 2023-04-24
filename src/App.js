import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Navbar } from "./components/Navbar";
import { Cart } from './pages/cart/cart';
import { Shop } from "./pages/shop/shop";

function App() {
  return (
    <div className="wrapper">
      <h1>
        <Navbar/>
        <Routes>
          <Route path='/' element={<Shop/>} />
          <Route path='/cart' element={<Cart/>} />
          
        </Routes>
      </h1>
    </div>
  );
}

export default App;
