import {
  IconDiscover,
  IconLibrary,
  IconListMusic,
  IconLove,
  IconRecently,
  IconZingchart,
  IconTopic,
  IconTop100,
} from "@/assets/icons";

export enum SelectedOptionSidebar {
  Discover = "discover",
  Chart = "chart",
  Library = "library",
  Theme = "theme",
  Top100 = "top100",
  History = "history",
  Favorite = "favorite",
  Playlist = "playlist",
}

export const sidebarItems = [
  {
    id: SelectedOptionSidebar.Discover,
    lable: "Khám phá",
    IconComponent: IconDiscover,
    link: "/",
  },
  {
    id: SelectedOptionSidebar.Chart,
    lable: "Bảng xếp hạng",
    IconComponent: IconZingchart,
    link: "/chart",
  },
  {
    id: SelectedOptionSidebar.Theme,
    lable: "Chủ đề & Thể loại",
    IconComponent: IconTopic,
    link: "/hub",
  },
  {
    id: SelectedOptionSidebar.Top100,
    lable: "Top 100",
    IconComponent: IconTop100,
    link: "/top100",
  },
  {
    id: SelectedOptionSidebar.Library,
    lable: "Thư viện",
    IconComponent: IconLibrary,
    link: "/library",
  },
  {
    id: SelectedOptionSidebar.History,
    lable: "Nghe gần đây",
    IconComponent: IconRecently,
    link: "/history",
  },
  {
    id: SelectedOptionSidebar.Favorite,
    lable: "Bài hát yêu thích",
    IconComponent: IconLove,
    link: "/favorite",
  },
  {
    id: SelectedOptionSidebar.Playlist,
    lable: "Playlist",
    IconComponent: IconListMusic,
    link: "/playlist",
  },
];
