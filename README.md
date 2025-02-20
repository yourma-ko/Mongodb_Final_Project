# Laptop Store - Frontend

This section provides instructions for setting up and running the frontend of the **Laptop Store** project.

## Prerequisites

Ensure you have the following installed on your machine:

- **[Node.js](https://nodejs.org/)** (Latest LTS recommended)  
- **npm** or **yarn** (Node package managers)  

## Installation

### 1. Clone the Repository


git clone https://github.com/yourma-ko/Mongodb_Final_Project
cd laptop-store/frontend

### 2. Install Dependencies
Using npm:


npm install
Or using yarn:


yarn install
### 3. Install Required Libraries

npm install react-router-dom @mui/material @emotion/react @emotion/styled redux react-redux axios react-icons

Or using yarn:
yarn add react-router-dom @mui/material @emotion/react @emotion/styled redux react-redux axios react-icons
Configuration
### 4. Set Up Environment Variables
Create a .env file in the frontend directory and add the required environment variables:


VITE_API_URL=http://localhost:5000/api
Adjust the API URL according to your backend setup.

Running the Application
### 5. Start the Development Server
Using npm:


npm run dev
Or using yarn:


yarn dev
The application will run at http://localhost:5173/ (default Vite port).
  
 ### Technologies Used
Vite – Fast build tool for React
React – UI framework
React Router – Client-side routing
Material UI – UI components and styling
Redux – State management
Axios – API requests
React Icons – Icon library
Building for Production
 ### 6. Build the Project
Using npm:


npm run build
Or using yarn:


yarn build
This will create an optimized build in the dist/ folder.


# Laptop Store - backend
## Prerequisites
Make sure you have installed 
SDK .Net 8.0.405 

## Installation
1. Put your MongoDb URI either in API/appsettings.json as a value in "Mongo" field or put it in .env file  as MONGO_CONNECTION_STRING 
2. write cd {your local path to a project folder}\API in termital
3. write dotnet run in terminal
## OR
follow the link to go to deployed API swagger https://mongodb-project-z0ng.onrender.com/swagger/index.html

## Endpoints
### User enpoints 
    1. GET api/User - get all users
    2. POST api/User/register - register new user 
    3. POST api/User/login - login existing user 
    4. GET api/User/{id} - get user by id
### Product edpoints 
    1. GET api/Product - get all products
    2. POST api/Product - add new product
    3. PUT api/product - update product
    4. GET api/Product/{id} - get product by id
    5. POST api/Product/many - add many products
    6. DELETE api/Product/{id} - delete product by id
### Cart Endpoints
    1. api/Cart/{CustomerId} - get cart by customer id
    2. DELETE api/Cart/{CustomerId} - delete cart by Customer id
    3. POST api/Cart/{CustomerId}/items - add item to cart
    4. DELETE api/Cart/{CustomerId}/items - delete item from cart 
    5. POST api/Cart/{CustomerId}/checkout - checkout all cart items
    6. POST api/Cart/{CustomerId}/items/{productId}/quantity change cart item quantity
    7. GET api/Cart/{CustomerId}/total - get total price of items in cart 
### Technologies Used
1. .Net framework
2. MongoDb.Driver
3. Docker
4. Render
5. MongoDb Atlas