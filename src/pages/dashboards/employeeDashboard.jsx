import { Grid, Button } from "@mui/material";
import React from "react";

export const EmployeeDashboard = () => {
    return (
            <Grid 
                container 
                direction="row" 
                textAlign="center"
                mt={50}
            >
                <Grid item xs={4}>
                    <Button
                        disableRipple
                        type="submit"
                        variant="contained" 
                        size="large" 
                        style={{
                            fontSize: 28,  
                            backgroundColor: 'black', 
                            color: 'white' , 
                            width: '400px',
                            height: '150px',  
                            borderRadius: '30px'
                        }}
                    > 
                        Review Applications
                    </Button>
                </Grid>

                <Grid item xs={4}>
                    <Button
                        disableRipple
                        type="submit"
                        variant="contained" 
                        size="large" 
                        style={{
                            fontSize: 28, 
                            backgroundColor: 'black', 
                            color: 'white' , 
                            width: '400px',
                            height: '150px',  
                            borderRadius: '30px'
                        }}
                    > 
                        Messages
                    </Button>
                </Grid>

                <Grid item xs={4}>
                    <Button
                        disableRipple
                        type="submit"
                        variant="contained" 
                        size="large" 
                        style={{
                            fontSize: 28, 
                            backgroundColor: 'black', 
                            color: 'white' , 
                            width: '400px',
                            height: '150px',  
                            borderRadius: '30px'
                        }}
                    > 
                        Manage Products
                    </Button>
                </Grid>
            </Grid>
    )
}