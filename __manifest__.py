# -*- coding: utf-8 -*-
{
    'name': "美味公司演示数据",

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
    'depends': ['accountcore'],
    'application': False,
    'images': ['static/description/icon.png'],
    'data': [
        'data/glob_tag.xml',
        'data/users.xml',
        'data/org.xml',
        'data/items_wang_lai.xml',
        'data/items_bu_men.xml',
        'data/items_yuan_gong.xml',
        'data/items_yuan_cai_liao.xml',
        'data/items_ku_cun_shang_pin.xml',
        'data/items_yuan_cai_liao.xml',
        'data/items_yuan_cai_liao.xml',
        'data/items_cheng_ben_fei_yong.xml',
        'data/items_di_zhi_yi_hao.xml',
        'data/items_gu_ding_zi_chan.xml',
        'data/items_wu_xing_zi_chan.xml',
        'data/items_cheng_ben_dui_xiang.xml',
        'data/items_zai_jian_gong_chen.xml',
        'data/items_zhou_zhuan_cai_liao.xml',
        'data/report_model.xml',
    ],
    'post_init_hook': '_load',
    'uninstall_hook': '_uninstall',
}
