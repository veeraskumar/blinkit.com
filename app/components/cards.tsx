import Image from "next/image";
// import { CardDataType } from "../types/cardstype";
import getData from "../utils/data";
import { LuTimer } from "react-icons/lu";

export default async function Cards({ category }: { category: string[] }) {
  const data = await getData();

  const filterData = data.filter(
    (d) => d.recommended === true && category.includes(d.category),
  );

  return (
    <>
      {filterData.map((d, i) => (
        <div
          key={i}
          className="lg:min-w-45 bg-white shadow shadow-gray-200 sm:min-w-70 min-w-40 p-1 my-1"
        >
          <div className="relative w-full p-5 h-50">
            <Image
              src={d.imgUrl}
              alt={d.title}
              fill
              className="object-contain"
            />
          </div>
          <div className="flex flex-col gap-1">
            <p className="flex items-center text-[9px] font-bold">
              <LuTimer />
              {d.deliveryTime} MINS
            </p>
            <h3 className="text-sm font-semibold line-clamp-2">{d.title}</h3>
            <p className="text-[#666] text-[12px]">{d.quanity}</p>
            <div className="flex items-center justify-between p-1">
              <div className="">
                {d.discount ? (
                  <>
                    <p className="text-[12px] font-semibold">
                      ₹{d.price - d.price * (d.discount / 100)}
                    </p>
                    <p className="line-through text-[12px] text-[#828282]">
                      ₹{d.price}
                    </p>
                  </>
                ) : (
                  <p className="text-[12px] font-semibold">₹{d.price}</p>
                )}
              </div>
              <div>
                <p className="bg-white text-[#318616] border border-[#318616] py-2 px-5 text-sm rounded-xl flex items-center justify-evenly">
                  Add
                </p>
              </div>
            </div>
          </div>
        </div>
      ))}
    </>
  );
}
