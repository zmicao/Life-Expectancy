# 09图：2010年中国各地区女性预期寿命热点图
# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo

indexs = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
values = [82.21, 80.48, 77.47, 77.28, 77.27, 78.86, 78.44, 78.81, 82.44, 78.81, 80.21, 77.84, 78.64, 77.06, 79.06, 77.59, 77.35, 77.48, 79.37, 79.05, 80.01, 78.6, 77.59, 74.11, 72.43, 70.07, 76.74, 74.06, 72.07, 75.71, 74.86]

geo = Geo("2010年中国各地区女性预期寿命热点图", "数据来源于《中国卫生健康统计年鉴2018》", title_color="#fff", title_pos="center", width=1200, height=600,
          background_color='#404a59')

# type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
geo.add("2010年中国各地区女性预期寿命热点图", indexs, values, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
        visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
geo.show_config()
geo.render(path="./2010年中国各地区女性预期寿命热点图.html")