"""
criterion
"""

import math

import numpy as np


def get_criterion_function(criterion):
    if criterion == "info_gain":
        return __info_gain
    elif criterion == "info_gain_ratio":
        return __info_gain_ratio
    elif criterion == "gini":
        return __gini_index
    elif criterion == "error_rate":
        return __error_rate


def __label_stat(y, l_y, r_y):
    """Count the number of labels of nodes"""
    left_labels = {}
    right_labels = {}
    all_labels = {}
    for t in y.reshape(-1):
        if t not in all_labels:
            all_labels[t] = 0
        all_labels[t] += 1
    for t in l_y.reshape(-1):
        if t not in left_labels:
            left_labels[t] = 0
        left_labels[t] += 1
    for t in r_y.reshape(-1):
        if t not in right_labels:
            right_labels[t] = 0
        right_labels[t] += 1

    return all_labels, left_labels, right_labels


def __entropy(labels):
    if len(labels) == 0:
        return 0.0

    total = sum(labels.values())
    p = [v / total for v in labels.values()]

    return -np.sum([p_i * np.log2(p_i) for p_i in p])


def __info_gain(y, l_y, r_y):
    """
    Calculate the info gain

    y, l_y, r_y: label array of father node, left child node, right child node
    """
    all_labels, left_labels, right_labels = __label_stat(y, l_y, r_y)
    info_gain = 0.0
    # =============== TODO (students) ===============
    entropy = __entropy(all_labels)
    info_gain = (
        entropy
        - (len(l_y) / len(y)) * __entropy(left_labels)
        - (len(r_y) / len(y)) * __entropy(right_labels)
    )
    # ===============================================
    # raise NotImplementedError("Implement __info_gain")
    return info_gain


def __info_gain_ratio(y, l_y, r_y):
    """
    Calculate the info gain ratio

    y, l_y, r_y: label array of father node, left child node, right child node
    """
    info_gain = __info_gain(y, l_y, r_y)
    # =============== TODO (students) ===============
    p_l = len(l_y) / len(y)
    p_r = len(r_y) / len(y)

    if p_l == 0 or p_r == 0:
        return 0.0

    split_info = -p_l * np.log2(p_l) - p_r * np.log2(p_r)

    info_gain_ratio = info_gain / split_info
    # ===============================================
    # raise NotImplementedError("Implement __info_gain_ratio")
    return info_gain_ratio


def __gini_index(y, l_y, r_y):
    """
    Calculate the gini index

    y, l_y, r_y: label array of father node, left child node, right child node
    """
    all_labels, left_labels, right_labels = __label_stat(y, l_y, r_y)
    before = 0.0
    after = 0.0

    # =============== TODO (students) ===============
    before = 1 - np.sum((np.array(list(all_labels.values())) / len(y)) ** 2)

    left_gini = 1 - np.sum((np.array(list(left_labels.values())) / len(l_y)) ** 2) if len(l_y) > 0 else 0
    right_gini = 1 - np.sum((np.array(list(right_labels.values())) / len(r_y)) ** 2) if len(r_y) > 0 else 0

    after = (len(l_y) / len(y)) * left_gini + (len(r_y) / len(y)) * right_gini
    # ===============================================
    # raise NotImplementedError("Implement __gini_index")
    return before - after


def __error_rate(y, l_y, r_y):
    """Calculate the error rate"""
    all_labels, left_labels, right_labels = __label_stat(y, l_y, r_y)
    before = 0.0
    after = 0.0

    # =============== TODO (students) ===============
    before = 1 - max(all_labels.values()) / len(y)

    left_error = 1 - max(left_labels.values()) / len(l_y) if len(l_y) > 0 else 0
    right_error = 1 - max(right_labels.values()) / len(r_y) if len(r_y) > 0 else 0

    after = (len(l_y) / len(y)) * left_error + (len(r_y) / len(y)) * right_error
    # ===============================================
    # raise NotImplementedError("Implement __error_rate")
    return before - after
