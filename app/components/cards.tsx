import { CardDataType } from "../types/cardstype";

export default function Cards({ data }: { data: CardDataType[] }) {
  return (
    <div>
      {data.map((d) => (
        <div key={d.id}>{d.imgUrl}</div>
      ))}
    </div>
  );
}
