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
} from "@nextui-org/react";
import axios from "axios";
import { useState } from "react";
import { FaArrowRight } from "react-icons/fa";
import { axiosInstance } from "../pages/Dashboard";

export default function AddCompany({
  classes,
  title,
  action,
  company,
  setCompanies,
}) {
  const { isOpen, onOpen, onOpenChange } = useDisclosure();
  const [companyName, setCompanyName] = useState(company?.company_name || "");
  const [companyAddress, setCompanyAddress] = useState(
    company?.company_address || ""
  );
  const [companyRegistrationNumber, setCompanyRegistrationNumber] = useState(
    company?.company_registration_number || ""
  );

  const handleSave = async () => {
    try {
      if (company) {
        await axios.patch(
          company.url,
          {
            company_name: companyName,
            company_address: companyAddress,
            company_registration_number: companyRegistrationNumber,
          },
          { withCredentials: true }
        );
      } else {
        const response = await axiosInstance.post("/companies/", {
          company_name: companyName,
          company_address: companyAddress,
          company_registration_number: companyRegistrationNumber,
        });
        const newCompany = await axios.get(response.data.url, {
          withCredentials: true,
        });
        setCompanies((prev) => [...prev, newCompany.data]);
        setCompanyAddress("");
        setCompanyName("");
        setCompanyRegistrationNumber("");
      }
    } catch (error) {
      console.log(error);
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
                {action} Company
              </ModalHeader>
              <ModalBody>
                <Input
                  autoFocus
                  isRequired
                  label="Company Name"
                  placeholder="Enter company name"
                  value={companyName}
                  onChange={(e) => setCompanyName(e.target.value)}
                  variant="bordered"
                />
                <Input
                  label="Registration Number"
                  isRequired
                  placeholder="Enter company registration number"
                  value={companyRegistrationNumber}
                  onChange={(e) => setCompanyRegistrationNumber(e.target.value)}
                  variant="bordered"
                />
                <Input
                  label="Address"
                  isRequired
                  placeholder="Enter company address"
                  value={companyAddress}
                  onChange={(e) => setCompanyAddress(e.target.value)}
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
