/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "photo-zmp3.zmdcdn.me",
        port: "",
        pathname: "/banner/**",
      },
      {
        protocol: "https",
        hostname: "photo-resize-zmp3.zmdcdn.me",
        port: "",
        pathname: "/**",
      },
    ],
  },
};

module.exports = nextConfig;
