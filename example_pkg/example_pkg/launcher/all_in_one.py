#launch service and client
#launch subscriber and publisher

from obeyon_rfs.launch import LaunchConfig,LaunchCore,LaunchNode,ConnectToCore

def main():
    return LaunchConfig(
        grid_cells=(4,3),
        instructions=[
            LaunchCore(
                cell=(1,2),
            ),
            # LaunchCore(
            #     name="TEAM_EXAMPLE_CORE",
            #     host="localhost",
            #     port=50000,
            #     cell=(1,2),
            #     # random_host=True,
            #     # random_port=True,
            # ),
            # ConnectToCore(
            #     host="localhost",
            #     port=50000,
            #     cell=(1,2),
            # ),
            LaunchNode(
                package="example_pkg",
                executable="nodes.publisher_node",
                cell=(2,1),
            ),
            LaunchNode(
                package="example_pkg",
                executable="nodes.subscriber_node",
                cell=(2,3),
            ),
            LaunchNode(
                package="example_pkg",
                executable="nodes.service_client",
                cell=(3,1),
            ),
            LaunchNode(
                package="example_pkg",
                executable="nodes.service_server",
                cell=(3,3),
            ),
            LaunchNode(
                package="example_pkg",
                executable="nodes.action_client",
                cell=(4,1),
            ),
            LaunchNode(
                package="example_pkg",
                executable="nodes.action_server",
                cell=(4,3),
            ),
        ]
    )

