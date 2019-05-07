# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo
# 省和直辖市
province_distribution = {'北京': 80.18, '天津': 78.89, '河北': 74.97, '山西': 74.92, '内蒙古': 74.44, '辽宁': 76.38, '吉林': 76.18, '黑龙江': 75.98, '上海': 80.26, '江苏': 76.63, '浙江': 77.73, '安徽': 75.08, '福建': 75.76, '江西': 74.33, '山东': 76.46, '河南': 74.57, '湖北': 74.87, '湖南': 74.7, '广东': 76.49, '广西': 75.11, '海南': 76.3, '重庆': 75.7, '四川': 74.75, '贵州': 71.1, '云南': 69.54, '西藏': 68.17, '陕西': 74.68, '甘肃': 72.23, '青海': 69.96, '宁夏': 73.38, '新疆': 72.35}
provice=list(province_distribution.keys())
values=list(province_distribution.values())
# maptype='china' 只显示全国直辖市和省级
# 数据只能是省名和直辖市的名称
map = Map("2010年中国各地区预期寿命统计",'平均值', width=1200, height=600)
map.add("", provice, values, visual_range=[57, 83],  maptype='china', is_visualmap=True, is_map_symbol_show=False,
    visual_text_color='#000')
map.show_config()
map.render(path="./2010年中国各地区预期寿命平均值统计.html")