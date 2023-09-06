"""
Este script encontra e carrega os outros automaticamente.
This script finds and loads the others automatically.
"""

from importlib import import_module
from pathlib import Path
import time

CURRENT_FILE = Path(__file__)


# PT: Iterando caminhos para os arquivos com extensão '.py'.
# EN: Iterating paths for files with extension '.py'.
for filepath in CURRENT_FILE.parent.glob('*.py'):
    # Getting file name without extension.
    module_name = str(filepath.stem)

    # If module name is the same this file.
    if module_name == CURRENT_FILE.stem:
        # Jump iteration.
        continue

    # Displaying file name and elapsed time as running.
    print(f'{filepath.name}')
    print('└── Elapsed Time: (running)', end='', flush=True)

    # Storing the current time.
    before_time = time.time()

    try:
        # Importing module by module name and calling main function.
        import_module(module_name).main()
    except KeyboardInterrupt:
        print('\nExited!')
        exit(1)

    # Displaying elapsed time.
    print(f'\r└── Elapsed Time: {time.time() - before_time:.2f}s     \n')

print('Bye!')
