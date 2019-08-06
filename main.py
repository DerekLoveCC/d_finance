import scipy as sp
import tvm

if __name__ == '__main__':
    rate = 0.05
    cash_flow = [504, -432, -432, -432, 843]
    npv = tvm.TimeValueOfMoney.npv(rate, cash_flow)
    print(npv)

    npv1 = sp.npv(rate, cash_flow)
    print(npv1)

    pp = tvm.TimeValueOfMoney()
    pp.draw_npv([0.000001, 1], cash_flow)
