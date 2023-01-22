// simple form in mui that has a text field and a button


import * as React from 'react';
import { TextField, Button } from '@mui/material';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import UserService from "../services/user.service";


export default function SimpleForm() {

    const handleSubmit = (event) => {
      event.preventDefault();
      const data = new FormData(event.currentTarget);
      console.log(data.get("city"));
      console.log(data.get("planet"));
      UserService.sendData(data.get("city"), data.get("planet")).then(
        () => {
          console.log("hello world");
        },
        error => {
          const resMessage =
            (error.response &&
              error.response.data &&
              error.response.data.message) ||
            error.message ||
            error.toString();
        }
      );
    };
    
    return (
      <Box
      sx={{
        marginTop: 8,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <Typography component="h1" variant="h5">
        Mustafar
      </Typography>
      <Typography component="h5" variant="h7">
        E.g. "What would SF look like on Mars?"
      </Typography>
      <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
        <TextField
          margin="normal"
          fullWidth
          id="city"
          label="city"
          name="city"
          autoFocus
        />
        <TextField
          margin="normal"
          fullWidth
          name="planet"
          label="planet"
          type="planet"
          id="planet"
        />
        <Button
          type="submit"
          fullWidth
          variant="contained"
          sx={{ mt: 3, mb: 2 }}
        >
          Generate
        </Button>
        
      </Box>
    </Box>
    );
}
