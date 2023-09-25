import React from "react";
import { FaHandshake, FaPercent, FaSave, FaArrowRight } from "react-icons/fa";;
import {Card, CardBody} from "@nextui-org/react";

function StatCard({icon, heading, body}) {
  return (
    <Card className="min-w-[100%] md:min-w-[60vw] flex flex-row items-center justify-between gap-2 md:w-[60vw]" shadow>
      <CardBody>
        <div className="h-[100%] bg-gray-300 w-max p-4 rounded-full">{icon}</div>
      </CardBody>
      <CardBody>
        <div className="flex flex-col gap-2">
          <h1 className="text-xl font-semibold">{heading}</h1>
          <p>{body}</p>
        </div>
      </CardBody>
      <CardBody><FaArrowRight size={32} /></CardBody>
    </Card>
  );
}
const stats = [
{
  icon: <FaHandshake size={36} />,
  heading: "60,000+",
  body: "Companies Verified"
},
{
  icon: <FaSave size={36} />,
  heading: "300,000",
  body: "Employee Records Managed"
},
{
  icon: <FaPercent size={36} />,
  heading: "99.7%",
  body: "Accuracy Rate"
}
];
export default function Stats() {
  return (
    <section className="w-[100%] flex flex-col items-center mt-16 px-4 md:px-0 gap-4">
      {stats.map(stat => (
        <StatCard key={stat.heading} icon={stat.icon} heading={stat.heading} body={stat.body} />
      ))}
    </section>
  );
}
