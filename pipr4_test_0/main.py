from pipr4_test_0.party import Party
from pipr4_test_0.voting import Voting



tickets = 301
threshold = 0.05  # 5% threshold

parties =  {"Flowers":1256, "Cars":4325, "Knights":446, "Queens":100,"Eagles":9880}
v = Voting(tickets, parties, threshold)

v.print_results()