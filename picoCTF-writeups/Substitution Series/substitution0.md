## substitution0 Question 
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?

## Given file:
message.txt => The following are the contents of the file,
```
OHNFUMWSVZLXEGCPTAJDYIRKQB 

Suauypcg Xuwaogf oacju, rvds o waoiu ogf jdoduxq ova, ogf hacywsd eu dsu huudxu
mace o wxojj noju vg rsvns vd roj ugnxcjuf. Vd roj o huoydvmyx jnoaohouyj, ogf, od
dsod dveu, yglgcrg dc godyaoxvjdj—cm ncyaju o wauod pavbu vg o jnvugdvmvn pcvgd
cm ivur. Dsuau ruau drc acygf hxonl jpcdj guoa cgu ukdauevdq cm dsu honl, ogf o
xcgw cgu guoa dsu cdsua. Dsu jnoxuj ruau uknuufvgwxq soaf ogf wxcjjq, rvds oxx dsu
oppuoaognu cm hyagvjsuf wcxf. Dsu ruvwsd cm dsu vgjund roj iuaq aueoalohxu, ogf,
dolvgw oxx dsvgwj vgdc ncgjvfuaodvcg, V ncyxf soafxq hxoeu Zypvdua mca svj cpvgvcg
aujpundvgw vd.

Dsu mxow vj: pvncNDM{5YH5717Y710G_3I0XY710G_03055505}
```

## Solution

As we can see the contents of the file, the last line in the file contains an encrypted flag.
Considering this is a substitution cipher problem, we need to find out what type of substitution is performed on the message.txt file. How to find that ?

The very firs line in the file:
```
OHNFUMWSVZLXEGCPTAJDYIRKQB 
```
is very likely the cipher alphabet used for a monoalphabetic substitution cipher.

In a monoalphabetic substitution cipher, each plaintext letter maps to exactly one ciphertext letter for the entire message. A common way to specify the key is by giving a 26-letter permutation of the alphabet:
```
Plain : ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cipher: OHNFUMWSVZLXEGCPTAJDYIRKQB
```

A few observations that needs to be considered are as follows:
- The string contains 26 unique letters.
- No letter repeats.
- It is a permutation of A–Z.
So the first line is most likely the actual substitution key needed to decrypt the ciphertext below it.

On using online tool such as cyberchef,
## Flag = PICOCTF{5UB5717U710N_3V0LU710N_03055505}
