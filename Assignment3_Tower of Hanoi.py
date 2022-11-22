def move(from_tower, to_tower, current_move):
        print("Move", current_move, ": move the top disk from", from_tower, "to", to_tower)


n = int(input("Enter number of Disks: "))
source = n
interim = 0
dest = 0
print("Minimum required moves", (2**n)-1)
for i in range(1, (2**n)):
    if n % 2 == 0:
        if i % 3 == 1:
            move('source', 'intermediate', i)
            source -= 1
            interim += 1
            print('No of disc in source', source, 'No of disc in intermediate', interim)
        elif i % 3 == 2:
            move('source', 'destination', i)
            source -= 1
            dest += 1
            print('No of disc in source', source, 'No of disc in destination', dest)
        elif i % 3 == 0:
            move('intermediate', 'destination', i)
            interim -= 1
            dest += 1
            print('No of disc in interim', interim, 'No of disc in destination', dest)
    else:
        if i % 3 == 1:
            if source != 0:
                move('source', 'destination', i)
                source -= 1
                dest += 1
                print('No of disc in source', source, 'No of disc in destination', dest)
            else:
                move('destination', 'source', i)
                dest += 1
                source -= 1
                print('No of disc in destination', dest, 'No of disc in source', source)
        elif i % 3 == 2:
            if source != 0:
                move('source', 'intermediate', i)
                source -= 1
                interim += 1
                print('No of disc in source', source, 'No of disc in intermediate', interim)
            else:
                move('intermediate', 'source', i)
                interim -= 1
                source += 1
                print('No of disc in intermediate', interim, 'No of disc in source', source)
        elif i % 3 == 0:
            if dest != 0:
                move('destination', 'intermediate', i)
                dest -= 1
                interim += 1
                print('No of disc in destination', dest, 'No of disc in intermediate', interim)
            else:
                move('intermediate', 'destination', i)
                interim -= 1
                dest += 1
                print('No of disc in intermediate', interim, 'No of disc in destination', dest)


