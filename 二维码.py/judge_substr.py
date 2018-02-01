#案例名：判断是否为子串
str_a= "欢迎"
str_b= "欢迎大家来到吉林大学"

if str_a in str_b:
    print("是子串")
else:
    print("不是子串")

#定义函数判断
def is_sub_str(sub_strs,strs):
    """判断sub_strs是否为strs的子串
    ：param  sub_strs:待判断子串
    :param   strs:父串
    :return: False|True
    """
    if sub_strs in strs:
        return True
    else:
        return False
a=is_sub_str(str_a,str_b)
print(a)


# 判断一个子串是否为另一个串通过循环位移产生的串的子串
#  str_b= "欢迎大家来到吉林大学"  -->>右移一位"院欢迎大家来到吉林大学"

#判断str_a是否为str_b通过循环右移N位产生的串的子串
def right_move(strs,n_steps):
    """对strs进行循环右移操作，移动n_step步

    :param strs:待移动的串
    :param n_steps:移动步数
    :return:移动后的串 strs
    """
    length=len(strs)
    if length==0:
        return strs
    steps=n_steps%length
    ret_strs=strs[-n_steps:]+strs[:-n_steps]
    return ret_strs
r_str_b = right_move(str_b,2)
print(r_str_b)

def can_rotae_get_substrs(strs,sub_str):
    """判断sub_str是否为strs循环右移后的字符串
    :param strs:
    :param sub_str:
    :return:
    """
    length=len(strs)
    for i in range(length):
        if is_sub_str(sub_str,right_move(strs,i)):
            return True
        return False
str_a="欢迎"
str_b="欢迎大家来到吉林大学"
flag=can_rotae_get_substrs(str_b,str_a)
print(flag)

print(is_sub_str(str_a,str_b*2))
