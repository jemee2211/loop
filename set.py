#set = {}

breakfast = {"dosa","tee","bhakhri"}
dinner = {"pizza","sandwich","dal"}
#food = (breakfast,dinner)

dinner.update(breakfast)
breakfast.add("khaman")
dinner.remove("pizza")
for i in dinner:
    print(i)