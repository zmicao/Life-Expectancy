# 08图：2010年中国各地区男性预期寿命热点图
# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo

indexs = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
values = [78.28, 77.42, 72.7, 72.87, 72.04, 74.12, 74.12, 73.52, 78.2, 74.6, 75.58, 72.65, 73.27, 71.94, 74.05, 71.84, 72.68, 72.28, 74, 71.77, 73.2, 73.16, 72.25, 68.43, 67.06, 66.33, 72.84, 70.6, 68.11, 71.31, 70.3]

geo = Geo("2010年中国各地区男性预期寿命热点图", "数据来源于《中国卫生健康统计年鉴2018》", title_color="#fff", title_pos="center", width=1200, height=600,
          background_color='#404a59')

# type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
geo.add("2010年中国各地区男性预期寿命热点图", indexs, values, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
        visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
geo.show_config()
geo.render(path="./2010年中国各地区男性预期寿命热点图.html")
