# HeatMap of Life Expectancy in China (1990-2010)
# This Python file uses the following encoding: utf-8
from pyecharts import Bar, Timeline, Map, Geo, Page

def create_charts():
    page = Page()

    indexs_1 = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
                '湖南', '广东', '广西', '海南', '重庆', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
    values_1 = [72.86, 72.32, 70.35, 68.97, 65.68, 70.22, 67.95, 66.97, 74.9, 71.37, 71.38, 69.48, 68.57, 66.11, 70.57,
                70.15, 67.25, 66.93, 72.52, 68.72, 70.01, 66.33, 64.29, 63.49, 59.64, 67.4, 67.24, 60.57, 66.94, 63.59]

    geo_1 = Geo("中国各地区预期寿命(平均值)热点图(1990-2010)", "来自《中国卫生健康统计年鉴2018》", title_color="#000", title_pos="center",
                width=1200, height=600)

    geo_1.add("", indexs_1, values_1, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
              visual_text_color="#000", symbol_size=15, is_visualmap=True, is_roam=False)

    indexs_4 = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
                '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
    values_4 = [76.1, 74.91, 72.54, 71.65, 69.87, 73.34, 73.1, 72.37, 78.14, 73.91, 74.7, 71.85, 72.55, 68.95, 73.92,
                71.54, 71.08, 70.66, 73.27, 71.29, 72.92, 71.73, 71.2, 65.96, 65.49, 64.37, 70.07, 67.47, 66.03, 70.17,
                67.41]

    geo_4 = Geo("中国各地区预期寿命(平均值)热点图(1990-2010)", "来自《中国卫生健康统计年鉴2018》", title_color="#000", title_pos="center",
                width=1200, height=600)

    geo_4.add("", indexs_4, values_4, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
              visual_text_color="#000", symbol_size=15, is_visualmap=True, is_roam=False)

    indexs_7 = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
                '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
    values_7 = [80.18, 78.89, 74.97, 74.92, 74.44, 76.38, 76.18, 75.98, 80.26, 76.63, 77.73, 75.08, 75.76, 74.33, 76.46,
                74.57, 74.87, 74.7, 76.49, 75.11, 76.3, 75.7, 74.75, 71.1, 69.54, 68.17, 74.68, 72.23, 69.96, 73.38,
                72.35]

    geo_7 = Geo("中国各地区预期寿命(平均值)热点图(1990-2010)", "来自《中国卫生健康统计年鉴2018》", title_color="#000", title_pos="center",
                width=1200, height=600)

    geo_7.add("", indexs_7, values_7, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
              visual_text_color="#000", symbol_size=15, is_visualmap=True, is_roam=False)

    chart = Timeline(is_auto_play=True, timeline_left=80,
                     timeline_bottom=0,
                     timeline_play_interval=1600  # 每1600ms播放一张
                     )
    chart.add(geo_1, '1990年')
    chart.add(geo_4, '2000年')
    chart.add(geo_7, '2010年')
    page.add(chart)

    indexs_2 = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
                '湖南', '广东', '广西', '海南', '重庆', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
    values_2 = [71.07, 71.03, 68.47, 67.33, 64.47, 68.72, 66.65, 65.5, 72.77, 69.26, 69.66, 67.75, 66.49, 64.87, 68.64,
                67.96, 65.51, 65.41, 69.71, 67.17, 66.93, 65.06, 63.04, 62.08, 57.64, 66.23, 66.35, 59.29, 65.95, 61.95]

    geo_2 = Geo("中国各地区预期寿命(男性)热点图(1990-2010)", "来自《中国卫生健康统计年鉴2018》", title_color="#000", title_pos="center",
                width=1200, height=600)

    geo_2.add("", indexs_2, values_2, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
              visual_text_color="#000", symbol_size=15, is_visualmap=True, is_roam=False)

    indexs_5 = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
                '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
    values_5 = [74.33, 73.31, 70.68, 69.96, 68.29, 71.51, 71.38, 70.39, 76.22, 71.69, 72.5, 70.18, 70.3, 68.37, 71.7,
                69.67,
                69.31, 69.05, 70.79, 69.07, 70.66, 69.84, 69.25, 64.54, 64.24, 62.52, 68.92, 66.77, 64.55, 68.71, 65.98]

    geo_5 = Geo("中国各地区预期寿命(男性)热点图(1990-2010)", "来自《中国卫生健康统计年鉴2018》", title_color="#000", title_pos="center",
                width=1200, height=600)

    geo_5.add("", indexs_5, values_5, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
              visual_text_color="#000", symbol_size=15, is_visualmap=True, is_roam=False)

    indexs_8 = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
                '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
    values_8 = [78.28, 77.42, 72.7, 72.87, 72.04, 74.12, 74.12, 73.52, 78.2, 74.6, 75.58, 72.65, 73.27, 71.94, 74.05,
                71.84,
                72.68, 72.28, 74, 71.77, 73.2, 73.16, 72.25, 68.43, 67.06, 66.33, 72.84, 70.6, 68.11, 71.31, 70.3]

    geo_8 = Geo("中国各地区预期寿命(男性)热点图(1990-2010)", "来自《中国卫生健康统计年鉴2018》", title_color="#000", title_pos="center",
                width=1200, height=600)

    geo_8.add("", indexs_8, values_8, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
              visual_text_color="#000", symbol_size=15, is_visualmap=True, is_roam=False)

    chart = Timeline(is_auto_play=True, timeline_left=80,
                     timeline_bottom=0,
                     timeline_play_interval=1600  # 每1600ms播放一张
                     )
    chart.add(geo_2, '1990年')
    chart.add(geo_5, '2000年')
    chart.add(geo_8, '2010年')
    page.add(chart)

    indexs_3 = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
                '湖南', '广东', '广西', '海南', '重庆', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
    values_3 = [74.93, 73.73, 72.53, 70.93, 67.22, 71.94, 69.49, 68.73, 77.02, 73.57, 74.24, 71.36, 70.93, 67.49, 72.67,
                72.55, 69.23, 68.7, 75.43, 70.34, 73.28, 67.7, 65.63, 64.98, 61.57, 68.79, 68.25, 61.96, 68.05, 63.26]

    geo_3 = Geo("中国各地区预期寿命(女性)热点图(1990-2010)", "来自《中国卫生健康统计年鉴2018》", title_color="#000", title_pos="center",
                width=1200, height=600)

    geo_3.add("", indexs_3, values_3, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
              visual_text_color="#000", symbol_size=15, is_visualmap=True, is_roam=False)

    indexs_6 = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
                '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
    values_6 = [78.01, 76.63, 74.57, 73.57, 71.79, 75.36, 75.04, 74.66, 80.04, 76.23, 77.21, 73.59, 75.07, 69.32, 76.26,
                73.41, 73.02, 72.47, 75.93, 73.75, 75.26, 73.89, 73.39, 67.57, 66.89, 66.15, 71.3, 68.26, 67.7, 71.84,
                69.14]

    geo_6 = Geo("中国各地区预期寿命(女性)热点图(1990-2010)", "来自《中国卫生健康统计年鉴2018》", title_color="#000", title_pos="center",
                width=1200, height=600)

    geo_6.add("", indexs_6, values_6, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
              visual_text_color="#000", symbol_size=15, is_visualmap=True, is_roam=False)

    indexs_9 = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
                '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
    values_9 = [82.21, 80.48, 77.47, 77.28, 77.27, 78.86, 78.44, 78.81, 82.44, 78.81, 80.21, 77.84, 78.64, 77.06, 79.06,
                77.59, 77.35, 77.48, 79.37, 79.05, 80.01, 78.6, 77.59, 74.11, 72.43, 70.07, 76.74, 74.06, 72.07, 75.71,
                74.86]

    geo_9 = Geo("中国各地区预期寿命(女性)热点图(1990-2010)", "来自《中国卫生健康统计年鉴2018》", title_color="#000", title_pos="center",
                width=1200, height=600)

    geo_9.add("", indexs_9, values_9, type="effectScatter", is_random=True, effect_scale=5, visual_range=[57, 83],
              visual_text_color="#000", symbol_size=15, is_visualmap=True, is_roam=False)

    chart = Timeline(is_auto_play=True, timeline_left=80,
                     timeline_bottom=0,
                     timeline_play_interval=1600  # 每1600ms播放一张
                     )
    chart.add(geo_3, '1990年')
    chart.add(geo_6, '2000年')
    chart.add(geo_9, '2010年')
    page.add(chart)
    return page

create_charts().render(path="./中国主要年份各地区预期寿命统计(1990-2010)热点图.html")
