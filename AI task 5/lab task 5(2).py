import math

scores = [3, 5, 2, 9, 3, 5, 2, 9]
tree_depth = int(math.log2(len(scores)))


def minimax(depth, node_index, max_turn, scores, target_depth, counter):
    if depth == target_depth:
        counter[0] += 1
        return scores[node_index]

    if max_turn:
        return max(
            minimax(depth + 1, node_index * 2, False,
                    scores, target_depth, counter),
            minimax(depth + 1, node_index * 2 + 1, False,
                    scores, target_depth, counter)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True,
                    scores, target_depth, counter),
            minimax(depth + 1, node_index * 2 + 1, True,
                    scores, target_depth, counter)
        )


def alphabeta(depth, index, max_turn, scores, target_depth,
              alpha, beta, counter):

    if depth == target_depth:
        counter[0] += 1
        return scores[index]

    if max_turn:
        value = float('-inf')

        for i in range(2):
            value = max(value, alphabeta(
                depth + 1, index * 2 + i, False, scores,
                target_depth, alpha, beta, counter
            ))

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value
    else:
        value = float('inf')

        for i in range(2):
            value = min(value, alphabeta(
                depth + 1, index * 2 + i, True, scores,
                target_depth, alpha, beta, counter
            ))

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value
minimax_counter = [0]
minimax_value = minimax(
    0, 0, True, scores, tree_depth, minimax_counter
)
alphabeta_counter = [0]
alphabeta_value = alphabeta(
    0, 0, True, scores, tree_depth,
    float('-inf'), float('inf'), alphabeta_counter
)
print("Minimax optimal value:", minimax_value)
print("Minimax evaluated leaves:", minimax_counter[0])

print("Alpha-Beta optimal value:", alphabeta_value)
print("Alpha-Beta evaluated leaves:", alphabeta_counter[0])