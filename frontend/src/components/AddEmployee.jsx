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

export default function AddEmployee({ title, classes, action, employee, setEmployees}) {
  const { isOpen, onOpen, onOpenChange } = useDisclosure();
  const [employeeName, setEmployeeName] = useState(employee?.employee_name || "");
  const [dateJoined, setDateJoined] = useState(employee?.date_started || new Date().getDate());
  const [dateLeft, setDateLeft] = useState(employee?.date_left || new Date().getDate());
  const [employeeID, setEmployeeID] = useState(employee?.employee_id || "");
  const [role, setRole] = useState(employee?.role?.url || new Set([]));
  const [roles, setRoles] = useState([]);

  useEffect(() => {
    const getRoles = async () => {
      try {
        const response = await axiosInstance.get("/roles/");
        setRoles(response.data);
      } catch (error) {
        console.log(error);
      }
    };
    getRoles();
  }, []);

  const handleSave = async () => {
    try {
      if (employee) {
        await axios.patch(
          employee.url,
          {
            employee_name: employeeName,
            employee_id: employeeID,
            role: Array.from(role.values())[0] || role,
            date_started: dateJoined,
            date_left: dateLeft,
          },
          { withCredentials: true }
        );
      } else {
        const response = await axiosInstance.post("/employees/", {
          employee_name: employeeName,
          employee_id: employeeID,
          role: Array.from(role.values())[0],
          date_started: dateJoined,
          date_left: dateLeft,
        });
        const newEmployee = await axios.get(response.data.url, {
          withCredentials: true,
        });
        setEmployees(prev => ([...prev, newEmployee.data]))
        setDateJoined(new Date().getDate());
        setDateLeft(new Date().getDate());
        setEmployeeName("");
        setEmployeeID("");
        setRole(new Set([]))
      }
    } catch (error) {
      console.log(error);
    }
  };
  return (
    <>
      <Button
        variant={classes ? "flat" : "shadow" }
        className={classes ? classes : "bg-black/80 text-white"}
        endContent={
          classes ? null :
          <FaArrowRight className="text-xl bg-gray-300 px-1 py-1 text-black rounded-full" />
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
                {action} Employee
              </ModalHeader>
              <ModalBody>
                <Input
                  autoFocus
                  isRequired
                  label="Employee Name"
                  placeholder="Enter employee name"
                  value={employeeName}
                  onChange={(e) => setEmployeeName(e.target.value)}
                  variant="bordered"
                />
                <Input
                  label="Employee ID"
                  isRequired
                  placeholder="Enter employee ID"
                  value={employeeID}
                  onChange={(e) => setEmployeeID(e.target.value)}
                  variant="bordered"
                />
                <Input
                  label="Date Joined"
                  isRequired
                  type="date"
                  value={dateJoined}
                  onChange={(e) => setDateJoined(e.target.value)}
                  variant="bordered"
                />
                <Input
                  label="Date Left"
                  isRequired
                  type="date"
                  value={dateLeft}
                  onChange={(e) => setDateLeft(e.target.value)}
                  variant="bordered"
                />
                <Select
                  label={employee?.role && employee.role.url === role ? employee.role.role_name : "Role"}
                  isRequired
                  placeholder="Select a role"
                  items={roles}
                  selectedKeys={role}
                  onSelectionChange={setRole}
                  variant="bordered"
                >
                  {roles.map((role) => (
                    <SelectItem key={role.url} value={role.url}>
                      {role.role_name}
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
