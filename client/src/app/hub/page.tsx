"use client";
import { IconGoRight, IconPlay } from "@/assets/icons";
import Image from "next/image";
import { useState } from "react";

export default function Home() {
  const [hoveredButton, setHoveredButton] = useState<string | null>(null);

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
  const albums = [
    {
      id: "test",
      desc: "Ngày lễ hoàn hảo để tận hưởng cái ôm từ ai đó",
      imgUrl: "/next.svg",
    },
    {
      id: "test2",
      desc: "Ngày lễ hoàn hảo để tận hưởng cái ôm từ ai đó",
      imgUrl: "/next.svg",
    },
    {
      id: "test3",
      desc: "Ngày lễ hoàn hảo để tận hưởng cái ôm từ ai đó",
      imgUrl: "/next.svg",
    },
  ];
  const themes = [
    {
      id: 1,
      title: "Những ngày đông ấm áp",
    },
    {
      id: 2,
      title: "Nhạc này siêu nhiệt",
    },
  ];
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
      {themes.map((item, index) => (
        <div key={index} className="mt-[48px]">
          <div className="flex justify-between p-4  text-xl">
            <div className="text-header text-white">{item.title}</div>
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
                    src={item.imgUrl}
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
                  {item.desc}
                </div>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
