import paramiko
import base64

host = "129.212.235.171"
user = "master_zmuwemtfup"
password = "VjdUUR4pRsTj"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=user, password=password)

app_path = "applications/jcclwggqub/public_html"
mu_plugin_dir = f"{app_path}/wp-content/mu-plugins"

php_code = """<?php
/*
Plugin Name: Kodari Footer Custom CSS
Description: Automatically injects CSS to reduce footer vertical spacing.
*/
add_action('wp_head', function() {
    echo "<style>
    /* 푸터 상위 컨테이너 여백 완전 제거 */
    .site-footer, 
    .site-primary-footer-wrap,
    .site-below-footer-wrap,
    .ast-builder-footer-grid-columns,
    .ast-footer-copyright,
    .site-footer-primary-section-1,
    .site-footer-primary-section-2,
    .site-footer-below-section-1,
    .site-footer-below-section-2,
    .ast-small-footer {
        padding-top: 5px !important;
        padding-bottom: 5px !important;
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }

    /* 푸터 내부 그리드 및 위젯 영역 여백 제거 */
    .site-footer .ast-builder-grid-row,
    .site-footer .ast-row,
    .site-footer .footer-widget-area,
    .site-footer .widget-area {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }

    /* 푸터 내부 위젯 간격 최소화 */
    .site-footer .widget {
        margin-bottom: 5px !important;
        padding-bottom: 0 !important;
    }

    /* 문단 태그 등 불필요한 기본 마진 제거 */
    .site-footer p {
        margin-bottom: 0 !important;
    }
    
    /* 요소 내부 요소 강제 초기화 */
    .site-footer .ast-builder-grid-row-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    </style>";
});
"""

b64_php = base64.b64encode(php_code.encode()).decode()

cmd = f"echo {b64_php} | base64 -d > {mu_plugin_dir}/kodari-footer-css.php"
stdin, stdout, stderr = ssh.exec_command(cmd)

print("✅ MU Plugin Updated via Base64!")

# Clear cache
stdin, stdout, stderr = ssh.exec_command(f"cd {app_path} && wp cache flush && wp breeze clear_all_cache")
print("Cache clear:", stdout.read().decode())

ssh.close()
