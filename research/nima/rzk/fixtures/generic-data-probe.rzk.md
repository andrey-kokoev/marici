```rzk
#lang rzk-1
#data NimaGenericProbe (A : U)
  := nima-generic-probe (a : A)
#define nima-probe-make (A : U) (a : A) : NimaGenericProbe A := nima-generic-probe A a
#define nima-probe-read (A : U) (x : NimaGenericProbe A) : A
  := match x (nima-generic-probe a => a)
#define nima-probe-split (A B : U) ((a,b) : Sigma (_ : A), B) : A := a
```
