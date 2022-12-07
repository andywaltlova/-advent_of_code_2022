from __future__ import annotations

from dataclasses import dataclass

from utils import get_input


@dataclass
class File:
    name: str
    size: int

    def __str__(self):
        return f'{self.name} ({self.size})'

@dataclass
class Directory:
    name: str
    parent: Directory
    files: list[File] = None
    directories: dict[str, Directory] = None
    size = None

    def add_dir(self, name):
        dir_obj = Directory(name, self)
        if self.directories is not None:
            self.directories[name] = dir_obj
        else:
            self.directories = {name: dir_obj}

    def add_file(self, name, size):
        file_obj = File(name, size)
        if self.files is not None:
            self.files.append(file_obj)
        else:
            self.files = [file_obj]

    def __str__(self):
        dirs = [str(dir_obj) for dir_obj in self.directories] if self.directories else 'None'
        files = [str(file) for file in self.files]  if self.files else 'None'
        return f'{self.name} ({self.size}) | dirs: {dirs} | files: {files}'

    def set_size(self):
        size = 0
        if self.files:
            size += sum([file.size for file in self.files])
        if self.directories:
            for child_dir in self.directories.values():
                child_dir.set_size()
                size += child_dir.size
        self.size = size

def load_filesystem(data: list[str]):
    root = Directory('/', None)
    current_dir = root
    for line in data[1:]:
        if line.startswith('$'):
            # cd or ls
            if (cmd := line.lstrip('$ ')).startswith('cd'):
                _, dir_name = cmd.split(' ')
                if dir_name == '..':
                    current_dir = current_dir.parent
                else:
                    current_dir = current_dir.directories.get(
                        dir_name,
                        Directory(dir_name, current_dir)
                    )
        else:
            # listed files or directories
            size, name = line.split(' ')
            if size == 'dir':
                current_dir.add_dir(name)
            else:
                current_dir.add_file(name, int(size))
    return root

def sum_max_n_sized_dirs(root, n):
    size = 0
    if root.size <= n:
        size += root.size
    if root.directories:
        for child_dir in root.directories.values():
            size += sum_max_n_sized_dirs(child_dir, n)
    return size

def find_smallest_dir_to_delete(dir_obj, need_to_free, smallest):
    if dir_obj.size >= need_to_free and dir_obj.size < smallest.size:
        smallest = dir_obj
    if dir_obj.directories:
        for child_dir in dir_obj.directories.values():
            smallest = find_smallest_dir_to_delete(child_dir, need_to_free, smallest)
    return smallest

if __name__ == "__main__":
    path = 'data/07.txt'
    data = get_input(path)

    root: Directory = load_filesystem(data)
    root.set_size() # computes sizes of all child dirs

    # Part 1
    print(sum_max_n_sized_dirs(root, 100_000))

    # Part 2
    needed_space = 30_000_000 - (70_000_000 - root.size)
    print(find_smallest_dir_to_delete(root, needed_space, root).size)



