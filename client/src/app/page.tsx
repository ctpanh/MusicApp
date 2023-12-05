"use client";
import { IconGoRight, IconPlay } from "@/assets/icons";
import {
  getAllAlbums,
  getListAlbumsByGenre,
  getNewestSongs,
} from "@/services/discovery/discoveryApi";
import { Album, Song } from "@/services/discovery/discoveryHelpers";
import { getAllGenre } from "@/services/hub/hubApi";
import { Genre } from "@/services/hub/hubHelpers";
import useAuthStore from "@/stores/authStore";
import Image from "next/image";
import { useEffect, useState } from "react";

export default function Home() {
  const [hoveredButton, setHoveredButton] = useState<number | null>(null);
  const [newestSongs, setNewestSongs] = useState<Song[]>([]);
  const [albums, setAlbums] = useState<Album[]>([]);
  const [genre, setGenre] = useState<Genre[]>([]);
  const { authorized } = useAuthStore();

  const getGenres = async () => {
    const res = await getAllGenre();
    setGenre(res.data);
  };

  const getAlbums = async () => {
    const res = await getAllAlbums();
    setAlbums(res.data);
  };

  const getSongs = async () => {
    const res = await getNewestSongs();
    setNewestSongs(res.data);
  };

  useEffect(() => {
    getGenres;
    getAlbums;
    getSongs;
  }, []);

  return (
    <div className="h-[calc(100%_-_84px)] overflow-auto">
      {authorized && (
        <div className="mt-[48px]">
          <div className="flex justify-between p-4  text-xl">
            <div className="text-header text-white">Gần đây</div>
            <div className="flex items-center text-header text-white cursor-pointer hover:text-[#8d22c3]">
              Xem thêm
              <IconGoRight />
            </div>
          </div>
          <div className="flex justify-center items-center px-4 gap-5">
            <div className="w-1/2 flex flex-col gap-4">
              {newestSongs.slice(0, 4).map((song, index) => (
                <div
                  onMouseEnter={() => setHoveredButton(song.id)}
                  onMouseLeave={() => setHoveredButton(null)}
                  key={index}
                  className="flex items-center p-2 gap-5 max-w-3xl rounded focus:bg-[#393243] hover:bg-[#393243] cursor-default"
                  style={{ position: "relative" }}
                >
                  <Image
                    src={song.image_file_path}
                    width={60}
                    height={60}
                    alt="Image"
                    className={`rounded-lg w-[60px] h-[60px] ${
                      hoveredButton === song.id && "opacity-50"
                    }`}
                  />
                  <div className="text-xs tracking-tight text-white">
                    <div className="font-bold">{song.title}</div>
                    <div className="font-light opacity-50">{song.artist}</div>
                    <div className="font-light opacity-50">
                      {song.release_date}
                    </div>
                  </div>
                  {hoveredButton === song.id && (
                    <div className="absolute px-4 text-white cursor-pointer">
                      <IconPlay />
                    </div>
                  )}
                </div>
              ))}
            </div>
            <div className="w-1/2 flex flex-col gap-4">
              {newestSongs.slice(4, 8).map((song, index) => (
                <div
                  onMouseEnter={() => setHoveredButton(song.id)}
                  onMouseLeave={() => setHoveredButton(null)}
                  key={index}
                  className="flex items-center p-2 gap-5 max-w-3xl rounded focus:bg-[#393243] hover:bg-[#393243] cursor-default"
                  style={{ position: "relative" }}
                >
                  <Image
                    src={song.image_file_path}
                    width={60}
                    height={60}
                    alt="Image"
                    className={`rounded-lg w-[60px] h-[60px] ${
                      hoveredButton === song.id && "opacity-50"
                    }`}
                  />
                  <div className="text-xs tracking-tight text-white">
                    <div className="font-bold">{song.title}</div>
                    <div className="font-light opacity-50">{song.artist}</div>
                    <div className="font-light opacity-50">
                      {song.release_date}
                    </div>
                  </div>
                  {hoveredButton === song.id && (
                    <div className="absolute px-4 text-white cursor-pointer">
                      <IconPlay />
                    </div>
                  )}
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
      <div className="mt-[48px]">
        <div className="flex justify-between p-4  text-xl">
          <div className="text-header text-white">Mới phát hành</div>
          <div className="flex items-center text-header text-white cursor-pointer hover:text-[#8d22c3]">
            Xem thêm
            <IconGoRight />
          </div>
        </div>
        <div className="flex justify-center items-center px-4 gap-5">
          <div className="w-1/2 flex flex-col gap-4">
            {newestSongs.slice(0, 4).map((song, index) => (
              <div
                onMouseEnter={() => setHoveredButton(song.id)}
                onMouseLeave={() => setHoveredButton(null)}
                key={index}
                className="flex items-center p-2 gap-5 max-w-3xl rounded focus:bg-[#393243] hover:bg-[#393243] cursor-default"
                style={{ position: "relative" }}
              >
                <Image
                  src={song.image_file_path}
                  width={60}
                  height={60}
                  alt="Image"
                  className={`rounded-lg w-[60px] h-[60px] ${
                    hoveredButton === song.id && "opacity-50"
                  }`}
                />
                <div className="text-xs tracking-tight text-white">
                  <div className="font-bold">{song.title}</div>
                  <div className="font-light opacity-50">{song.artist}</div>
                  <div className="font-light opacity-50">
                    {song.release_date}
                  </div>
                </div>
                {hoveredButton === song.id && (
                  <div className="absolute px-4 text-white cursor-pointer">
                    <IconPlay />
                  </div>
                )}
              </div>
            ))}
          </div>
          <div className="w-1/2 flex flex-col gap-4">
            {newestSongs.slice(4, 8).map((song, index) => (
              <div
                onMouseEnter={() => setHoveredButton(song.id)}
                onMouseLeave={() => setHoveredButton(null)}
                key={index}
                className="flex items-center p-2 gap-5 max-w-3xl rounded focus:bg-[#393243] hover:bg-[#393243] cursor-default"
                style={{ position: "relative" }}
              >
                <Image
                  src={song.image_file_path}
                  width={60}
                  height={60}
                  alt="Image"
                  className={`rounded-lg w-[60px] h-[60px] ${
                    hoveredButton === song.id && "opacity-50"
                  }`}
                />
                <div className="text-xs tracking-tight text-white">
                  <div className="font-bold">{song.title}</div>
                  <div className="font-light opacity-50">{song.artist}</div>
                  <div className="font-light opacity-50">
                    {song.release_date}
                  </div>
                </div>
                {hoveredButton === song.id && (
                  <div className="absolute px-4 text-white cursor-pointer">
                    <IconPlay />
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </div>
      {genre.map((genre, index) => (
        <div key={index} className="mt-[48px]">
          <div className="flex justify-between p-4  text-xl">
            <div className="text-header text-white">{genre.name}</div>
            <div className="flex items-center text-header text-white cursor-pointer hover:text-[#8d22c3]">
              Xem thêm
              <IconGoRight />
            </div>
          </div>
          <div className="flex justify-center items-center px-4 gap-5">
            {albums.map((item, index) => (
              <div
                onMouseEnter={() => setHoveredButton(item.id)}
                onMouseLeave={() => setHoveredButton(null)}
                key={index}
                className="flex flex-col justify-center items-center p-2 gap-5 max-w-3xl rounded cursor-default"
                style={{ position: "relative" }}
              >
                <div className="flex flex-col justify-center items-center hover:scale-110 transition-transform duration-300">
                  <Image
                    src={item.image_file_path}
                    width={100}
                    height={100}
                    alt="Image"
                    className={`rounded w-[181px] h-[181px] ${
                      hoveredButton === item.id && "opacity-50"
                    }`}
                  />
                  {hoveredButton === item.id && (
                    <div className="absolute px-4 text-white cursor-pointer">
                      <IconPlay />
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
