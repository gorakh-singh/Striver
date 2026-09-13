num=int(input())
for _ in range(num):
     
    i,k=map(int,input().split())
    if k < i or k > 2 * i - 1:
            print(-1)
    else:
        matrix = [[0 for _ in range(i)] for _ in range(i)]
        n=1
        c = 2 * i - k
        for x in range(0,c):
            matrix[x][x]=n
            n+=1

        for x in range(c,i):
            if matrix[c-1][x]==0:
                    matrix[c-1][x]=n
                    n+=1

        for x in range(c,i):
            if matrix[x][c-1]==0:
                matrix[x][c-1]=n
                n+=1

        for g in range(i):
            for j in range(i):
                if matrix[g][j]==0:
                    matrix[g][j]=n
                    n+=1

        for y in matrix:
             print(*y)