def fcfs_disk(request, head):
    total_seek = 0
    current = head
    print("seek seq:", end="")
    for i in requests:
        if i==head:
          print(f"{i}(skipped)", end="")
          head= None
          continue
        distance = abs(current - i)
        total_seek += distance
        current = i
        print(i, end=" ")

    print("\ntotal number of seek operations =", total_seek)

n=(int(input("enter num of reqs:")))

requests = []
print("enter requests:")
for i in range(n):
  req=int(input(f"requests{i+1}:"))
  requests.append(req)
head = int(input("enter the head position:"))

fcfs_disk(requests, head)