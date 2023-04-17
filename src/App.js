import './App.css';
import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';


function NavBar() {
  return (
    <div className="Nav">
        <h1 className='Logo'>PC PALACE</h1>  
        <div className='search'>
        <Box display='flex' 
      component="form"
      sx={{
        '& > :not(style)': { m: 2, width: '50ch', ml:30},
      }}
    >
      <TextField id="outlined-basic" label="Search" variant="outlined"  style={{ backgroundColor: 'white', color: 'black', borderRadius: 30 }} />
     
      <Button variant="contained" size="medium" style={{ backgroundColor: 'black', color: 'white' , borderRadius: 30}}> Login</Button>
   
  
    </Box>
    </div>
    </div>
  );
}

export default NavBar;
