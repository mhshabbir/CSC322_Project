import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Navbar} from "./components/navbar";

import { Login } from "./Login";
import { Register } from "./Register";

function App() {
  return (
      <Router>
        <Navbar />
        <Routes>
          <Route path='/'/>
          <Route path='/cart'/>
          
        </Routes>
      </Router>
    </div>
  );
}

export default App;
