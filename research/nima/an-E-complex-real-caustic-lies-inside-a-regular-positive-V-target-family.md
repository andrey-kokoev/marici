# An E complex/real caustic lies inside a regular positive V target family

Keep positive moment-curve nine-point external data fixed and vary only V's strictly positive source parameter `w₂=e>0`, with `(w₄,w₅,w₆,w₇,w₈,t,u)=(1,1,1,1,1,3,2)`. V's exact 8×8 target Jacobian in the fixed first-pivot chart is

```
−23293063987200 (35e+19)/(23e+102)²,
```

so **V is target-regular for every `e>0`**. The complete E fibre along this same positive V target curve obeys a special rank-three linear lift forcing `q=det(T)=0`, followed by a quadratic. Its exact quadratic discriminant is

```
36 (597475225 e⁴ + 202824050 e³ − 497275515 e²
    − 467083828 e + 13468900)
/(2825 e² − 503787 e − 169286)².
```

The quartic numerator changes from **positive at `e=1/40`** (two real, nonpositive E sheets) to **negative at `e=1/35`** (two nonreal E sheets); its derivative is strictly negative on `(1/40,1/35)`. Therefore it has a **unique simple root** in that interval (approximately `0.02801114`), while V's positive target map remains regular. This is an **interior complex/real transition of the algebraic E fibre along a regular positive V family**, not a boundary of V's positive image.

A quadratic fibre discriminant zero does **not by itself prove a pole of the complete rational E two-sheet trace**: the sheet sum may remove or modify it, and the corresponding E source need not lie on a positive real contour. No physical nine-point form singularity is asserted.

Checker: `research/nima/checkers/check_nine_point_E_complex_real_caustic_within_positive_V_family.py`; result: `research/nima/results/nine-point-E-complex-real-caustic-within-positive-V-family.json`.
