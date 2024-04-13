from dataclasses import dataclass
from obeyon_rfs.comm_type.msgs import MessageType



@dataclass
class CustomMsg(MessageType):
    data:str = "Hello, World!"
    count:int = 0
    time:str = "2021-01-01 00:00:00"
