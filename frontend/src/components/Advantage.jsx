import {Image} from "@nextui-org/react";
import advantage from "../assets/advantage.webp";

export default function Advantage() {
  return (
    <section className="flex flex-col md:flex-row gap-8 items-center justify-center mt-16 px-4 md:px-0">
      <Image
        isZoomed
        width={300}
        height={350}
        src={advantage}
        alt="NextUI Album Cover"
        classNames="m-5 md"
      />
      <div>
        <h1 className="text-2xl font-semibold mb-4">Fully Customizable<br/>Employee Verification<br />Solution</h1>
        <p className="max-w-[40ch] lg:max-w-[60ch]">Talent Verify Online caters to businesses of all shapes and sizes, with customizable solutions for every industry</p>
      </div>
    </section>
  );
}