import obeyon_rfs as orfs
from example_pkg.comm_type.actions import (
    CountingActionRequestType,
    CountingActionFeedbackType,
    CountingActionResultType,
    CountingActionType,
)

def received_request_callback(request:CountingActionRequestType,feedback_sender:ActionFeedbackSender):
    orfs.loginfo("Received request :",request.model_dump_json())

    counting=0
    while True:
        feedback = CountingActionFeedbackType(
            counting=counting,
            counting_goal=request.counting_goal
        )
        orfs.loginfo("Sending feedback :",feedback.model_dump_json())
        feedback_sender.send(feedback)
        counting+=1
        if counting>=request.counting_goal:
            break
        orfs.spin_once(0.5)

    result = CountingActionResultType(
        counted=counting,
        counting_goal=request.counting_goal
    )
    orfs.loginfo("Sending result :",result.model_dump_json())
    return result

def main(args:orfs.InitArgs=None):
    orfs.init(args=args)
    node=orfs.Node("action_server_node")

    action_server = node.create_action_server(
        'counter_action',
        CountingActionType,
        received_request_callback,
    )

    orfs.spin()


if __name__=="__main__":
    main()