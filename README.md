# My ros2 humble slam && Nav2 with Lidar-only-odometry  
## Test branch command list:
#### Paste this in each terminal

Launch RPLIDAR
<pre lang="markdown"> ros2 launch sllidar_ros2 sllidar_a1_launch.py  </pre>

Launch laser odometry
<pre lang="markdown"> ros2 launch rf2o_laser_odometry rf2o_laser_odometry.launch.py  </pre>

Run Static tf
<pre lang="markdown"> ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 base_link laser  </pre>

Launch slam toolbox
<pre lang="markdown"> ros2 launch slam_toolbox online_sync_launch.py params_file:=/home/khemin/my_slam_config.yaml </pre>

Launch Nav2
<pre lang="markdown"> ros2 launch nav2_bringup bringup_launch.py \
    slam:=True \
    map:=dummy.yaml \
    use_sim_time:=False \
    params_file:=/opt/ros/humble/share/nav2_bringup/params/nav2_params.yaml </pre>

  Run Rviz2 (optional)
  <pre lang="markdown"> rviz2  </pre>


  



## Command list:
Paste this in each terminal
<pre lang="markdown"> ros2 launch sllidar_ros2 view_sllidar_a1_launch.py  </pre>
<pre lang="markdown"> ros2 launch rf2o_laser_odometry rf2o_laser_odometry.launch.py </pre>
<pre lang="markdown"> ros2 launch slam slam_toolbox_launch.py </pre>

## Package github link:
https://github.com/Adlink-ROS/rf2o_laser_odometry.git

https://github.com/Slamtec/sllidar_ros2.git

## RPLIDAR A1 setup

Since the package launch file for rplidar a1 scan_mode is set to 'Sensitivity'
<pre lang="markdown"> cd < your_workspace >/src/sllidar_ros2/launch/ </pre>
<pre lang="markdown"> gedit view_sllidar_a1_launch.py </pre>

In line 20 change to:
<pre lang="markdown"> scan_mode = LaunchConfiguration('scan_mode', default='Standard') </pre>

Build your workspace
<pre lang="markdown"> cd < your_workspace > </pre>
<pre lang="markdown"> colcon build  </pre>
<pre lang="markdown"> source install/setup.bash </pre>


## Laser Odometry Setup 

Since the package launch publish /odom_rf2o, we need to remap it to /odom as it is a default topic for slam and Nav2.
<pre lang="markdown"> cd < your_workspace >/src/rf2o_laser_odometry/launch </pre>
<pre lang="markdown"> gedit rf2o_laser_odometry.launch.py </pre>

Replace everything with

<pre lang="markdown">
import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression, ThisLaunchFileDir
from launch_ros.actions import Node
from launch.conditions import IfCondition, UnlessCondition

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rf2o_laser_odometry',
            executable='rf2o_laser_odometry_node',
            name='rf2o_laser_odometry',
            output='screen',
            parameters=[{
                'laser_scan_topic': '/scan',
                'odom_topic': '/odom_rf2o',
                'publish_tf': True,
                'base_frame_id': 'base_link',
                'odom_frame_id': 'odom',
                'init_pose_from_topic': '',
                'freq': 20.0
            }],
            remappings=[
                ('/odom_rf2o', '/odom')  
            ]
        ),
    ]) </pre>



<Github command>
<repo owner skill issue lol>
  
<git pull origin master>
<git pull --rebase origin master>
<git push origin master>
