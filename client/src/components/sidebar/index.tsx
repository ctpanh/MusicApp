"use client";
import { useEffect, useState } from "react";
import ButtonSidebar from "./buttonSideBar";
import {
  SelectedOptionSidebar,
  sidebarItems,
} from "@/services/sidebar/sidebarHelpers";
import Link from "next/link";
import { usePathname } from "next/navigation";
import Image from "next/image";
import { IconAdd } from "@/assets/icons";

const Sidebar = () => {
  const [selectedOption, setSelectedOption] = useState<SelectedOptionSidebar>(
    SelectedOptionSidebar.Discovery
  );
  const logoUrl =
    "https://zmp3-static.zmdcdn.me/skins/zmp3-v6.1/images/backgrounds/logo-dark.svg";
  const currentURL = usePathname();
  useEffect(() => {
    if (currentURL.includes("chart")) {
      setSelectedOption(SelectedOptionSidebar.Chart);
    } else if (currentURL.includes("library")) {
      setSelectedOption(SelectedOptionSidebar.Library);
    } else if (currentURL.includes("hub")) {
      setSelectedOption(SelectedOptionSidebar.Theme);
    } else if (currentURL.includes("top100")) {
      setSelectedOption(SelectedOptionSidebar.Top100);
    } else if (currentURL.includes("history")) {
      setSelectedOption(SelectedOptionSidebar.History);
    } else if (currentURL.includes("favorite")) {
      setSelectedOption(SelectedOptionSidebar.Favorite);
    } else if (currentURL.includes("playlist")) {
      setSelectedOption(SelectedOptionSidebar.Playlist);
    } else if (currentURL.includes("upload")) {
      setSelectedOption(SelectedOptionSidebar.Upload);
    } else {
      setSelectedOption(SelectedOptionSidebar.Discovery);
    }
  }, [currentURL]);
  return (
    <div className="h-full w-[240px] flex flex-col bg-[#231b2e]">
      <div className="flex items-center px-5 h-[70px] w-[240px]">
        <Image src={logoUrl} width={120} height={40} alt="logo" />
      </div>
      <div className="overflow-auto">
        {sidebarItems.map((item, index) => (
          <Link key={index} href={item.link}>
            <ButtonSidebar
              IconComponent={item.IconComponent}
              selected={selectedOption === item.id}
              onClick={() => setSelectedOption(item.id)}
            >
              {item.lable}
            </ButtonSidebar>
          </Link>
        ))}
      </div>
      <div className="fixed w-[240px] h-[70px] bottom-0 flex items-center border-t px-6 bottom-0 cursor-pointer">
        <IconAdd />
        <div className="text-white font-medium">Tạo playlist mới</div>
      </div>
    </div>
  );
};

export default Sidebar;
