# This Python file uses the following encoding: utf-8
from pyecharts import Bar, Timeline, Map, Geo, Page

def create_charts():
    page = Page()

    province_distribution_1 = {'北京': 72.86, '天津': 72.32, '河北': 70.35, '山西': 68.97, '内蒙古': 65.68, '辽宁': 70.22,
                               '吉林': 67.95,
                               '黑龙江': 66.97, '上海': 74.9, '江苏': 71.37, '浙江': 71.38, '安徽': 69.48, '福建': 68.57,
                               '江西': 66.11,
                               '山东': 70.57, '河南': 70.15, '湖北': 67.25, '湖南': 66.93, '广东': 72.52, '广西': 68.72,
                               '海南': 70.01,
                               '重庆': 66.33, '贵州': 64.29, '云南': 63.49, '西藏': 59.64, '陕西': 67.4, '甘肃': 67.24, '青海': 60.57,
                               '宁夏': 66.94, '新疆': 63.59}
    provice_1 = list(province_distribution_1.keys())
    values_1 = list(province_distribution_1.values())
    map_1 = Map("Life Expectancy by Regions in China (1990-2010)", 'Average', title_pos="center", width=1200, height=600)
    map_1.add("", provice_1, values_1, visual_range=[57, 83], maptype='china', is_visualmap=True, is_map_symbol_show=False,
              visual_text_color='#000')

    province_distribution_4 = {'北京': 76.1, '天津': 74.91, '河北': 72.54, '山西': 71.65, '内蒙古': 69.87, '辽宁': 73.34, '吉林': 73.1,
                               '黑龙江': 72.37, '上海': 78.14, '江苏': 73.91, '浙江': 74.7, '安徽': 71.85, '福建': 72.55,
                               '江西': 68.95,
                               '山东': 73.92, '河南': 71.54, '湖北': 71.08, '湖南': 70.66, '广东': 73.27, '广西': 71.29,
                               '海南': 72.92,
                               '重庆': 71.73, '四川': 71.2, '贵州': 65.96, '云南': 65.49, '西藏': 64.37, '陕西': 70.07, '甘肃': 67.47,
                               '青海': 66.03, '宁夏': 70.17, '新疆': 67.41}
    provice_4 = list(province_distribution_4.keys())
    values_4 = list(province_distribution_4.values())
    map_4 = Map("Life Expectancy by Regions in China (1990-2010)", 'Average', title_pos="center", width=1200, height=600)
    map_4.add("", provice_4, values_4, visual_range=[57, 83], maptype='china', is_visualmap=True, is_map_symbol_show=False,
              visual_text_color='#000')

    province_distribution_7 = {'北京': 80.18, '天津': 78.89, '河北': 74.97, '山西': 74.92, '内蒙古': 74.44, '辽宁': 76.38,
                               '吉林': 76.18,
                               '黑龙江': 75.98, '上海': 80.26, '江苏': 76.63, '浙江': 77.73, '安徽': 75.08, '福建': 75.76,
                               '江西': 74.33,
                               '山东': 76.46, '河南': 74.57, '湖北': 74.87, '湖南': 74.7, '广东': 76.49, '广西': 75.11, '海南': 76.3,
                               '重庆': 75.7, '四川': 74.75, '贵州': 71.1, '云南': 69.54, '西藏': 68.17, '陕西': 74.68, '甘肃': 72.23,
                               '青海': 69.96, '宁夏': 73.38, '新疆': 72.35}
    provice_7 = list(province_distribution_7.keys())
    values_7 = list(province_distribution_7.values())
    map_7 = Map("Life Expectancy by Regions in China (1990-2010)", 'Average', title_pos="center", width=1200, height=600)
    map_7.add("", provice_7, values_7, visual_range=[57, 83], maptype='china', is_visualmap=True, is_map_symbol_show=False,
              visual_text_color='#000')

    chart = Timeline(is_auto_play=True, timeline_left=80,
                     timeline_bottom=0,
                     timeline_play_interval=1600  # Play next Chart Every 1600ms
                     )
    chart.add(map_1, '1990')
    chart.add(map_4, '2000')
    chart.add(map_7, '2010')
    page.add(chart)

    province_distribution_2 = {'北京': 71.07, '天津': 71.03, '河北': 68.47, '山西': 67.33, '内蒙古': 64.47, '辽宁': 68.72,
                               '吉林': 66.65,
                               '黑龙江': 65.5, '上海': 72.77, '江苏': 69.26, '浙江': 69.66, '安徽': 67.75, '福建': 66.49,
                               '江西': 64.87,
                               '山东': 68.64, '河南': 67.96, '湖北': 65.51, '湖南': 65.41, '广东': 69.71, '广西': 67.17,
                               '海南': 66.93,
                               '重庆': 65.06, '贵州': 63.04, '云南': 62.08, '西藏': 57.64, '陕西': 66.23, '甘肃': 66.35,
                               '青海': 59.29,
                               '宁夏': 65.95, '新疆': 61.95}
    provice_2 = list(province_distribution_2.keys())
    values_2 = list(province_distribution_2.values())
    map_2 = Map("Life Expectancy by Regions in China (1990-2010)", 'Male', title_pos="center", width=1200, height=600)
    map_2.add("", provice_2, values_2, visual_range=[57, 83], maptype='china', is_visualmap=True, is_map_symbol_show=False,
              visual_text_color='#000')

    province_distribution_5 = {'北京': 74.33, '天津': 73.31, '河北': 70.68, '山西': 69.96, '内蒙古': 68.29, '辽宁': 71.51,
                               '吉林': 71.38,
                               '黑龙江': 70.39, '上海': 76.22, '江苏': 71.69, '浙江': 72.5, '安徽': 70.18, '福建': 70.3, '江西': 68.37,
                               '山东': 71.7, '河南': 69.67, '湖北': 69.31, '湖南': 69.05, '广东': 70.79, '广西': 69.07, '海南': 70.66,
                               '重庆': 69.84, '四川': 69.25, '贵州': 64.54, '云南': 64.24, '西藏': 62.52, '陕西': 68.92,
                               '甘肃': 66.77,
                               '青海': 64.55, '宁夏': 68.71, '新疆': 65.98}
    provice_5 = list(province_distribution_5.keys())
    values_5 = list(province_distribution_5.values())
    map_5 = Map("Life Expectancy by Regions in China (1990-2010)", 'Male', title_pos="center", width=1200, height=600)
    map_5.add("", provice_5, values_5, visual_range=[57, 83], maptype='china', is_visualmap=True, is_map_symbol_show=False,
              visual_text_color='#000')

    province_distribution_8 = {'北京': 78.28, '天津': 77.42, '河北': 72.7, '山西': 72.87, '内蒙古': 72.04, '辽宁': 74.12,
                               '吉林': 74.12,
                               '黑龙江': 73.52, '上海': 78.2, '江苏': 74.6, '浙江': 75.58, '安徽': 72.65, '福建': 73.27, '江西': 71.94,
                               '山东': 74.05, '河南': 71.84, '湖北': 72.68, '湖南': 72.28, '广东': 74, '广西': 71.77, '海南': 73.2,
                               '重庆': 73.16, '四川': 72.25, '贵州': 68.43, '云南': 67.06, '西藏': 66.33, '陕西': 72.84, '甘肃': 70.6,
                               '青海': 68.11, '宁夏': 71.31, '新疆': 70.3}
    provice_8 = list(province_distribution_8.keys())
    values_8 = list(province_distribution_8.values())
    map_8 = Map("Life Expectancy by Regions in China (1990-2010)", 'Male', title_pos="center", width=1200, height=600)
    map_8.add("", provice_8, values_8, visual_range=[57, 83], maptype='china', is_visualmap=True, is_map_symbol_show=False,
              visual_text_color='#000')

    chart = Timeline(is_auto_play=True, timeline_left=80,
                     timeline_bottom=0,
                     timeline_play_interval=1600  # Play next Chart Every 1600ms
                     )
    chart.add(map_2, '1990')
    chart.add(map_5, '2000')
    chart.add(map_8, '2010')
    page.add(chart)

    province_distribution_3 = {'北京': 74.93, '天津': 73.73, '河北': 72.53, '山西': 70.93, '内蒙古': 67.22, '辽宁': 71.94,
                               '吉林': 69.49,
                               '黑龙江': 68.73, '上海': 77.02, '江苏': 73.57, '浙江': 74.24, '安徽': 71.36, '福建': 70.93,
                               '江西': 67.49,
                               '山东': 72.67, '河南': 72.55, '湖北': 69.23, '湖南': 68.7, '广东': 75.43, '广西': 70.34, '海南': 73.28,
                               '重庆': 67.7, '贵州': 65.63, '云南': 64.98, '西藏': 61.57, '陕西': 68.79, '甘肃': 68.25, '青海': 61.96,
                               '宁夏': 68.05, '新疆': 63.26}
    provice_3 = list(province_distribution_3.keys())
    values_3 = list(province_distribution_3.values())
    map_3 = Map("Life Expectancy by Regions in China (1990-2010)", 'Female', title_pos="center", width=1200, height=600)
    map_3.add("", provice_3, values_3, visual_range=[57, 83], maptype='china', is_visualmap=True, is_map_symbol_show=False,
              visual_text_color='#000')

    province_distribution_6 = {'北京': 78.01, '天津': 76.63, '河北': 74.57, '山西': 73.57, '内蒙古': 71.79, '辽宁': 75.36,
                               '吉林': 75.04,
                               '黑龙江': 74.66, '上海': 80.04, '江苏': 76.23, '浙江': 77.21, '安徽': 73.59, '福建': 75.07,
                               '江西': 69.32,
                               '山东': 76.26, '河南': 73.41, '湖北': 73.02, '湖南': 72.47, '广东': 75.93, '广西': 73.75,
                               '海南': 75.26,
                               '重庆': 73.89, '四川': 73.39, '贵州': 67.57, '云南': 66.89, '西藏': 66.15, '陕西': 71.3, '甘肃': 68.26,
                               '青海': 67.7, '宁夏': 71.84, '新疆': 69.14}
    provice_6 = list(province_distribution_6.keys())
    values_6 = list(province_distribution_6.values())
    map_6 = Map("Life Expectancy by Regions in China (1990-2010)", 'Female', title_pos="center", width=1200, height=600)
    map_6.add("", provice_6, values_6, visual_range=[57, 83], maptype='china', is_visualmap=True, is_map_symbol_show=False,
              visual_text_color='#000')

    province_distribution_9 = {'北京': 82.21, '天津': 80.48, '河北': 77.47, '山西': 77.28, '内蒙古': 77.27, '辽宁': 78.86,
                               '吉林': 78.44,
                               '黑龙江': 78.81, '上海': 82.44, '江苏': 78.81, '浙江': 80.21, '安徽': 77.84, '福建': 78.64,
                               '江西': 77.06,
                               '山东': 79.06, '河南': 77.59, '湖北': 77.35, '湖南': 77.48, '广东': 79.37, '广西': 79.05,
                               '海南': 80.01,
                               '重庆': 78.6, '四川': 77.59, '贵州': 74.11, '云南': 72.43, '西藏': 70.07, '陕西': 76.74, '甘肃': 74.06,
                               '青海': 72.07, '宁夏': 75.71, '新疆': 74.86}
    provice_9 = list(province_distribution_9.keys())
    values_9 = list(province_distribution_9.values())
    map_9 = Map("Life Expectancy by Regions in China (1990-2010)", 'Female', title_pos="center", width=1200, height=600)
    map_9.add("", provice_9, values_9, visual_range=[57, 83], maptype='china', is_visualmap=True, is_map_symbol_show=False,
              visual_text_color='#000')

    chart = Timeline(is_auto_play=True, timeline_left=80,
                     timeline_bottom=0,
                     timeline_play_interval=1600  # Play next Chart Every 1600ms
                     )
    chart.add(map_3, '1990')
    chart.add(map_6, '2000')
    chart.add(map_9, '2010')
    page.add(chart)
    return page

create_charts().render(path="./GeoMap of Life Expectancy by Regions in China (1990-2010).html")