/* eslint-disable react/prop-types */
import {
  Modal,
  ModalContent,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Button,
  useDisclosure,
  Input,
  Select,
  SelectItem,
} from "@nextui-org/react";
import { useEffect, useState } from "react";
import { FaArrowRight } from "react-icons/fa";
import { axiosInstance } from "../pages/Dashboard";
import axios from "axios";

// eslint-disable-next-line react/prop-types
export default function AddDepartment({ classes, title, action, department, setDepartments }) {
  const { isOpen, onOpen, onOpenChange } = useDisclosure();
  const [departmentName, setDepartmentName] = useState(
    department?.department_name || ""
  );
  const [company, setCompany] = useState(department?.company?.url || new Set([]));
  const [companies, setCompanies] = useState([]);

  useEffect(() => {
    const getCompanies = async () => {
      try {
        const response = await axiosInstance.get("/companies/");
        setCompanies(response.data);
      } catch (error) {
        console.log(error);
      }
    };
    getCompanies();
  }, []);

  const handleSave = async() => {
    try {
      if(department) {
        await axios.patch(department.url, {department_name: departmentName, company: Array.from(company.values())[0] || company}, {withCredentials: true})
      } else {
        const response = await axiosInstance.post("/departments/", {department_name: departmentName, company: Array.from(company.values())[0]});
        const newDepartment = await axios.get(response.data.url, {
          withCredentials: true,
        });
        setDepartments((prev) => [...prev, newDepartment.data]);
        setCompany(new Set([]))
        setDepartmentName("")
      }
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <>
      <Button
        variant={classes ? "flat" : "shadow" }
        className={classes ? classes : "bg-black/80 text-white"}
        endContent={
          classes ? null : (
            <FaArrowRight className="text-xl bg-gray-300 px-1 py-1 text-black rounded-full" />
          )
        }
        onPress={onOpen}
      >
        {title}
      </Button>
      <Modal isOpen={isOpen} onOpenChange={onOpenChange} placement="top-center">
        <ModalContent>
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1">
                {action} Department
              </ModalHeader>
              <ModalBody>
                <Input
                  isRequired
                  autoFocus
                  label="Department Name"
                  placeholder="Enter department name"
                  value={departmentName}
                  onChange={(e) => setDepartmentName(e.target.value)}
                  variant="bordered"
                />
                <Select
                  label={department && department?.company?.url  === company ? department?.company?.company_name : "Company"}
                  isRequired
                  placeholder="Select a company"
                  items={companies}
                  selectedKeys={company}
                  onSelectionChange={setCompany}
                  variant="bordered"
                >
                  {companies.map((company) => (
                    <SelectItem key={company.url} value={company.url} className="text-black">
                      {company.company_name}
                    </SelectItem>
                  ))}
                </Select>
              </ModalBody>
              <ModalFooter>
                <Button color="danger" variant="flat" onPress={onClose}>
                  Close
                </Button>
                <Button
                  className="bg-black/80 disabled:bg-gray-400 text-white font-semibold"
                  onPress={() => {
                    handleSave();
                    onClose();
                  }}
                >
                  Save
                </Button>
              </ModalFooter>
            </>
          )}
        </ModalContent>
      </Modal>
    </>
  );
}
