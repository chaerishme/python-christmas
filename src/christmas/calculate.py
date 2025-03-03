class Calculate:
    def __init__(self, input_view):
        self.total_menu = input_view.total_menu
        self.main = input_view.main
        self.dessert = input_view.dessert


    def calc_prev_price(self, orders):
        prev_price = sum(self.total_menu[menu] * count for menu, count in orders.items())
        return prev_price
    

    def give_giveaway(self, prev_price):
        if prev_price >= 120000:
            return True
        
        return False


    def calc_date_dc(self, date):
        if date > 25:
            return 0
        return (date - 1) * 100


    def calc_day(self, date):
        if date % 7 == 1 or date % 7 == 2:
            return True # 주말
        return False # 평일


    def calc_day_dc(self, day, order):
        if day:
            main_count = sum(count for menu, count in order.items() if menu in self.main)
            return main_count * 2023
        
        dessert_count = sum(count for menu, count in order.items() if menu in self.dessert)
        return dessert_count * 2023


    def calc_star_dc(self, date):
        if date % 7 == 3 or date == 25:
            return 1000
        return 0