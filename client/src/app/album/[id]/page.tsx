"use client";
import Image from "next/image";
import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { Album } from "@/services/discovery/discoveryHelpers";
import { getAlbumById } from "@/services/album/albumApi";
import { IconPlay } from "@/assets/icons";

export default function Home() {
  const params = useParams();
  const id = params.id;
  const [album, setAlbum] = useState<Album>();
  const [hoveredButton, setHoveredButton] = useState<boolean>(false);

  const getAlbum = async () => {
    if (id) {
      const res = await getAlbumById(+id);
      setAlbum(res.data);
    }
  };
  useEffect(() => {
    getAlbum();
  }, []);
  return (
    <div className="w-full flex">
      {album && (
        <div
          onMouseEnter={() => setHoveredButton(true)}
          onMouseLeave={() => setHoveredButton(false)}
          className="flex flex-col justify-center items-center p-2 gap-5 w-[300px] rounded cursor-default"
          style={{ position: "relative" }}
        >
          <div className="flex flex-col justify-center items-center hover:scale-110 transition-transform duration-300">
            <Image
              src={album.image_file_path}
              width={100}
              height={100}
              alt="Image"
              className={`rounded w-[181px] h-[181px] ${
                hoveredButton && "opacity-50"
              }`}
            />
            {hoveredButton && (
              <div className="absolute px-4 text-white cursor-pointer">
                <IconPlay />
              </div>
            )}
          </div>
          <div className="text-xs font-bold tracking-tight text-white opacity-50">
            {album.title}
          </div>
        </div>
      )}
    </div>
  );
}
