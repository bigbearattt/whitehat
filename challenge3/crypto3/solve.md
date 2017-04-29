- First, we need to filter all icon face in faces.txt
>>>f = open("faces.txt", "r")
>>>text = f.read()

>>>icon = text.split() 
#slpit text to substring not include space

>>>from collections import Counter
>>>c = Counter(i for i in icon if len(i) > 1) 
#We count how many time a substring icon occurances. And remember, an icon had len > 1
>>>for i in c:
...print i, c[i]

@@ 12
:/ 100
<3 84
*_* 42
:> 7
:0 38
;) 15
:) 33
=]] 57
;)) 26
;] 147
=)) 79
:() 2
^^ 13
(-_-) 106
^_^ 18
:v 1
-.- 2
:~) 36
=) 107
-_- 46
~_~ 25
:'( 71
:') 89
_._! 27
:)) 45

>>> print "Number icon face:",len(c)
Number icon face: 26
#have 26 diffence icon, same with alphabet, I replace icon with a char 
#like you see, some icon substring is in a other icon substring e.g: (-_-) and -_-
#So we replace the longger icon substring first
>>>k = 0
>>>for i in c:
    if len(i) > 3:
        char = chr(ord('a')+k)
        text = text.replace(i, char)
        k+=1
>>>for i in c:
    if len(i) == 3:
        char = chr(ord('a')+k)
        text = text.replace(i, char)
        k+=1
>>>for i in c:
    if len(i) == 2:
        char = chr(ord('a')+k)
        text = text.replace(i, char)
        k+=1
>>>text
d n t z b m w   z j w   k o n l   ( d z k )   r q   n   q t w d r n o   h r f e   a k   r f k a m c n z r a f   q w d b m r z v   d a c t w z r z r a f q .   z j w m w   n m w   z j m w w   d a c c a f   z v t w q   a k   d z k q :   i w a t n m e v ,   n z z n d h - e w k w f d w   n f e   c r s w e . 
i w a t n m e v - q z v o w   d z k q   j n q   n   d a b t o w   a k   g b w q z r a f q   ( z n q h q )   r f   m n f l w   a k   d n z w l a m r w q .   k a m   w s n c t o w ,   x w p ,   k a m w f q r d ,   d m v t z a ,   p r f n m v   a m   q a c w z j r f l   w o q w .   z w n c   d n f   l n r f   q a c w   t a r f z q   k a m   w u w m v   q a o u w e   z n q h .   c a m w   t a r f z q   k a m   c a m w   d a c t o r d n z w e   z n q h q   b q b n o o v .   z j w   f w s z   z n q h   r f   d j n r f   d n f   p w   a t w f w e   a f o v   n k z w m   q a c w   z w n c   q a o u w   t m w u r a b q   z n q h .   z j w f   z j w   l n c w   z r c w   r q   a u w m   q b c   a k   t a r f z q   q j a x q   v a b   n   d z k   x r f w m .   k n c a b q   w s n c t o w   a k   q b d j   d z k   r q   e w k d a f   d z k   g b n o q . 
x w o o ,   n z z n d h - e w k w f d w   r q   n f a z j w m   r f z w m w q z r f l   h r f e   a k   d a c t w z r z r a f q .   j w m w   w u w m v   z w n c   j n q   a x f   f w z x a m h ( a m   a f o v   a f w   j a q z )   x r z j   u b o f n m n p o w   q w m u r d w q .   v a b m   z w n c   j n q   z r c w   k a m   t n z d j r f l   v a b m   q w m u r d w q   n f e   e w u w o a t r f l   w s t o a r z q   b q b n o o v .   q a ,   z j w f   a m l n f r y w m q   d a f f w d z q   t n m z r d r t n f z q   a k   d a c t w z r z r a f   n f e   z j w   x n m l n c w   q z n m z q !   v a b   q j a b o e   t m a z w d z   a x f   q w m u r d w q   k a m   e w k w f d w   t a r f z q   n f e   j n d h   a t t a f w f z q   k a m   n z z n d h   t a r f z q .   j r q z a m r d n o o v   z j r q   r q   n   k r m q z   z v t w   a k   d z k q ,   w u w m v p a e v   h f a x q   n p a b z   e w k   d a f   d z k   -   q a c w z j r f l   o r h w   n   x a m o e   d b t   a k   n o o   a z j w m   d a c t w z r z r a f q . 
c r s w e   d a c t w z r z r a f q   c n v   u n m v   t a q q r p o w   k a m c n z q .   r z   c n v   p w   q a c w z j r f l   o r h w   x n m l n c w   x r z j   q t w d r n o   z r c w   k a m   z n q h - p n q w e   w o w c w f z q   ( o r h w   b d q p   r d z k ) . 
d z k   l n c w q   a k z w f   z a b d j   a f   c n f v   a z j w m   n q t w d z q   a k   r f k a m c n z r a f   q w d b m r z v :   d m v t z a l m n t j v ,   q z w l a ,   p r f n m v   n f n o v q r q ,   m w u w m q w   w f l w f w w m r f l ,   c a p r o w   q w d b m r z v   n f e   a z j w m q .   l a a e   z w n c q   l w f w m n o o v   j n u w   q z m a f l   q h r o o q   n f e   w s t w m r w f d w   r f   n o o   z j w q w   r q q b w q . 
j w m w   r k   v a b m   k o n l   k o 4 l _ d z k _ r q _ f r l j z c n m w 
#delete space in word, and replace triple space by 1 space
>>>text = text.replace("   ","___")
>>>text = text.replace(" ","")
>>>text = text.replace("___"," ")
>>>text
dntzbmw zjw konl (dzk) rq n qtwdrno hrfe ak rfkamcnzraf qwdbmrzv dactwzrzrafq. zjwmw nmw zjmww daccaf zvtwq ak dzkq: iwatnmev, nzzndh-ewkwfdw nfe crswe.
iwatnmev-qzvow dzkq jnq n dabtow ak gbwqzrafq (znqhq) rf mnflw ak dnzwlamrwq. kam wsnctow, xwp, kamwfqrd, dmvtza, prfnmv am qacwzjrfl woqw. zwnc dnf lnrf qacw tarfzq kam wuwmv qaouwe znqh. camw tarfzq kam camw dactordnzwe znqhq bqbnoov. zjw fwsz znqh rf djnrf dnf pw atwfwe afov nkzwm qacw zwnc qaouw tmwurabq znqh. zjwf zjw lncw zrcw rq auwm qbc ak tarfzq qjaxq vab n dzk xrfwm. kncabq wsnctow ak qbdj dzk rq ewkdaf dzk gbnoq.
xwoo, nzzndh-ewkwfdw rq nfazjwm rfzwmwqzrfl hrfe ak dactwzrzrafq. jwmw wuwmv zwnc jnq axf fwzxamh(am afov afw jaqz) xrzj ubofnmnpow qwmurdwq. vabm zwnc jnq zrcw kam tnzdjrfl vabm qwmurdwq nfe ewuwoatrfl wstoarzq bqbnoov. qa, zjwf amlnfrywmq daffwdzq tnmzrdrtnfzq ak dactwzrzraf nfe zjw xnmlncw qznmzq! vab qjaboe tmazwdz axf qwmurdwq kam ewkwfdw tarfzq nfe jndh attafwfzq kam nzzndh tarfzq. jrqzamrdnoov zjrq rq n krmqz zvtw ak dzkq, wuwmvpaev hfaxq npabz ewk daf dzk - qacwzjrfl orhw n xamoe dbt ak noo azjwm dactwzrzrafq.
crswe dactwzrzrafq cnv unmv taqqrpow kamcnzq. rz cnv pw qacwzjrfl orhw xnmlncw xrzj qtwdrno zrcw kam znqh-pnqwe wowcwfzq (orhw bdqp rdzk).
dzk lncwq akzwf zabdj af cnfv azjwm nqtwdzq ak rfkamcnzraf qwdbmrzv: dmvtzalmntjv, qzwla, prfnmv nfnovqrq, mwuwmqw wflwfwwmrfl, caprow qwdbmrzv nfe azjwmq. laae zwncq lwfwmnoov jnuw qzmafl qhrooq nfe wstwmrwfdw rf noo zjwqw rqqbwq.
jwmw rk vabm konl ko4l_dzk_rq_frljzcnmw

#And now we use http://quipqiup.com/ in statistics mode
#we get:
capture the flag (ctf) is a special kind of information security competitions. 
there are three common types of ctfs: jeopardy, attack-defence and mixed. 
jeopardy-style ctfs has a couple of questions (tasks) in range of categories. 
for example, web, forensic, crypto, binary or something else. team can gain some 
points for every solved task. more points for more complicated tasks usually. 
the next task in chain can be opened only after some team solve previous task. 
then the game time is over sum of points shows you a ctf winer. famous example
of such ctf is defcon ctf quals. well, attack-defence is another interesting 
kind of competitions. here every team has own network(or only one host) with 
vulnarable services. your team has time for patching your services and developing
exploits usually. so, then organizers connects participants of competition and the
wargame starts! you should protect own services for defence points and hack opponents
for attack points. historically this is a first type of ctfs, everybody knows about 
def con ctf - something like a world cup of all other competitions. mixed competitions
may vary possible formats. it may be something like wargame with special time for 
task-based elements (like ucsb ictf). ctf games often touch on many other aspects of
information security: cryptography, stego, binary analysis, reverse engeneering, mobile 
security and others. good teams generally have strong skills and experience in all these
issues. 
here if your flag fl4g_ctf_is_nightmare

but the flag is 'fl4g _ ctf _ is _ nightmare' because we have delete single space

WhiteHat{dd9ad4e5c365c8f29b2d44345a9d1b7e14460d95}

