import React from 'react';
import "../styles/Navbar.css";
import logo from "../assets/cara.png";
import { useState } from 'react';
import BestSellers from './BestSellers';
import GiftSets from './GiftSets';
import Body from './Body';
import { FaShoppingBag } from "react-icons/fa";
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

const NavBar = () => {
    const [show, setShow] = useState(false);
    const [show2, setShow2] = useState(false);
    const [show3, setShow3] = useState(false);
    const [show4, setShow4] = useState(false);

    const showHandler = () => {
        setShow(true);
        setShow2(false);
        setShow3(false);
        setShow4(false);
    }

    const showHandler2 = () => {
        setShow2(true);
        setShow(false);
        setShow3(false);
        setShow4(false);
    }

    const showHandler3 = () => {
        setShow3(true);
        setShow(false);
        setShow2(false);
        setShow4(false);
    }

    const showHandler4 = () => {
        setShow4(true);
        setShow(false);
        setShow2(false);
        setShow3(false);
    }

    const dontShowHandler = () => {
        setShow(false);
        setShow2(false);
        setShow3(false);
        setShow4(false);
    }

    return (
        <div>
            <header className="banner" role="banner">
                <nav className="navbar" role="navigation" aria-label="menu">
                    <Link to="/">
                        <img src="logo.png" className="ml-32" alt="Logo" width="180" height="30" />
                    </Link>

                    <ul className="menuNav">
                        <li className="dropdown nav-link nav-link-fade-up transition-all duration-700" onMouseOver={showHandler}>
                            Products
                            {show && (
                                <div>
                                    <ul className="dropdown-nav" onMouseLeave={dontShowHandler}>
                                        <BestSellers />
                                    </ul>
                                </div>
                            )}
                        </li>

                        <li className="dropdown nav-link nav-link-fade-up" onMouseOver={showHandler2}>
                            Shopping Items
                            {show2 && (
                                <ul className="dropdown-nav dropdown-nav2" onMouseLeave={dontShowHandler}>
                                    <GiftSets />
                                </ul>
                            )}
                        </li>

                        {/* Add Login/Signup Links */}
                        <li className="nav-link">
                            <a href="/login.html">Login</a>
                        </li>

                        <li className="nav-link">
                            <a href="/signin.html">Sign Up</a>
                        </li>

                        <p className="navLine absolute bg-red-600 w-1 font-extralight h-9 z-50"></p>
                    </ul>

                    <Link to="/cart" className="cart-icon">
                        <FaShoppingBag className="text-2xl" />
                    </Link>
                </nav>
            </header>
        </div>
    );
}

export default NavBar;