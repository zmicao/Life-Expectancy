# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo
# 省和直辖市
province_distribution = {'北京': 72.86, '天津': 72.32, '河北': 70.35, '山西': 68.97, '内蒙古': 65.68, '辽宁': 70.22, '吉林': 67.95, '黑龙江': 66.97, '上海': 74.9, '江苏': 71.37, '浙江': 71.38, '安徽': 69.48, '福建': 68.57, '江西': 66.11, '山东': 70.57, '河南': 70.15, '湖北': 67.25, '湖南': 66.93, '广东': 72.52, '广西': 68.72, '海南': 70.01, '重庆': 66.33, '贵州': 64.29, '云南': 63.49, '西藏': 59.64, '陕西': 67.4, '甘肃': 67.24, '青海': 60.57, '宁夏': 66.94, '新疆': 63.59}
provice=list(province_distribution.keys())
values=list(province_distribution.values())
# maptype='china' 只显示全国直辖市和省级
# 数据只能是省名和直辖市的名称
map = Map("1990年中国各地区预期寿命统计",'平均值', width=1200, height=600)
map.add("", provice, values, visual_range=[57, 83],  maptype='china', is_visualmap=True, is_map_symbol_show=False,
    visual_text_color='#000')
map.show_config()
map.render(path="./1990年中国各地区预期寿命平均值统计.html")