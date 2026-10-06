# ROS2 System Status Monitor
实现系统状态监控（CPU、内存、网络），包含自定义消息接口和 Qt 显示窗口。
## 运行方式
1. 编译: colcon build
2. 发布者: ros2 run status_publisher sys_status_pub
3. 显示界面: ros2 run status_publisher status_gui
关于 GUI 运行的说明：
本项目在 WSL (Windows Subsystem for Linux) 环境下开发。受限于 WSL 的图形界面机制，运行 ros2 run status_publisher status_gui 时可能需要配置 WSLg 或 X11 转发（如 VcXsrv）才能正常弹出 Qt 窗口。核心逻辑与数据通信功能在 sys_status_pub 节点中已验证无误。
