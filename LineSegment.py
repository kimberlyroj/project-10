# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 3/9/2022
# Description: A class named Point that has two data members, x_coord and y_coord, representing the two coordinates of the point.
import math
class Point:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def get_x_coord(self):
        return self.x_coord

    def get_y_coord(self):
        return self.y_coord

    def distanceTo(self, point_2):
        return math.sqrt(abs((point_2.x_coord - self.x_coord) ** 2 + (point_2.y_coord - self.y_coord) ** 2))


class LineSegment:
    def __init__(self, point_1, point_2):
        self.endpoint_1 = point_1
        self.endpoint_2 = point_2

    def get_endpoint_1(self):
        return self.endpoint_1

    def get_endpoint_2(self):
        return self.endpoint_2

    def length(self):
        return self.endpoint_1.distanceTo(self.endpoint_2)

    def is_parallel_to(self, line_segment):
        if self.slope() == line_segment.slope():
            return True
        else:
            return False

    def slope(self):
        return (self.endpoint_2.get_y_coord() - self.endpoint_1.get_y_coord()) / (
                self.endpoint_2.get_x_coord() - self.endpoint_1.get_x_coord())


if __name__ == '__main__':
    point_1 = Point(7, 4)
    point_2 = Point(-6, 18)

    print(point_1.distanceTo(point_2))

    line_seg_1 = LineSegment(point_1, point_2)
    print(line_seg_1.length())
    print(line_seg_1.slope())

    point_3 = Point(-2, 2)
    point_4 = Point(24, 12)

    line_seg_2 = LineSegment(point_3, point_4)

    print(line_seg_2.length())
    print(line_seg_2.slope())
    print(line_seg_1.is_parallel_to(line_seg_2))