import xlrd     # 导入读取Excel模块


class ExcelData:
    """
    用来封装读取Excel数据的公用方法
    """

    def __init__(self, sheet_Name):
        self.data = xlrd.open_workbook("../WebElements.xlsx")  # 通过Excel存放路径打开Excel：xlrd.open_workbook("excel_path")
        self.table = self.data.sheet_by_name(sheet_Name)  # 通过sheet_Name的方式打开Excel
        self.number_rows = self.table.nrows  # 获取总行数
        self.number_cols = self.table.ncols  # 获取总列数
        self.keys = self.table.col_values(1)  # 获取第二列作为key值

    def dict_data(self):
        r = []
        s = {}
        values = self.table.col_values(2)  # 获取第三列作为values值
        for x in list(range(1, self.number_rows)):  # 遍历所有的行，并把每行的数据放入list中
            s[self.keys[x]] = values[x]  # 把每行对应列的数据拿出来放入s字典中
        r.append(s)  # 每次取到的数据放入列表
        return r

    def list_to_dict(self):
        return self.dict_data()[0]  # 取出列表中的字典

    def get_data(self, value):
        return self.list_to_dict()[value]  # 取字典中对应的value值


if __name__ == "__main__":
    sheetName = "登录"
    a = ExcelData(sheetName)
    print("读取到excel中第二列和第三列对应的数据为：", a.dict_data())
    print("把列中的字典取出来为：", a.list_to_dict())
