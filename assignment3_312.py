def load_acm(file_path):
    acm = {}
    try:
        with open(file_path) as f:
            for line in f:
                user, obj, perm = line.strip().split(',')
                acm.setdefault(user, {}).setdefault(obj, set()).add(perm) 
    except FileNotFoundError:
        print("please check file name and try again")
    return acm



def print_acm(acm): 
    print("ACM Capabilities")
    for user, perms in sorted(acm.items()):
        for obj, actions in sorted(perms.items()):
            print(f'{user} -> {obj}: {"".join(sorted(actions))}')



def process_request(acm, request_file):
    print("Access Request")
    try:
        with open(request_file) as f:
            for line in f:
                user, obj, perm = line.strip().split(',')
                if user in acm and obj in acm[user] and perm in acm[user][obj]:
                    print(f"Permit: {user} has '{perm}' access on {obj}")
                    print("\n")
                else:
                    print(f"Deny: {user} does not '{perm}' access on {obj}")
                    print("\n")
    except FileNotFoundError:
        print("please check file name and try again")


def update_acm(acm, update_file):
    try:
        with open(update_file) as f:
            for line in f:
                action, user, obj, perm = line.strip().split(',')
                if action == 'add':
                    acm.setdefault(user, {}).setdefault(obj, set()).add(perm)
                    print(f"Added perms: {user} -> {obj}: {perm}")
                    print("\n")
                elif action == 'remove':
                    if user in acm and obj in acm[user] and perm in acm[user][obj]:
                        acm[user][obj].discard(perm)
                        print(f"Removed perms: {user} -> {obj}: {perm}")
                        print("\n")
                        if not acm[user][obj]:
                            del acm[user][obj]
                        if not acm[user]:
                            del acm[user]
                    else:
                        print(f"Invalid update (perms not found): {user} -> {obj}: {perm}")
                        print("\n")
    except FileNotFoundError:
        print("please check file name and try again")


# ui/menu in main, probably add a loop as well else it will just crash
# 
def main():
    # acm = load_acm('input-acm-entries.txt')
    # print_acm(acm)
    # process_request(acm, 'sample-requests.txt')
    # update_acm(acm, 'sample-update-acm-entries.txt')
    # print_acm(acm)

    acm = {}
    while True:
        print("\n")
        print("1. Load input ACM")
        print("2. Print ACM")
        print("3. Update ACM entries from file")
        print("4. Evaluate access requests from file")
        print("5. Exit")

        choice = input("Select option (1-5): ").strip()

        # break at 5, else number try again

        if choice == "1":
            filename = input("Enter ACM filename: ").strip()
            acm = load_acm(filename)
        elif choice == "2":
            print_acm(acm)
        elif choice == "3":
            filename = input("Enter update filename: ").strip()
            update_acm(acm, filename)
        elif choice == "4":
            filename = input("Enter access request filename: ").strip()
            process_request(acm, filename)
        elif choice == "5":
            print("Exiting program")
            break   
        else:
            print("Try again, invalid input")

    # problem was just filenames being fixed/hardcoded
    # also, no success or fail msg for update, was just silent

if __name__ == "__main__":
    main()