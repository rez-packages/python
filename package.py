name = "python"
version = "2.7.9"

tools = ["python"]


variants=[["platform-linux", "arch-x86_64", "gcc-6.4"], ["platform-linux", "arch-x86_64","gcc-4.8"]]

def commands():
    env.PATH.append("{root}/bin")
