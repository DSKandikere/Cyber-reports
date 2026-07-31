# Challenge Information
- Challenge Name: FlagBOIS
- Category: Forensics
- Difficulty: Easy
- Points: 100
- CTF: Flash CTF – July 2026

# Challenge Description

> We've been seeing some weird NetBIOS name registrations recently, can you figure out what "hostnames" these workstations have?
```
FDGLGJGMGMECGJHEHLGODDHEGCGJDAAA

HDFPGEGDDAGEGFFPHEDAFPHHDBGOHNAA
```

# Analysis
Initially I thought this is a hex, but found hex is between 0-9 and A-F, and The provided strings are the characters between A to P.

This pattern is commonly associated with NetBIOS First-Level Encoding, where:
- Each byte is represented using two characters.
- Each character represents a 4-bit value.
- The values range from A to P (0-15).

Therefore, the given strings are likely encoded NetBIOS names that need to be decoded.

# Solution

## Step 1: Identify Encoding

Since the data only contains characters A-P, I suspected NetBIOS name encoding.

I used CyberChef to decode the strings.

## Step 2: CyberChef Recipe

CyberChef operations used: From NetBIOS Name

Input:
```
FDGLGJGMGMECGJHEHLGODDHEGCGJDAAA
```
Output:
```
SkillBit{n3tbi0
```
Second input:
```
HDFPGEGDDAGEGFFPHEDAFPHHDBGOHNAA
```
Output:
```
s_dc0de_t0_w1n}
```

Combining both decoded parts:
```
SkillBit{n3tbi0s_dc0de_t0_w1n}
```

# Final Flag
```
SkillBit{n3tbi0s_dc0de_t0_w1n}
```

# Tools Used
1. CyberChef
2. NetBIOS First-Level Encoding knowledge

# Key Takeaways
- NetBIOS names can be encoded using an A-P character mapping scheme.
- Strings containing only characters from A-P should be checked for NetBIOS encoding.
- CyberChef provides a quick way to decode protocol-specific encodings without writing custom scripts.
- Understanding network protocols helps identify hidden data during forensic investigations.
