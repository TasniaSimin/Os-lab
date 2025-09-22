requests = [14, 20, 29, 40, 50, 110]
head = 29
direction = "left"

requests.sort()

left = [r for r in requests if r < head]
right = [r for r in requests if r > head]
equal = [r for r in requests if r == head]

seek_sequence = [head]
total_seek_time = 0
current_head = head

if direction == "left":
    left.sort(reverse=True)
    for track in left:
        seek_sequence.append(track)
        total_seek_time += abs(current_head - track)
        current_head = track

    for track in right:
        seek_sequence.append(track)
        total_seek_time += abs(current_head - track)
        current_head = track

for track in equal:
    if track != head:
        seek_sequence.append(track)
        total_seek_time += abs(current_head - track)
        current_head = track
print("Seek Sequence:", seek_sequence)
print("Total Seek Time:", total_seek_time)
