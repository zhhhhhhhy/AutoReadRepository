from pathlib import Path
from typing import List

def read_file(path: str, encoding: str = "utf-8") -> str:
    """读取文本文件全部内容，失败时抛 IOError。"""
    return Path(path).read_text(encoding=encoding)

def walk_dir_plain(root: str | Path,pattern: str = "*",files_only: bool = True,recursive: bool = True) -> List[Path]:
    root = Path(root)
    if not root.is_dir():
        raise NotADirectoryError(root)

    # 选遍历方式
    if recursive:
        generator = root.rglob(pattern)
    else:
        generator = root.glob(pattern)

    # 显式循环收集
    result: List[Path] = []
    for item in generator:
        if files_only:
            if item.is_file():
                result.append(item)
        else:
            result.append(item)
    return result



    
if __name__ == "__main__":
    text = read_file("README.md")
    print(text)

    folder = r"D:\\worker\\AutoReadRepository"  # 换成你的路径
    all_py = walk_dir_plain(folder, pattern="*.py")
    print(f"共 {len(all_py)} 个 Python 文件")
    for file in all_py:
        print(file)
