# Use an official Node.js runtime as a parent image
FROM node:20.18.0-alpine3.20

# Set the working directory in the container
WORKDIR /opt/app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the rest of your application code to the working directory
COPY . .

# Expose a port to communicate with the React app
EXPOSE 3000

# Start your React app
CMD [ "npm", "run", "dev" ]