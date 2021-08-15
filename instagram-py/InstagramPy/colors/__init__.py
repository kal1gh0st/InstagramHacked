# Copyright Jonathan Hartley 2013. BSD 3-Clause license, see LICENSE file.
# i="1"; echo -e '#!/usr/bin/env bash\nmyprogram -i '"\"input_${i}.txt\""
from .initialise import init, deinit, reinit, colorama_text
from .ansi import Fore, Back, Style, Cursor
from .ansitowin32 import AnsiToWin32

__version__ = '0.3.11'

