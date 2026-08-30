# Correction: the scalar seam boundary does not see off-seam reciprocal zero pairs

Event 10279 overstated the critical boundary of
\(\operatorname{Re}\zeta'/\zeta\) as the complete divisor current. That is
false without an additional transverse observable.

A zero

\[
\rho=\beta+i\gamma
\]

contributes locally

\[
\operatorname{Re}\frac1{\sigma+it-\rho}
=
\frac{\sigma-\beta}
{(\sigma-\beta)^2+(t-\gamma)^2}.
\]

If \(\beta=1/2\), the one-sided limit
\(\sigma=1/2+\varepsilon\), \(\varepsilon\downarrow0\), produces the expected
atomic seam contribution.

Now take an off-seam reciprocal pair at the same height,

\[
\rho_\pm=\frac12\pm d+i\gamma,
\qquad d>0.
\]

At the seam, their scalar real-part contributions are

\[
\frac{-d}{d^2+(t-\gamma)^2}
+
\frac{d}{d^2+(t-\gamma)^2}
=
0.
\]

Thus a reciprocal off-seam pair is completely invisible to the scalar seam
current.

## Exact consequence

The identity

\[
J_P=dS
\]

on the seam can hold whether or not off-seam reciprocal pairs exist. It
identifies the scalar argument current, not the complete divisor and not RH.

This is precisely the invisible-state mechanism that the polarized Green
programme was designed to prevent. The scalar explicit formula is a shadow
of the constructor, not a faithful zero observer.

## Transverse recovery

Let \(\varepsilon=\sigma-1/2\). The paired contribution is

\[
F_d(\varepsilon,x)
=
\frac{\varepsilon-d}{(\varepsilon-d)^2+x^2}
+
\frac{\varepsilon+d}{(\varepsilon+d)^2+x^2},
\qquad x=t-\gamma.
\]

Although

\[
F_d(0,x)=0,
\]

its first normal derivative is

\[
\partial_\varepsilon F_d(0,x)
=
2\frac{x^2-d^2}{(x^2+d^2)^2},
\]

which is nonzero. More robustly, the full two-sided \(\varepsilon\)-family
recovers the displaced poles at \(\varepsilon=\pm d\).

Therefore the complete divisor theorem requires either:

1. the polarized off-seam logarithmic-derivative family;
2. its normal jet with a proved faithfulness theorem;
3. or an equivalent two-sector Green/Birman–Schwinger observer.

A single seam boundary current is insufficient.

## Repair to the hierarchy

The corrected hierarchy is

\[
\text{finite prime currents}
\to
\text{dual-valued meromorphic family in }\sigma+it
\to
\text{polarized divisor identification}
\to
\text{seam restriction}.
\]

Restricting to the seam before divisor identification loses reciprocal
off-seam pairs.

The next executable theorem must retain \(\sigma\) as a genuine normal
coordinate and prove that the prime-side continuation agrees with the full
polarized logarithmic derivative. RH is then the statement that the
off-seam pole part is absent, rather than an inference from a seam current
that cancels it automatically.
