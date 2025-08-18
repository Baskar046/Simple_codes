def cap(s):
    words=s.split()     #split words into ['selva','baskar']
    store=[]
    for i in words:     #first takes word of selva
        if len(i)>1:        #selva (5) char < 1:  it's true
            cap_word=i[0].upper() + i[1:-1] + i[-1].upper()     #cap_word=S+elv+A
            store.append(cap_word)      #store='SelvA'
        else:
            cap_word=i.upper()  #it's run less one string 
            store.append(cap_word)  #it's append into store 
    return ' '.join(store)      #it's join "SelvA BaskaR" 
res=cap("selva baskar")
print(res)
