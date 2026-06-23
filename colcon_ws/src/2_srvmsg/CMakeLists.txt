cmake_minimum_required(VERSION 3.8)
project(srvmsg)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(custom_interfaces REQUIRED)
find_package(rosidl_default_runtime REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

install(
  PROGRAMS
    add_ints_server.py
    add_ints_client.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
