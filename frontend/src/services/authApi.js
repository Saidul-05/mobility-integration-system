import axios from 'axios';

const authApi = axios.create({
  baseURL: '/api',
});

authApi.interceptors.request.use(config => {
  const token = localStorage.getItem('access');
  if (token) {
    config.headers['Authorization'] = `Bearer ${token}`;
  }
  return config;
}, err => Promise.reject(err));

export default authApi;
