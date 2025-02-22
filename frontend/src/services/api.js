import axios from 'axios';

const api = axios.create({
  // If running Docker locally, Django might be on http://localhost:8000
  // or replace with the container name if using Docker networks
  baseURL: process.env.REACT_APP_DJANGO_URL || 'http://localhost:8000/api',
});

export default api;
