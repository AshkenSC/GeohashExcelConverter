from openpyxl import load_workbook
import pygeohash as pgh
import matplotlib.pyplot as plt


# step1: 载入工作表
workbook = load_workbook('source_excel.xlsx')
sheet = workbook.get_sheet_by_name("Sheet1")


# 指定表格数据读取范围
start_loc_range = sheet['A2':'A201']
end_loc_range = sheet['B2':'B201']
# 新建列表，用于存放读取的数据
start_loc_geohash = []
end_loc_geohash = []
# 读取start_loc列
for row_of_cell in start_loc_range:
    for cell in row_of_cell:
        start_loc_geohash.append(cell.value)
# 读取end_loc列
for row_of_cell in end_loc_range:
    for cell in row_of_cell:
        end_loc_geohash.append(cell.value)


# step2: 转换为坐标
start_loc_coord = []
end_loc_coord = []
for i in range(len(start_loc_geohash)):
    decode = pgh.decode(start_loc_geohash[i])
    start_loc_coord.append(decode)
for i in range(len(end_loc_geohash)):
    decode = pgh.decode(end_loc_geohash[i])
    end_loc_coord.append(decode)


# step3: 生成散点图
# 设置图表大小、标题和标签：
plt.figure(figsize=(10, 6))
plt.title("Scatter Graph of Coordinates", fontsize=24)
plt.xlabel("Longitude", fontsize=14)
plt.ylabel("Latitude", fontsize=14)
# 设置刻度标记属性
plt.tick_params(axis='both', which='major', labelsize=14)
# 画点，其中参数s设置了点的大小
for i in range(len(start_loc_coord)):
    plt.scatter(start_loc_coord[i][0], start_loc_coord[i][1], color='blue', s=50)
    plt.scatter(end_loc_coord[i][0], end_loc_coord[i][1], color='red', s=50)
plt.show()
