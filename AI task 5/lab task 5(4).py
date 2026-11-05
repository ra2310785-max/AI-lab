scores = [3, 5, 2, 9, 3, 5, 2, 9]

def alphabeta(depth, index, max_turn, alpha, beta, order, count):

    if depth == 3:
        count[0] += 1
        return scores[index]

    if max_turn:
        best = -999

        for i in order:
            value = alphabeta(depth+1, index*2+i,
                              False, alpha, beta, order, count)

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 999

        for i in order:
            value = alphabeta(depth+1, index*2+i,
                              True, alpha, beta, order, count)

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


count1 = [0]
result1 = alphabeta(0, 0, True, -999, 999,
                    [0, 1], count1)

count2 = [0]
result2 = alphabeta(0, 0, True, -999, 999,
                    [1, 0], count2)

print("First Order Value:", result1)
print("First Order Leaves:", count1[0])

print("Second Order Value:", result2)
print("Second Order Leaves:", count2[0])