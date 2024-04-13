import obeyon_rfs as orfs
from obeyon_rfs.node import Node
from example_pkg.comm_type.msgs import CustomMsgType


def callback(msg:CustomMsgType):
    orfs.log_info("Received :",msg.data,msg.count,msg.time)

def main(args:orfs.InitArgs=None):
    orfs.init(args=args)
    node=Node("listener_node")
    subscriber = node.create_subscriber(
        'chatting',
        CustomMsgType,
        callback
    )
    orfs.spin()

if __name__=='__main__':
    main()