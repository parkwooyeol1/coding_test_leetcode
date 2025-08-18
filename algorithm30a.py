def combine(n,k):
    result = []
    def dfs(start, temp):
        if len(temp) == k:
            result.append(temp[:])
            return
        for i in range(start, n+1):
            dfs(i+1, temp + [i])
    dfs(1, [])
    return result

    
n = 4
k = 2
print(combine(n,k))
        
    



            


            
        

    
