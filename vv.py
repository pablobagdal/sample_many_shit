def F(x, m):
    if x >= 26:
        if m == 4 or m == 2:
            return True
        else:
            return False
    else:
        if m == 0: # наступает 1 ход Пети
            if x % 2 == 0:
                return F(x + 1, m + 1) and F(x + 2, m + 1)
            else:
                return F(x + 1, m + 1) and F(x + 2, m + 1) and F(x * 2, m + 1)
        elif m == 1: # наступает 1 ход Вани
            if x % 2 == 0:
                if F(x + 1, m + 1) and F(x + 2, m + 1):
                    return False
                else:
                    return F(x + 1, m + 1) or F(x + 2, m + 1)
            else:
                if F(x + 1, m + 1) and F(x + 2, m + 1) and F(x * 2, m + 1):
                    return False
                else:
                    return F(x + 1, m + 1) or F(x + 2, m + 1) or F(x * 2, m + 1)
        elif m == 2: # наступает 2 ход Пети
            if x % 2 == 0:
                return F(x + 1, m + 1) and F(x + 2, m + 1)
            else:
                return F(x + 1, m + 1) and F(x + 2, m + 1) and F(x * 2, m + 1)
        elif m == 3: # наступает 2 ход Вани
            if x % 2 == 0:
                return F(x + 1, m + 1) or F(x + 2, m + 1)
            else:
                return F(x + 1, m + 1) or F(x + 2, m + 1) or F(x * 2, m + 1)
        else:
            return False
for S in range(1,26):
    if F(S,0) == True:
        print(S)
        break
