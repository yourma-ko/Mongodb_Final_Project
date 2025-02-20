import axios from "axios";

export const axiosInstance = axios.create({
    baseURL:"https://mongodb-project-z0ng.onrender.com/api/",
    headers: {
        "Content-Type": "application/json",
      }
})