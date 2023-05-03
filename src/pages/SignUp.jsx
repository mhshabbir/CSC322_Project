import React, {useState} from 'react';
import { createTheme, ThemeProvider, Link, Grid, Box, Button, TextField, Container, Typography } from "@mui/material";
import { NavbarNoButton } from '../components/Navbar';

const theme = createTheme();
theme.spacing(2);

export default function SignUp(){
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(email);
    }

    return(
        <ThemeProvider theme={theme}>
        <NavbarNoButton />
        <Container component="main" maxWidth="xs">
            <Box 
                sx={{
                    marginTop: 8,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                }}
            >

                <Typography component="h1" variant="h5">
                    Sign up
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
                        name="username"
                        label="Username"
                        id="username-field"
                        placeholder="user123"
                        autoFocus
                    />

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

                    <TextField
                        margin="normal"
                        required
                        name="confirm-password"
                        label="Confirm Password"
                        type="password"
                        id="confirm-password-field"
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
                            borderRadius: '30px',
                        }}
                    > 
                        Register
                    </Button>

                    <Grid container>
                        <Grid item>
                            <Link href="/Login" variant="body2">
                                {"Already have an account? Sign in"}
                            </Link>
                        </Grid>
                    </Grid>

                </Box>
            </Box> 
        </Container>
    </ThemeProvider>
    );
}