# ROS2 System Status Monitor
实现系统状态监控（CPU、内存、网络），包含自定义消息接口和 Qt 显示窗口。
## 运行方式
1. 编译: colcon build
2. 发布者: ros2 run status_publisher sys_status_pub
3. 显示界面: ros2 run status_publisher status_gui
