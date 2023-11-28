import { NextPage } from "next";

interface ButtonSidebarProps {
  children?: React.ReactNode;
  IconComponent: () => JSX.Element;
  selected?: boolean;
  onClick?: () => void;
}

const ButtonSidebar: NextPage<ButtonSidebarProps> = (props) => {
  const { children, IconComponent, selected, ...otherProps } = props;

  return (
    <button
      className={`${
        selected ? "bg-[#393243] border-l-4 border-[#9b4de0]" : "bg-[#231b2e]"
      } text-white text-sm font-medium w-full flex items-center justify-start gap-2 py-3 px-5`}
      {...otherProps}
    >
      <IconComponent />
      {children}
    </button>
  );
};

export default ButtonSidebar;
