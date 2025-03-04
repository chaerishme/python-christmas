from enum import Enum
from calculate import Calculate


class Badge(Enum):
    """12월 이벤트 배지 정보를 저장하는 클래스"""
    SANTA = ("산타", 20000)
    TREE = ("트리", 10000)
    STAR = ("별", 5000)

    def __init__(self, label, threshold):
        self.label = label
        self.threshold = threshold


class OutputView:
    """출력을 담당하는 클래스"""
    def print_menu(self, orders):
        print()
        print("<주문 메뉴>")
        for menu, count in orders.items():
            print(f"{menu} {count}개")
        print()

    def print_price(self, orders):
        calculator = Calculate()
        prev_price = calculator.calc_prev_price(orders)
        print("<할인 전 총주문 금액>")
        print(f"{prev_price:,}원")
        print()

        return prev_price

    def print_giveaway(self, prev_price):
        calculator = Calculate()
        print("<증정 메뉴>")

        if calculator.give_giveaway(prev_price):
            print("샴페인 1개")
            print()
            return

        print("없음")
        print()

    def print_benefit(self, date, orders, prev_price):
        print("<혜택 내역>")
        date_dc = self.print_date_dc(date)
        day_dc = self.print_day_dc(date, orders)
        special_dc = self.print_special_dc(date)
        giveaway_dc = self.print_giveaway_dc(prev_price)

        if not date_dc and not day_dc and not special_dc and not giveaway_dc:
            print("없음\n")

        total = date_dc + day_dc + special_dc + giveaway_dc
        dc_price = date_dc + day_dc + special_dc
        print("\n<총혜택 금액>")
        print(f"-{total:,}원\n")

        return total, dc_price

    def print_date_dc(self, date):
        calculator = Calculate()
        date_dc = calculator.calc_date_dc(date)

        if date_dc == 0:
            return 0

        print(f"크리스마스 디데이 할인: -{date_dc:,}원")
        return date_dc

    def print_day_dc(self, date, orders):
        calculator = Calculate()
        day = calculator.calc_day(date)
        day_dc = calculator.calc_day_dc(day, orders)

        if day_dc <= 0:
            return 0

        if day and day_dc > 0:
            print(f"주말 할인: -{day_dc:,}원")
            return day_dc

        if not day and day_dc > 0:
            print(f"평일 할인: -{day_dc:,}원")
            return day_dc

    def print_special_dc(self, date):
        if date % 7 == 3 or date == 25:
            print("특별 할인: -1,000원")
            return 1000
        return 0

    def print_giveaway_dc(self, prev_price):
        calculator = Calculate()

        if calculator.give_giveaway(prev_price):
            print("증정 이벤트: -25,000원")
            return 25000

        return 0

    def print_result(self, prev_price, total_dc, dc_price):
        print("<할인 후 예상 결제 금액>")
        result_price = prev_price - dc_price
        print(f"{result_price:,}원")
        print()

        print("<12월 이벤트 배지>")
        for badge in Badge:
            if total_dc >= badge.threshold:
                print(badge.label)
                return
        
        return

    def print_no_dc(self, prev_price):
        print("<증정 메뉴>\n없음\n")
        print("<혜택 내역>\n없음\n")
        print(f"<할인 후 예상 결제 금액>\n{prev_price:,}\n")
        print("<12월 이벤트 배지>\n없음")
