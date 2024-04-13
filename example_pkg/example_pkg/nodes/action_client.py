import obeyon_rfs as orfs
from example_pkg.comm_type.actions import (
    CountingActionRequestType,
    CountingActionFeedbackType,
    CountingActionResultType,
    CountingActionType,
)

def received_feedback_callback(feedback:CountingActionFeedbackType):
    orfs.loginfo(f"Received feedback: {feedback.model_dump_json()}")
    pass
def received_result_callback(result:CountingActionResultType):
    orfs.loginfo(f"Received result: {result.model_dump_json()}")
    pass

def main(args:orfs.InitArgs=None):
    orfs.init(args=args)
    node=orfs.Node("action_client_node")

    action_client = node.create_action_client(
        'counter_action',
        CountingActionType
    )

    while True:
        request = CountingActionRequestType(
            counting_goal=10
        )
        orfs.loginfo("Sending request: ",request.counting_goal)
        act_progress=action_client.send_request(request,timeout=5.0)
        while True:
            if act_progress.is_done():
                break
            act_progress.wait_new_feedback()
            orfs.loginfo("Received feedback: ",act_progress.new_feedback.model_dump_json())
        orfs.loginfo("Received result: ",act_progress.result.model_dump_json())
        orfs.spin_once(0.5)



if __name__=="__main__":
    main()