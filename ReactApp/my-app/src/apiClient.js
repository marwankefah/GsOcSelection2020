import axios from 'axios';

export const BASE_URI = 'http://localhost:5000';
const client = axios.create({
 baseURL: BASE_URI,
 json: true
});

class APIClient {
 constructor(accessToken) {
   this.accessToken = accessToken;
 }


 getposts() {
   return this.perform('get', '/');
 }

 async perform (method, resource, data) {
     console.log(method)
   return client({
     method,
     url: BASE_URI,
     data,
       // not for this phase
     // headers: {
     //   Authorization: `Bearer ${this.accessToken}`
     // }
   }).then(resp => {
     return resp.data ? resp.data : [];
   })
 }
}

export default APIClient;