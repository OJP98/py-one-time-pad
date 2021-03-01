def GetFileContent(filename: str) -> str:
    _file = open(filename, 'r')
    msg = _file.readline()
    _file.close()
    return msg.strip()


def WriteToFile(filename: str, content: str):
    with open(filename, 'w') as _file:
        _file.write(content)
