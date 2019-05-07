from pyecharts import Bar, Timeline

attr = ["Average", "Male", "Female"]
v1 =[68.55, 66.84, 70.47]
v2 =[71.40, 69.63, 73.33]
v3 =[74.83, 72.38, 77.37]

bar_1 = Bar("Bar Chart of Life Expectancy by Regions in China in 1990", "From: China's Health Statistics Yearbook 2018")
bar_1.add("", attr, v1)

bar_2 = Bar("Bar Chart of Life Expectancy by Regions in China in 2000", "From: China's Health Statistics Yearbook 2018")
bar_2.add("", attr, v2)

bar_3 = Bar("Bar Chart of Life Expectancy by Regions in China in 2010", "From: China's Health Statistics Yearbook 2018")
bar_3.add("", attr, v3, is_legend_show=True)

timeline = Timeline(is_auto_play=True,
                    timeline_bottom=0,
                    timeline_play_interval=1600  # Play next Chart Every 1600ms
                   )

timeline.add(bar_1, '1990')
timeline.add(bar_2, '2000')
timeline.add(bar_3, '2010')
timeline.render(path = "./Bar Chart of Life Expectancy by Regions in China (1990-2010).html")