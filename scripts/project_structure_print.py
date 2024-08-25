# scripts/project_structure_print.py
import os
import sys

# from src.bot.decorators import sync_error_handler

# Добавляем корневую директорию проекта в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# @sync_error_handler
def print_project_structure(output_file=None):
    # Print the structure of the project and optionally save to a file.
    # Directories to exclude
    exclude_dirs = [
        ".git",
        "__pycache__",
        ".pytest_cache",
        "python_game_simple.egg-info",
        "venv",
        ".mypy_cache",
        "migrations",
        "node_modules",
        "dist",
        "build",
        ".pytest_cache",
        ".vscode",
        ".idea",
        "github",
        "instance",
    ]
    # Files to exclude
    exclude_files = [
        "_variable_level.py"
    ]  # 'project_structure_print.py', 'project_structure_for_now.txt',
    # File extensions to exclude
    exclude_extensions = [".png", ".ttf", ".wav", ".toml"]
    # Get the current working directory and get the parent directory
    cwd = os.getcwd()
    # cwd = os.path.dirname(cwd)

    def print_and_write(line, file=None):
        print(line)
        if file:
            file.write(line + "\n")

    def print_directory(path, prefix="", file=None):
        entries = sorted(os.listdir(path))
        dirs = [
            d
            for d in entries
            if os.path.isdir(os.path.join(path, d)) and d not in exclude_dirs
        ]
        files = [
            f
            for f in entries
            if os.path.isfile(os.path.join(path, f))
            and f not in exclude_files
            and not any(f.endswith(ext) for ext in exclude_extensions)
            and not f.startswith("._")
        ]

        for i, entry in enumerate(dirs + files):
            is_last = i == len(dirs + files) - 1
            is_dir = entry in dirs
            connector = "└── " if is_last else "├── "
            print_and_write(f"{prefix}{connector}{entry}{'/' if is_dir else ''}", file)
            if is_dir:
                extension = "    " if is_last else "│   "
                print_directory(os.path.join(path, entry), prefix + extension, file)

    f = open(output_file, "w") if output_file else None
    try:
        print_and_write("|-- python_game_simple", f)
        print_directory(cwd, "    ", f)
    finally:
        if f:
            f.close()


if __name__ == "__main__":
    print_project_structure("scripts/project_structure_for_now.txt")
