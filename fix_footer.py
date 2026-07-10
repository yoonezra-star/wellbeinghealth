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

ssh.exec_command(f"mkdir -p {mu_plugin_dir}")

php_code = """<?php
/*
Plugin Name: Kodari Footer Custom CSS
Description: Automatically injects CSS to reduce footer vertical spacing.
*/
add_action('wp_head', function() {
    echo "<style>
    /* 푸터 세로 간격 축소 */
    .site-footer, 
    .ast-builder-footer-grid-columns, 
    .site-primary-footer-wrap, 
    .site-below-footer-wrap,
    .ast-footer-copyright {
        padding-top: 15px !important;
        padding-bottom: 15px !important;
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }
    .footer-widget-area {
        padding-top: 10px !important;
        padding-bottom: 10px !important;
        margin-bottom: 0 !important;
    }
    .site-footer .widget {
        margin-bottom: 10px !important;
    }
    </style>";
});
"""

b64_php = base64.b64encode(php_code.encode()).decode()

cmd = f"echo {b64_php} | base64 -d > {mu_plugin_dir}/kodari-footer-css.php"
stdin, stdout, stderr = ssh.exec_command(cmd)

print("✅ MU Plugin Created via Base64!")

# Clear cache
stdin, stdout, stderr = ssh.exec_command(f"cd {app_path} && wp cache flush && wp breeze clear_all_cache")
print("Cache clear:", stdout.read().decode())

ssh.close()
