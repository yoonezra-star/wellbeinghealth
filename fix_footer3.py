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
    /* 메인 컨텐츠와 푸터 사이의 거대한 여백 완전 제거 */
    .site-content { padding-bottom: 0 !important; margin-bottom: 0 !important; }
    .site-main { padding-bottom: 0 !important; margin-bottom: 0 !important; }
    #main { padding-bottom: 0 !important; margin-bottom: 0 !important; }
    
    /* 푸터 자체의 모든 여백 완전 박살내기 */
    footer.site-footer,
    footer.site-footer .site-primary-footer-wrap,
    footer.site-footer .ast-builder-grid-row-container,
    footer.site-footer .ast-builder-grid-row-container-inner,
    footer.site-footer .ast-builder-footer-grid-columns,
    footer.site-footer .site-below-footer-wrap {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }
    
    /* 푸터 안의 모든 문단, 위젯, 목록 요소의 상하 여백 제거 */
    footer.site-footer * {
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }
    
    /* 저작권 텍스트에 최소한의 여백만 부여 */
    footer.site-footer .ast-footer-copyright {
        padding-top: 10px !important;
        padding-bottom: 10px !important;
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

ssh.close()
