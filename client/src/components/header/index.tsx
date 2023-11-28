"use client";
import { IconSetting, IconUser } from "@/assets/icons";
import {
  headeSettingItem,
  headerAccountItem,
} from "@/services/header/headerHelpers";
import Link from "next/link";
import { useState } from "react";

const Header = () => {
  const [clickedAccount, setClickedAccount] = useState(false);
  const [clickedSetting, setClickedSetting] = useState(false);
  return (
    <div className="px-16 py-4 w-full h-fit flex items-center justify-between bg-opacity">
      <form className="w-full px-5">
        <label
          htmlFor="default-search"
          className="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white"
        >
          Search
        </label>
        <div className="relative ">
          <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
            <svg
              className="w-5 h-5 text-white"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 20 20"
            >
              <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
              />
            </svg>
          </div>
          <input
            type="search"
            id="default-search"
            className="block w-1/2 p-4 pl-10 text-sm text-white border border-gray-300 rounded-full bg-[#393243] focus:bg-[#34224f]"
            placeholder="Tìm kiếm bài hát, nghệ sĩ, lời bài hát..."
            required
          />
        </div>
      </form>
      <div className="flex gap-4 items-center">
        <div className="w-10 h-10 flex items-center justify-center rounded-full bg-[#393243]">
          <div
            className="cursor-pointer"
            onClick={() => {
              setClickedAccount(false);
              setClickedSetting(!clickedSetting);
            }}
          >
            <IconSetting />
          </div>
          <div
            className={`${
              !clickedSetting && "hidden"
            } absolute right-16 z-10 mt-32 w-56 origin-top-right rounded-md bg-[#34224f] shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none`}
          >
            {headeSettingItem.map((item, index) => (
              <div
                key={index}
                className="flex items-center text-white block px-2 py-2 gap-2 text-sm cursor-pointer"
              >
                <item.IconComponent />
                {item.label}
              </div>
            ))}
          </div>
        </div>
        <div>
          <div
            className="cursor-pointer"
            onClick={() => {
              setClickedSetting(false);
              setClickedAccount(!clickedAccount);
            }}
          >
            <IconUser />
          </div>
          <div
            className={`${
              !clickedAccount && "hidden"
            } absolute right-16 z-10 mt-2 w-56 origin-top-right rounded-md bg-[#34224f] shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none`}
          >
            {headerAccountItem.map((item, index) => (
              <div key={index} className="flex items-center">
                <item.IconComponent />
                <Link
                  href={item.link}
                  className="text-white block px-4 py-2 text-sm gap-2"
                >
                  {item.label}
                </Link>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Header;
