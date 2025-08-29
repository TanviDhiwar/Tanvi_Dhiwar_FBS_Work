digit = int(input("Enter three digit number:"))

f_num = digit // 100
s_num = (digit // 10) % 10
t_num = digit % 10
if(f_num == 2 * s_num and f_num == t_num /2):
    print("Yes,You have done it")
else:
    print("Please Try Next Time")
print(f'{f_num},{s_num},{t_num}')
