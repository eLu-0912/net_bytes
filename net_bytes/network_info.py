# SPDX-FileCopyrightText: 2024 Takeru Harashima
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil

class NetworkInfoTalker(Node):
    def __init__(self):
        super().__init__('network_info')
        self.pub = self.create_publisher(String, 'network_info', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        net_io = psutil.net_io_counters()
        bytes_sent = net_io.bytes_sent / (1024 ** 2)
        bytes_recv = net_io.bytes_recv / (1024 ** 2)

        # ネットワーク情報をフォーマット
        net_bytes = f"送信バイト: {bytes_sent:.2f}MB, 受信バイト: {bytes_recv:.2f}MB"

        msg = String()
        msg.data = net_bytes
        self.pub.publish(msg)

def main():
    rclpy.init()
    network_info_talker = NetworkInfoTalker()
    rclpy.spin(network_info_talker)
