import obeyon_rfs
from obeyon_rfs.components import LocalNetworkCorePingerNode, AppNode
from obeyon_rfs.comm_type.msgs import SimpleMsg
from obeyon_rfs.components import Publisher
import asyncio
import datetime


async def publish_timer_callback():
    global pub
    await pub.publish(SimpleMsg(message="Hello from talker_node",utc_time=datetime.datetime.now().isoformat()))
    print("published")
    

if __name__=='__main__':
    core_searcher_node=LocalNetworkCorePingerNode()
    core_searcher_node.start_as_main()
    host,port = core_searcher_node.return_core_host_port()
    print(host,port)

    app_node = AppNode(
        node_name="talker_node",
        core_host=host,
        core_port=port
    )
    pub=app_node.create_publisher("app_chatting", SimpleMsg)
    app_node.create_timer(1, publish_timer_callback)

    app_node.start_as_main()