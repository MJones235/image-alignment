import "./ImageUpload.css";
import ImageIcon from "@mui/icons-material/Image";
import { Typography } from "@mui/material";

export const ImageUpload = (props: ImageUploadProps) => {
  return (
    <div className="image-upload-wrapper">
      <div className="image-upload-container">
        {props.selectedImage ? (
          <img
            src={props.selectedImage}
            alt="Template"
            className="image-upload-image"
          />
        ) : (
          <div>
            <ImageIcon fontSize="inherit" color="inherit" />
            <Typography>Click to upload image</Typography>
          </div>
        )}
      </div>
      <input
        type="file"
        accept="image/*"
        onChange={props.onChange}
        className="image-upload-input"
      />
    </div>
  );
};

interface ImageUploadProps {
  selectedImage: string | null;
  onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
}
