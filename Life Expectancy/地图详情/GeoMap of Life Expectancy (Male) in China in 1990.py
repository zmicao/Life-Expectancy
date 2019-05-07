# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo
# 省和直辖市
province_distribution = {'北京': 71.07, '天津': 71.03, '河北': 68.47, '山西': 67.33, '内蒙古': 64.47, '辽宁': 68.72, '吉林': 66.65, '黑龙江': 65.5, '上海': 72.77, '江苏': 69.26, '浙江': 69.66, '安徽': 67.75, '福建': 66.49, '江西': 64.87, '山东': 68.64, '河南': 67.96, '湖北': 65.51, '湖南': 65.41, '广东': 69.71, '广西': 67.17, '海南': 66.93, '重庆': 65.06, '贵州': 63.04, '云南': 62.08, '西藏': 57.64, '陕西': 66.23, '甘肃': 66.35, '青海': 59.29, '宁夏': 65.95, '新疆': 61.95}
provice=list(province_distribution.keys())
values=list(province_distribution.values())
# maptype='china' 只显示全国直辖市和省级
# 数据只能是省名和直辖市的名称
map = Map("1990年中国各地区预期寿命统计",'男性', width=1200, height=600)
map.add("", provice, values, visual_range=[57, 83],  maptype='china', is_visualmap=True, is_map_symbol_show=False,
    visual_text_color='#000')
map.show_config()
map.render(path="./1990年中国各地区男性预期寿命统计.html")