def balaji():
    return "This is my bank balance"
test_dict={"fname":balaji,"age":50,"address":"salem"}
print("The original dictionary is:" +str(test_dict))
res = test_dict['fname']()#we stored result in var so return is used
print("The required result is: " +str(res))