class InputView:
    def __init__(self):
        self.total_menu = {"양송이수프": 6000, "타파스": 5500, "시저샐러드": 8000, "티본스테이크": 55000, "바비큐립": 54000, "해산물파스타": 35000, "크리스마스파스타": 25000, "초코케이크": 15000, "아이스크림": 5000, "제로콜라": 3000, "레드와인": 60000, "샴페인": 25000}
        self.beverage = {"제로콜라", "레드와인", "샴페인"}


    def read_date(self):
        while True:
            print("12월 중 식당 예상 방문 날짜는 언제인가요? (숫자만 입력해 주세요!)")
            date = input()

            if not date.isdigit() or int(date) > 31 or int(date) < 1:
                print("[ERROR] 유효하지 않은 날짜입니다. 다시 입력해 주세요.")
                continue

            return int(date)


    def read_order(self):
        while True:
            print("주문하실 메뉴를 메뉴와 개수를 알려 주세요. (e.g. 해산물파스타-2,레드와인-1,초코케이크-1)")
            order = input().strip()

            try:
                orders = self._parse_order(order)
                if self._order_beverage_only(orders):
                    print("[ERROR] 음료만 주문할 수 없습니다. 다시 입력해 주세요.")
                    continue

                return orders

            except ValueError:
                print("[ERROR] 유효하지 않은 주문입니다. 다시 입력해 주세요.")


    def _parse_order(self, order):
        orders = order.split(",")
        order_list = {}
        total_count = 0

        for order in orders:
            menu = order.split("-")

            if len(menu) != 2:
                raise ValueError

            menu_name, count = menu[0], menu[1]

            if menu_name not in self.total_menu:
                raise ValueError

            if not count.isdigit() or int(count) < 1:
                raise ValueError

            if menu_name in order_list:
                raise ValueError

            order_list[menu_name] = int(count)
            total_count = total_count + int(count)

        if total_count > 20:
            raise ValueError

        return order_list


    def _order_beverage_only(self, orders):
        return all(menu in self.beverage for menu in orders)

