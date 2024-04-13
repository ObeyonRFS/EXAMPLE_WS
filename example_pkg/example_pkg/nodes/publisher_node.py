import datetime
import obeyon_rfs as orfs
from example_pkg.comm_type.msgs import CustomMsg


def main(args:orfs.InitArgs=None):
    orfs.init(args=args)
    node=orfs.Node("talker_node")

    publisher = node.create_publisher('chatting',CustomMsg)
    count=0
    while True:
        count+=1
        msg=CustomMsg(
            data="Hello, World!",
            count=count,
            time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        publisher.publish(msg)
        orfs.loginfo("Published :",msg.data,msg.count,msg.time)
        orfs.spin_once(0.5)


if __name__=='__main__':
    main()