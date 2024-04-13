import random
import obeyon_rfs as orfs
from obeyon_rfs.node import Node
from example_pkg.comm_type.srvs import AddTwoIntsRequest, AddTwoIntsResponse, AddTwoInts

def main(args:orfs.InitArgs=None):
    orfs.init(args=args)
    node = Node("service_client_node")
    client = node.create_service_client(
        'add_two_ints',
        AddTwoInts
    )

    while True:
        request = AddTwoIntsRequest(
            a=random.randint(0,4),
            b=random.randint(0,4)
        )
        orfs.loginfo("Requesting: ",request.a,request.b)
        response=client.send_request(request)
        orfs.loginfo("Response: ",response.sum)
        orfs.spin_once(0.5)

if __name__ == '__main__':
    main()