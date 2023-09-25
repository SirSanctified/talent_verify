import { Outlet } from "react-router-dom";
import Nav from "./Nav";
import Footer from "./Footer";

const Layout = () => (
  <>
    <Nav />
    <Outlet />
    <Footer />
  </>
);
export default Layout;
