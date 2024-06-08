notes = [10000, 5000, 2000, 1000, 500, 200]
coins = [100, 50, 25, 10, 5, 1]
N = float(input())
cents = int(round(N * 100))
print("NOTAS:")
for note in notes:
    num_notes = cents // note
    cents = cents % note
    print(f"{num_notes} nota(s) de R$ {note / 100:.2f}")
print("MOEDAS:")
for coin in coins:
    num_coins = cents // coin
    cents = cents % coin
    print(f"{num_coins} moeda(s) de R$ {coin / 100:.2f}")
