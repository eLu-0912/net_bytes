#!/bin/bash
#SPDX-FileCopyrightText: 2024 Takeru Harashima
#SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 10 ros2 launch net_bytes talker_listener.launch.py > /tmp/net_bytes.log 
