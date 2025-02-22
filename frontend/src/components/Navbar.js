import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav style={{ padding: '1rem', backgroundColor: '#ccc' }}>
      <Link to="/" style={{ marginRight: '1rem' }}>Home</Link>
      {/* Add more links/routes as needed */}
    </nav>
  );
}

export default Navbar;
