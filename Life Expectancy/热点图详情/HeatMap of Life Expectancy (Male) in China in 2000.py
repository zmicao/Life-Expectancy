# 05图：2000年中国各地区男性预期寿命热点图
# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo

indexs = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
values = [74.33, 73.31, 70.68, 69.96, 68.29, 71.51, 71.38, 70.39, 76.22, 71.69, 72.5, 70.18, 70.3, 68.37, 71.7, 69.67, 69.31, 69.05, 70.79, 69.07, 70.66, 69.84, 69.25, 64.54, 64.24, 62.52, 68.92, 66.77, 64.55, 68.71, 65.98]

geo = Geo("2000年中国各地区男性预期寿命热点图", "数据来源于《中国卫生健康统计年鉴2018》", title_color="#fff", title_pos="center", width=1200, height=600,
          background_color='#404a59')

# type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
geo.add("2000年中国各地区男性预期寿命热点图", indexs, values, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
        visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
geo.show_config()
geo.render(path="./2000年中国各地区男性预期寿命热点图.html")
