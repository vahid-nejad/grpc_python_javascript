import grpc
import concurrent
from concurrent import futures
import food_pb2_grpc
import food_pb2

class FoodServicer(food_pb2_grpc.FoodServicer):
    def OrderFood(self, request, context):
       print("grpc call recieved")

       response= food_pb2.FoodResponse()
       response.message = f"here are {request.qty} of {request.food}!"

       return response



def main():
    server= grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    food_pb2_grpc.add_FoodServicer_to_server(FoodServicer(),server)
    server.add_insecure_port('[::]:4567')
    server.start()
    print(f"server started at port 4567")
    server.wait_for_termination()


main()
