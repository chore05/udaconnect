import grpc
import location_pb2
import location_pb2_grpc

print("sending payload test")

# Create channel and stub to use
channel = grpc.insecure_channel("127.0.0.1:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)


payload =  location_pb2.LocationMessage(person_id=4, latitude=45, longitude=7) 
    
# SEnd sample payload to server
response = stub.Create(payload)
print(f"Response from gRPC server: {response}")