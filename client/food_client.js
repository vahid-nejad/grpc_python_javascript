const grpc = require('grpc')
const messages = require('./food_pb')
const services = require('./food_grpc_pb')

function main(){
    const client = new services.FoodClient('localhost:4567',grpc.credentials.createInsecure()) ;
    const foodRequest =  new messages.FoodRequest
    foodRequest.setQty(100);
    foodRequest.setFood("SUSHI");

    client.orderFood(foodRequest,function(err, response){
       
        if (err) {
            console.log(err);
            
        } else {
            console.log(response.getMessage());
        }
        
    });
     
}

main();