from obeyon_rfs.components import LocalNetworkCorePingerNode, AppNode
from obeyon_rfs.comm_type.msgs import SimpleMsg


async def callback(msg:SimpleMsg):
    print("Received",msg.message,msg.utc_time)

def main():
    core_searcher_node=LocalNetworkCorePingerNode()
    core_searcher_node.start_as_main()
    host,port = core_searcher_node.return_core_host_port()
    print(host,port)

    app_node = AppNode(
        node_name="listener_node",
        core_host=host,
        core_port=port
    )
    sub=app_node.create_subscriber("app_chatting", SimpleMsg, callback)
    app_node.start_as_main()
    

if __name__=='__main__':
    main()


