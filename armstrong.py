def is_armstrong(n: int) -> bool:
    if n < 0:
        return False
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n
def armstrong_in_range(start: int, end:int):
    if end < start:
        start, end = end, start
        for num in range(max(0, start), end + 1):
            if is_armstrong(num):
                yield num
                if __name__ == "__main__":
                    n = int(input("Enter a non-negative integer to check: ").strip())
                    if is_armstrong(n):
                        print(f"{n} is an Armstong number.")
                    else:
                            print(f"{n} is an NOT Armstong number.")
                print("\nArmstrong number from 0 to 10000:")
                print(list(armstrong_in_range(0,10000)))
