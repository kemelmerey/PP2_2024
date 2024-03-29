#1
"""
Print i as long as i is less than 6.
"""
#Anwer:
i = 1
while i < 6:
  print(i)
  i += 1

#2
"""
Stop the loop if i is 3.
"""
#Anwer:
i = 1
while i < 6:
  if i == 3:
    break
  i+=1

#3
"""
In the loop, when i is 3, jump directly to the next iteration.
"""
#Anwer:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#4
"""
Print a message once the condition is false.
"""
#Anwer:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")