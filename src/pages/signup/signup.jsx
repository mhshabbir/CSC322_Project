import React, {useState} from 'react';
import {    Link, 
            Grid, 
            Box, 
            Button, 
            TextField, 
            Container, 
            Typography,
        } from "@mui/material";

export const SignUp = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        setEmail(e.target.value);
        setPassword(e.target.value);
        console.log(email, password);
    }

    return(
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

                    <Box mt={1}>
                        <Button
                            type="submit"
                            variant="contained" 
                            href="/SignUp" 
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
                    </Box>
                    

                    <Grid mt={1} container>
                        <Grid item>
                            <Link href="/login" variant="body2">
                                {"Already have an account? Sign in"}
                            </Link>
                        </Grid>
                    </Grid>

                </Box>
            </Box> 
        </Container>
    );
}