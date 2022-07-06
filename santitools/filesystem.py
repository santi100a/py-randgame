def readfile(filename: str) -> str | None:
    """
    Reads a file and returns the contents. \r\n
    If the file does not exist, returns None.
    """
    try:
        return open(filename, 'r').read()
    except:
        return None
def writefile(filename: str, data: str) -> bool:
    """
    Writes data to a file. \r\n
    If the file does not exist, it will be created. \r\n
    This erases the original file's contents, and overwrites them \r\n
    with the new data you specify. \r\n
    It returns a boolean, indicating whether or not the write was successful. \r\n
    """
    try:
        open(filename, 'w').write(data)
        return True
    except:
        return False
def appendfile(filename: str, data: str) -> bool:
    """
    Appends data to a file.\r\n
    If the file does not exist, it will be created.\r\n
    This adds your data to the original file's contents, and appends them
    to its end.\r\n
    It returns a boolean, indicating whether or not the append was successful.
    """
    try:
        open(filename, 'a').write(data)
        return True
    except:
        return False
def deletefile(filename: str) -> bool:
    """
    Deletes a file. \n
    ! Remember to avoid deleting important files. \n
    ! This will delete the file, and not just erase its contents.
    It returns a boolean, indicating whether or not the delete was successful.
    NOTE: If the file does not exist, it will return False (the delete will fail).winget ins
    """
    try:
        import os
        os.remove(filename)
        return True
    except:
        return False