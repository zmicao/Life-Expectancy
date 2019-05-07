# 04图：2000年中国各地区预期寿命平均值热点图
# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo

indexs = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
values = [76.1, 74.91, 72.54, 71.65, 69.87, 73.34, 73.1, 72.37, 78.14, 73.91, 74.7, 71.85, 72.55, 68.95, 73.92, 71.54, 71.08, 70.66, 73.27, 71.29, 72.92, 71.73, 71.2, 65.96, 65.49, 64.37, 70.07, 67.47, 66.03, 70.17, 67.41]

geo = Geo("2000年中国各地区预期寿命平均值热点图", "数据来源于《中国卫生健康统计年鉴2018》", title_color="#fff", title_pos="center", width=1200, height=600,
          background_color='#404a59')

# type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
geo.add("2000年中国各地区预期寿命平均值热点图", indexs, values, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
        visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
geo.show_config()
geo.render(path="./2000年中国各地区预期寿命平均值热点图.html")