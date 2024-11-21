# Use a lightweight Node.js image as the base
FROM node:20.18

# Set the working directory in the container
WORKDIR /app

# Copy package.json to install dependencies
COPY package.json ./
COPY package-lock.json ./

# Install dependencies
RUN npm install