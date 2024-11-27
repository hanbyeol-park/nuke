import os
import platform
import glob
import nuke
from PyQt5.QtWidgets import QMessageBox

def open_folder():
    """
    Read node 를 선택한 상태에서 실행하면
    Read node 가 가지고 있는 파일 경로에 맞는 탐색기가 오픈되는 스크립트.
    """
    nodes = nuke.selectedNodes()
    if not nodes:
        return
    for node in nodes:
        if not node.Class() == "Read":
            continue

        file_path = node.knob("file").value()
        file_directory = os.path.dirname(file_path)

        os_type = platform.system()
        if os_type == "Linux":
            os.system('xdg-open "%s"' % file_directory)

        elif os_type == "Windows":
            os.startfile(file_directory)

        else:
            print ("mac 은 지원 안 합니다.")

def set_read_node_path():
    """
    Write node 를 선택한 상태에서 실행하면
    저장 경로와 frame 수 에 맞게 Read node 가 만들어지는 스크립트.
    """
    nodes = nuke.selectedNodes()
    if not nodes:
        msg = QMessageBox()
        msg.setWindowTitle("Check")
        msg.setText("Please select the 'Write' nodes")
        msg.setStandardButtons(QMessageBox.Yes)
        msg.setIcon(QMessageBox.Information)
        return

    for node in nodes:
        if not node.Class() == "Write":
            continue

        path = node.knob("file").value()
        ext = path.split(".")[-1]

        if ext == "mov":
            nuke.createNode("Read", "file {}".format(path), inpanel=True)
            
        elif ext in ["png", "exr", "jpg"]:
            
            file_dir = os.path.dirname(path)
            file_name= os.path.basename(path)
            split = file_name.split(".")
            real_file_name = split[0]
            file_ext = split[2]
            files = sorted(glob.glob(f"{file_dir}/{real_file_name}.*.{file_ext}"))
            
            first_image = files[0]
            last_image = files[-1]
            first_frame = first_image.split(".")[1]
            last_frame = last_image.split(".")[1]
            
            read_node = nuke.nodes.Read()
            read_node.knob("file").setValue(path)
            read_node.knob("first").setValue(int(first_frame))
            read_node.knob("last").setValue(int(last_frame))
