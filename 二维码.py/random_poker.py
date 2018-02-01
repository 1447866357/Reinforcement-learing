#案例：随机数  彩票号
#35选5,12选2  7

import random
#a=random.randint(1,10)
#daletou_qian=[i for i in range(1,36)]
#daletou_hou=[i for i in range(1,13)]
#daletou_hou_random=random.sample(daletou_hou,k=2)
#daletou_qian_random=random.sample(daletou_qian,k=10)
#print(daletou_qian_random,daletou_hou_random)

#扑克牌洗牌
poker_num=[str(i) for i in range(2,11)]
poker_str=["A","J","Q","K"]
poker_king=["大王","小王"]
print(poker_num)
poker_color=["红","黑","方","花"]
pokers=["%s%s"%(i,j)for i in poker_color
       for j in poker_num+poker_str]+poker_king
print(pokers)
print(len(pokers))

#随机洗牌
random.shuffle(pokers)
print(pokers)

#斗地主  发牌  17张牌   20张牌
person_a=pokers[0:51:3]
person_b=pokers[1:51:3]
person_c=pokers[2:51:3]
last_3=pokers[-3:]
print("person_a:",person_a)
print("person_b:",person_b)
print("person_c:",person_c)

