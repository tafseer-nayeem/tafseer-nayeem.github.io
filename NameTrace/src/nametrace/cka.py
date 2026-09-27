from __future__ import annotations

import numpy as np


def center_rows(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    return x - x.mean(axis=0, keepdims=True)


def linear_cka(x: np.ndarray, y: np.ndarray) -> float:
    x = center_rows(x)
    y = center_rows(y)
    xty = x.T @ y
    numerator = np.linalg.norm(xty, ord="fro") ** 2
    denom = np.linalg.norm(x.T @ x, ord="fro") * np.linalg.norm(y.T @ y, ord="fro")
    return float(numerator / denom) if denom > 0 else float("nan")


def cka_matrix(representations: dict[str, np.ndarray]) -> tuple[list[str], np.ndarray]:
    labels = list(representations)
    mat = np.eye(len(labels), dtype=float)
    for i, a in enumerate(labels):
        for j, b in enumerate(labels[i + 1 :], start=i + 1):
            value = linear_cka(representations[a], representations[b])
            mat[i, j] = mat[j, i] = value
    return labels, mat
