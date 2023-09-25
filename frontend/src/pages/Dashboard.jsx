/* eslint-disable react-refresh/only-export-components */
import { Tabs, Tab } from "@nextui-org/react";
import { useLoaderData } from "react-router-dom";
import { tabs } from "../constants";
import axios from "axios";

export const axiosInstance = axios.create({
  baseURL: "http://127.0.0.1:8000",
  withCredentials: true,
});

function Dashboard() {
  const data = useLoaderData();
  const { companies, departments, employees, roles } = data;
  return (
    <main className=" min-h-screen overflow-x-scroll mt-8 px-4 md:max-w-[98%] lg:max-w-[75%] mx-auto z-0">
      <Tabs aria-label="Dynamic tabs" items={tabs} className="-z-50">
        {(item) => (
          <Tab key={item.id} title={item.label}>
            <item.content
              data={
                item.id === "companies"
                  ? companies
                  : item.id === "departments"
                  ? departments
                  : item.id === "employees"
                  ? employees
                  : item.id === "roles"
                  ? roles
                  : null
              }
              itemId={item.id}
            />
          </Tab>
        )}
      </Tabs>
    </main>
  );
}

export const loader = async () => {
  try {
    const companies = (await axiosInstance.get("/companies/")).data;
    const employees = (await axiosInstance.get("/employees/")).data;
    const departments = (await axiosInstance.get("/departments/")).data;
    const roles = (await axiosInstance.get("/roles/")).data;
    const data = { companies, employees, departments, roles };
    return data;
  } catch (error) {
    return error.message;
  }
};

export default Dashboard;
