scores = [3, 5, 2, 9, 3, 5, 2, 9]
count = 0

def alphabeta(depth, index, max_turn, alpha, beta):
    global count

    if depth == 3:
        count += 1
        return scores[index]

    if max_turn:
        best = -999

        for i in range(2):
            value = alphabeta(depth + 1, index * 2 + i,
                              False, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best
    else:
        best = 999

        for i in range(2):
            value = alphabeta(depth + 1, index * 2 + i,
                              True, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best
result = alphabeta(0, 0, True, -999, 999)

print("Optimal value:", result)
print("Evaluated leaves:", count)