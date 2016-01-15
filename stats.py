def mean(vals):
   '''Calculate the arithmetic mean of a list'''
   assert type(vals) is list, 'wrong input'
 
#   list = []
#   for i in vals:
#      list.append(float(i))

   vals = [float(x) for x in vals]
   length = len(vals)
   total = sum(vals)

   if length  == 0.0:
      return 0.0
   else:
      return total/length

print (mean([2,4])) 
#print (mean('hello'))
