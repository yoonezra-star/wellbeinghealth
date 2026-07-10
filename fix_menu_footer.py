import paramiko
import base64
import json

host = "129.212.235.171"
user = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=user, password=password)

app_path = "applications/jcclwggqub/public_html"
mu_plugin_dir = f"{app_path}/wp-content/mu-plugins"

# 1. 메뉴 글자 보이게 하기 (mfold 초기화)
stdin, stdout, stderr = ssh.exec_command(f"cd {app_path} && wp user get yoonezra@gmail.com --field=ID")
user_id = stdout.read().decode().strip()
if user_id.isdigit():
    # mfold를 삭제하여 기본값(펼침)으로 복구
    ssh.exec_command(f"cd {app_path} && wp user meta delete {user_id} mfold")
    print(f"✅ User {user_id} mfold meta deleted.")

# 2. 푸터 2단 분리 CSS 및 간격 추가 수정
php_code = """<?php
/*
Plugin Name: Kodari Footer & Menu Fix
Description: Fixes footer layout (2 columns) and reduces spacing.
*/
add_action('wp_head', function() {
    echo "<style>
    /* 메뉴바 너비 강제 고정 (글자 보이게) */
    @media (min-width: 783px) {
        body.folded #adminmenu, body.folded #adminmenuwrap, body.folded #adminmenuback {
            width: 160px !important;
        }
        body.folded #wpcontent, body.folded #wpfooter {
            margin-left: 160px !important;
        }
        body.folded .wp-menu-name {
            display: block !important;
        }
    }

    /* 푸터 2단 분리 (왼쪽 로고, 오른쪽 내용) */
    .site-footer .ast-builder-grid-row {
        display: flex !important;
        flex-direction: row !important;
        justify-content: space-between !important;
        align-items: center !important;
        flex-wrap: wrap !important;
        padding-top: 10px !important;
        padding-bottom: 10px !important;
    }

    /* 왼쪽 섹션 (로고) */
    .site-footer .site-footer-section-1, 
    .site-footer .ast-footer-site-stack {
        flex: 0 0 auto !important;
        text-align: left !important;
        margin: 0 !important;
    }

    /* 오른쪽 섹션 (저작권 등) */
    .site-footer .site-footer-section-2,
    .site-footer .ast-footer-copyright {
        flex: 1 !important;
        text-align: right !important;
        margin: 0 !important;
    }

    /* 모바일 대응 */
    @media (max-width: 768px) {
        .site-footer .ast-builder-grid-row {
            flex-direction: column !important;
            text-align: center !important;
        }
        .site-footer .site-footer-section-1,
        .site-footer .site-footer-section-2 {
            text-align: center !important;
            width: 100% !important;
        }
    }

    /* 기존 광활한 여백 제거 유지 */
    .site-content { padding-bottom: 0 !important; margin-bottom: 0 !important; }
    .site-main { padding-bottom: 0 !important; margin-bottom: 0 !important; }
    footer.site-footer { padding: 0 !important; margin: 0 !important; }
    </style>";
});
"""

b64_php = base64.b64encode(php_code.encode()).decode()
cmd = f"echo {b64_php} | base64 -d > {mu_plugin_dir}/kodari-footer-css.php"
ssh.exec_command(cmd)
print("✅ MU Plugin Updated (Footer 2 Columns + Menu Force).")

# 3. 캐시 삭제
ssh.exec_command(f"cd {app_path} && wp cache flush && wp breeze clear_all_cache")
print("✅ Cache flushed.")

ssh.close()
