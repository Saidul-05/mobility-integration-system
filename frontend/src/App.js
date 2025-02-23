import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';

// Pages
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Checkout from './pages/Checkout';

function App() {
  return (
    <div>
      {/* Common navigation bar */}
      <Navbar />

      {/* Define all your routes here */}
      <Routes>
        {/* Home page */}
        <Route path="/" element={<Home />} />

        {/* Auth pages */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Checkout page (serviceId is hardcoded as 1 for example) */}
        <Route path="/checkout" element={<Checkout serviceId={1} />} />
      </Routes>
    </div>
  );
}

export default App;
