import os
import nbformat

def clear_code_cells_in_notebook(nb_path):
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    modified = False
    for cell in nb.cells:
        if cell.cell_type == "code":
            if cell.source.strip():  # Only modify if there's content
                cell.source = ""
                cell.outputs = []
                cell.execution_count = None
                modified = True

    if modified:
        with open(nb_path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)
        print(f"[Modified] {nb_path}")
    else:
        print(f"[Skipped]  {nb_path}")

def clear_all_code_cells(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(".ipynb"):
                full_path = os.path.join(dirpath, file)
                clear_code_cells_in_notebook(full_path)

if __name__ == "__main__":
    clear_all_code_cells(".")  # Current directory
