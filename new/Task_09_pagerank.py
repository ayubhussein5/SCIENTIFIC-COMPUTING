import numpy as np

# New case: rank 5 web pages of a college website (Google PageRank idea).
pages = ["Home", "Courses", "Admissions", "Fees", "Contact"]
# links[i][j] = 1 if page j links to page i
links = np.array([
    [0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0]
], dtype=float)

M = links / links.sum(axis=0)          # column-stochastic link matrix
d = 0.85                               # damping factor used by Google
n = len(pages)
G = d * M + (1 - d) / n * np.ones((n, n))

vals, vecs = np.linalg.eig(G)
k = np.argmax(np.real(vals))
rank = np.abs(np.real(vecs[:, k])); rank /= rank.sum()

print(f"Dominant eigenvalue: {np.real(vals[k]):.6f}")
for p, r in sorted(zip(pages, rank), key=lambda t: -t[1]):
    print(f"{p:<11} {r:.4f}")
