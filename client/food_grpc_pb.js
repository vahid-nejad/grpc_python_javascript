// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var food_pb = require('./food_pb.js');

function serialize_FoodRequest(arg) {
  if (!(arg instanceof food_pb.FoodRequest)) {
    throw new Error('Expected argument of type FoodRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_FoodRequest(buffer_arg) {
  return food_pb.FoodRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_FoodResponse(arg) {
  if (!(arg instanceof food_pb.FoodResponse)) {
    throw new Error('Expected argument of type FoodResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_FoodResponse(buffer_arg) {
  return food_pb.FoodResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


var FoodService = exports.FoodService = {
  orderFood: {
    path: '/Food/OrderFood',
    requestStream: false,
    responseStream: false,
    requestType: food_pb.FoodRequest,
    responseType: food_pb.FoodResponse,
    requestSerialize: serialize_FoodRequest,
    requestDeserialize: deserialize_FoodRequest,
    responseSerialize: serialize_FoodResponse,
    responseDeserialize: deserialize_FoodResponse,
  },
};

exports.FoodClient = grpc.makeGenericClientConstructor(FoodService);
