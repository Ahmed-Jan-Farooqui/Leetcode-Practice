'''
    Rate Limiting API
    
    Given an array requests, where requests[i] represents the request made by some domain at the 
    ith second, and the constraints:
        1. Any domain can make only 2 requests per 5 seconds.
        2. Any domain can make only 5 requests per 30 seconds.
    Return an array of strings with the status code: 200 or 432, where the ith position is the
    response to the request received at the ith second. 
    
    Example:
        Input:
        ["www.abc.com", "www.xyz.com", "www.abc.com", "www.abc.com"]
    
        Output:
        [200, 200, 200, 432]
'''


def rateLimiter(requests: list[str]):
    from collections import defaultdict
    five_window_l = 0
    five_window_r = 5 if len(requests) >= 5 else len(requests)
    thirty_window_l = 0
    thirty_window_r = 30 if len(requests) >= 30 else len(requests)
    thirty_window_dict = defaultdict(int)
    five_window_dict = defaultdict(int)
    final = [0 for idx in range(len(requests))]

    # Init dictionaries
    for idx in range(five_window_r):
        domain = requests[idx]
        five_window_dict[domain] += 1

    for idx in range(thirty_window_r):
        domain = requests[idx]
        thirty_window_dict[domain] += 1

    # Iterate through the windows
    while five_window_r < len(requests):
        print(requests[five_window_l: five_window_r])
        print(five_window_dict)
        # Check if window_l value is fine.
        domain = requests[five_window_l]
        print(domain)
        if five_window_dict[domain] > 2:
            final[five_window_l] = 432
        else:
            final[five_window_l] = 200

        # Update window values
        five_window_dict[domain] -= 1
        five_window_l += 1

        five_window_r += 1
        if five_window_r < len(requests):
            domain = requests[five_window_r]
            five_window_dict[domain] += 1

    # Iterate through the final window
    for idx in range(five_window_r):
        domain = requests[idx]
        if five_window_dict[domain] > 2:
            final[idx] = 432
        else:
            final[idx] = 200

    # Iterate through the 30-second window
    while thirty_window_r < len(requests):
        domain = requests[thirty_window_l]
        if thirty_window_dict[domain] > 5:
            final[thirty_window_l] = 432

        # Update window values
        thirty_window_dict[domain] -= 1
        thirty_window_l += 1

        thirty_window_r += 1
        if thirty_window_r < len(requests):
            domain = requests[thirty_window_r]
            thirty_window_dict[domain] += 1

    # Iterate through the final window
    for idx in range(thirty_window_r):
        domain = requests[idx]
        if thirty_window_dict[domain] > 5:
            final[idx] = 432

    print(final)
    return final


arr1 = ["www.abc.com", "www.xyz.com", "www.abc.com", "www.xyz.com", "www.abc.com",
        "www.xyz.com", "www.abc.com", "www.xyz.com", "www.abc.com", "www.xyz.com",
        "www.abc.com", "www.xyz.com", "www.abc.com", "www.xyz.com", "www.abc.com",
        "www.xyz.com", "www.abc.com", "www.xyz.com", "www.abc.com", "www.xyz.com"]

arr2 = ["www.abc.com", "www.xyz.com", "www.abc.com", "www.xyz.com", "www.abc.com",
        "www.xyz.com", "www.abc.com", "www.xyz.com", "www.abc.com", "www.xyz.com"]


print(rateLimiter(arr2))


def gray_to_binary(value: str) -> str:
    binary = value[0]  # first bit is the same
    for i in range(1, len(value)):
        prev_bit = int(binary[i - 1])
        gray_bit = int(value[i])
        binary += str(prev_bit ^ gray_bit)
    return binary


# Example usage:
gray_str = bin(13)[2:]
binary_str = gray_to_binary(gray_str)
decimal_value = int(binary_str, 2)

print(decimal_value)
