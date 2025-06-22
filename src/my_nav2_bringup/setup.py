from setuptools import find_packages, setup

package_name = 'my_nav2_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/nav2_launch.py', 'launch/nav2_slam_launch.py']),
        ('share/' + package_name + '/config', ['config/nav2_params.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='khemin',
    maintainer_email='khemin2549@gmail.com',
    description='Bringup launch file for Navigation2 with SLAM Toolbox',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
