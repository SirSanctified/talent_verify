/* eslint-disable react/prop-types */
import {
  Table,
  TableHeader,
  TableColumn,
  TableBody,
  TableRow,
  TableCell,
} from "@nextui-org/react";
import AddCompany from "./AddCompany";
import AddEmployee from "./AddEmployee";
import AddDepartment from "./AddDepartment";
import AddRole from "./AddRole";
import { FaEdit, FaTrash } from "react-icons/fa";
import { axiosInstance } from "../pages/Dashboard";
import { useEffect, useState } from "react";
import DeletePopover from "./DeletePopover";

const handleDelete = async(url, data, setData) => {
  await axiosInstance.delete(url);
  setData(data.filter((item) => item.url !== url));
}

const DeleteIcon = () => (
  <FaTrash className="text-red-500 text-xl hover:text-red-800 hover:cursor-pointer" />
)

export default function CompanyTable({ data, itemId }) {
  const [elements, setElements] = useState(data);
  useEffect(() => {}, [elements]);
  return (
    <section className="mt-4 z-0">
      {itemId === "companies" ? (
        <AddCompany title="Add Company" action="Add" setCompanies={setElements} />
      ) : itemId === "departments" ? (
        <AddDepartment title={"Add Department"} action="Add" setDepartments={setElements} />
      ) : itemId === "employees" ? (
        <AddEmployee title="Add Employee" action="Add" setEmployees={setElements} />
      ) : itemId === "roles" ? (
        <AddRole title="Add Role" action="Add" setRoles={setElements} />
      ) : null}
      <Table aria-label={`Collection of ${itemId}`} className="mt-1">
        {itemId === "companies" ? (
          <TableHeader>
            <TableColumn>NAME</TableColumn>
            <TableColumn>ADDRESS</TableColumn>
            <TableColumn>REG NUMBER</TableColumn>
            <TableColumn></TableColumn>
            <TableColumn></TableColumn>
          </TableHeader>
        ) : itemId === "departments" ? (
          <TableHeader>
            <TableColumn>NAME</TableColumn>
            <TableColumn>COMPANY</TableColumn>
            <TableColumn></TableColumn>
            <TableColumn></TableColumn>
          </TableHeader>
        ) : itemId === "employees" ? (
          <TableHeader>
            <TableColumn>NAME</TableColumn>
            <TableColumn>ID</TableColumn>
            <TableColumn>JOINED</TableColumn>
            <TableColumn>LEFT</TableColumn>
            <TableColumn>ROLE</TableColumn>
            <TableColumn></TableColumn>
            <TableColumn></TableColumn>
          </TableHeader>
        ) : itemId === "roles" ? (
          <TableHeader>
            <TableColumn>NAME</TableColumn>
            <TableColumn>DEPARTMENT</TableColumn>
            <TableColumn></TableColumn>
            <TableColumn></TableColumn>
          </TableHeader>
        ) : null}
        <TableBody emptyContent={`No ${itemId} to display yet`}>
          {itemId === "companies"
            ? elements.map((item) => (
                <TableRow key={item.url}>
                  <TableCell>
                    <AddCompany
                      title={item.company_name}
                      action="Edit"
                      classes="bg-transperant text-blue-700"
                      company={item}
                    />
                  </TableCell>
                  <TableCell>{item.company_address}</TableCell>
                  <TableCell>{item.company_registration_number}</TableCell>
                  <TableCell><AddCompany title={<FaEdit className="text-blue-500 text-xl hover:text-blue-800 hover:cursor-pointer" />} action="Edit" company={item} classes="bg-transperant" /></TableCell>
                  <TableCell><DeletePopover btnTitle={<DeleteIcon />} itemName={item.company_name} itemType="Company" handleDelete={() => handleDelete(item.url, elements, setElements)} /></TableCell>
                </TableRow>
              ))
            : itemId === "departments"
            ? elements.map((item) => (
                <TableRow key={item.url}>
                  <TableCell>
                  <AddDepartment
                      title={item.department_name}
                      action="Edit"
                      classes="bg-transperant text-blue-700"
                      department={item}
                    />
                  </TableCell>
                  <TableCell>{item.company.company_name}</TableCell>
                  <TableCell><AddDepartment title={<FaEdit className="text-blue-500 text-xl hover:text-blue-800 hover:cursor-pointer" />} action="Edit" department={item} classes="bg-transperant" /></TableCell>
                  <TableCell><DeletePopover btnTitle={<DeleteIcon />} itemName={item.department_name} itemType="Department" handleDelete={() => handleDelete(item.url, elements, setElements)} /></TableCell>
                </TableRow>
              ))
            : itemId === "employees"
            ? elements.map((item) => (
                <TableRow key={item.url}>
                  <TableCell>
                  <AddEmployee
                      title={item.employee_name}
                      action="Edit"
                      classes="bg-transperant text-blue-700"
                      employee={item}
                    />
                  </TableCell>
                  <TableCell>{item.employee_id}</TableCell>
                  <TableCell>{item.date_started}</TableCell>
                  <TableCell>{item.date_left}</TableCell>
                  <TableCell>{item.role.role_name}</TableCell>
                  <TableCell><AddEmployee title={<FaEdit className="text-blue-500 text-xl hover:text-blue-800 hover:cursor-pointer" />} action="Edit" employee={item} classes="bg-transperant" /></TableCell>
                  <TableCell><DeletePopover btnTitle={<DeleteIcon />} itemName={item.employee_name} itemType="Employee" handleDelete={() => handleDelete(item.url, elements, setElements)} /></TableCell>
                </TableRow>
              ))
            : itemId === "roles"
            ? elements.map((item) => (
                <TableRow key={item.url}>
                  <TableCell>
                  <AddRole
                      title={item.role_name}
                      action="Edit"
                      classes="bg-transperant text-blue-700"
                      role={item}
                    />
                  </TableCell>
                  <TableCell>{item.department?.department_name || item.department_name}</TableCell>
                  <TableCell><AddRole title={<FaEdit className="text-blue-500 text-xl hover:text-blue-800 hover:cursor-pointer" />} action="Edit" role={item} classes="bg-transperant" /></TableCell>
                  <TableCell><DeletePopover btnTitle={<DeleteIcon />} itemName={item.role_name} itemType="Role" handleDelete={() => handleDelete(item.url, elements, setElements)} /></TableCell>
                </TableRow>
              ))
            : null}
        </TableBody>
      </Table>
    </section>
  );
}
