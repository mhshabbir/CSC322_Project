import product1 from "./assets/products/1.png";
import product2 from "./assets/products/2.png";
import product3 from "./assets/products/3.png";
import product4 from "./assets/products/9.png";

export const PRODUCTS = [
  {
    id: 1,
    productName: "IPhone",
    price: 999.0,
    productImage: product1,
    category: "Motherboard",
    reviews: ["Great product ID 1"],
    productlink: "/product/product1",
  },
  {
    id: 2,
    productName: "Macbook Pro 2022 (M1)",
    price: 1999.0,
    productImage: "https://c1.neweggimages.com/ProductImage/34-156-153-V07.jpg",
    category: "CPU",
    reviews: ["Great product id 2","cool","nice"],
    productlink: "/product/product2",
  },
  {
    id: 3,
    productName: "Cannon M50 Camera",
    price: 699.0,
    productImage: product3,
    category: "Case",
    reviews: ["Great product id 2","cool","nice"],
    productlink: "/product/product3",
  },
  {
    id: 4,
    productName: "Dell XPS 15",
    price: 2400.0,
    productImage: product4,
    category: "Motherboard",
    reviews: ["Good Product ID 3"],
    productlink: "/product/product4",
  },
  {
  id: 5,
  productName: "Dell XPS 15",
  price: 2400.0,
  productImage: product4,
  category: "CPU",
  reviews: ["Good Product ID 3"],
  productlink: "/product/product4",
},
];
