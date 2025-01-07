# SPDX-FileCopyrightText: 2024 Takeru Harashima
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil

rclpy.init()
node = Node("network_info")
pub = node.create_publisher(String, "network_info", 10)

def cb():
    msg = String()
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent / (1024 ** 2)
    bytes_recv = net_io.bytes_recv / (1024 ** 2)
    net_bytes = f"送信バイト: {bytes_sent:.2f}MB, 受信バイト: {bytes_recv:.2f}MB"
    msg.data = net_bytes
    pub.publish(msg)

def main():
    node.create_timer(1.0, cb)  # 1秒ごとにcallbackを実行
    rclpy.spin(node)
