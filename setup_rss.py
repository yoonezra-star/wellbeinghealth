import paramiko
import time

host = "129.212.235.171"
user = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

def setup_rss():
    print("🚀 코다리 백엔드 침투 개시...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(host, username=user, password=password, timeout=10)
        print("✅ 서버 접속 성공!")
        
        app_path = "applications/jcclwggqub/public_html"
        
        # 1. 플러그인 설치 및 활성화
        print("📦 WP RSS Aggregator 설치 중...")
        cmd_install = f"cd {app_path} && wp plugin install wp-rss-aggregator --activate"
        stdin, stdout, stderr = ssh.exec_command(cmd_install)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err: print("알림:", err)
        
        # 2. 실시간 건강 뉴스 피드 소스 등록
        print("📰 건강 뉴스 피드 소스 등록 중...")
        feed_url = "https://news.google.com/news/rss/headlines/section/topic/HEALTH?hl=ko&gl=KR&ceid=KR%3Ako"
        cmd_create = f"cd {app_path} && wp post create --post_type=wprss_feed --post_title='실시간 건강 뉴스' --post_status=publish --porcelain"
        stdin, stdout, stderr = ssh.exec_command(cmd_create)
        post_id = stdout.read().decode().strip()
        
        if post_id.isdigit():
            print(f"✅ 피드 소스 생성 완료 (ID: {post_id})")
            cmd_meta1 = f"cd {app_path} && wp post meta add {post_id} wprss_url '{feed_url}'"
            cmd_meta2 = f"cd {app_path} && wp post meta add {post_id} wprss_state 'active'"
            cmd_meta3 = f"cd {app_path} && wp post meta add {post_id} wprss_limit '5'"
            
            ssh.exec_command(cmd_meta1)
            ssh.exec_command(cmd_meta2)
            ssh.exec_command(cmd_meta3)
            print("✅ 피드 URL 및 기본 설정 완료!")
            
            # 초기 피드 가져오기
            cmd_fetch = f"cd {app_path} && wp wprss fetch-all"
            stdin, stdout, stderr = ssh.exec_command(cmd_fetch)
            print(stdout.read().decode())
            
        else:
            print("❌ 피드 소스 생성 실패:", stderr.read().decode())
            
    except Exception as e:
        print("에러 발생:", e)
    finally:
        ssh.close()
        print("🔌 서버 접속 종료.")

if __name__ == "__main__":
    setup_rss()
