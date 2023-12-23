find_package(Python3 REQUIRED COMPONENTS Interpreter)

if(NOT Python_FOUND)
    message(FATAL_ERROR "Python3 interpreter not found. Make sure Python3 is installed.")
endif()

execute_process(COMMAND ${Python3_EXECUTABLE} deep_feature_extractor.py)

function(RUN_PYTHON_SCRIPT MY_SCRIPT)
    execute_process(
        COMMAND ${CMAKE_COMMAND} -E echo "Running Python script."
        COMMAND ${Python_EXECUTABLE} ${MY_SCRIPT}
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        RESULT_VARIABLE PYTHON_SCRIPT_RESULT
    )

    if(NOT ${PYTHON_SCRIPT_RESULT} EQUAL 0)
        message(FATAL_ERROR "Error running Python script")
    endif()
endfunction()


