import pandas as pd
from cvx.simulator.trading_costs import LinearCostModel


def test_linear_model():
    trades = pd.Series(index=["A", "B"], data=[20.0, -10.0])
    prices = pd.Series(index=["A", "B"], data=[100.0, 300.0])

    model = LinearCostModel(name="Linear Cost Model", factor=0.0010, bias=0.5)
    x = model.eval(prices=prices, trades=trades).sum()
    assert x == 5.0 + 15.0
