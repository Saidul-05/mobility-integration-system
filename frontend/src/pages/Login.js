import React, { useState } from 'react';
import axios from 'axios';

function Login() {
  const [formData, setFormData] = useState({ username: '', password: '' });

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    axios.post('/api/users/login/', formData)
      .then(res => {
        localStorage.setItem('access', res.data.access);
        localStorage.setItem('refresh', res.data.refresh);
        alert('Logged in successfully!');
      })
      .catch(err => console.error(err));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      <input name="username" placeholder="Username" onChange={handleChange} />
      <input name="password" placeholder="Password" type="password" onChange={handleChange} />
      <button type="submit">Login</button>
    </form>
  );
}

export default Login;
