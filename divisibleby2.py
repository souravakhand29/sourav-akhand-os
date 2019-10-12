def isDivisibleBy2(bin): 
    l = len(bin) 
    if((l % 2) == 1): 
          
      
        bin = '0' + bin
          
     
    odd_sum = 0
    even_sum = 0
    isOddDigit = 1
    for i in range(0, len(bin), 2): 
          
        if(isOddDigit): 
            odd_sum += equivalentBase4(bin[i:i + 2]) 
                
        else: 
            even_sum += equivalentBase4(bin[i:i + 2]) 
              
        isOddDigit = isOddDigit ^ 1
  
   
    if(abs(odd_sum - even_sum) % 2 == 0): 
        return "Yes"
    else: 
        return "No"
if __name__=="__main__": 
    bin = "10000101001"
    print(isDivisibleBy2(bin)) 
