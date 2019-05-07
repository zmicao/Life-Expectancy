# 06图：2000年中国各地区女性预期寿命热点图
# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo

indexs = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
values = [78.01, 76.63, 74.57, 73.57, 71.79, 75.36, 75.04, 74.66, 80.04, 76.23, 77.21, 73.59, 75.07, 69.32, 76.26, 73.41, 73.02, 72.47, 75.93, 73.75, 75.26, 73.89, 73.39, 67.57, 66.89, 66.15, 71.3, 68.26, 67.7, 71.84, 69.14]

geo = Geo("2000年中国各地区女性预期寿命热点图", "数据来源于《中国卫生健康统计年鉴2018》", title_color="#fff", title_pos="center", width=1200, height=600,
          background_color='#404a59')

# type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
geo.add("2000年中国各地区女性预期寿命热点图", indexs, values, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
        visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
geo.show_config()
geo.render(path="./2000年中国各地区女性预期寿命热点图.html")