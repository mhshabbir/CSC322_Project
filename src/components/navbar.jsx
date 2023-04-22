import './navbar.css';
import * as React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

export default function Navbar(){
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
<TextField id="outlined-basic" label="Search" variant="outlined" style={{ backgroundColor: 'white', color: 'black' }} />
<Button variant="contained" size="medium" style={{ backgroundColor: 'black', color: 'white' }}> Login</Button>


</Box>
</div>
</div>)
}