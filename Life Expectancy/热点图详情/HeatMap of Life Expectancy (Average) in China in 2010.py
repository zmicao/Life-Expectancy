# 07图：2010年中国各地区预期寿命平均值热点图
# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo

indexs = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
values = [80.18, 78.89, 74.97, 74.92, 74.44, 76.38, 76.18, 75.98, 80.26, 76.63, 77.73, 75.08, 75.76, 74.33, 76.46, 74.57, 74.87, 74.7, 76.49, 75.11, 76.3, 75.7, 74.75, 71.1, 69.54, 68.17, 74.68, 72.23, 69.96, 73.38, 72.35]

geo = Geo("2010年中国各地区预期寿命平均值热点图", "数据来源于《中国卫生健康统计年鉴2018》", title_color="#fff", title_pos="center", width=1200, height=600,
          background_color='#404a59')

# type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
geo.add("2010年中国各地区预期寿命平均值热点图", indexs, values, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
        visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
geo.show_config()
geo.render(path="./2010年中国各地区预期寿命平均值热点图.html")