from typing import Type
from obeyon_rfs.interface_system.comm_type.srvs import ServiceRequestType,ServiceResponseType,ServiceType

class AddTwoIntsRequest(ServiceRequestType):
    a: int = 0
    b: int = 0
class AddTwoIntsResponse(ServiceResponseType):
    result: int = 0

class AddTwoInts(ServiceType):
    request_type:Type[AddTwoIntsRequest] = AddTwoIntsRequest
    response_type:Type[AddTwoIntsResponse] = AddTwoIntsResponse

AddTwoInts.request_type = AddTwoIntsRequest