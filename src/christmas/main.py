from input_view import InputView
from output_view import OutputView


def main():
    input_view = InputView()
    output_view = OutputView()

    print("안녕하세요! 우테코 식당 12월 이벤트 플래너입니다.")
    date = input_view.read_date()
    orders = input_view.read_order()
    print(f"12월 {date}일에 우테코 식당에서 받을 이벤트 혜택 미리 보기!")

    output_view.print_menu(orders)
    prev_price = output_view.print_price(orders)

    if prev_price < 10000:
        output_view.print_no_dc(prev_price)
        return

    output_view.print_giveaway(prev_price)
    total_dc, dc_price = output_view.print_benefit(date, orders, prev_price)
    output_view.print_result(prev_price, total_dc, dc_price)


if __name__ == "__main__":
    main()
