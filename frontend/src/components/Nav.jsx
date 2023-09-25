import {useState} from "react";
import {
  Navbar,
  NavbarBrand,
  NavbarContent,
  NavbarItem,
  Link,
} from "@nextui-org/react";
import { FaBars, FaTimes } from "react-icons/fa"
import SignInModal from "./SignInModal"

export default function Nav() {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <Navbar position="static" className="bg-black/30">
      <NavbarBrand>
        <p className="flex items-center justify-center px-4 py-2 rounded-full bg-gray-500 mr-2 text-xl font-bold">T.</p>
        <p className="font-bold text-inherit">Talent Verify</p>
      </NavbarBrand>
      <NavbarContent className="hidden sm:flex gap-4" justify="center">
        <NavbarItem isActive>
          <Link color="foreground" href="/" aria-current="page">
            Home
          </Link>
        </NavbarItem>
        <NavbarItem>
          <Link color="foreground" href="/dashboard">
            Dashboard
          </Link>
        </NavbarItem>
        <NavbarItem>
          <Link color="foreground" href="#">
            Services
          </Link>
        </NavbarItem>
      </NavbarContent>
      <NavbarContent justify="end">
        <NavbarItem>
          <SignInModal title="Login" />
        </NavbarItem>
        <NavbarItem className="block sm:hidden z-50">
          {isOpen
            ? (
                <>
                  <FaTimes
                    size={32}
                    onClick={() => setIsOpen(!isOpen)}
                  />
                  <NavbarContent className="flex flex-col items-start bg-black text-white h-max w-screen gap-4 absolute left-0 top-16 px-8 py-8 z-50">
                    <NavbarItem isActive>
                      <Link className="text-white" href="#" aria-current="page">
                        Home
                      </Link>
                    </NavbarItem>
                    <NavbarItem>
                      <Link className="text-white" href="#">
                        Customers
                      </Link>
                    </NavbarItem>
                    <NavbarItem>
                      <Link className="text-white" href="#">
                        Services
                      </Link>
                    </NavbarItem>
                  </NavbarContent>
                </>
              )
            : <FaBars
                size={32}
                className="hover:cursor-pointer"
                onClick={() => setIsOpen(!isOpen)}
              />
          }
        </NavbarItem>
      </NavbarContent>
    </Navbar>
  );
}
