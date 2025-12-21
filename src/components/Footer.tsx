import { AiFillInstagram } from "react-icons/ai";
import { BsFillThreadsFill } from "react-icons/bs";
import { FaFacebook, FaLinkedin } from "react-icons/fa";
import { FaSquareXTwitter } from "react-icons/fa6";
import appstore from "../assets/app-store.png";
import playstore from "../assets/play-store.png";
import { useState } from "react";

interface LinksType {
  key: number;
  li: string;
  href: string;
}

const Footer = () => {
  const usefulLinks1: LinksType[] = [
    { key: 1, li: "Blog", href: "/blog" },
    { key: 2, li: "Privacy", href: "/privacy" },
    { key: 3, li: "Terms", href: "/terms" },
    { key: 4, li: "FAQs", href: "/faqs" },
    { key: 5, li: "Security", href: "/security" },
    { key: 6, li: "Contact", href: "/contact" },
  ];
  const usefulLinks2: LinksType[] = [
    { key: 1, li: "Partner", href: "/partner" },
    { key: 2, li: "Franchise", href: "/franchise" },
    { key: 3, li: "Seller", href: "/seller" },
    { key: 4, li: "Warehouse", href: "/warehouse" },
    { key: 5, li: "Deliver", href: "/deliver" },
    { key: 6, li: "Resources", href: "/resources" },
  ];
  const usefulLinks3: LinksType[] = [
    { key: 1, li: "Recipes", href: "/recipes" },
    { key: 2, li: "Bistro", href: "/bistro" },
    { key: 3, li: "Distric", href: "/distric" },
  ];

  const categories: LinksType[] = [
    { key: 1, li: "Vegetables & Fruits", href: "/vegetables-fruits" },
    { key: 2, li: "Dairy & Breakfast", href: "dairy-breakfast" },
    { key: 3, li: "Munchies", href: "Munchies" },
    { key: 4, li: "Cold Drinks & Juices", href: "cold-drinks-juices" },
    { key: 5, li: "Instant & Frozen Food", href: "instant-frozen-food" },
    { key: 6, li: "Tea, Coffee & Milk Drinks", href: "tea-coffee-milk-drinks" },
    { key: 7, li: "Bakery & Biscuits", href: "" },
    { key: 8, li: "Sweet Tooth", href: "" },
    { key: 9, li: "Atta, Rice & Dal", href: "" },
    { key: 10, li: "Dry Fruits, Masala & Oil", href: "" },
    { key: 11, li: "Sauces & Spreads", href: "" },
    { key: 12, li: "Chicken, Meat & Fish", href: "" },
    { key: 13, li: "Paan Corner", href: "" },
    { key: 14, li: "Organic & Premium", href: "" },
    { key: 15, li: "Baby Care", href: "" },
    { key: 16, li: "Pharma & Wellness", href: "" },
    { key: 17, li: "Cleaning Essentials", href: "" },
    { key: 18, li: "Home Furnishing & Decor", href: "" },
    { key: 19, li: "Personal Care", href: "" },
    { key: 20, li: "Pet Care", href: "" },
    { key: 21, li: "Beauty & Cosmetics", href: "" },
    { key: 22, li: "Kitchen & Dining", href: "" },
    { key: 23, li: "Fashion & Accessories", href: "" },
    { key: 24, li: "Electronics & Electricals", href: "" },
    { key: 25, li: "Stationery Needs", href: "" },
    { key: 26, li: "Books", href: "" },
    { key: 27, li: "Toys & Games", href: "" },
    { key: 28, li: "Print Store", href: "" },
    { key: 29, li: "E-Gift Cards", href: "" },
    { key: 30, li: "Rakhi Gifts", href: "" },
  ];

  const [isFooterOpen, setIsFooterOpen] = useState<boolean>(false);

  const showFooter = (): void => {
    setIsFooterOpen((prev) => !prev);
  };

  return (
    <>
      <div
        className="text-gray font-bold lg:hidden md:hidden flex justify-between items-center m-2"
        onClick={showFooter}
      >
        <span>India's last minute app - blinkit</span>
        <span>{isFooterOpen ? "-" : "+"}</span>
      </div>
      <div
        className={`lg:m-10 m-6 ${isFooterOpen ? "block" : "hidden"} md:block `}
      >
        <footer className="md:grid md:grid-cols-[35%_65%] grid grid-cols-1 m-auto gap-4">
          <div>
            <div className="font-bold">Useful Links</div>
            <div className="text-[14px] font-light mt-2.5">
              <ul className="grid grid-cols-3">
                <li>
                  <ul className="grid gap-2">
                    {usefulLinks1.map((links) => (
                      <li key={links.key}>
                        <a href={links.href}>{links.li}</a>
                      </li>
                    ))}
                  </ul>
                </li>
                <li>
                  <ul className="grid gap-2">
                    {usefulLinks2.map((links) => (
                      <li key={links.key}>
                        <a href={links.href}>{links.li}</a>
                      </li>
                    ))}
                  </ul>
                </li>
                <li>
                  <ul className="grid gap-2">
                    {usefulLinks3.map((links) => (
                      <li key={links.key}>
                        <a href={links.href}>{links.li}</a>
                      </li>
                    ))}
                  </ul>
                </li>
              </ul>
            </div>
          </div>
          <div>
            <div className="font-bold ">
              Categories{" "}
              <span className="text-green ml-3 font-light">see all</span>
            </div>
            <ul className="md:grid md:grid-cols-3 grid grid-cols-2 text-[14px] font-light gap-3 mt-5">
              {categories.map((links) => (
                <li key={links.key}>
                  <a href={links.href}>{links.li}</a>
                </li>
              ))}
            </ul>
          </div>
        </footer>
        <div className="md:gird md:grid-cols-3 md:justify-center md:items-center grid grid-cols-1 justify-center items-center text-center my-10">
          <div className="text-[12px] font-light text-gray">
            &copy; Blink Commerce Private Limited, 2016-2025
          </div>
          <div className="flex gap-3 justify-center items-center mt-5">
            <div>Download App</div>
            <div className="flex justify-center items-center gap-3">
              <img
                src={appstore}
                alt=""
                className="object-fill"
                width={92}
                height={30}
              />
              <img
                src={playstore}
                alt=""
                className="object-fill"
                width={92}
                height={30}
              />
            </div>
          </div>
          <div className="flex text-3xl md:gap-7 object-fill justify-center items-center mt-5 gap-3">
            <FaFacebook />
            <FaSquareXTwitter />
            <AiFillInstagram />
            <FaLinkedin />
            <BsFillThreadsFill />
          </div>
        </div>
        <div className="text-[14px] text-gray leading-[1.8]">
          “Blinkit” is owned & managed by "Blink Commerce Private Limited" and
          is not related, linked or interconnected in whatsoever manner or
          nature, to “GROFFR.COM” which is a real estate services business
          operated by “Redstone Consultancy Services Private Limited”.
        </div>
      </div>
    </>
  );
};

export default Footer;
