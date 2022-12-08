from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    reading_laser = Node(
        package='roomba',
        executable='reading_laser',
        output='screen',
        remappings=[
            ('laser_scan', '/dolly/laser_scan')
        ]
    )

    return LaunchDescription([
        reading_laser
    ])

