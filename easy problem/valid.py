def isValid( s ):
    st = []
    f = True
    for i in s:
        if(len(st)!=0 and i == ')' and st[-1]== '(' ):
            st = st[:-1]
            
        
        elif(len(st)!=0 and i == ']' and st[-1]== '[' ):
            st = st[:-1]
        
        elif(len(st)!=0 and i == '}'and st[-1]== '{' ):
            st = st[:-1]
        else:
            st.append(i)

    if(len(st)!=0):
            f = False

    return f 
        





s = "(){}"
print(isValid( s ))