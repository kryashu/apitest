# apitest
This repository is maintained for interview of redcarpetup internshala interview assesment.

It contains two python script each of them is used for hosting an API at localhost:8080 where:

# flask_API1:
 Contains two methods post_location() for the post API Interview stage 1, this API Post lat,lng of any location with pin code+address+city and you can add new pin code in database test table main.
 and method get_using_postgres() for the get API Interview stage 2 to fetch all the nearby pin codes within a radius
 Main table contains 5 colums namely key to store pincodes,add to store name of area , city to store name of the city and lat and lng for latitude and longitude respectivly, accuracy from the csv file is skipped as it was not required.
 
# check_coordinates:
Its is the API for interview stage 3 which checks where does the given latitude/longitude lies according to geojson data provided.
