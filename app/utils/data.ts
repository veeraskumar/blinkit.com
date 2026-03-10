import { CardDataType } from "../types/cardstype";
import products from "../../public/products.json";

export default async function getData() {
  // const res = await fetch("/products.json");

  // if (!res.ok) throw new Error();

  const data = products;

  return data;
}
