"""
혜택 계산을 담당하는 모듈
"""
from menu import TOTAL_MENU


class Calculate:
    """
    손님이 받을 혜택을 계산하는 클래스.
    조건에 맞춰 혜택을 계산
    """
    def __init__(self):
        """calculate 인스턴스 초기화"""
        self.total_menu = TOTAL_MENU
        self.main = {"티본스테이크", "바비큐립", "해산물파스타", "크리스마스파스타"}
        self.dessert = {"초코케이크", "아이스크림"}

    def calc_prev_price(self, orders):
        prev_price = sum(
            self.total_menu[menu] * count for menu, count in orders.items()
        )
        return prev_price

    def give_giveaway(self, prev_price):
        if prev_price >= 120000:
            return True

        return False

    def calc_date_dc(self, date):
        if date > 25:
            return 0
        return (date - 1) * 100 + 1000

    def calc_day(self, date):
        if date % 7 == 1 or date % 7 == 2:
            return True  # 주말
        return False  # 평일

    def calc_day_dc(self, day, orders):
        if day:
            main_count = sum(
                count for menu, count in orders.items() if menu in self.main
            )
            return main_count * 2023

        dessert_count = sum(
            count for menu, count in orders.items() if menu in self.dessert
        )
        return dessert_count * 2023

    def calc_star_dc(self, date):
        if date % 7 == 3 or date == 25:
            return 1000
        return 0
