# main.py

def calculate_sum():
    # 在此编写代码
     sum=0
     for i in range(51):
          sum=i+sum
     return sum
     pass

if __name__ == "__main__":
    result = calculate_sum()
    print(f"1+2+...+50的和是：{result}")
