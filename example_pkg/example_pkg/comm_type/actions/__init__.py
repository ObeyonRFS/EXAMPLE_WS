from obeyon_rfs.interface_system.comm_type.actions import ActionRequestType,ActionFeedbackType,ActionResultType,ActionType

class CountingActionRequestType(ActionRequestType):
    counting_goal:int
class CountingActionFeedbackType(ActionFeedbackType):
    counting:int
    counting_goal:int
    pass
class CountingActionResultType(ActionResultType):
    counted:int
    counting_goal:int

class CountingActionType(ActionType):
    request:CountingActionRequestType = CountingActionRequestType()
    feedback:CountingActionFeedbackType = CountingActionFeedbackType()
    result:CountingActionResultType = CountingActionResultType()