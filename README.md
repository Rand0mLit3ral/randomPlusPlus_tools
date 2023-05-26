# RandomPlusPlus Tools 1.0.1
#### This library will help you when writing code using the ```random``` library

</br>

A simple code example and its implementation using the ```RandomPlusPlus_Tools``` library:</br>

#### Without a library

```
import random

list = [1,2,3,4,5,6,7,8]
not_to_list = [1,3,6]
x = random.choise(list)
while True:
    if x in not_to_list:
	x = random.choise(list)
    else:
	print(x)
```

#### And with the RandomPlusPlus_Tools library

```
import RandomPlusPlus_Tools as rppt

print(rppt.Rlist([1,2,3,4,5,6,7,8], [1,3,6])
```

</br>

both there and there the answer will be the same (any number from the list except 1, 3 and 6)
but the length of the code is noticeably less using the library
