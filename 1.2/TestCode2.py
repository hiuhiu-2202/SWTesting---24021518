from Code2 import check_ticket


def main():
    tests = 0

    with open("1.2/test2.txt", "r", encoding="utf-8") as file:

        for line in file:

            # Đọc age, slot và Expected Output
            parts = line.strip().split(maxsplit=2)

            age = int(parts[0])
            slot = int(parts[1])
            expectOut = parts[2]

            tests += 1

            # Gọi hàm kiểm thử
            output = check_ticket(age, slot)

            # In kết quả
            print(
                f"Test #{tests}: "
                f"Input: age = {age}, "
                f"slot = {slot}, "
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