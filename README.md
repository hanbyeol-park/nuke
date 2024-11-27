# nuke

## Description
This script provides two functionalities for Nuke users working with "Read" and "Write" nodes:

### open_folder():
When executed, it opens the file explorer at the location of the file path associated with the selected "Read" nodes.
The script determines the operating system (Linux, Windows) and uses appropriate system commands to open the file explorer.
Note: macOS is not supported in this version.

선택된 "Read" 노드의 파일 경로에 맞는 파일 탐색기를 엽니다.
운영 체제(Linux, Windows)를 감지하여 적합한 시스템 명령어를 사용해 파일 탐색기를 실행합니다.
참고: 현재 macOS는 지원되지 않습니다.

### set_read_node_path():
When executed, it automatically creates "Read" nodes based on the file path and frame range of selected "Write" nodes.
If the "Write" node has a sequence of images (e.g., PNG, EXR, JPG), it will create a Read node for that sequence, automatically setting the first and last frames.
If the "Write" node points to a video (e.g., MOV), a Read node is created with that file.

선택된 "Write" 노드에 따라 자동으로 "Read" 노드를 생성합니다.
"Write" 노드가 이미지 시퀀스(예: PNG, EXR, JPG)를 가리키고 있으면, 해당 시퀀스를 위한 "Read" 노드를 생성하고, 첫 번째와 마지막 프레임을 자동으로 설정합니다.
"Write" 노드가 비디오 파일(예: MOV)을 가리키고 있으면, 해당 비디오에 대한 "Read" 노드를 생성합니다.

## Usage
1. Select one or more "Read" nodes in Nuke.
2. Run the open_folder() function to open the file explorer at the file path associated with the node.
     This will open the folder where the media for the selected Read node is stored.
3. Select one or more "Write" nodes in Nuke.
4. Run the set_read_node_path() function to create corresponding "Read" nodes.
     This will automatically create Read nodes with the correct file paths and frame ranges.

## Requirements
Nuke (for running the Nuke-specific commands like nuke.selectedNodes(), nuke.createNode()).
PyQt5 (for using QMessageBox for user notifications).
This script requires that the paths of the "Write" nodes are valid and point to image or video files.

## Installation
To use the script:
1. Save the script as a .py file.
2. Load it into Nuke using run() or add it to your custom menu if desired.

## Supported Operating Systems
Linux: Opens the file explorer using xdg-open.
Windows: Uses os.startfile() to open the file explorer.
macOS: Currently not supported by this script.

## Example Code

open_folder()   # Opens the file explorer for selected 'Read' nodes
set_read_node_path()  # Creates Read nodes based on selected 'Write' nodes

## License
This script is free to use under the MIT License. You can modify it as per your needs.
