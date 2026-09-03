# Normalized parity defects bound route coherence, not scale

## Question

What scale-free overlap bound follows from normalized parity defects, and can any such defect threshold imply strict return without absolute route-load control?

## Normalized defects

For nonzero route amplitudes define

\[
\eta_+=\frac{\|(U-I)b_+\|}{\|b_+\|},
\qquad
\eta_-=\frac{\|(U+I)b_-\|}{\|b_-\|}.
\]

Both lie in \([0,2]\). Dividing the sharp parity-defect estimate by \(\|b_+\|\|b_-\|\) gives

\[
\frac{|\langle b_+,b_-\rangle|}{\|b_+\|\|b_-\|}
\le
\frac12\left(
\eta_-\sqrt{1-\eta_+^2/4}
+
\eta_+\sqrt{1-\eta_-^2/4}
\right).
\]

Writing

\[
\eta_+=2\sin\alpha,
\qquad
\eta_-=2\sin\beta,
\qquad
0\le\alpha,\beta\le\frac{\pi}{2},
\]

turns the right-hand side into \(\sin(\alpha+\beta)\). It ranges from zero to one and is attained by aligned same-parity components.

## Saturation

For

\[
b_+=(4,3),
\qquad
b_-=(5,12),
\]

the normalized defects are \(6/5\) and \(10/13\), and both the coherence ratio and the bound equal \(56/65\).

For

\[
b_+=b_-=(4,3),
\]

the normalized defects are \(6/5\) and \(8/5\); the coherence ratio and bound both equal one. Hence nonzero defect data need not imply any coherence suppression.

## Scale hostile

Under simultaneous scaling

\[
b_+\mapsto s b_+,
\qquad
b_-\mapsto s b_-,
\]

both normalized defects and the coherence ratio remain unchanged, while every Gram entry and its largest eigenvalue scale by \(s^2\). Therefore no threshold expressed only through \(\eta_+,\eta_-\) can imply strict return.

Even exact parity, \(\eta_+=\eta_-=0\), only makes the Gram matrix diagonal. Its diagonal route loads can still exceed one.

## Operational composition

The normalized formula is useful as a coherence factor

\[
C\le \gamma\sqrt{UV},
\]

where \(\gamma\) is its right-hand side. The route-Gram certificate still requires absolute load bounds \(U,V\). Normalized parity information controls route alignment, not total return magnitude.

## Verification

`research/aspect/checkers/check_normalized_parity_overlap.py` verifies intermediate and unit-coherence saturation and a scale hostile using exact rational vectors.

## Disposition

The scale-free parity question is completely classified. Absolute physical route normalization is an irreducible input to strict confinement; normalized symmetry defects cannot replace it.
