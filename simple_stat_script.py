def mean(vals):
   '''Calculate the arithmetic mean of a list'''
   assert type(vals) is list, 'wrong input'
   
   length = len(vals)
   total = sum(vals)

   if length  == 0.0:
      return 0.0
   else:
      return total/length

def test_mean():
   assert mean([2,4]) == 3.0

test_mean()

def test_empty_list():
   assert mean([]) == 0.0
test_empty_list()

#print (mean([2,4])) 
#print (mean('hello'))
