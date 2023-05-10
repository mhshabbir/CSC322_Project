
import React, { useContext, useState , useEffect} from 'react'
import { ShopContext } from '../../context/shop-context';
import { Stack, Button, Box, Paper, TextField, Typography, Container } from '@mui/material';
import { PRODUCTS } from '../../products';

export const DisplayProduct = (props) => {
  const {id, productName, price, productImage, reviews} = props.data;
  const {addToCart} = useContext(ShopContext);
  const {cartItems} = useContext(ShopContext);
  const cartItemAmount = cartItems[id];

  const [reviewsState, setReviewsState] = useState(reviews);

  const handleFormSubmit = (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const newComment = formData.get('comment');
    const updatedReviews = [...reviewsState, newComment];
    setReviewsState(updatedReviews);

    reviews.push(newComment)
    console.log(reviews);
     e.target.reset();
  };

  console.log(reviews);
  const DisplayComments = () => {

    return (
      <Stack spacing={1}>
        {reviewsState.map((comment, index) => (
          <Paper elevation={1} sx={{ p: 2}} key={index}>
            <Typography>
              USERNAME:
            </Typography>
            <Typography>
              {comment}
            </Typography>
          </Paper>
        ))}
      </Stack>
    );
  };

  return (
    <Container component="main" sx={{ width: 700, height: 200, mb: 4 }}>
      <Box textAlign="center">
        <Box textAlign='center' sx={{ p: 2, border: 2, mb: 5 }}>
          <img src={productImage} alt="" height="420" width="327"/>
          <Typography>
            {productName}
          </Typography>
          <Button 
            style={{ 
              backgroundColor: 'black', 
              color: 'white' , 
              width:'200px',  
              borderRadius: '30px'
            }}
            className='addToCartBttn' 
            onClick={()=> addToCart(id)}
          >
            Add To Cart {cartItemAmount > 0 && <> ({cartItemAmount})</>}
          </Button>
        </Box>
        <Stack spacing={2}>
          <Paper component="form" onSubmit={handleFormSubmit} elevation={1} sx={{ p: 3 }}>
            <Typography>
              Leave a comment:
            </Typography>
            <TextField 
              name="comment"
              rows="3" 
              multiline 
              fullWidth 
              sx={{ pb: 2 }} 
            />
            <Button
              type="submit"
              variant="contained"
              size="medium"
              style={{ 
                backgroundColor: 'black', 
                color: 'white' , 
                width:'200px',  
                borderRadius: '30px'
              }}
            > 
              Submit
            </Button>
          </Paper>
=======
import React, { useContext, useState } from 'react';
import { ShopContext } from '../../context/shop-context';
import {
  Stack,
  Button,
  Box,
  Paper,
  TextField,
  Typography,
  Container,
} from '@mui/material';

export const DisplayProduct = (props) => {
  const { id, productName, productImage, reviews } = props.data;
  const { addToCart, cartItems } = useContext(ShopContext);
  const cartItemAmount = cartItems[id];
  const [comment, setComment] = useState('');

  const handleFormSubmit = (e) => {
    e.preventDefault();
    console.log(comment);
    setComment('');
  };

  const RenderComments = (filtered) => {
    const comments = [];

    for (let i = 0; i < filtered.length; i++) {
      comments.push(
        <Paper elevation={1} sx={{ p: 2 }} key={i}>
          <Typography>USERNAME</Typography>

          <Typography>{filtered[i]}</Typography>
        </Paper>
      );
    }
    return comments;
  };

  const CensorComments = (comments) => {
    const filteredComments = [];
    const Filter = require('bad-words');
    const filter = new Filter();
    comments.forEach((element) => {
      filteredComments.push(filter.clean(element));
    });
    return filteredComments;
  };

  const DisplayComments = () => {
    const comments = RenderComments(CensorComments(reviews));
    return <Stack spacing={1}>{comments}</Stack>;
  };

  return (
    <Container component="main" sx={{ width: 700, height: 200, mb: 4 }}>
      <Box textAlign="center">
        <Box textAlign="center" sx={{ p: 2, border: 2, mb: 5 }}>
          <img
            src={productImage}
            alt=""
            height="420"
            width="327"
            style={{ objectFit: 'contain' }}
          />

          <Typography>{productName}</Typography>

          <Button
            style={{
              backgroundColor: 'black',
              color: 'white',
              width: '200px',
              borderRadius: '30px',
            }}
            className="addToCartBttn"
            onClick={() => addToCart(id)}
          >
            Add To Cart {cartItemAmount > 0 && <> ({cartItemAmount})</>}
          </Button>
        </Box>

        <Stack spacing={2}>
          <Paper
            component="form"
            elevation={1}
            sx={{ p: 3 }}
            onSubmit={handleFormSubmit}
          >
            <Typography>Leave a comment:</Typography>

            <TextField
              rows="3"
              multiline
              fullWidth
              sx={{ pb: 2 }}
              value={comment}
              onChange={(e) => setComment(e.target.value)}
            />

            <Button
              type="submit"
              variant="contained"
              size="medium"
              style={{
                backgroundColor: 'black',
                color: 'white',
                width: '200px',
                borderRadius: '30px',
              }}
            >
              Submit
            </Button>
          </Paper>


          <DisplayComments />
        </Stack>
      </Box>
    </Container>
  )
}

