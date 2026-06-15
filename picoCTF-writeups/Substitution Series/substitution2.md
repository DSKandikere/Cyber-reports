# CTF Writeup - Monoalphabetic Substitution Cipher

## Challenge Description

The challenge provided a long encrypted text along with a flag in the following format:

```
ZNV{L6Y4G_4L41H515_15_73B10W5_8F1KV808}
```

One hint was provided:

1. Try refining your frequency attack, maybe analyzing groups of letters would improve your results?

Theis hint suggested that the challenge involved a classical substitution cipher rather than a modern encryption algorithm.

---

## Initial Analysis

Upon examining the ciphertext, several observations could be made:

* Word boundaries were preserved.
* Punctuation remained unchanged.
* Certain words appeared repeatedly throughout the ciphertext.
* Letter frequencies were not uniform.

These characteristics are typical of a **monoalphabetic substitution cipher**, where each plaintext letter is replaced by a unique ciphertext letter throughout the entire message.

For example:

```
nafy
zqgswnfyefzwyxnh
qvvflexuf
```

appeared multiple times, indicating that common English words or phrases were being encrypted using a fixed substitution mapping.

---

## Frequency Analysis

The first step was to perform a frequency analysis of the ciphertext letters.

In English text, the most common letters are:

```
E, T, A, O, I, N, S, H, R
```

By comparing the frequency distribution of ciphertext letters with standard English letter frequencies, candidate mappings could be established.

Additionally, repeated short words were analyzed:

```
nafy
qvn
ntl
```

These were likely common English words such as:

```
that
the
and
for
with
```

which helped in constructing the substitution table.

---

## Pattern Recognition

The second hint suggested using punctuation and word structure.

Since spaces and punctuation were preserved, the lengths of words remained unchanged. This made it possible to compare ciphertext word patterns against common English words.

Repeated technical-looking words occurring throughout the text indicated that the plaintext was likely discussing cryptography, substitution ciphers, or frequency analysis itself.

As more mappings were discovered, larger portions of the text became readable, eventually revealing the complete substitution alphabet.

---

## Recovering the Plaintext

After enough substitutions were identified, the remaining letters could be solved incrementally.

The resulting plaintext described the concept of frequency analysis and how monoalphabetic substitution ciphers can be broken by exploiting letter frequencies and common word patterns.

---

## Obtaining the Flag

Using the recovered substitution mapping, the encrypted flag:

```
ZNV{L6Y4G_4L41H515_15_73B10W5_8F1KV808}
```

was decrypted to obtain the final flag.

```
picoCTF{N6R4M_4N41Y515_15_73D10U5_8E1BF808}
```

---

## Lessons Learned

* Monoalphabetic substitution ciphers are vulnerable to frequency analysis.
* Preserved word boundaries provide valuable information for cryptanalysis.
* Repeated words and common English patterns significantly reduce the search space.
* Combining frequency statistics with pattern matching is often sufficient to completely recover the plaintext.

## Tools Used

* Frequency Analysis
* Manual Pattern Matching

## Category

Cryptography

## Difficulty

Medium

## Techniques

* Frequency Analysis
* Classical Cryptography
* Monoalphabetic Substitution Cipher
* Pattern Recognition
