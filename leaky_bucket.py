capacity = 10
input_size = 4
out_size = 1
storage = 0
iterations = 4

for i in range(0,iterations):
    size_left = capacity - storage
    if input_size <= size_left:
        storage += input_size
    else:
        print("Packet lost: ",input_size)
    print(f"Buffer size = {storage} out of capacity {capacity}")
    storage -= 1