#list items in an array on their own line

arr = ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]

for i in arr:
    print(i)



arr = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]


def foo(arr):
    for i in arr:
        if not isinstance(i, list):
            print(i)
        else:
            foo(i)


