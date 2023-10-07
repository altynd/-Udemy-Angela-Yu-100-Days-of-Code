from my_nutritionix import get_data
from my_sheety import load_data, post_data

text = input("tell me what you did: ")
data = get_data(text)
post_data(data)
load_data()


# 1. data=get_data("what i am doing") - DONE

# 2. post_data(data) to googlesheet - DONE

# 3. load_data() - get info from googlesheet - DONE
