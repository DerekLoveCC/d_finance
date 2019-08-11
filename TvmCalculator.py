import matplotlib.pyplot as plt


class TvmCalculator:
    """ the calculator of time value of money"""

    @staticmethod
    def npv(rate, cash_flow):
        total = 0.0
        for index, value in enumerate(cash_flow):
            total += value / (1 + rate) ** index
        return total

    @staticmethod
    def pv_f(fv, rate, n):
        return fv / (1 + rate) ** n

    @staticmethod
    def fv_f(pv, rate, n):
        return pv * (1 + rate) ** n

    @staticmethod
    def pv_perpetuity(pmt, rate):
        return pmt / rate

    @staticmethod
    def pv_perpetuity_due(pmt, rate):
        return (pmt / rate) * (1 + rate)

    @staticmethod
    def pv_annuity(pmt, rate, n):
        return (pmt / rate) * (1 - 1 / (1 + rate) ** n)

    @staticmethod
    def pv_annuity_due(pmt, rate, n):
        return TvmCalculator.pv_annuity(pmt, rate, n) * (1 + rate)

    @staticmethod
    def pv_growing_annuity(pmt, rate, growth, n):
        return pmt / (rate - growth) * (1 - (1 + growth) ** n / (1 + rate) ** n)

    @staticmethod
    def fv_annuity(pmt, rate, n):
        # (pmt/r)*(1-/(1+r)**n)*(1+r)**n=(pmt/r) * ((1+r)**n - 1)
        return TvmCalculator.pv_annuity(pmt, rate, n) * (1 + rate) ** n

    @staticmethod
    def fv_annuity_due(pmt, rate, n):
        """pv_annuity_due(pmt,r,n)*(1+r)**n=(pmt/r)*(1-(1+r)**n)*(1+r)*(1+r)**n=(pmt/r)*((1+r)**n - 1)*(1+r)"""
        return (pmt / rate) * ((1 + rate) ** n - 1) * (1 + rate)

    @staticmethod
    def fv_growing_annuity(pmt, rate, growth, n):
        return (pmt / (rate - growth))((1 + rate) ** n - (1 + growth) ** n)

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
