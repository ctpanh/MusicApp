"use client";
import { IconHeart, IconPlay1 } from "@/assets/icons";
import Image from "next/image";
import { useState } from "react";

export default function Home() {
  const [hoveredButton, setHoveredButton] = useState<string | null>(null);

  const songs = [
    {
      id: "trip1",
      title: "Alo",
      imgUrl: "/next.svg",
      artist: "Vu",
      album: "50 phut",
      time: "03:12",
    },
    {
      id: "trip2",
      title: "Blo",
      imgUrl: "/next.svg",
      artist: "Vu",
      album: "50 phut",
      time: "05:12",
    },
  ];
  return (
    <div className="w-full h-[calc(100%_-_84px)] overflow-auto p-10">
      <div className="w-full flex items-center gap-3 mb-8 capitalize text-4xl text-white font-bold">
        Bảng xếp hạng
        <div className="cursor-pointer">
          <IconPlay1 />
        </div>
      </div>
      {songs.map((item, index) => (
        <button
          key={index}
          onMouseEnter={() => setHoveredButton(item.id)}
          onMouseLeave={() => setHoveredButton(null)}
          className="w-full flex items-center text-left p-2.5 text-xs font-light gap-4 text-white rounded focus:bg-[#393243] hover:bg-[#393243] "
        >
          <div className="flex items-center gap-10 w-1/2 mr-2.5">
            <div
              className={`font-black text-4xl ${
                index + 1 === 1
                  ? "text-red-500"
                  : index + 1 === 2
                  ? "text-lime-500"
                  : index + 1 === 3
                  ? "text-cyan-500"
                  : "text-white"
              }`}
            >
              {index + 1}
            </div>
            <div
              className="flex items-center gap-5 max-w-3xlcursor-default"
              style={{ position: "relative" }}
            >
              <Image
                src={item.imgUrl}
                width={60}
                height={60}
                alt="Image"
                className={`rounded-lg w-[60px] h-[60px] ${
                  hoveredButton === item.id && "opacity-50"
                }`}
              />
              <div className="text-xs tracking-tight text-white">
                <div className="font-bold">{item.title}</div>
                <div className="font-light opacity-50">{item.artist}</div>
              </div>
              {hoveredButton === item.id && (
                <div className="absolute px-4 text-white cursor-pointer">
                  <IconPlay1 />
                </div>
              )}
            </div>
          </div>
          <div className={`w-1/2 opacity-50`}>{item.album}</div>
          <div className="flex gap-5 justify-end items-center mr-0 opacity-50">
            {hoveredButton === item.id && (
              <div className="px-12 absolute cursor-pointer">
                <IconHeart />
              </div>
            )}
            {item.time}
          </div>
        </button>
      ))}
    </div>
  );
}