import React, { useState } from "react";
import { Button, TextField } from "@mui/material";
//import { NavbarNoButton } from "../components/avbar";

export default function Login() {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email);
    }

    return (
        <div>
            
            <form onSubmit={handleSubmit}>
                <TextField
                    required
                    id="email-field"
                    label="Email"
                    defaultValue="example@domain.com"
                    margin="normal"
                />

                <TextField
                    required
                    id="password-field"
                    label="Password"
                    defaultValue="********"
                    margin="normal"
                />

            </form>
            <div>
                <Button variant="contained" href="/Login" size="medium" style={{ backgroundColor: 'black', color: 'white' , width:'200px',  borderRadius: '30px'}}> Login</Button>
            </div>
            
            <label>Don't have an account? Sign-up here</label>
            <Button variant="contained" href="/SignUp" size="medium" style={{ backgroundColor: 'black', color: 'white' , width:'200px',  borderRadius: '30px'}}> Sign Up</Button>
            
        </div>    
    )
}