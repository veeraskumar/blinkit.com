import Image from "next/image";
import Cards from "./components/cards";
import ProductRow from "./layouts/cradscroll";

const listOfImage = [
  "/paan-corner_web.avif",
  "/Slice-2_10.avif",
  "/Slice-3_9.avif",
  "/Slice-4_9.avif",
  "/Slice-5_4.avif",
  "/Slice-6_5.avif",
  "/Slice-7_3.avif",
  "/Slice-7-1_0.avif",
  "/Slice-8_4.avif",
  "/Slice-10.avif",
  "/Slice-11.avif",
  "/Slice-12.avif",
  "/Slice-13.avif",
  "/Slice-14.avif",
  "/Slice-15.avif",
  "/Slice-16.avif",
  "/Slice-17.avif",
  "/Slice-18.avif",
  "/Slice-19.avif",
  "/Slice-20.avif",
];
export default function Home() {
  return (
    <div className="w-full lg:px-10 px-2">
      <div className="lg:block hidden">
        <div className="relative w-full p-5 h-60">
          <Image
            src={"/frame-1.avif"}
            alt="/frame1"
            className="absolute"
            fill
            loading="lazy"
            sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
          />
        </div>
        <div className="flex items-center gap-3 p-5">
          <div className="relative w-full p-5 h-50">
            <Image
              src={"/pharmacy-WEB.avif"}
              alt="/frame1"
              className="absolute"
              fill
              loading="lazy"
              sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
            />
          </div>
          <div className="relative w-full p-5 h-50">
            <Image
              src={"/pet_crystal_WEB-1.avif"}
              alt="/frame1"
              className="absolute"
              fill
              loading="lazy"
              sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
            />
          </div>
          <div className="relative w-full p-5 h-50">
            <Image
              src={"/baby_crystal_WEB-1.avif"}
              alt="/frame1"
              className="absolute"
              fill
              loading="lazy"
              sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
            />
          </div>
        </div>
      </div>
      <div className="grid lg:grid-cols-10 md:grid-cols-4 grid-cols-4">
        {listOfImage.map((l, i) => (
          <div key={i} className="relative w-full lg:p-5 h-50 p-2">
            <Image
              src={l}
              alt={l}
              className="absolute object-contain"
              fill
              sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
            />
          </div>
        ))}
      </div>
      <div>
        <div>
          <div className="flex items-center justify-between">
            <h3 className="text-2xl font-semibold">Dairy, Bread & Eggs</h3>
            <p className="text-[#0c831f] text-[20px]">see all</p>
          </div>
          <ProductRow>
            <Cards category={["milk"]} />
          </ProductRow>
        </div>
        <div>
          <div className="flex items-center justify-between">
            <h3 className="text-2xl font-semibold">Rolling paper & tobacco</h3>
            <p className="text-[#0c831f] text-[20px]">see all</p>
          </div>
          <ProductRow>
            <Cards category={["milk"]} />
          </ProductRow>
        </div>
        <div>
          <div className="flex items-center justify-between">
            <h3 className="text-2xl font-semibold">Snacks & Munchies</h3>
            <p className="text-[#0c831f] text-[20px]">see all</p>
          </div>
          <ProductRow>
            <Cards category={["milk"]} />
          </ProductRow>{" "}
        </div>
        <div>
          <div className="flex items-center justify-between">
            <h3 className="text-2xl font-semibold">Hookah</h3>
            <p className="text-[#0c831f] text-[20px]">see all</p>
          </div>

          <ProductRow>
            <Cards category={["milk"]} />
          </ProductRow>
        </div>
        <div>
          <div className="flex items-center justify-between">
            <h3 className="text-2xl font-semibold">Mouth fresheners</h3>
            <p className="text-[#0c831f] text-[20px]">see all</p>
          </div>
          <ProductRow>
            <Cards category={["milk"]} />
          </ProductRow>
        </div>
        <div>
          <div className="flex items-center justify-between">
            <h3 className="text-2xl font-semibold">Cold Drinks & Juices</h3>
            <p className="text-[#0c831f] text-[20px]">see all</p>
          </div>
          <ProductRow>
            <Cards category={["milk"]} />
          </ProductRow>
        </div>
        <div>
          <div className="flex items-center justify-between">
            <h3 className="text-2xl font-semibold">Candies & Gums</h3>
            <p className="text-[#0c831f] text-[20px]">see all</p>
          </div>
          <ProductRow>
            <Cards category={["milk"]} />
          </ProductRow>
        </div>
      </div>
    </div>
  );
}
