def array(arr):
    for i in arr:
        if i%2!=0:
            arr.remove(i)
    print(arr)
if __name__=="__main__":
    array([8,9])