# 03图：1990年中国各地区女性预期寿命热点图
# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo

indexs = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
values = [74.93, 73.73, 72.53, 70.93, 67.22, 71.94, 69.49, 68.73, 77.02, 73.57, 74.24, 71.36, 70.93, 67.49, 72.67, 72.55, 69.23, 68.7, 75.43, 70.34, 73.28, 67.7, 65.63, 64.98, 61.57, 68.79, 68.25, 61.96, 68.05, 63.26]

geo = Geo("1990年中国各地区女性预期寿命热点图", "数据来源于《中国卫生健康统计年鉴2018》", title_color="#fff", title_pos="center", width=1200, height=600,
          background_color='#404a59')

# type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
geo.add("1990年中国各地区女性预期寿命热点图", indexs, values, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
        visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
geo.show_config()
geo.render(path="./1990年中国各地区女性预期寿命热点图.html")