import subprocess

# Command passed through shell
subprocess.run("echo Hello", shell=True)

# Command not passed to shell
subprocess.run(["echo", "Hello"])