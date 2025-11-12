# bookbot

bootbot is a CLI application which takes in a raw text file. It returns the
total word count, as-well as the count of each letter that appears in the text
and orders them by usage. The this is my first [Boot.dev](https://www.boot.dev) project.

**Example:**

```{bash}

❯ python3 main.py books/frankenstein.txt
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt
----------- Word Count -----------
Found 75767 total words
--------- Character Count ---------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
,: 5962
p: 5952
g: 5795
b: 4868
v: 3737
.: 3121
k: 1661
;: 1350
x: 691
“: 506
j: 497
q: 325
”: 316
z: 235
:: 211
?: 208
!: 201
-: 173
’: 144
_: 124
—: 123
*: 97
1: 91
™: 57
‘: 43
(: 35
): 35
æ: 28
8: 24
2: 19
0: 18
7: 18
3: 15
4: 12
5: 12
6: 9
9: 9
/: 8
â: 8
ê: 7
&: 5
•: 4
[: 2
]: 2
ë: 2
$: 2
#: 1
ô: 1
%: 1
============ END ============
```
