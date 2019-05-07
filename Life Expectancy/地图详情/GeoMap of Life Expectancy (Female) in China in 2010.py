# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo
# 省和直辖市
province_distribution = {'北京': 82.21, '天津': 80.48, '河北': 77.47, '山西': 77.28, '内蒙古': 77.27, '辽宁': 78.86, '吉林': 78.44, '黑龙江': 78.81, '上海': 82.44, '江苏': 78.81, '浙江': 80.21, '安徽': 77.84, '福建': 78.64, '江西': 77.06, '山东': 79.06, '河南': 77.59, '湖北': 77.35, '湖南': 77.48, '广东': 79.37, '广西': 79.05, '海南': 80.01, '重庆': 78.6, '四川': 77.59, '贵州': 74.11, '云南': 72.43, '西藏': 70.07, '陕西': 76.74, '甘肃': 74.06, '青海': 72.07, '宁夏': 75.71, '新疆': 74.86}
provice=list(province_distribution.keys())
values=list(province_distribution.values())
# maptype='china' 只显示全国直辖市和省级
# 数据只能是省名和直辖市的名称
map = Map("2010年中国各地区预期寿命统计",'女性', width=1200, height=600)
map.add("", provice, values, visual_range=[57, 83],  maptype='china', is_visualmap=True, is_map_symbol_show=False,
    visual_text_color='#000')
map.show_config()
map.render(path="./2010年中国各地区女性预期寿命统计.html")