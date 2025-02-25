# main.py

def left_side(x, num_terms):
  """
    计算方程右侧的固定值。
    """
    return (1 + 2 * x) / (1 + x + x**2)

def find_num_terms(x, tolerance=1e-6):
    """
    寻找满足左侧与右侧差异小于容差的最小项数。
    """
    num_terms = 1

    right_value = right_side(x)

    while True:
        left_value = left_side(x, num_terms)
        if abs(left_value - right_value) < tolerance:
            break

        num_terms += 1

    return num_terms


if __name__ == "__main__":
    x = 0.25  # 题目给定的 x 值
    num_terms = find_num_terms(x)
    print(f"所需最小项数: {num_terms}")
