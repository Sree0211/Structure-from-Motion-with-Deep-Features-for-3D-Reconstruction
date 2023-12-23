cmake_minimum_required(VERSION 3.10)
project(sfm_3d CXX)
set(CMAKE_CXX_STANDARD_REQUIRED 17)

# Link library
find_package(OpenCV REQUIRED)
include_directories(sfm_3d ${OPENCV_INCLUDE_DIRS})

# standard compiler warnings
# Set compiler-specific warning flags
if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    # GCC
    target_compile_options(sfm_3d PRIVATE -Wall -Wextra -pedantic)
elseif(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    # Clang
    target_compile_options(sfm_3d PRIVATE -Wall -Wextra -pedantic)
endif()

# enable doxygen
include(cmake/Doxygen.cmake)
#option(DOXYGEN "Enable Doxygen documentation" ON)
enable_doxygen()

# Add my python script
include(cmake/run_python_script.cmake)
RUN_PYTHON_SCRIPT(src/deep_feature_extractor.py)


# add the executables and directories
add_executable(sfm_3d src/main.cpp)
target_include_directories(sfm_3d PRIVATE src/main.cpp src/keypoint_fusion.h 
                            src/tentative_matching.h src/feature_verification.h  src/visualization.h)
target_link_libraries(sfm_3d ${OpenCV_LIBS})




