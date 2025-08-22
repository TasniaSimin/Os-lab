from typing import Sequence
requests = list(map(int, input("Enter the disk requests: ").split()))
requests.sort()
print("sorted requests: ",requests)
head = int(input("Enter head value : "))

total_mov = 0
Sequence=[]

while requests:
  requests.sort(key=lambda X: abs(X-head))
  closest = requests.pop(0)
  
  total_mov += abs(head-closest)
  head = closest
 
  Sequence.append(head)

print ("Total head mov: ",total_mov)