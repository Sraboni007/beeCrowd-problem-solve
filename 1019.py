x = [100,50,20,10,5,2,1]
N = int(input())
flag  = True
for note in x:
    if flag:
        print( f"{N}")
        flag = False
      
    num_notes = N // note
    N %= note
    print(f"{num_notes} nota(s) de R$ {note},00")
