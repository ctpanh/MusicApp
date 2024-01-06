import axios from "axios";
axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:8000/api";

export const getAllPlaylist = () => {
  return axios.get("/playlist/all");
};
