import xadmin

# 全局配置
from xadmin import views

from apps.main.models import Navigation, Shop, User


class BaseStyleSettings:
    # 开启主题修改
    enable_themes = True
    # 使用bootbootstrap的主题
    use_bootswatch = True


# 注册自定义全局配置
xadmin.site.register(views.BaseAdminView, BaseStyleSettings)


class GlobalSettings:
    # 修改标题
    site_title = '91商城后台管理'
    # 修改底部显示
    site_footer = '91科技有限公司,用技术解决你的空虚'


xadmin.site.register(views.CommAdminView, GlobalSettings)


class NavigationAdmin:
    # 默认情况下显示object对象
    list_display = ['nav_id', 'nav_name']


xadmin.site.register(Navigation, NavigationAdmin)


class ShopAdmin:
    # 默认情况下显示object对象
    list_display = ['shop_id', 'name', 'sub_title', 'create_date']
    # 修改分页的默认的条数
    list_per_page = 10
    # 搜索字段
    search_fields = ['name', 'sub_title']
    list_editor = []


xadmin.site.register(Shop, ShopAdmin)

# 自定义的admin
from xadmin.plugins import auth


# 显示自定义的方式
class UserAdmin(auth.UserAdmin):
    list_display = ['id', 'username', 'email', 'img_show']


# 先注销
xadmin.site.unregister(User)
# 在注册
xadmin.site.register(User, UserAdmin)
