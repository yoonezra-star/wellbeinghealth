import paramiko
import os

def run_ssh_command(hostname, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        out = stdout.read().decode().strip()
        err = stderr.read().decode().strip()
        ssh.close()
        return out, err
    except Exception as e:
        return None, str(e)

hostname = "129.212.235.171"
username = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

print("Checking environment...")
out, err = run_ssh_command(hostname, username, password, "python3 --version && pip3 --version")
print(f"OUT: {out}")
print(f"ERR: {err}")

print("\nCreating automation directory...")
out, err = run_ssh_command(hostname, username, password, "mkdir -p ~/automation/wellbeinghealth")
print(f"OUT: {out}")
print(f"ERR: {err}")
