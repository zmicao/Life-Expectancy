# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo
# 省和直辖市
province_distribution = {'北京': 74.93, '天津': 73.73, '河北': 72.53, '山西': 70.93, '内蒙古': 67.22, '辽宁': 71.94, '吉林': 69.49, '黑龙江': 68.73, '上海': 77.02, '江苏': 73.57, '浙江': 74.24, '安徽': 71.36, '福建': 70.93, '江西': 67.49, '山东': 72.67, '河南': 72.55, '湖北': 69.23, '湖南': 68.7, '广东': 75.43, '广西': 70.34, '海南': 73.28, '重庆': 67.7, '贵州': 65.63, '云南': 64.98, '西藏': 61.57, '陕西': 68.79, '甘肃': 68.25, '青海': 61.96, '宁夏': 68.05, '新疆': 63.26}
provice=list(province_distribution.keys())
values=list(province_distribution.values())
# maptype='china' 只显示全国直辖市和省级
# 数据只能是省名和直辖市的名称
map = Map("1990年中国各地区预期寿命统计",'女性', width=1200, height=600)
map.add("", provice, values, visual_range=[57, 83],  maptype='china', is_visualmap=True, is_map_symbol_show=False,
    visual_text_color='#000')
map.show_config()
map.render(path="./1990年中国各地区女性预期寿命统计.html")