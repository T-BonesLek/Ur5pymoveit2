cmake_minimum_required(VERSION 3.5)
project(pymoveit2)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

# Install Python package
ament_python_install_package(pymoveit2)

# Install examples
set(EXAMPLES_DIR examples)
install(PROGRAMS
    ${EXAMPLES_DIR}/ex_collision_mesh.py
    ${EXAMPLES_DIR}/ex_collision_primitive.py
    ${EXAMPLES_DIR}/ex_gripper.py
    ${EXAMPLES_DIR}/ex_servo.py

    DESTINATION lib/${PROJECT_NAME}
)

#intall textilePrograms
set(textilePrograms_DIR textilePrograms)
install(PROGRAMS
    ${textilePrograms_DIR}/io_port_toggle.py
    ${textilePrograms_DIR}/place_cotton.py
    ${textilePrograms_DIR}/pick_goal.py
    ${textilePrograms_DIR}/joint_goal.py
    ${textilePrograms_DIR}/main.py

    DESTINATION lib/${PROJECT_NAME}
)

# Setup the project
ament_package()
