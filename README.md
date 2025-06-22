# My ros2 humble slam && Nav2(unfinish) with Lidar-only-odometry  
## Test branch command list:
<pre lang="markdown"> ros2 launch sllidar_ros2 sllidar_a1_launch.py  </pre>
<pre lang="markdown"> ros2 launch rf2o_laser_odometry rf2o_laser_odometry.launch.py  </pre>
<pre lang="markdown"> ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 base_link laser  </pre>
<pre lang="markdown"> ros2 launch slam_toolbox online_sync_launch.py params_file:=/home/khemin/my_slam_config.yaml </pre>
<pre lang="markdown"> ros2 launch nav2_bringup bringup_launch.py \
    slam:=True \
    map:=dummy.yaml \
    use_sim_time:=False \
    params_file:=/opt/ros/humble/share/nav2_bringup/params/nav2_params.yaml
  </pre>

  



## Command list:
Paste this in each terminal
<pre lang="markdown"> ros2 launch sllidar_ros2 view_sllidar_a1_launch.py  </pre>
<pre lang="markdown"> ros2 launch rf2o_laser_odometry rf2o_laser_odometry.launch.py </pre>
<pre lang="markdown"> ros2 launch slam slam_toolbox_launch.py </pre>

## Package github link:
https://github.com/Adlink-ROS/rf2o_laser_odometry.git

https://github.com/Slamtec/sllidar_ros2.git

## rplidar a1 setup

Since the package launch file for rplidar a1 scan_mode is set to 'Sensitivity'
<pre lang="markdown"> cd < your_workspace >/src/sllidar_ros2/launch/ </pre>
<pre lang="markdown"> gedit view_sllidar_a1_launch.py </pre>

In line 20 change to:
<pre lang="markdown"> scan_mode = LaunchConfiguration('scan_mode', default='Standard') </pre>

Build your workspace
<pre lang="markdown"> cd < your_workspace > </pre>
<pre lang="markdown"> colcon build  </pre>
<pre lang="markdown"> source install/setup.bash </pre>





<Github command>
<repo owner skill issue lol>
  
<git pull origin master>
<git pull --rebase origin master>
<git push origin master>
