# 02图：1990年中国各地区男性预期寿命热点图
# This Python file uses the following encoding: utf-8
from pyecharts import Map, Geo

indexs = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '广西', '海南', '重庆', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
values = [71.07, 71.03, 68.47, 67.33, 64.47, 68.72, 66.65, 65.5, 72.77, 69.26, 69.66, 67.75, 66.49, 64.87, 68.64, 67.96, 65.51, 65.41, 69.71, 67.17, 66.93, 65.06, 63.04, 62.08, 57.64, 66.23, 66.35, 59.29, 65.95, 61.95]

geo = Geo("1990年中国各地区男性预期寿命热点图", "数据来源于《中国卫生健康统计年鉴2018》", title_color="#fff", title_pos="center", width=1200, height=600,
          background_color='#404a59')

# type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
geo.add("1990年中国各地区男性预期寿命热点图", indexs, values, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
        visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
geo.show_config()
geo.render(path="./1990年中国各地区男性预期寿命热点图.html")