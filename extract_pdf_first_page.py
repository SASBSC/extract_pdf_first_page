# 转自https://cloud.tencent.com/developer/article/1584421
# coding:utf-8
import os
import fitz
# import pdb

# 解析
def analysis(file_path, save_path, num):
    # 资源列表
    file_array = []
    if os.path.isdir(file_path):
        # 目录循环压入
        file_count = get_path_file(file_path)
        for v in file_count:
            file_array.append(v)
    else:
        # 单文件，单次调用
        file_array.append(file_path)

    # 判断为空情况
    if not file_array:
        print("此目录下无文件")
    # 执行解析
    file_count_num = len(file_array)
    print("程序运行中，共计%s个文件" % file_count_num)
    for v in file_array:
        # print("文件路径：%s" % v)
        # 获取文件名称及类型
        file_name = os.path.basename(v)
        # print("文件信息：%s" % file_name)
        if '.pdf' not in file_name:
            print("此文件非PDF文件")
        #  打开PDF文件，生成一个对象
        doc = fitz.open(v)
        # 总页数
        count_page = doc.pageCount
        # print("文件共计：%s页" % count_page)
        if count_page > 1:
            page = doc[num]
            rotate = int(0)
            # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
            pm = page.getPixmap(matrix=trans, alpha=False)
            # 保存路径
            # p_1 = v.replace(file_path, save_path)
            p_1 = save_path
            # pdb.set_trace()  #运行至此暂停
            p_2 = p_1.replace(file_name, '')
            # pdb.set_trace()  #运行至此暂停
            if not os.path.exists(p_2):
                os.makedirs(p_2)
            new_file_name = file_name.replace(".pdf", "")
            pm.writePNG(p_2 + '%s.png' % new_file_name)
            print("运行完成")
        else:
            print("此文档无内容，跳出")
            continue


# 返回目录下所有文件
def get_path_file(files_path):
    data = []
    for root, dirs, files in os.walk(files_path, topdown=False):
        for name in files:
            f_p = os.path.join(root, name).replace("\\", "/")
            data.append(f_p)
    return data


if __name__ == '__main__':
    print("|---------------------------------|")
    print("|                                 |")
    print("|         PDF 批量生成封面        |")
    print("|                                 |")
    print("|---------------------------------|")

    # 当前目录下的文件
    now_path = os.getcwd()
    print("当前位置：%s" % now_path)
    # 保存路径
    print("请输入参数，以 / 结尾，处理完成后会自动退出")
    save_path = input("图片保存地址:")
    # exit()
    # 判断目录
    save_path_status = os.path.exists(save_path)
    if not save_path_status:
        os.mkdir(save_path)
    # 截取页数
    num = 0
    # 路径或文件名
    file_path = input("PDF文件地址:")
    # 调用方法
    analysis(file_path, save_path, num)
