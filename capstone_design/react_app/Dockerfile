FROM node:21.7.3-alpine
RUN mkdir -p /Final_Project
WORKDIR /Final_Project
COPY ./capstone_design/react_app ./
RUN npm install

EXPOSE 80

ENTRYPOINT ["npm", "run", "start"]