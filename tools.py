from pathlib import Path

def read_file(file_path:str)->str:
    """
    读取指定路径文件的全部内容。
    
    Args:
        file_path: 文件的完整路径或相对路径。
    
    Returns:
        文件的内容字符串，或者在失败时返回错误信息。
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return f"Error: File '{file_path}' does not exist."
        else:
            return path.read_text(encoding='utf-8')  
    except Exception as e:
        return f"Error reading file: {str(e)}"
    
def write_file(file_path:str, content:str)->str:
    """
    将文本内容写入文件。如果文件不存在则创建，如果存在则覆盖。
    会自动递归创建父目录。
    
    Args:
        file_path: 目标文件路径。
        content: 要写入的文本内容。
    """
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
        return f"Success: Content written to '{file_path}'."
    except Exception as e:
        return f"Error writing file: {str(e)}"
    
def list_directory(dir_path: str = ".") -> str:
    """
    列出指定目录下的所有文件和子目录。
    
    Args:
        dir_path: 目录路径，默认为当前目录。
    """
    try:
        path = Path(dir_path)
        if not path.exists():
            return f"Error: Directory '{dir_path}' does not exist."
        
        # 获取文件列表，过滤掉隐藏文件(可选)
        items = [p.name for p in path.iterdir() if not p.name.startswith('.')]
        return f"Directory '{dir_path}' contents: {', '.join(items)}"
    except Exception as e:
        return f"Error listing directory: {str(e)}"