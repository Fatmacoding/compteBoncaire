dect = {"hi":"123" ,"hii":"1231","hiii":"1232","hiiii":"1233"}
k = list(dect.keys())
j = list(dect.values())
n = input('entrer :   ')
index = j.index(n)
print("k =  " , k , type(k))
print("j =  " , j , type(j))
print('k[', index,'] =  ' ,k[index] )
