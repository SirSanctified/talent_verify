/* eslint-disable react/prop-types */
import React from "react";

import {
  Popover,
  PopoverTrigger,
  PopoverContent,
  Button,
} from "@nextui-org/react";

export default function DeletePopover({
  btnTitle,
  itemType,
  itemName,
  handleDelete,
}) {
  const [isOpen, setIsOpen] = React.useState(false);

  return (
    <div className="flex flex-col gap-2">
      <Popover
        isOpen={isOpen}
        onOpenChange={(open) => setIsOpen(open)}
        backdrop="blur"
        showArrow
        className="max-w-[250px]"
      >
        <PopoverTrigger>
         <Button className="bg-transparent">{btnTitle}</Button>
        </PopoverTrigger>
        <PopoverContent>
          <div className="px-1 py-2">
            <div className="text-small font-bold mb-4">Delete {itemType}</div>
            <div className="text-tiny">
              Are you sure wou want to permanantly delete{" "}
              {itemType.toLowerCase()} {itemName}?
            </div>
            <div className="flex items-center justify-between mt-4">
              <Button
                size="sm"
                variant="bordered"
                className="text-white bg-slate-600"
                onClick={() => setIsOpen((prev) => !prev)}
              >
                Cancel
              </Button>
              <Button
                onClick={() => {
                  handleDelete();
                  setIsOpen((prev) => !prev);
                }}
                size="sm"
                variant="bordered"
                className="text-white bg-red-500"
              >
                Confirm
              </Button>
            </div>
          </div>
        </PopoverContent>
      </Popover>
    </div>
  );
}
