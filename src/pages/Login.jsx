import React, { useState } from "react";
import { createTheme, ThemeProvider, Link, Grid, Box, Button, TextField, Container, Typography } from "@mui/material";
import { NavbarNoButton } from "../components/Navbar";

const theme = createTheme();

export default function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email, password);
    }

    return (
        <ThemeProvider theme={theme}>
            <NavbarNoButton />
            <Container component="main" maxWidth="xs">
                <Box 
                    sx={{
                        marginTop: 8,
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center',
                        justifyContent: 'center'
                    }}
                >

                    <Typography component="h1" variant="h5">
                        Sign in
                    </Typography>

                    <Box component="form" 
                        onSubmit={handleSubmit} 
                        noValidate 
                        sx={{   display: 'flex',
                                flexDirection: 'column',
                                alignItems: 'center',
                                justifyContent: 'center' }}
                    >

                        <TextField
                            margin="normal"
                            required
                            name="email"
                            label="Email"
                            id="email-field"
                            placeholder="example@domain.com"
                            autoFocus
                        />

                        <TextField
                            margin="normal"
                            required
                            name="password"
                            label="Password"
                            type="password"
                            id="password-field"
                            placeholder="********" 
                        />

                        <Button
                            type="submit"
                            variant="contained" 
                            href="/Login" 
                            size="medium" 
                            style={{ 
                                backgroundColor: 'black', 
                                color: 'white' , 
                                width:'200px',  
                                borderRadius: '30px'
                            }}
                        > 
                            Login
                        </Button>

                        <Grid container>
                            <Grid item>
                                <Link href="/SignUp" variant="body2">
                                    {"Don't have an account? Sign-up"}
                                </Link>
                            </Grid>
                        </Grid>

                    </Box>
                </Box> 
            </Container>
        </ThemeProvider>
             
    );
}