import axios from 'axios';

// If you're running Docker on the same machine:
// Django is on http://localhost:8000
// Adjust if different or behind a reverse proxy
const baseURL = process.env.REACT_APP_DJANGO_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: `${baseURL}/`,
});

export default api;
