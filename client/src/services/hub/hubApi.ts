import axios from "axios";
axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:8000/api/genre";

export const getAllGenre = () => {
  return axios.get("/all");
};
