import matplotlib.pyplot as plt


class TimeValueOfMoney:
    @staticmethod
    def npv(rate, cash_flow):
        total = 0.0
        for index, value in enumerate(cash_flow):
            total += value / (1 + rate) ** index
        return total

    def draw_npv(self, rate_range, cash_flow, step=0.0001):
        npv_list = []
        rate_list = []

        current_rate = rate_range[0]
        high_rate = rate_range[1]
        while current_rate < high_rate:
            rate_list.append(current_rate)
            npv_list.append(self.npv(current_rate, cash_flow))
            current_rate += step

        plt.plot(rate_list, npv_list)
        plt.plot([0, rate_list[len(rate_list) - 1]], [0, 0])
        plt.show()
