import sys
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from status_interfaces.msg import SystemStatus
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow

class StatusWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('系统状态监控')
        self.setGeometry(100, 100, 500, 400)

        self.central = QtWidgets.QWidget()
        self.setCentralWidget(self.central)
        self.layout = QtWidgets.QVBoxLayout(self.central)

        self.labels = {}
        fields = [
            ('stamp', '时间戳'),
            ('hostname', '主机名'),
            ('cpu_percent', 'CPU 使用率 (%)'),
            ('memory_percent', '内存使用率 (%)'),
            ('memory_total', '内存总量 (MB)'),
            ('memory_available', '剩余内存 (MB)'),
            ('net_sent', '网络发送 (MB)'),
            ('net_recv', '网络接收 (MB)'),
        ]
        for key, title in fields:
            label = QtWidgets.QLabel(f"{title}: --")
            label.setStyleSheet("font-size: 14px; padding: 4px;")
            self.layout.addWidget(label)
            self.labels[key] = label

        # 【关键修改】将 ROS2 节点作为窗口内部的属性，而不是父类
        self.node = Node("status_gui")
        self.subscription = self.node.create_subscription(
            SystemStatus, 'sys_status', self.status_callback, 10
        )

    def status_callback(self, msg):
        print(f"窗口收到数据! CPU: {msg.cpu_percent}")
        data = {
            'stamp': f"{msg.stamp.sec}.{msg.stamp.nanosec}",
            'hostname': msg.hostname,
            'cpu_percent': f"{msg.cpu_percent:.1f}",
            'memory_percent': f"{msg.memory_percent:.1f}",
            'memory_total': f"{msg.memory_total:.0f}",
            'memory_available': f"{msg.memory_available:.0f}",
            'net_sent': f"{msg.net_sent:.1f}",
            'net_recv': f"{msg.net_recv:.1f}",
        }
        QTimer.singleShot(0, lambda: self.update_ui(data))

    def update_ui(self, data):
        for key, value in data.items():
            if key in self.labels:
                title = self.labels[key].text().split(':')[0]
                self.labels[key].setText(f"{title}: {value}")

def main():
    rclpy.init()
    app = QtWidgets.QApplication(sys.argv)
    window = StatusWindow()
    window.show()

    executor = MultiThreadedExecutor()
    executor.add_node(window.node)

    app.processEvents()
    while rclpy.ok():
        try:
            executor.spin_once(timeout_sec=0.1)
        except Exception:
            pass
        app.processEvents()

    app.quit()
    executor.remove_node(window.node)
    window.node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
