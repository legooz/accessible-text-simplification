"""Validate shareable notebooks without executing training or downloading data."""
import ast
from pathlib import Path
import sys

import nbformat
from IPython.core.interactiveshell import InteractiveShell

shell = InteractiveShell.instance()
failures = []
count = 0
for path in Path('.').rglob('*.ipynb'):
    if any(part in {'.git', '.venv', 'venv', 'node_modules', '.ipynb_checkpoints'} for part in path.parts):
        continue
    count += 1
    try:
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
        for index, cell in enumerate(notebook.cells):
            if cell.cell_type != 'code':
                continue
            if cell.get('outputs') or cell.get('execution_count') is not None:
                raise ValueError(f'cell {index}: clear saved execution output before committing')
            ast.parse(shell.transform_cell(cell.source), filename=f'{path}:cell-{index}')
    except Exception as exc:
        failures.append(f'{path}: {type(exc).__name__}: {exc}')
if failures:
    print('\n'.join(failures))
    sys.exit(1)
print(f'Validated {count} notebooks. No training was executed.')
