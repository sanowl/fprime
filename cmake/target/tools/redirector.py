import sys
import subprocess
from security import safe_command

if len(sys.argv) < 2:
    print("[ERROR] Supply output file then tool")
    sys.exit(1)
with open(sys.argv[1], "w") as file_handle:
    sys.exit(safe_command.run(subprocess.run, sys.argv[2:], stdout=file_handle).returncode)
