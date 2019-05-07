# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo
# 省和直辖市
province_distribution = {'北京': 76.1, '天津': 74.91, '河北': 72.54, '山西': 71.65, '内蒙古': 69.87, '辽宁': 73.34, '吉林': 73.1, '黑龙江': 72.37, '上海': 78.14, '江苏': 73.91, '浙江': 74.7, '安徽': 71.85, '福建': 72.55, '江西': 68.95, '山东': 73.92, '河南': 71.54, '湖北': 71.08, '湖南': 70.66, '广东': 73.27, '广西': 71.29, '海南': 72.92, '重庆': 71.73, '四川': 71.2, '贵州': 65.96, '云南': 65.49, '西藏': 64.37, '陕西': 70.07, '甘肃': 67.47, '青海': 66.03, '宁夏': 70.17, '新疆': 67.41}
provice=list(province_distribution.keys())
values=list(province_distribution.values())
# maptype='china' 只显示全国直辖市和省级
# 数据只能是省名和直辖市的名称
map = Map("2000年中国各地区预期寿命统计",'平均值', width=1200, height=600)
map.add("", provice, values, visual_range=[57, 83],  maptype='china', is_visualmap=True, is_map_symbol_show=False,
    visual_text_color='#000')
map.show_config()
map.render(path="./2000年中国各地区预期寿命平均值统计.html")