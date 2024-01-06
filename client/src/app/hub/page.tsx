"use client";
import { IconGoRight, IconPlay } from "@/assets/icons";
import { getAllAlbums } from "@/services/album/albumApi";
import { Album } from "@/services/discovery/discoveryHelpers";
import { getAllGenre } from "@/services/hub/hubApi";
import { Genre } from "@/services/hub/hubHelpers";
import Image from "next/image";
import Link from "next/link";
import { useEffect, useState } from "react";

export default function Home() {
  const [hoveredButton, setHoveredButton] = useState<number | null>(null);
  const [albums, setAlbums] = useState<Album[]>([]);
  const [genre, setGenre] = useState<Genre[]>([]);
  const getGenres = async () => {
    const res = await getAllGenre();
    setGenre(res.data);
  };

  const getAlbums = async () => {
    const res = await getAllAlbums();
    setAlbums(res.data);
  };
  const highlights = [
    {
      id: 1,
      imgUrl: "/vercel.svg",
      title: "test1",
    },
    {
      id: 2,
      imgUrl: "/vercel.svg",
      title: "test2",
    },
  ];
  useEffect(() => {
    getGenres();
    getAlbums();
  }, []);
  return (
    <div className="h-[calc(100%_-_84px)] overflow-auto text-white">
      <div className="px-5 mb-5">
        <div className="w-full flex items-center gap-3 mb-5 capitalize text-xl text-white font-bold">
          Nổi bật
        </div>
        <div className="flex items-center w-full">
          {highlights.map((item, index) => (
            <div key={index} className=" w-1/2 p-5">
              <Image
                src={item.imgUrl}
                width={200}
                height={200}
                alt="Image"
                className={`rounded w-[181px] h-[181px]  hover:scale-110 transition-transform duration-300`}
              />
              <div>{item.title}</div>
            </div>
          ))}
        </div>
      </div>
      <div className="flex justify-center">
        <div className="flex items-center justify-center rounded-full border border-[#393243] w-1/6 py-2 px-6 text-xs font-medium">
          TẤT CẢ
        </div>
      </div>
      {genre.map((genre, index) => (
        <div key={index} className="mt-[48px]">
          <div className="flex justify-between p-4  text-xl">
            <div className="text-header text-white">{genre.name}</div>
            <Link
              href={`/hub/${genre.id}`}
              className="flex items-center text-header text-white cursor-pointer hover:text-[#8d22c3]"
            >
              Xem thêm
              <IconGoRight />
            </Link>
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
                    <Link
                      href={`/album/${item.id}`}
                      className="absolute px-4 text-white cursor-pointer"
                    >
                      <IconPlay />
                    </Link>
                  )}
                </div>
                <div className="text-xs font-bold tracking-tight text-white opacity-50">
                  {item.title}
                </div>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
