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
Plugin Name: Kodari Final Fix (Menu & Footer)
Description: Forcefully fixes the collapsed menu and re-layouts the custom footer.
*/

// 1. 관리자 메뉴 강제 펼침 (Admin Area)
add_action('admin_head', function() {
    echo "<style>
    /* 메뉴 글자 강제 노출 및 너비 고정 */
    #adminmenu, #adminmenuwrap, #adminmenuback { width: 160px !important; }
    #wpcontent, #wpfooter { margin-left: 160px !important; }
    .wp-menu-name { display: block !important; }
    #collapse-menu { display: none !important; } /* 실수로 누르지 못하게 숨김 */
    
    /* 모바일 대응 시 예외 처리 */
    @media screen and (max-width: 782px) {
        #adminmenu, #adminmenuwrap, #adminmenuback { width: auto !important; }
        #wpcontent, #wpfooter { margin-left: 0 !important; }
    }
    </style>";
    
    echo "<script>
    jQuery(document).ready(function($) {
        // body에 folded 클래스가 있으면 제거하여 강제로 펼침
        if ($('body').hasClass('folded')) {
            $('body').removeClass('folded');
        }
        // 사용자가 다시 접지 못하게 이벤트 리스너 제거 또는 버튼 비활성화
        $('#collapse-menu').off('click');
    });
    </script>";
});

// 2. 푸터 레이아웃 2단 분리 및 여백 제거 (Front-end)
add_action('wp_head', function() {
    echo "<style>
    /* 메인 컨텐츠 하단 여백 제거 */
    .site-content { padding-bottom: 0 !important; margin-bottom: 0 !important; }

    /* 커스텀 푸터(.wbh-footer) 레이아웃 2단 분리 */
    .wbh-footer-inner {
        display: grid !important;
        grid-template-columns: 180px 1fr !important;
        grid-template-areas: 
            'logo links'
            'logo copy'
            'logo maker'
            'logo note' !important;
        gap: 5px 30px !important;
        align-items: center !important;
        padding: 10px 0 !important;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .wbh-footer-logo { grid-area: logo; text-align: center; }
    .wbh-footer-logo img { max-width: 150px !important; height: auto !important; }
    
    .wbh-footer-links { grid-area: links; display: flex; gap: 15px; margin: 0 !important; font-size: 13px; }
    .wbh-footer-copy { grid-area: copy; margin: 0 !important; font-size: 12px; }
    .wbh-footer-maker { grid-area: maker; margin: 0 !important; font-size: 12px; }
    .wbh-footer-note { grid-area: note; font-size: 11px; color: #888; margin: 0 !important; line-height: 1.4; }

    /* 구분선 제거 또는 조정 */
    .wbh-footer-divider { display: none !important; }

    /* Astra 기본 푸터 래퍼 여백 제거 */
    .site-footer, .site-below-footer-wrap, .ast-builder-grid-row-container {
        padding: 0 !important;
        margin: 0 !important;
    }

    /* 모바일 대응 (768px 이하) */
    @media (max-width: 768px) {
        .wbh-footer-inner {
            display: flex !important;
            flex-direction: column !important;
            text-align: center !important;
            padding: 20px 10px !important;
        }
        .wbh-footer-logo { margin-bottom: 15px !important; }
        .wbh-footer-links { justify-content: center; flex-wrap: wrap; margin-bottom: 10px !important; }
        .wbh-footer-note { margin-top: 10px !important; }
    }
    </style>";
});
"""

b64_php = base64.b64encode(php_code.encode()).decode()
cmd = f"echo {b64_php} | base64 -d > {mu_plugin_dir}/kodari-footer-css.php"
ssh.exec_command(cmd)

# Purge Cache
ssh.exec_command(f"cd {app_path} && wp cache flush && wp breeze clear_all_cache")

ssh.close()
