
docker pull mongodb/mongodb-community-server:latest

docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest

#build Docker Image
docker build -t data-loader-mongodb:v1 .

#Run Docker Container
docker run --name dl-v1 -p 8000:8000 -d data-loader-mongodb:v1

#create a network
docker network create api-to-mongodb-network

#connect containers to network
docker network connect api-to-mongodb-network dl-v2
docker network connect api-to-mongodb-network mongodb

#ping both containers
docker exec -it dl-v2 ping mongodb

docker network inspect api-to-mongodb-network