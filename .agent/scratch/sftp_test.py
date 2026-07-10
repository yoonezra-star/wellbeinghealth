import paramiko

hostname = "129.212.235.171"
username = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

sftp = ssh.open_sftp()
print("SFTP Current Dir:", sftp.getcwd())
print("SFTP List Dir:", sftp.listdir('.'))

try:
    sftp.mkdir("wellbeing_test")
    print("SFTP mkdir success")
except Exception as e:
    print(f"SFTP mkdir failed: {e}")

ssh.close()
