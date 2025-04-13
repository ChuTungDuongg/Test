def backtracking(a, M):
    n = len(a)
    
    def backtrack(index, current_sum):
        print(f"Index: {index}, Current Sum: {current_sum}")  # In ra giá trị hiện tại của index và current_sum
        
        # Điều kiện dừng: Nếu đã xét hết các phần tử
        if index == n:
            if current_sum == M:
                print(f"Found a valid combination with sum {current_sum} at index {index}")
                return 1
            return 0
        
        # Bao gồm phần tử hiện tại (chọn phần tử a[index])
        print(f"Including element a[{index}] = {a[index]}")  # Thông báo chọn phần tử
        include = backtrack(index + 1, current_sum + a[index])
        
        # Loại bỏ phần tử hiện tại (không chọn phần tử a[index])
        print(f"Excluding element a[{index}] = {a[index]}")  # Thông báo không chọn phần tử
        exclude = backtrack(index + 1, current_sum)
        
        # Trả về tổng số cách tìm được tổng M
        return include + exclude

    return backtrack(0, 0)

# Ví dụ sử dụng
a = [3, 5, 2]
M = 5
print("Total number of ways to reach the sum:", backtracking(a, M))
