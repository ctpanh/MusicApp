"use client";
import { IconGoRight, IconPlay } from "@/assets/icons";
import { getListAlbumsByGenre } from "@/services/discovery/discoveryApi";
import { Album } from "@/services/discovery/discoveryHelpers";
import Image from "next/image";
import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { Genre } from "@/services/hub/hubHelpers";
import { getGenreById } from "@/services/hub/hubApi";

export default function Home() {
  const params = useParams();
  const id = params.id;
  const [hoveredButton, setHoveredButton] = useState<number | null>(null);
  const [albums, setAlbums] = useState<Album[]>([]);
  const [genre, setGenre] = useState<Genre>();

  const getAlbums = async () => {
    if (id) {
      const res = await getListAlbumsByGenre(+id);
      setAlbums(res.data);
    }
  };

  const getGenre = async () => {
    if (id) {
      const res = await getGenreById(+id);
      setGenre(res.data);
    }
  };

  useEffect(() => {
    getGenre();
    getAlbums();
  }, []);
  return (
    <div>
      <div className="mt-[48px]">
        {genre && (
          <div className="flex justify-between p-4  text-xl">
            <div className="text-header text-white">{genre.name}</div>
          </div>
        )}
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
                  src={"/" + item.image_file_path}
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
              <div className="text-xs font-bold tracking-tight text-white opacity-50">
                {item.title}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
