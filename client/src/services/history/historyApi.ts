import axios from "axios";
axios.defaults.withCredentials = true;

export const getRecentlyHeardSongs = (userId: number) => {
  return axios.get(`/history/recently-heard-songs/${userId}`);
};
