FROM node:21.7.3-alpine
RUN mkdir -p /Final_Project
WORKDIR /Final_Project
COPY ./capstone_design/react_app ./
RUN npm install

EXPOSE 3000

ENTRYPOINT ["HOST=0.0.0.0", "npm", "run", "start"]