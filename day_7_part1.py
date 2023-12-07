
with open("input_7day.txt", "r") as file:
    data = file.readlines()
    hands_bids = dict([x.split() for x in data])
    hands_ranks = hands_bids.copy()

card_symbols = '23456789TJQKA'

for hand in hands_bids.keys():
    value = 0
    second_order_value=''
    for card in hand:
        second_order_value = second_order_value + str(card_symbols.find(card)+10)
        value += hand.count(card) ** 2

    hands_ranks[hand]=int(str(value*100000) + second_order_value)

sorted_hands_ranks = {k: v for k, v in sorted(hands_ranks.items(), key=lambda item: item[1])}

x = 1
result = {}
for k, v in sorted_hands_ranks.items():
    result[k] = x * int(hands_bids[k])
    x += 1

print(sum(result.values()))
