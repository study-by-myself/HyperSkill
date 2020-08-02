
~~~
1. list
  delete, remove, pop 차이
  del a[index] : 인덱스를 이용하여 지운다
  a.remove(A) : A에 해당하는 값을 찾아 첫 번째 요소를 지운다
  a.pop() : 맨 뒤에꺼 하나 없애고 리턴해줌
  a.pop(index) : index를 이용하여 지우고 그 값을 리턴해줌
  a.insert(index, item) : index에 item을 넣는다
  
2. sort
  a.sort() : return None, 정렬만 시켜줌
  sorted(a) : 새로 정렬된 리스트를 리턴시켜줌
  
3. add
  a.append(1) : 뒤에 1이라는 요소갸 추가됨
  a.extend([2, 3]) : 뒤에 [2, 3]이라는 리스트가 추가됨. a += [2,3] 과 동일.
~~~

~~~
>>> a
[1, 2, 3]
>>> id(a)
139766034191624
>>> id(a[0])
139766056006880
>>> id(a[0])
139766056006880
>>> id(a[0])
139766056006880
>>> id(a[1])
139766056006912
>>> id(a[2])
139766056006944
~~~

