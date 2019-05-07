# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo
# 省和直辖市
province_distribution = {'北京': 78.28, '天津': 77.42, '河北': 72.7, '山西': 72.87, '内蒙古': 72.04, '辽宁': 74.12, '吉林': 74.12, '黑龙江': 73.52, '上海': 78.2, '江苏': 74.6, '浙江': 75.58, '安徽': 72.65, '福建': 73.27, '江西': 71.94, '山东': 74.05, '河南': 71.84, '湖北': 72.68, '湖南': 72.28, '广东': 74, '广西': 71.77, '海南': 73.2, '重庆': 73.16, '四川': 72.25, '贵州': 68.43, '云南': 67.06, '西藏': 66.33, '陕西': 72.84, '甘肃': 70.6, '青海': 68.11, '宁夏': 71.31, '新疆': 70.3}
provice=list(province_distribution.keys())
values=list(province_distribution.values())
# maptype='china' 只显示全国直辖市和省级
# 数据只能是省名和直辖市的名称
map = Map("2010年中国各地区预期寿命统计",'男性', width=1200, height=600)
map.add("", provice, values, visual_range=[57, 83],  maptype='china', is_visualmap=True, is_map_symbol_show=False,
    visual_text_color='#000')
map.show_config()
map.render(path="./2010年中国各地区男性预期寿命统计.html")