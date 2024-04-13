from obeyon_rfs.components import LocalNetworkCoreNode
import socket

def main():
    # print(socket.gethostbyname(socket.gethostname()))
    node = LocalNetworkCoreNode("core_node")
    node.start_as_main()

if __name__=='__main__':
    main()


