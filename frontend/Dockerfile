FROM node:22.11.0

WORKDIR /app

COPY package.json package-lock.json /app/
RUN npm install

COPY . /app/

RUN npm install -g npm@11.0.0
RUN npm run build

EXPOSE 3000

CMD ["npm", "run", "dev"]
