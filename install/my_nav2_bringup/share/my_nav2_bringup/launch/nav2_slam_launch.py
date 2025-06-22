from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    return LaunchDescription([
        # SLAM Toolbox node
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[PathJoinSubstitution([
                FindPackageShare('my_nav2_bringup'),
                'config',
                'nav2_params.yaml'
            ])]
        ),

        # Nav2 bringup
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('my_nav2_bringup'),
                    'launch',
                    'nav2_launch.py'
                ])
            ]),
            launch_arguments={
                'use_sim_time': 'false',
                'params_file': PathJoinSubstitution([
                    FindPackageShare('my_nav2_bringup'),
                    'config',
                    'nav2_params.yaml'
                ])
            }.items()
        )
    ])

