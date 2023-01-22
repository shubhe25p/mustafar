import './App.css';
import Box from '@mui/material/Box';
import { Routes, Route } from "react-router-dom";
import SimpleForm from "./components/SimpleForm"


function App() {
  return (
    <Box sx={{ flexGrow: 1}}>
       <div className="container mt-3">
          <Routes>
            <Route path="/" element={<SimpleForm />} /> 
          </Routes>
           
        </div> 
    </Box>
  );
}

export default App;
