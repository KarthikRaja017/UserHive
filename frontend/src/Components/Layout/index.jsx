import Header from "../Header";
const Layout = ({ children }) => {
  return (
    <>
      <Header />
      <main className="container p-4">{children}</main>
    </>
  );
};

export default Layout;
