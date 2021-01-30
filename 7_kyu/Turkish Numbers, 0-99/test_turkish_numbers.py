Test.describe("Randomized tests")
from random import shuffle

TURKISH = """sıfır;bir;iki;üç;dört;beş;altı;yedi;sekiz;dokuz;on;on bir;on \
iki;on üç;on dört;on beş;on altı;on yedi;on sekiz;on dokuz;yirmi;yirmi bir;yirmi \
iki;yirmi üç;yirmi dört;yirmi beş;yirmi altı;yirmi yedi;yirmi sekiz;yirmi \
dokuz;otuz;otuz bir;otuz iki;otuz üç;otuz dört;otuz beş;otuz altı;otuz \
yedi;otuz sekiz;otuz dokuz;kırk;kırk bir;kırk iki;kırk üç;kırk dört;kırk \
beş;kırk altı;kırk yedi;kırk sekiz;kırk dokuz;elli;elli bir;elli iki;elli \
üç;elli dört;elli beş;elli altı;elli yedi;elli sekiz;elli \
dokuz;altmış;altmış bir;altmış iki;altmış üç;altmış dört;altmış beş;altmış \
altı;altmış yedi;altmış sekiz;altmış dokuz;yetmiş;yetmiş bir;yetmiş \
iki;yetmiş üç;yetmiş dört;yetmiş beş;yetmiş altı;yetmiş yedi;yetmiş \
sekiz;yetmiş dokuz;seksen;seksen bir;seksen iki;seksen üç;seksen dört;seksen \
beş;seksen altı;seksen yedi;seksen sekiz;seksen dokuz;doksan;doksan \
bir;doksan iki;doksan üç;doksan dört;doksan beş;doksan altı;doksan \
yedi;doksan sekiz;doksan dokuz""".split(";")
  
nums = list(range(100))
shuffle(nums)
for n in nums:
    Test.assert_equals(get_turkish_number(n), TURKISH[n])