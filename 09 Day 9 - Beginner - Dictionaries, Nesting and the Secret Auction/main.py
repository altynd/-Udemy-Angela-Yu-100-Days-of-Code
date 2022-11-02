# student_scores = {
#     "Harry":81,
#     "Ron":78,
#     "Hermione":99,
#     "Draco":74,
#     "Neville":62,
# }
#
# student_grades = {}
#
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceed"
#     elif score >70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# for key in student_grades:
#     print(f"key is {key}, value is {student_grades[key]}")


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Gamburg", "Stuttgard"]
    },
]


def add_new_country(country, visits, cities):
    # variant 1
    travel_log.append(
        {
            "country": country,
            "visits": visits,
            "cities": cities
        }
    )
    # variant2
    # new_country = {}
    # new_country["country"] = country
    # new_country["visits"] = visits
    # new_country["cities"] = cities
    # travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
