import numpy as np

def topsis(matrix, weights, impacts, labels=None):
    matrix = np.array(matrix, dtype=float)
    weights = np.array(weights, dtype=float)

    n_rows, n_cols = matrix.shape

    if len(weights) != n_cols:
        raise ValueError("Number of weights must match number of criteria")

    if len(impacts) != n_cols:
        raise ValueError("Number of impacts must match number of criteria")

    # Step 1: Normalize the decision matrix
    norm_matrix = matrix / np.sqrt((matrix ** 2).sum(axis=0))

    # Step 2: Apply weights
    weighted_matrix = norm_matrix * weights

    # Step 3: Determine ideal best and worst
    ideal_best = np.zeros(n_cols)
    ideal_worst = np.zeros(n_cols)

    for j in range(n_cols):
        if impacts[j] == "+":
            ideal_best[j] = weighted_matrix[:, j].max()
            ideal_worst[j] = weighted_matrix[:, j].min()
        else:
            ideal_best[j] = weighted_matrix[:, j].min()
            ideal_worst[j] = weighted_matrix[:, j].max()

    # Step 4: Calculate distances
    dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Calculate TOPSIS score
    scores = dist_worst / (dist_best + dist_worst)

    # Step 6: Ranking
    ranking_indices = scores.argsort()[::-1]

    if labels is None:
        labels = [f"A{i+1}" for i in range(n_rows)]

    result_scores = {labels[i]: round(float(scores[i]), 4) for i in range(n_rows)}
    ranking = [labels[i] for i in ranking_indices]

    return result_scores, ranking
