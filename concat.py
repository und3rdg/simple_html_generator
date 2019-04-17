#!/bin/python
from string import Template

_src_dir = "src/"
_dest_dir = "dist/"

_input_files = [
        'head.html',
        'nav.html',
        'body.html',
        'footer.html',
        ]

locale = {
        'lang': {
            'en': 'en',
            'tc': 'tc',
            'sc': 'sc',
            },
        'home': {
            'en': 'Home',
            'tc': '主頁',
            'sc': '主页',
            },
        'whats_on': {
            'en': "What's on",
            'tc': '節目及活動',
            'sc': '节目及活动',
            },
        'go_to_search': {
            'en': 'Go to Search',
            'tc': '到 搜尋',
            'sc': '到 搜索',
            },

        'log_in': {
            'en': 'Log in',
            'tc': '登入',
            'sc': '登入',
            },
        'register': {
            'en': 'Register',
            'tc': '註冊',
            'sc': '注册',
            },
        'hello': { # ${hello} user_name 
            'en': 'Hello',
            'tc': '您好',
            'sc': '您好',
            },
        'logout': {
            'en': 'Logout',
            'tc': '登出',
            'sc': '登出',
            },
        'loggedin_extra_text': {
            'en': 'Your items in the shopping cart will be removed after you log out.',
            'tc': '登出後您在購物籃裡的貸物將會被移除。',
            'sc': '登出后您在购物篮里的贷物将会被移除。',
            },

        'switch_to_en': {
            'en': 'Switch to English',
            'tc': '轉換到 English',
            'sc': '转换到 English',
            },
        'switch_to_tc': {
            'en': 'Switch to Traditional Chinese',
            'tc': '轉換到 Traditional Chinese',
            'sc': '转换到 Traditional Chinese',
            },
        'switch_to_sc': {
            'en': 'Switch to Simplified Chinese',
            'tc': '轉換到 Simplified Chinese',
            'sc': '转换到 Simplified Chinese',
            },

        'active_lang_en': {
            'en': 'active',
            'tc': '',
            'sc': '',
            },
        'active_lang_tc': {
            'en': '',
            'tc': 'active',
            'sc': '',
            },
        'active_lang_sc': {
            'en': '',
            'tc': '',
            'sc': 'active',
            },

        'go_to_privacy_policy': {
            'en': 'Go to Privacy Policy',
            'tc': '到 私隱政策',
            'sc': '到 私隐政策',
            },
        'privacy_policy': {
            'en': 'Privacy Policy',
            'tc': '私隱政策',
            'sc': '私隐政策',
            },
        'go_to_site_information': {
            'en': 'Go to Site Information',
            'tc': '到 網站資訊',
            'sc': '到 网站资讯',
            },
        'site_information': {
            'en': 'Site information',
            'tc': '網站資訊',
            'sc': '网站资讯',
            },
        'go_to_contact_us': {
            'en': 'Go to Contact Us',
            'tc': '到 聯絡我們',
            'sc': '到 联络我们',
            },
        'contact_us': {
            'en': 'Contact Us',
            'tc': '聯絡我們',
            'sc': '联络我们',
            },

        'follow_us': {
            'en': 'Follow us',
            'tc': '關注我們',
            'sc': '关注我们',
            },
        'join_us_on_facebook': {
            'en': 'Join us on Facebook',
            'tc': '關注我們的Facebook',
            'sc': '关注我们的Facebook',
            },
        'follow_us_on_twitter': {
            'en': 'Follow us on Twitter',
            'tc': '關注我們的Twitter',
            'sc': '关注我们的Twitter',
            },
        'find_us_on_weibo': {
            'en': 'Find us on Weibo',
            'tc': '關注我們的微博',
            'sc': '关注我们的微博',
            },
        'follow_us_on_wechat': {
            'en': 'Follow us on WeChat',
            'tc': '關注我們的WeChat',
            'sc': '关注我们的WeChat',
            },
        'subscribe_to_e_newsletter': {
            'en': 'Subscribe to e-Newsletter',
            'tc': '訂閱電子通訊',
            'sc': '订阅电子通讯',
            },

        'copy_right': {
            'en': 'West Kowloon Cultural District Authority © ',
            'tc': '西九文化區管理局 © ',
            'sc': '西九文化区管理局 © ',
            },

}



def generate_locale_dict(language, lang):
    new_dict = dict()
    for tpl in language.items():
        variable,translation = tpl
        new_dict[variable] = translation[lang]
    return new_dict



def concat(input_files, dest_dir):
    def container(lang):
        fileName = dest_dir + 'index_' + lang + '.html'
        with open(dest_dir + 'index_' + lang + '.html', 'w') as outfile:
            for file_name in input_files:
                with open(_src_dir + file_name, 'r') as in_file:
                    outfile.write(Template(in_file.read()).safe_substitute(generate_locale_dict(locale, lang)))
    return container
lang_compiler = concat(_input_files, _dest_dir)


lang_compiler('en')
lang_compiler('tc')
lang_compiler('sc')

print('\n🐧 <--> 🐧 <--> 🐧')
