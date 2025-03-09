A,B="2",3
Txt="@"
print((A+Txt)*B)#concatenation(add the two strings and print the output B times )

A,B=2,5.0
C=A*B
print(C)#AE of integer and float will result in float 

A,B=2,6
C=A/B#division of two integer will be float
print(C)

A,B=1.5,3
C=A//B
print(C,A/B)#integer division with float and int will give int displayed as float

A,B=12,5
C=A//B#integer division give the same result as tha of floor 
print(C)

A,B=5,6
C=-6
D=A%B
E=A%C
print(D)
print(E)#when deno is neg then remainder is negative