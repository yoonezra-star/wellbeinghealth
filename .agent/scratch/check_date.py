import paramiko

hostname = "129.212.235.171"
username = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

stdin, stdout, stderr = ssh.exec_command("date")
print(f"Server Date: {stdout.read().decode().strip()}")

ssh.close()
