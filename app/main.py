import subprocess
import sys
from tempfile import mkdtemp

import os
import shutil

def main():
    command = sys.argv[3]
    args = sys.argv[4:]
   
    temporary_dir = mkdtemp()
    shutil.copy2(command, temporary_dir)
    os.chroot(temporary_dir)
    command = os.path.join("/", os.path.basename(command))

    completed_process = subprocess.run([command, *args], capture_output=True)

    sys.stdout.buffer.write(completed_process.stdout)
    sys.stderr.buffer.write(completed_process.stderr)
    sys.exit(completed_process.returncode)

if __name__ == "__main__":
    main()
