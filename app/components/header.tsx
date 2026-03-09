import Link from "next/link";
import Image from "next/image";
import { IoCartOutline } from "react-icons/io5";
import { CiSearch } from "react-icons/ci";
import { FaCaretDown, FaCaretRight } from "react-icons/fa";
import { CgProfile } from "react-icons/cg";

const listScroll = [
  "milk",
  "bread",
  "sugar",
  "butter",
  "paneer",
  "chocolate",
  "curd",
  "rice",
  "egg",
  "chips",
];

export default function Header() {
  return (
    <header className="w-full sticky top-0 z-50 bg-white text-black">
      <div className="flex items-center justify-between not-lg:flex-col py-3 h-full w-full border-b border-gray-200">
        <div className="flex items-center not-lg:justify-between lg:w-[35%] w-full">
          <Image
            src={"/Logo.svg"}
            alt="blinkit logo"
            width={176}
            height={86}
            className="px-3 lg:block hidden"
          />
          <div className="px-5 not-lg:w-[85%]">
            <h3 className="font-bold text-xl">Delivery in 23 minutes</h3>
            <div className="flex gap-2">
              <p className="text-sm line-clamp-1">
                6, Murugesan St, near Harrington Road Subway, Aminjikarai, Mukta
                Gardens, Shenoy Nagar, Chennai, Tamil Nadu 600031, India
              </p>
              <FaCaretDown className="text-2xl" />
            </div>
          </div>
          <div>
            <CgProfile className="text-2xl lg:hidden mr-5" />
          </div>
        </div>
        <div className="lg:w-[40%] w-full border h-15 border-gray-200 rounded-2xl overflow-hidden bg-gray-100 flex items-center not-lg:p-6">
          <Link href={"/s"}>
            <div className="flex items-center">
              <CiSearch className="text-2xl lg:mx-4" />
              <div className="auto-scroll-y flex flex-col">
                {listScroll.concat(listScroll).map((l, i) => (
                  <p key={i} className="my-4 py-2 px-4 text-gray-500">
                    Search &quot;{l}&quot;
                  </p>
                ))}
              </div>
            </div>
          </Link>
        </div>
        <div className="lg:flex items-center justify-around w-[20%] hidden">
          {/* <Link href={"login"} className="text-xl"> */}
          Login
          {/* </Link> */}
          <button
            className="text-sm font-bold bg-gray-200 text-white p-3 rounded-2xl flex items-center gap-2 cursor-not-allowed"
            disabled={false}
          >
            <IoCartOutline className="text-3xl" /> My Cart
          </button>
        </div>
      </div>
      <div className="lg:hidden w-[95%] fixed bottom-0 m-5 flex items-center justify-between p-2 bg-[#0c831f] text-white rounded-2xl">
        <div className="flex items-center gap-1">
          <IoCartOutline className="text-3xl bg-green-300 rounded-lg p-0.5" />
          <div className="text-sm">
            <p>item</p>
            <p>$</p>
          </div>
        </div>
        <p className="flex items-center gap-1">
          Veiw Cart <FaCaretRight />{" "}
        </p>
      </div>
    </header>
  );
}
