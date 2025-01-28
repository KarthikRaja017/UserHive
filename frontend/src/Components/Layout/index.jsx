import { Header } from "@/components/Header";

const Layout = ({ children }) => {
  return (
    <>
      <Header />
      <main className="container p-4">{children}</main>
    </>
  );
};

export default Layout;
