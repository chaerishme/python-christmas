class OutputView:
    def print_menu(self, orders):
        print()
        print("<주문 메뉴>")
        for menu, count in orders.items():
            print(f"{menu} {count}개")
        print()

