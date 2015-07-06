from users import *
from manhattan import *
from computeNearestNeighbor import *
from recommend import *
from pearson import *

user_hailey = users["Hailey"]
user_veronica = users["Veronica"]
user_angelica = users["Angelica"]
user_jordyn = users["Jordyn"]
user_bill = users["Bill"]

# print manhattan(user_hailey, user_veronica)
# print manhattan(user_hailey, user_jordyn)
# print "--"
# print computeNearestNeighbor("Hailey", users)
# print ".."
# print recommend("Hailey", users)
# print recommend("Chan", users)
# print recommend("Sam", users)
print pearson(user_angelica, user_bill)
print pearson(user_angelica, user_hailey)