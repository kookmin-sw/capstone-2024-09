FROM node:21.7.3-alpine
RUN mkdir -p /Final_Project
WORKDIR /Final_Project
COPY package.json package-lock.json ./
RUN npm install
COPY . ./
EXPOSE 3000