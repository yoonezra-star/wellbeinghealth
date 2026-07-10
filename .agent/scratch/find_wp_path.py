import paramiko
hostname = '129.212.235.171'
username = 'master_zmuwemtfup'
password = 'VjdUUR4pRsTj'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

stdin, stdout, stderr = ssh.exec_command('find /home/master/applications -maxdepth 2 -name "public_html"')
paths = stdout.read().decode().strip().split('\n')
for p in paths:
    if p:
        stdin, out, err = ssh.exec_command(f'wp --path={p} option get home')
        url = out.read().decode().strip()
        print(f'Path: {p} -> URL: {url}')

ssh.close()
