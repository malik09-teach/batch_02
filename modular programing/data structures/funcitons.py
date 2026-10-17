'''def calling_name(name,age=18):
    print(name,age)
calling_name("name:abbas : age:",25)   
    
  
    
def infofunction (name,age=18,info_list=[]):
    info_list.append(name)
    info_list.append(age)
      
    return info_list
    
print("first call ",infofunction("huzaifa",22))
print("second call ",infofunction("abbas",25))    

    
def infofunction (name,age=18,info_list=[]):
    info_list.append(name)
    info_list.append(age)
      
    return info_list
    
print("first call ",infofunction("huzaifa",22))
print("second call ",infofunction("abbas",25))    
   
    
    
    
def summ(*nums):
    summs=0
    for i in nums:
        summs+=i
        print("summs value",summs)    
    return summs      
        
print(summ(1,25,50))        

'''

def names(*names,classi):

    for i in names:
       print(i)    
          
        
names("abbas","huzaifa ","iqra","ALISHBA",1)        