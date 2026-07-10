import http from 'k6/http';

export const options = {
  vus: 20,
  duration: '30s',
};

export default function () {
  http.get('http://13.201.20.86');
}