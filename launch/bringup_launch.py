#  Copyright 2020 ADLINK Technology, Inc.
#  Developer: Skyler Pan (skylerpan@gmail.com)
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (DeclareLaunchArgument, IncludeLaunchDescription)
from launch.launch_description_sources import PythonLaunchDescriptionSource
import launch_ros.actions


def generate_launch_description():

    controller_launch = os.path.join(get_package_share_directory('robot_tracking_controller'), 'launch', 'oa_target_tracker.launch.py')
    
    controller_pkg = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(controller_launch)
    )
    
    # Static TF publisher
    static_tf_camera_world = launch_ros.actions.Node(
        package='tf2_ros', node_executable='static_transform_publisher', output='screen',
        arguments=['0.0', '0.0', '0.0', '0.0', '0.0', '0', '/camera_link', '/world'])

    static_tf_camera_baselink = launch_ros.actions.Node(
        package='tf2_ros', node_executable='static_transform_publisher', output='screen',
        arguments=['0.0', '0.0', '0.0', '0.0', '0.0', '0', '/camera_link', '/base_link'])

    static_tf_baselink_basefootprint = launch_ros.actions.Node(
        package='tf2_ros', node_executable='static_transform_publisher', output='screen',
        arguments=['0.0', '0.0', '0.0', '0.0', '0.0', '0', '/base_link', '/base_footprint'])

    # Create the launch description and populate
    ld = LaunchDescription()

    # Declare the launch options
    ld.add_action(controller_pkg)
    ld.add_action(static_tf_camera_world)
    ld.add_action(static_tf_camera_baselink)
    ld.add_action(static_tf_baselink_basefootprint)

    return ld