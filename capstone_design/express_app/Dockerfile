FROM node:21.7.3-alpine
RUN mkdir -p /Final_Project
WORKDIR /Final_Project
COPY ./capstone_design/express_app ./
RUN npm ci

EXPOSE 3001

ENTRYPOINT ["npm", "run", "start"]