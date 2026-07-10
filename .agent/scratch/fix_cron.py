import paramiko

def fix_cron():
    hostname = "129.212.235.171"
    username = "master_zmuwemtfup"
    password = "VjdUUR4pRsTj"
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)
    
    abs_path = "/home/master/wellbeing_auto"
    
    # KST 10:00 = UTC 01:00
    # KST 15:00 = UTC 06:00
    cron_m = f"0 1 * * * python3 {abs_path}/server_poster.py morning >> {abs_path}/cron.log 2>&1"
    cron_a = f"0 6 * * * python3 {abs_path}/server_poster.py afternoon >> {abs_path}/cron.log 2>&1"
    
    stdin, stdout, stderr = ssh.exec_command("crontab -l")
    curr = stdout.read().decode()
    
    # Remove existing wellbeing_auto crons
    lines = [l.strip() for l in curr.split('\n') if l.strip() and "wellbeing_auto" not in l]
    lines.append(cron_m)
    lines.append(cron_a)
    
    new_cron = '\n'.join(lines) + '\n'
    ssh.exec_command(f"echo '{new_cron}' | crontab -")
    
    print("Cron fixed to UTC (KST 10:00, 15:00)!")
    ssh.close()

if __name__ == "__main__":
    fix_cron()
