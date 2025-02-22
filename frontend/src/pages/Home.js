import React, { useEffect, useState } from 'react';
import api from '../services/api';

function Home() {
  const [services, setServices] = useState([]);

  useEffect(() => {
    // Example: call Django for /services/
    api.get('/services/')
      .then(res => setServices(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ padding: '1rem' }}>
      <h2>Mobility Integration System</h2>
      <ul>
        {services.map(svc => (
          <li key={svc.id}>
            {svc.name} - {svc.category} (${svc.price})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Home;
