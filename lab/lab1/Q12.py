n = int(input())
# write your program below

def judege(i):
	if i<=0:
		return 0
	else:
		return cal(i)
		
def cal(i):
	s = 0
	for j in range (1,i+1):
		s = s + j*2-1
	return s
 
output = judege(n)
print(output)
