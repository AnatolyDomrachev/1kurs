import reverse

def path_from_market(path):
    print("path_from_market")

    back_path = reverse.reverse(path)
    num = 1
    for hop in back_path:
        print(num, hop)
        num += 1
