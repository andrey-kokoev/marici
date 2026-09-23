# Sixfold top-cell residue exactly equals the sourced four-mass loop-cell form

The positive loop-column n=9 contour is not merely set-theoretic. Its **oriented eight-form is exactly an iterated residue** of the sourced cyclic top-cell Grassmannian measure `d^(2×9)C/vol GL(2) /[(12)(23)…(91)]` (the primary positive-Grassmannian source displays this cyclic `G(2,n)` measure). This is a *source-contour* statement; it must not be confused with a residue of the eight-dimensional image canonical form at an image boundary.

Fix the `GL(2)` gauge at physical columns `(1,4)` to `I₂`. Take the eight source coordinates `(w₂,w₄,w₅,w₆,w₇,w₈,t,u)` and six transverse coordinates `(a,b,c,h,e,f)`:

```
C₉ = [[1,w₂,b,0,-h,-w₅,-w₆,-w₇,-w₈],
      [0, a,c,1,w₄,w₅t,w₆(t−e),w₇u,w₈(u−f)]].
```

At the sixfold boundary `a=b=c=h=e=f=0`, this is exactly the original positive four-pair source with physical column 3 zero. The nine cyclic adjacent minors, in order, are

```
a,  w₂c−ab,  b,  h,  w₅(w₄−ht),  w₅w₆e,
w₆w₇(t−e−u),  w₇w₈f,  −w₈(u−f).
```

The gauge-coordinate volume determinant in column-major order of the seven nonfixed columns, relative to `(source8,normal6)`, is **`w₅w₆w₇w₈`**. Six adjacent factors vanish; their leading normal product is `w₂w₅w₆w₇w₈·a b c h e f`. The three remaining adjacent factors limit to `−w₄w₅w₆w₇w₈·u(t−u)`. Consequently, in the explicitly stated differential and residue order, the sixfold residue density is

```
−1/[w₂w₄w₅w₆w₇w₈·u(t−u)],
```

**identically** the previously independently derived oriented source form—not merely up to an unspecified sign. The intersecting `(23)=w₂c−ab` pole is normal crossing after first taking `a=b=0` at generic `w₂≠0`, so the residue order is explicit.

The earlier `14×14` transverse target/fibre Jacobian certifies the contour meets the six-dimensional ambient fibre discretely on four exact sheets; the preceding image-interior examples show its targets need not be image-boundary points. Identifying the sixfold **source** residue with the complete image canonical form would still require a justified fibre-contour/global-residue theorem and all other source contributions. This calculation supplies the local orientation-normalized input for that comparison.

Checker: `research/nima/checkers/check_nine_point_loop_canonical_residue.py`; result: `research/nima/results/nine-point-loop-canonical-residue.json`.
