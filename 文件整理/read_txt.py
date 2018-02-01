def get_data_from_txt(file):
    with open(file,'rb')as f:
        data = f.read()
        return data.decode('gbk')

if __name__ == "__main__":
    ret = get_data_from_txt("知识点.txt")
    print(ret)