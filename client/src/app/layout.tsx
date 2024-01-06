import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "../../public/globals.css";
import Sidebar from "@/components/sidebar";
import Header from "@/components/header";
import AudioPlayer from "@/components/audio/AudioPlayer";
import AuthWatcher from "@/components/authwatcher";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "ANT Music",
  icons:
    "https://static-zmp3.zmdcdn.me/skins/zmp3-v5.2/images/icon_zing_mp3_60.png",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <AuthWatcher />
      <body className={inter.className}>
        <main className="h-screen flex flex-col justify-between bg-[#170f23]">
          <div className="h-[calc(100%_-_84px)] flex">
            <Sidebar />
            <div className="w-full h-full">
              <Header />
              {children}
            </div>
          </div>
          <div className="h-[84px]">
            <AudioPlayer />
          </div>
        </main>
      </body>
    </html>
  );
}
