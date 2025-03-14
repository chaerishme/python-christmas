"""
입력을 관리하고 예외처리를 하는 모듈
"""

from menu import TOTAL_MENU


class InputView:
    """
    손님의 입력을 처리하는 클래스.
    방문 날짜와 주문 내역을 입력받고 검증
    """

    def __init__(self):
        """InputView 인스턴스 초기화"""
        self.total_menu = TOTAL_MENU
        self.beverage = {"제로콜라", "레드와인", "샴페인"}

    def read_date(self):
        """손님으로부터 방문 날짜를 입력받고 예외처리"""
        while True:
            print("12월 중 식당 예상 방문 날짜는 언제인가요? (숫자만 입력해 주세요!)")
            date = input()

            if not date.isdigit() or int(date) > 31 or int(date) < 1:
                print("[ERROR] 유효하지 않은 날짜입니다. 다시 입력해 주세요.")
                continue

            return int(date)

    def read_order(self):
        """사용자로부터 주문 내역을 입력받고 예외 처리"""
        while True:
            print("주문하실 메뉴를 메뉴와 개수를 알려 주세요. (e.g. 해산물파스타-2,레드와인-1,초코케이크-1)")
            order = input().strip().split(",")

            try:
                orders = self._parse_order(order)
                if self._order_beverage_only(orders):
                    print("[ERROR] 음료만 주문할 수 없습니다. 다시 입력해 주세요.")
                    continue

                return orders

            except ValueError:
                print("[ERROR] 유효하지 않은 주문입니다. 다시 입력해 주세요.")

    def _parse_order(self, order):
        """주문 문자열 파싱하여 딕셔너리 형태로 변환"""
        order_list = {}
        for item in order:
            menu = item.split("-")
            if len(menu) != 2:
                raise ValueError
            menu_name, count = menu[0], menu[1]
            if (
                menu_name not in self.total_menu
                or not count.isdigit()
                or int(count) < 1
                or menu_name in order_list
            ):
                raise ValueError
            order_list[menu_name] = int(count)
        self._validate_order(order_list)
        return order_list

    def _validate_order(self, order_list):
        """주문 개수가 20개 초과하는지 확인"""
        if sum(order_list.values()) > 20:
            raise ValueError

    def _order_beverage_only(self, orders):
        """음료만 주문했는지 확인"""
        return all(menu in self.beverage for menu in orders)
