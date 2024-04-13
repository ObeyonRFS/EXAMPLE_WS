import obeyon_rfs as orfs
from obeyon_rfs.node import Node
from example_pkg.comm_type.srvs import AddTwoIntsRequest, AddTwoIntsResponse, AddTwoInts

def callback(request:AddTwoIntsRequest):
    response=AddTwoIntsResponse()
    response.result=request.a+request.b
    print("Request: ",request.a,"+",request.b)
    print("Response: ",response.result)
    return response

def main(args:orfs.InitArgs=None):
    orfs.init(args=args)
    node=Node("service_server_node")
    service = node.create_service(
        'add_two_ints',
        AddTwoInts,
        callback
    )
    orfs.spin()

if __name__=='__main__':
    main()