# The E/E_B positive overlap has two exact endpoint walls internal to E's image

Fix strictly positive E source weights `(w₄,w₅,w₆,w₇,w₈,t,u)=(1,1,1,1,1,3,2)` and vary its supported physical-column-3 weight `w₂=e>0` at positive rank-six moment-curve external data. Solve the **complete unique rational E_B inverse** at the **same target**. Its first two positive weights are exactly

```
w₂(E_B) = 2(445e−44)/895,
w₄(E_B) = (11531−250e)/(3488e+58879).
```

**All six other strict E_B positivity factors are positive for every `e>0`.** Thus E_B shares the target with a strictly positive E source **if and only if**

```
44/445 < e < 11531/250.
```

At the lower endpoint E_B reaches its `w₂=0` source facet; at the upper endpoint it reaches `w₄=0`. Yet the E source is **strictly positive at both**, and its exact target Jacobian along the family is

```
−29262643200(8e−1835)/(23e+51)²,
```

which is nonzero at both endpoint values. Their E_B support walls therefore pass through **interior target points of E's positive image**, not boundaries of the whole E-positive image. The other square neighbors E_C and E_D have `w₄<0` for **every `e>0`** along this family, so they never provide positive preimages here.

This classifies **one fixed positive-target curve**, not all target-space overlap or the full n=9 image. At least near each regular E endpoint the image has a positive interior sector, but other cells and contour multiplicities remain unresolved.

Checker: `research/nima/checkers/check_nine_point_label3_EB_positive_overlap_chamber.py`; result: `research/nima/results/nine-point-label3-EB-positive-overlap-chamber.json`.
