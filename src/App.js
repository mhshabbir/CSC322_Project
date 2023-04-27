import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Navbar } from "./components/Navbar";
import { Cart } from './pages/cart/cart';
import { Shop } from "./pages/shop/shop";
import Login from './pages/Login';

function App() {
  return (
    <div className="App">
      <h1>
        <Navbar />
        <Routes>
          <Route path='/' element={<Shop/>} />
          <Route path='/cart' element={<Cart/>} />
          <Route path='pages/Login' element={<Login/>} />
        </Routes>
      </h1>
    </div>
  );
}

export default App;
