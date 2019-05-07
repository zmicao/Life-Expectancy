# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo
# 省和直辖市
province_distribution = {'北京': 74.33, '天津': 73.31, '河北': 70.68, '山西': 69.96, '内蒙古': 68.29, '辽宁': 71.51, '吉林': 71.38, '黑龙江': 70.39, '上海': 76.22, '江苏': 71.69, '浙江': 72.5, '安徽': 70.18, '福建': 70.3, '江西': 68.37, '山东': 71.7, '河南': 69.67, '湖北': 69.31, '湖南': 69.05, '广东': 70.79, '广西': 69.07, '海南': 70.66, '重庆': 69.84, '四川': 69.25, '贵州': 64.54, '云南': 64.24, '西藏': 62.52, '陕西': 68.92, '甘肃': 66.77, '青海': 64.55, '宁夏': 68.71, '新疆': 65.98}
provice=list(province_distribution.keys())
values=list(province_distribution.values())
# maptype='china' 只显示全国直辖市和省级
# 数据只能是省名和直辖市的名称
map = Map("2000年中国各地区预期寿命统计",'男性', width=1200, height=600)
map.add("", provice, values, visual_range=[57, 83],  maptype='china', is_visualmap=True, is_map_symbol_show=False,
    visual_text_color='#000')
map.show_config()
map.render(path="./2000年中国各地区男性预期寿命统计.html")