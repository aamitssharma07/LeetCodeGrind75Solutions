# meetings = [[5, 10], [2, 3]]

meetings = [[1, 3], [5, 7], [4, 6], [7, 9], [9, 10]]

#Brut Force with complexity of O(n2)
#Logic is start with the first meeting and then check that any other meeting is collinding with that time and keep doing for all meetings
# min_rooms = 1
# total_meetings = len(meetings)
# for current_meeting in range(total_meetings-1):
#     cm_start_time = meetings[current_meeting][0]
#     cm_end_time = meetings[current_meeting][1]
#     other_meetings = current_meeting + 1
#     while(other_meetings<total_meetings):
#         if(meetings[other_meetings][0]>=cm_end_time or  meetings[other_meetings][1] <=  cm_start_time ):
#             pass
#         else:
#             min_rooms+=1
#         other_meetings+=1
# print(min_rooms)


start = []
end = []
for [x,y] in meetings:
    start.append(x)
    end.append(y)
start.sort()
end.sort()
rooms = 0
meeting_start = 0
meeting_end= 0
while(meeting_start<len(start)):
    if(start[meeting_start]<end[meeting_end]):
        rooms +=1
        meeting_start+=1
    else:
        meeting_end+=1
        meeting_start+=1
print(rooms)
