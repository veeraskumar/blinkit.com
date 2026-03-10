"use client";

import { useRef } from "react";
import { MdNavigateBefore, MdNavigateNext } from "react-icons/md";

export default function ProductRow({
  children,
}: {
  children: React.ReactNode;
}) {
  const scrollRef = useRef<HTMLDivElement>(null);

  const scroll = (dir: "left" | "right") => {
    if (!scrollRef.current) return;

    const amount = 300;

    scrollRef.current.scrollBy({
      left: dir === "left" ? -amount : amount,
      behavior: "smooth",
    });
  };

  return (
    <div className="w-full relative mb-2">
      <button
        onClick={() => scroll("left")}
        className="hidden lg:flex absolute left-0 top-1/2 -translate-y-1/2 z-10 rounded-2xl  bg-white shadow p-2"
      >
        <MdNavigateBefore className="text-2xl" />
      </button>

      <div
        ref={scrollRef}
        className="flex gap-3 overflow-x-auto hide-scrollbar scroll-smooth"
      >
        {children}
      </div>

      <button
        onClick={() => scroll("right")}
        className="hidden lg:flex absolute right-0 top-1/2 -translate-y-1/2 z-10 rounded-2xl  bg-white shadow p-2"
      >
        <MdNavigateNext className="text-2xl" />
      </button>
    </div>
  );
}
