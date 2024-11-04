a="""Python is dynamically typed and garbage-collected. 
It supports multiple programming paradigms, including structured 
(particularly procedural), object-oriented and functional programming. 
It is often described as a "batteries included" language 
due to its comprehensive standard library"""

a=a.lower()

v="aeiou"

d={}


for i in a:  ### p
  count=0
  if i in v:###a e i o u
    count=count+1## 0+1   -> cout =1
    if i in d.keys():
      d[i]+=count
    else:
      d[i]=count
