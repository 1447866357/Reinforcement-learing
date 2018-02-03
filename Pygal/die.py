from random import randint
import pygal
class Die():
    """表示骰子的类"""
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值"""
        return randint(1,self.num_sides)


die_1 = Die()
die_2 = Die(10)
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()

    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.y_title = "Frequency of Result"
hist.x_title = "Result"
hist.add('D6+D10',frequencies)
hist.render_to_file('die_visual_2.svg')
print(frequencies)
