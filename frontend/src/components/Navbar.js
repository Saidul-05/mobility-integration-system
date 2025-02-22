import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav style={{ padding: '1rem', backgroundColor: '#ddd' }}>
      <Link to="/" style={{ marginRight: '1rem' }}>Home</Link>
      {/* Add more links here as needed */}
    </nav>
  );
}

export default Navbar;
