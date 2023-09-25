import {FaTwitter, FaInstagram, FaFacebook, FaLinkedin } from "react-icons/fa";

export default function Footer() {
  return (
    <footer className="flex flex-col gap-2 items-center justify-center my-16">
      <div className="flex gap-4 items-center justify-center">
        <FaTwitter size={32} />
        <FaInstagram size={32} />
        <FaFacebook size={32} />
        <FaLinkedin size={32} />
      </div>
      <p className="text-center">&copy;{new Date().getFullYear()} Talent Verify</p>
    </footer>
  );
}