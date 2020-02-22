school = [{'class': '   1A', 'scores': [3,4,4,5,2]},
{'class': '2A', 'scores': [4,5,2]},
{'class': '11A', 'scores': [3,5,2]}]
school_avg = 0
for class_ in school:
    scores_sum = 0
    print(sum(class_["scores"])/len(class_["scores"]))
    class_avg = sum(class_["scores"])/len(class_["scores"])
    school_avg += class_avg
print(school_avg/len(school))
#     for score in (class_["scores"]):
#         scores_sum += score

#     y = scores_sum/len(class_["scores"])
#     print(y)

# result = scores_sum
# print(result/len(school))