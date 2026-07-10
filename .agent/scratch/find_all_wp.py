import paramiko
hostname = '129.212.235.171'
username = 'master_zmuwemtfup'
password = 'VjdUUR4pRsTj'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

stdin, stdout, stderr = ssh.exec_command('find /home -name "wp-config.php" 2>/dev/null')
paths = stdout.read().decode().strip().split('\n')
for p in paths:
    if p:
        dir_path = p.replace('/wp-config.php', '')
        stdin, out, err = ssh.exec_command(f'cd {dir_path} && wp option get home')
        url = out.read().decode().strip()
        print(f'Path: {dir_path} -> URL: {url}')

ssh.close()
