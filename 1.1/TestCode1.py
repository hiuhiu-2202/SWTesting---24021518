from Code1 import check_salary


def main():
    tests = 0

    with open("test1.txt", "r", encoding="utf-8") as file:

        for line in file:

            # Đọc hour và salary
            parts = line.strip().split(maxsplit=2)

            hour = float(parts[0])
            salary = float(parts[1])
            expectOut = parts[2]

            tests += 1

            # Gọi hàm kiểm thử
            output = check_salary(hour, salary)

            # In kết quả
            print(
                f"Test #{tests}: "
                f"Input: hour = {hour:.2f}, "
                f"salary = {salary:.2f}, "
                f"Expected Output: {expectOut}, "
                f"Output: {output}",
                end=""
            )

            # So sánh kết quả
            if output == expectOut:
                print(", Result: pass")
            else:
                print(", Result: fail")


if __name__ == "__main__":
    main()