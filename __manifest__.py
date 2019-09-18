# -*- coding: utf-8 -*-
{
    'name': "ac_demo_meiwei",

    'summary': """
        AccountCore模块的演示数据。安装Accourcore后，安装该模块，
        卸载该模块将删除全部记账凭证，期初余额，核算项目和相关科目""",

    'description': """
        美味食品(北京)有限公司，是一家制作糕点的连锁公司，其有若干门店和多家公司。
    """,
    'author': "黄虎",
    'website': "http://www.baidu.com",
    'category': 'accountcore/demo',
    'version': '0.1',
    'depends': ['base', 'accountcore'],
    'application': False,
    'images': ['static/description/icon.png'],
    'data': [
        'demo/users.xml',
        'demo/org.xml',
        'demo/items_wang_lai.xml',
        'demo/items_bu_men.xml',
        'demo/items_yuan_gong.xml',
        'demo/items_yuan_cai_liao.xml',
        'demo/items_ku_cun_shang_pin.xml',
        'demo/items_yuan_cai_liao.xml',
        'demo/items_yuan_cai_liao.xml',
        'demo/items_cheng_ben_fei_yong.xml',
        'demo/items_di_zhi_yi_hao.xml',
        'demo/items_gu_ding_zi_chan.xml',
        'demo/items_wu_xing_zi_chan.xml',
        'demo/accounts.xml',
    ],
    'demo': [

    ],
    'post_init_hook': '_load',
    'uninstall_hook': '_uninstall',
}
