def calculate_polynomial(n: int, x: int, xi_list: list) -> int:
    result=1
    for xi in xi_list:
        result*=(x-xi）
                 
    return result

if __name__ == "__main__":
    n = int(input())
    x = int(input())
    xi_list = list(map(int, input().split()))
    print(calculate_polynomial(n, x, xi_list))
