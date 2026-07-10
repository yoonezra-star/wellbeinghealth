import paramiko
import json

host = "129.212.235.171"
user = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

def main():
    print("🚀 코다리 위젯 추가 작전 개시...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(host, username=user, password=password, timeout=10)
        app_path = "applications/jcclwggqub/public_html"
        
        # 1. 사이드바 목록 가져오기
        stdin, stdout, stderr = ssh.exec_command(f"cd {app_path} && wp sidebar list --format=json")
        out = stdout.read().decode().strip()
        print("Sidebars:", out)
        
        # 2. 위젯 추가 (text 위젯 사용)
        sidebars = json.loads(out)
        target_sidebar = None
        
        # 우선순위에 따라 메인 사이드바 찾기
        priorities = ['sidebar-1', 'main-sidebar', 'sidebar', 'right-sidebar', 'primary']
        for p in priorities:
            for s in sidebars:
                if s['id'] == p:
                    target_sidebar = s['id']
                    break
            if target_sidebar:
                break
        
        # 못 찾으면 첫 번째 사이드바 사용
        if not target_sidebar and sidebars:
            for s in sidebars:
                if s['id'] != 'wp_inactive_widgets':
                    target_sidebar = s['id']
                    break
        
        if target_sidebar:
            print(f"✅ 타겟 사이드바 식별 완료: {target_sidebar}")
            cmd_add = f"cd {app_path} && wp widget add text {target_sidebar} --title='📰 실시간 건강 뉴스' --text='[wp-rss-aggregator]'"
            stdin, stdout, stderr = ssh.exec_command(cmd_add)
            result = stdout.read().decode()
            err = stderr.read().decode()
            if result:
                print("✅ 위젯 추가 성공:", result.strip())
            if err:
                print("❌ 알림:", err.strip())
        else:
            print("❌ 적합한 사이드바를 찾지 못했습니다.")
            
    except Exception as e:
        print("❌ 에러 발생:", e)
    finally:
        ssh.close()
        print("🔌 서버 접속 종료.")

if __name__ == "__main__":
    main()
