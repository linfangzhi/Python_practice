class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "%s 占地 %.2f"%(self.name,self.area)


class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return '%s %s' % (self.free_area, self.item_list)

    def add(self,item):
        print('%s'% item)
        if item.area>self.free_area:
            print('太大了')
            return
        self.item_list.append(item.name)
        self.free_area -= item.area






bed = HouseItem('席梦思',4)
chest = HouseItem('衣柜',2)
table = HouseItem('餐桌',1.5)

my_house = House('fa',60)

my_house.add(bed)
my_house.add(chest)
my_house.add(table)


print(my_house)