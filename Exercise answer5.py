dice_odds = {}
for i in range(1, 7):
    for j in range(1, 7):
        dice_sum = i + j
        if dice_sum not in dice_odds:
            dice_odds[dice_sum] = 1
        else:
            dice_odds[dice_sum]+=1

print(dice_odds)
