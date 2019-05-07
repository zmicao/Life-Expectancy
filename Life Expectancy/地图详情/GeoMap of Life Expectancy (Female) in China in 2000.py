# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo
# 省和直辖市
province_distribution = {'北京': 78.01, '天津': 76.63, '河北': 74.57, '山西': 73.57, '内蒙古': 71.79, '辽宁': 75.36, '吉林': 75.04, '黑龙江': 74.66, '上海': 80.04, '江苏': 76.23, '浙江': 77.21, '安徽': 73.59, '福建': 75.07, '江西': 69.32, '山东': 76.26, '河南': 73.41, '湖北': 73.02, '湖南': 72.47, '广东': 75.93, '广西': 73.75, '海南': 75.26, '重庆': 73.89, '四川': 73.39, '贵州': 67.57, '云南': 66.89, '西藏': 66.15, '陕西': 71.3, '甘肃': 68.26, '青海': 67.7, '宁夏': 71.84, '新疆': 69.14}
provice=list(province_distribution.keys())
values=list(province_distribution.values())
# maptype='china' 只显示全国直辖市和省级
# 数据只能是省名和直辖市的名称
map = Map("2000年中国各地区预期寿命统计",'女性', width=1200, height=600)
map.add("", provice, values, visual_range=[57, 83],  maptype='china', is_visualmap=True, is_map_symbol_show=False,
    visual_text_color='#000')
map.show_config()
map.render(path="./2000年中国各地区女性预期寿命统计.html")