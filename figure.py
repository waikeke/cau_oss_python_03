"""
이 figure 모듈은 line class를 이용하여 선의 길이를 설정 및 참조를 수행하며
area_square, area_circle, area_regular_triangle 함수로 
각각 정사각형, 원, 정삼각형의 넓이를 반환입니다.
"""
import math


class line:
    """
    line class는 선에 길이에 대해 저장하고 있는 클래스입니다.
    변수로는 외부에서 접근 불가한 __length가 있으며, 
    해당 변수를 수정,접근하기 위해 set_length, get_length 메소드를 제공합니다.
    """
    __length = 0

    def __init__(self, length):
        """
        생성자 초기 length값을 받습니다.
        Args:
            length (int or float): 초기 선의 길이 값입니다.
        """
        self.__length = length

    def set_length(self, length):
        """ 선의 길이를 수정합니다.
        Args:
            length (int or float): 수정하고자 하는 선의 길이입니다.
        """
        self.__length = length
    
    def get_length(self):
        """객체가 저장하고 있는 선의 길이를 반환합니다.
        Returns:
            int or float: 저장하고 있는 선의 길이 입니다.
        """
        return self.__length

    def area_square(length):
        """길이를 입력 받아 정사각형의 넓이를 구하는 함수입니다.
        Args:
            length (int or float): 한 변의 길이입니다.
        Returns:
            int or float: 정사각형의 넓이를 반환합니다.
        """
        return length*length

    def area_circle(length):
        """길이를 입력 받아 원의 넓이를 구하는 함수입니다.
        Args:
            length (int or float): 반지름의 길이입니다.
        Returns:
            int or float: 원의 넓이를 반환합니다.
        """
        return length*length*math.pi

    def area_regular_triangle(length):
        """길이를 입력 받아 정삼각형의 넓이를 구하는 함수입니다.
        Args:
            length (int or float): 한 변의 길이입니다.
        Returns:
            int or float: 정삼각형의 넓이를 반환합니다.
        """
        return length*length*math.sqrt(3)/4

