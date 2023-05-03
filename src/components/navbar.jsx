import React from "react";
import { Link } from "react-router-dom";
import { ShoppingCart } from "phosphor-react";
import { User } from "phosphor-react";
import "./navbar.css";

export const Navbar = () => {
  return (
    <div className="navbar">
      <div className="center-link">
        <Link to="/">
          Home
        </Link>
        <Link to="/build">
          Build
        </Link>
      </div>
      <div className="links">
        <Link to="/cart">
          <ShoppingCart size={32} />
        </Link>
        <Link to="/login">
        <User size={32} />
        </Link>
      </div>


    </div>
  );
};
