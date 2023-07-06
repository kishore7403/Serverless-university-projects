# [1]
FROM node:14-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

COPY . .

RUN npm run build

# Set environment variables
ENV NODE_ENV=production

# Expose port
EXPOSE 3000

# Start the app
CMD [ "npm", "start" ]

# References
# [1] 	M. Herman, "Dockerizing a React App," 07 April 2020. [Online]. Available: https://mherman.org/blog/dockerizing-a-react-app/. [Accessed 04 July 2023].