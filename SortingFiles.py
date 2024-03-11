from pathlib import Path
import argparse


def display_tree(path: Path, indent: str = "", prefix: str = ""):
    if path.is_dir():
        print(indent + prefix + str(path.name))
        indent += "    " if prefix else ""

        # Get a sorted list of children, with directories last
        children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))

        for index, child in enumerate(children):
            # Check if the current child is the last one in the directory
            is_last = index == len(children) - 1
            display_tree(child, indent, "└── " if is_last else "├── ")
    else:
        print(indent + prefix + str(path.name))

def parse_argv():
    parser = argparse.ArgumentParser("Sorting Files")
    parser.add_argument("-S", "--source", type = Path, required = True, help = "Files that need sorting")
    parser.add_argument("-D", "--destination", type = Path, default = Path("dist"), help = "Sorting files")
    return parser.parse_args()

def recursive_read():
    pass

def recursive_copy():
    pass

if __name__ == "__main__":

    args = parse_argv()

    source_path = Path(args.source)
    destination_path = Path(args.destination)

    print(f"Output data: {args}")

    recursive_read(source_path)

    recursive_read(destination_path)

    recursive_copy(source_path, destination_path)

    display_tree(args.source)

    display_tree(args.destination)
