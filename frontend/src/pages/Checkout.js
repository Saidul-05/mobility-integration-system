import React from 'react';
import authApi from '../services/authApi';

function Checkout({ serviceId }) {
  const handleCheckout = () => {
    // Post to Django's /api/checkout/ with the chosen service ID
    authApi.post('/checkout/', { service_id: serviceId })
      .then(res => {
        // Redirect user to Stripe checkout
        window.location.href = `https://checkout.stripe.com/pay/${res.data.sessionId}`;
      })
      .catch(err => console.error(err));
  };

  return (
    <div style={{ margin: '1rem' }}>
      <h2>Checkout Page</h2>
      <button onClick={handleCheckout}>
        Pay for Service {serviceId}
      </button>
    </div>
  );
}

export default Checkout;
