# def solution(year):
#     if 1 <= year <= 2005 :
#         if (year % 100) == 0:     
#             return int(year / 100)
#         return int((year/ 100)+1)

# print(solution(2))

def solution(inputstring):     
    # inputstring = "anna"
    
    # print(prt)
    return inputstring == inputstring[::-1]
     

print(solution("aabaa"))           
 