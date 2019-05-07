# 01图：1990年中国各地区预期寿命平均值热点图
# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo

indexs = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
values = [72.86, 72.32, 70.35, 68.97, 65.68, 70.22, 67.95, 66.97, 74.9, 71.37, 71.38, 69.48, 68.57, 66.11, 70.57, 70.15, 67.25, 66.93, 72.52, 68.72, 70.01, 66.33, 64.29, 63.49, 59.64, 67.4, 67.24, 60.57, 66.94, 63.59]

geo = Geo("1990年中国各地区预期寿命平均值热点图", "数据来源于《中国卫生健康统计年鉴2018》", title_color="#fff", title_pos="center", width=1200, height=600,
          background_color='#404a59')

# type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
geo.add("1990年中国各地区预期寿命平均值统计", indexs, values, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
        visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
geo.show_config()
geo.render(path="./1990年中国各地区预期寿命平均值热点图.html")