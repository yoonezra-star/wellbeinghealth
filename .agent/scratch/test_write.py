import paramiko

hostname = "129.212.235.171"
username = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

print("Listing current directory...")
stdin, stdout, stderr = ssh.exec_command("ls -F")
print(stdout.read().decode())

print("Testing write to home...")
stdin, stdout, stderr = ssh.exec_command("touch test_file.txt && ls test_file.txt")
print(f"OUT: {stdout.read().decode()}")
print(f"ERR: {stderr.read().decode()}")

ssh.close()
