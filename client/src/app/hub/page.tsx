"use client";
import { IconGoRight, IconPlay } from "@/assets/icons";
import { getListAlbumsByGenre } from "@/services/discovery/discoveryApi";
import { Album } from "@/services/discovery/discoveryHelpers";
import { getAllGenre } from "@/services/hub/hubApi";
import { Genre } from "@/services/hub/hubHelpers";
import Image from "next/image";
import Link from "next/link";
import { useEffect, useState } from "react";

export default function Home() {
  const [hoveredButton, setHoveredButton] = useState<number | null>(null);
  const [genresWithAlbums, setGenresWithAlbums] = useState<
    { genre: Genre; album: Album[] }[]
  >([]);
  const [genre, setGenre] = useState<Genre[]>([]);
  const getGenres = async () => {
    const res = await getAllGenre();
    setGenre(res.data);
  };
  useEffect(() => {
    getGenres();
  }, []);

  useEffect(() => {
    const fetchAlbums = async () => {
      const genresWithAlbumsData: { genre: Genre; album: Album[] }[] = [];

      for (const genreItem of genre) {
        try {
          const response = await getListAlbumsByGenre(genreItem.id);
          const albumsData = response.data.slice(0, 6);

          if (albumsData.length > 0) {
            genresWithAlbumsData.push({
              genre: genreItem,
              album: albumsData,
            });
          }
        } catch (error) {
          console.error(
            `Error fetching albums for genre ${genreItem.id}: ${error}`
          );
        }
      }

      setGenresWithAlbums(genresWithAlbumsData);
    };

    fetchAlbums();
  }, [genre]);
  return (
    <div className="h-[calc(100%_-_84px)] overflow-auto text-white">
      <div className="w-full">
        <Image
          src={
            "https://photo-zmp3.zmdcdn.me/cover/c/9/b/3/c9b3c456eeabd9d4e3241666397d71aa.jpg"
          }
          width={600}
          height={200}
          alt="Image"
          className="w-full"
        />
      </div>
      {genresWithAlbums.map(({ genre, album }, index) => (
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
            {album.map((item, index) => (
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
