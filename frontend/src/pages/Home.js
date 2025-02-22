import React, { useEffect, useState } from 'react';
import api from '../services/api';

function Home() {
  const [services, setServices] = useState([]);

  useEffect(() => {
    // Example: call Django API for services
    api.get('/services/')
      .then(response => {
        setServices(response.data);
      })
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ padding: '1rem' }}>
      <h2>Welcome to Mobility Integration System</h2>
      <p>Below is an example list of services from the Django backend:</p>
      <ul>
        {services.map(service => (
          <li key={service.id}>
            {service.name} - {service.category} (${service.price})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Home;
