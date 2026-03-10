import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import Header from "./components/header";
import Footer from "./components/footer";

const okra = localFont({
  src: [
    {
      path: "./fonts/Okra-Regular.woff2",
      weight: "400",
      style: "normal",
    },
    {
      path: "./fonts/Okra-Medium.woff2",
      weight: "500",
      style: "normal",
    },
    {
      path: "./fonts/Okra-Bold.woff2",
      weight: "600",
      style: "normal",
    },
  ],
  variable: "--font-okra",
});

export const metadata: Metadata = {
  title: "30,000+ products delivered to your doorstep | Blinkit",
  description:
    "Shop online for groceries and get your order delivered to your doorstep. Enjoy delivery of 30,000+ products with Blinkit",
  keywords: [
    "Buy Grocery Online",
    "Online Grocery",
    "Grofers",
    "Groffers",
    "Groferss",
    "blinkit grofers",
    "blinkit",
    "blink it",
    "Grocery Store",
    "Online Grocery Shopping",
    "Online Grocery Store",
    "Online Supermarket",
    "Free Delivery",
    "Great Offers",
    "Best Prices",
  ],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={okra.variable}>
        <Header />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
