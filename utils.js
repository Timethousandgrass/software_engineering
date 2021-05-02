import axios from "axios";

const instance = axios.create({
   baseURL:'http://localhost:1234/',
    timeout:1000,
    headers:{'Content-Type':'appllication/x-www-form-urlencoded;'}
});

export default instance;
