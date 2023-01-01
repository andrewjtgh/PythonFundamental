print("Hello World")
def hello(name):
  greet = "Hi! " + name
  print(greet)

hello("Jonathan")

def score(total, correct, wrong):
  return (correct*2+wrong)/total/2*100
"""
> score(20, 20, 0)
100.0 # because you got perfect score
> score(20, 15, 0)
75.0 # Because you got 75% of them correct and you didn’t show up to the
25%
> score(20, 15, 5) # ( 15 * 2 + 5 * 1 ) / (20 * 2)
87.5
> score(20, 10, 5)
62.5
> score(20, 0, 20)
50.0
"""

def score75(total, correct, wrong):
  return ( (min(30, 2 * correct) ) + (min ( max(15 - correct, 0), wrong) ) ) / 30 * 100

print(min(-15,0))
print(score75(20,20,0))
print(score75(20,15,0))
print(score75(20,15,5))
print(score75(20,10,5))
print(score75(20,0,20))
"""
> score75(20, 20, 0)
100.0 # because you got a perfect score
> score75(20, 15, 0)
100.0 # because you got 75% of the questions correctly, even if you didn't
show up for 5
> score75(20, 15, 5) # again we only take your top 75%
100.0
> score75(20, 10, 5)
83.33333333333334
> score75(20, 0, 20)
50.0
"""