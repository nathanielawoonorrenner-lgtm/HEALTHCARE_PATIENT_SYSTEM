from builtins import list

numbers ={1,3,5,8,9,12}
print(numbers)

student_info ={"Nathaniel",905001111,8.9,False}
print(student_info)

players_info ={"messi","rashford","carrick","pele","ronaldo","amad"}
print(players_info)

items =list(["spoon","fish",23, True])
print(items)
print(items[3])

week_day = (["monday","tuesday"])
week_day.append("wednesday")
print(week_day)
week_day.extend(["thursday", "Friday"])
week_day.insert(0 ,"sunday")
print(week_day)
week_day.remove("sunday")
week_day.pop(0)
for day in week_day:
    print(day)