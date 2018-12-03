from alipay import AliPay
from django.shortcuts import render, redirect

from shopping import settings


def pay(request):
    # 第一步实例化Alipay对象
    alipay = AliPay(
        appid=settings.APP_ID,
        app_notify_url=None,
        app_private_key_string=settings.APP_PRIVATE_KEY_STR,
        alipay_public_key_string=settings.APP_PUBLIC_KEY_STR,
        sign_type='RSA',
        debug=True
    )

    # 生成支付的参数
    """
    subject 支付的标题
    # 生成的订单号
    out_trade_no 
    # 支付的总金额
    total_amount
    # 支付完成之后前端跳转的界面 get请求
    return_url
    # 支付完成之后台回调接口
    notify_url post请求
    """
    # 跨域文件
    # csrf
    #
    order_str = alipay.api_alipay_trade_page_pay(
        subject='91支付-123',
        total_amount='100',
        out_trade_no='1234567',
        return_url='https://www.163.com/',
    )
    return redirect(settings.PAY_URL_DEV + '?' + order_str)


# 回调的url地址
def pay_callback(request):
    pass
