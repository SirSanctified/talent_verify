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
export default function AddRole({ classes, title, action, role, setRoles }) {
  const { isOpen, onOpen, onOpenChange } = useDisclosure();
  const [roleName, setRoleName] = useState(role?.role_name || "");
  const [department, setDepartment] = useState(
    role?.department?.url || new Set([])
  );
  const [departments, setDepartments] = useState([]);
  const [duties, setDuties] = useState(role?.duties || "");
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const getDepartments = async () => {
      try {
        const response = await axiosInstance.get("/departments/");
        setDepartments(response.data);
      } catch (error) {
        console.log(error);
      }
    };
    getDepartments();
  }, []);

  const handleSave = async () => {
    try {
      setIsLoading(true);
      if (role) {
        await axios.put(
          role.url,
          { duties, department, role_name: roleName },
          { withCredentials: true }
        );
      } else {
        const response = await axiosInstance.post("/roles/", {
          role_name: roleName,
          duties,
          department: Array.from(department.values())[0],
        });
        const newRole = await axios.get(response.data.url, {
          withCredentials: true,
        });
        setRoles((prev) => [...prev, newRole.data]);
        setDepartment(new Set([]));
        setDuties("");
        setRoleName("");
      }
    } catch (error) {
      console.log(error);
    } finally {
      setIsLoading(false);
    }
  };
  return (
    <>
      <Button
        variant={classes ? "flat" : "shadow"}
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
                {action} Role
              </ModalHeader>
              <ModalBody>
                <Input
                  isRequired
                  autoFocus
                  label="Role Name"
                  placeholder="Enter role name"
                  value={roleName}
                  onChange={(e) => setRoleName(e.target.value)}
                  variant="bordered"
                />
                <Select
                  label={
                    role?.department && role.department.url === department
                      ? role.department.department_name
                      : "Department"
                  }
                  isRequired
                  placeholder="Select a department"
                  items={departments}
                  selectedKeys={department}
                  onSelectionChange={setDepartment}
                  variant="bordered"
                >
                  {departments.map((department) => (
                    <SelectItem
                      key={department.url}
                      value={department.url}
                      className="text-black"
                    >
                      {department.department_name}
                    </SelectItem>
                  ))}
                </Select>
                <Input
                  isRequired
                  label="Duties"
                  placeholder="Enter duties separated by a comma"
                  value={duties}
                  onChange={(e) => setDuties(e.target.value)}
                  variant="bordered"
                />
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
                  isDisabled={isLoading}
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
