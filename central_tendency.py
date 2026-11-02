import statistics as s
def stat(d):
    mean = s.mean(d)
    median = s.median(d)
    mode = s.mode(d)
    return mean,median,mode

d = [1,2,3,4,5,5,6,6,7,8,9,10]
mean,median,mode=stat(d)
print("mean :",mean)    
print("median :",median)
print("mode :",mode) 
