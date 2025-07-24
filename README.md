# Catkin-Compile-Commands-Merger
Scripts to merge the compile_commands.json files from all packages in the build dir of a catkin workspace into a single compile_commands.json. Can also swap root directories (useful if building in docker container but editing files locally).

# Guide

The flag `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON` can be used with catkin to generate `cmopile_commands.json` files used for ROS1 workspaces. 

`merge_compile_commands.py` should be run in the root dir of a compiled catkin workspace. It will recurse the build directory and merge all found compile command into a single `compile_commands.json` file. Useful for things like LSP setup with nvim.

`modify_compile_commands.py` can be run after `merge_compile_commands.py` to replace path prefixes with a new one in the paths in `compile_commands.json`. Useful if code was not compiled locally (e.g. in a Docker container), as you can replace the path prefixes of the workspace in the container, with the path prefixes on local disk.
