import { Box, Button } from "@mui/material";
import { useState } from "react";
import { ImageUpload } from "../components/ImageUpload";
import { Repository } from "../data/repository";
import { fileToBase64 } from "../helpers/fileToBase64";

export const AlignImages = () => {
  const [template, setTemplate] = useState<string | null>(null);
  const [image, setImage] = useState<string | null>(null);
  const [aligned, setAligned] = useState<string | null>(null);

  const onTemplateChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      fileToBase64(event.target.files[0]).then(setTemplate);
    }
  };

  const onImageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      fileToBase64(event.target.files[0]).then(setImage);
    }
  };

  const alignImages = () => {
    if (template && image) {
      new Repository()
        .alignImages(template, image)
        .then((data) => setAligned(data["aligned-image"]));
    }
  };

  return (
    <div style={{ display: "flex", flexDirection: "column" }}>
      <Box sx={{ display: "flex" }}>
        <ImageUpload selectedImage={template} onChange={onTemplateChange} />
        <ImageUpload selectedImage={image} onChange={onImageChange} />
      </Box>
      <Button variant="contained" sx={{ margin: 1 }} onClick={alignImages}>
        Align Images
      </Button>
      {aligned && (
        <img
          src={aligned}
          alt="Aligned"
          width={600}
          style={{ margin: "8px" }}
        />
      )}
    </div>
  );
};
