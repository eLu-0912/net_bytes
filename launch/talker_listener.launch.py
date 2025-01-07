import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    network_info = launch_ros.actions.Node(
        package='net_bytes',
        executable='calendar',
        )
    listener = launch_ros.actions.Node(
        package='net_bytes',
        executable='listener',
        output='screen'
        )

    return launch.LaunchDescription([network_info, listener])
