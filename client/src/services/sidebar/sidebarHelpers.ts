import {
  IconDiscovery,
  IconLibrary,
  IconListMusic,
  IconLove,
  IconRecently,
  IconZingchart,
  IconTopic,
  IconTop100,
  IconUpload,
} from "@/assets/icons";

export enum SelectedOptionSidebar {
  Discovery = "discovery",
  Chart = "chart",
  Library = "library",
  Theme = "theme",
  Top100 = "top100",
  History = "history",
  Favorite = "favorite",
  Playlist = "playlist",
  Upload = "upload",
}

export const sidebarItems = [
  {
    id: SelectedOptionSidebar.Discovery,
    lable: "Khám phá",
    IconComponent: IconDiscovery,
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
  {
    id: SelectedOptionSidebar.Upload,
    lable: "Đã tải lên",
    IconComponent: IconUpload,
    link: "/upload",
  },
];
