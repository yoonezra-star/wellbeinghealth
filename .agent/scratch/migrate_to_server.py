import paramiko
import os

def migrate():
    hostname = "129.212.235.171"
    username = "master_zmuwemtfup"
    password = "VjdUUR4pRsTj"
    
    local_files = ["server_poster.py", "topic_queue.json", ".env"]
    remote_dir = "wellbeing_auto"
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)
    
    print(f"Ensuring {remote_dir} exists...")
    ssh.exec_command(f"mkdir -p {remote_dir}")
    
    # Get absolute path for Cron
    stdin, stdout, stderr = ssh.exec_command(f"cd {remote_dir} && pwd")
    abs_path = stdout.read().decode().strip()
    print(f"Absolute remote path: {abs_path}")
    
    sftp = ssh.open_sftp()
    for f in local_files:
        if os.path.exists(f):
            print(f"Uploading {f} to {remote_dir}/{f}...")
            # Use relative path for SFTP
            sftp.put(f, f"{remote_dir}/{f}")
        else:
            print(f"Local file {f} not found.")
    sftp.close()
    
    print("Installing dependencies...")
    ssh.exec_command("pip3 install requests paramiko python-dotenv openai")
    
    print("Setting up Cron jobs...")
    cron_m = f"0 10 * * * python3 {abs_path}/server_poster.py morning >> {abs_path}/cron.log 2>&1"
    cron_a = f"0 15 * * * python3 {abs_path}/server_poster.py afternoon >> {abs_path}/cron.log 2>&1"
    
    stdin, stdout, stderr = ssh.exec_command("crontab -l")
    curr = stdout.read().decode()
    lines = [l.strip() for l in curr.split('\n') if l.strip() and "wellbeing_auto" not in l]
    lines.append(cron_m)
    lines.append(cron_a)
    new_cron = '\n'.join(lines) + '\n'
    
    ssh.exec_command(f"echo '{new_cron}' | crontab -")
    
    print("Migration Success!")
    ssh.close()

if __name__ == "__main__":
    migrate()
