FROM node:21.7.3-alpine
RUN mkdir -p /Final_Project
WORKDIR /Final_Project
RUN ls -al
COPY ./capstone_design/react_app/package.json ./capstone_design/react_app/package-lock.json ./
RUN npm install
COPY . ./
EXPOSE 3000