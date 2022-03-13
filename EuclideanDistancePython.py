import numpy as np
class Euclidean_distance:
    
    distance_list = []

    def __init__(self,point_a_x,point_a_y,point_b_x,point_b_y):
        self.point_a_x = point_a_x
        self.point_a_y = point_a_y
        self.point_b_x = point_b_x
        self.point_b_y = point_b_y

    def calc_distance(self):
        dist = np.sqrt((abs(self.point_b_x - self.point_a_x))**2 + (abs(self.point_b_y - self.point_a_y))**2)
        self.distance_list.append(dist)
        return self.distance_list        

class Merged_List_distance_calc:
    def __init__(self, merged_lst):
        self.merged_lst = merged_lst

    def distance(self):
        for i in self.merged_lst:
            for j in self.merged_lst[0:]:
                Euclidean_distance_obj = Euclidean_distance(self.merged_lst[self.merged_lst.index(i)][0],self.merged_lst[self.merged_lst.index(i)][1],self.merged_lst[self.merged_lst.index(j)][0],self.merged_lst[self.merged_lst.index(j)][1])
                Distance = Euclidean_distance_obj.calc_distance()
        return Distance 
 
merged_list = [[1, 6], [2, 8], [5, 7], [4, 5], [7, 9], [8, 6], [6, 7]]
distance_obje = Merged_List_distance_calc(merged_list)
print(distance_obje.distance())
