# Use a lightweight Node.js image as the base
FROM node:20.18

# Set the working directory in the container
WORKDIR /app

# Copy package.json to install dependencies
COPY package.json ./

# Remove node modules to avoid non-determinism side effects
RUN rm -rf node_modules

# Copy the rest of the application code
COPY . .

# Install dependencies
RUN npm install

# Expose the port for the development server (default Vite port)
EXPOSE 5173

# Start the development server
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]