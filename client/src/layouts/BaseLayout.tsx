import { AppBar, Box, Toolbar } from "@mui/material";
import { ReactNode } from "react";

export const BaseLayout = (props: BaseLayoutProps) => {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar />
      </AppBar>
      <Box>{props.children}</Box>
    </Box>
  );
};

interface BaseLayoutProps {
  children?: ReactNode;
}
