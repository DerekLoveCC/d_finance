import scipy as sp
import TvmCalculator

if __name__ == '__main__':
    print(sp.rate(9, 0, 2, 4))
    # print(sp.fv(0.1, 2, 0, 100))

    # rate = 0.05
    # cash_flow = [504, -432, -432, -432, 843]
    # npv = TvmCalculator.TvmCalculator.npv(rate, cash_flow)
    # print(npv)
    #
    # npv1 = sp.npv(rate, cash_flow)
    # print(npv1)
    #
    # pp = TvmCalculator.TvmCalculator()
    # pp.draw_npv([0.000001, 1], cash_flow)
