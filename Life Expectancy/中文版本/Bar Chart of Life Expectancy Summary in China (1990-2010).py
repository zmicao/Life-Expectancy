from pyecharts import Bar, Timeline

attr = ["平均值", "男性", "女性"]
v1 =[68.55, 66.84, 70.47]
v2 =[71.40, 69.63, 73.33]
v3 =[74.83, 72.38, 77.37]

bar_1 = Bar("1990年中国各地区预期寿命(岁)总计", "来源于《中国卫生健康统计年鉴2018》")
bar_1.add("", attr, v1)

bar_2 = Bar("2000年中国各地区预期寿命(岁)总计", "来源于《中国卫生健康统计年鉴2018》")
bar_2.add("", attr, v2)

bar_3 = Bar("2010年中国各地区预期寿命(岁)总计", "来源于《中国卫生健康统计年鉴2018》")
bar_3.add("", attr, v3, is_legend_show=True)

timeline = Timeline(is_auto_play=True,
                    timeline_bottom=0,
                    timeline_play_interval=1600  # 每1600ms播放一张
                   )

timeline.add(bar_1, '1990年')
timeline.add(bar_2, '2000年')
timeline.add(bar_3, '2010年')
timeline.render(path = "./中国主要年份各地区预期寿命总计(柱形图).html")