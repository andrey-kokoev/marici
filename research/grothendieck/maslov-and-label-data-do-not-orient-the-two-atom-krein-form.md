# Maslov and Label Data Do Not Orient the Two-Atom Krein Form

## Smallest amplitude hostile

Retain two positive source atoms at fixed positions (u_1<u_2), with positive amplitudes (w_1,w_2). Fix (y>0) and choose the frequency so that

\[
x(u_2-u_1)=\pi.
\]

The cosine of the cross separation is then (-1). Half of the two-sector Krein form is

\[
\frac{J}{2}
=
a w_1^2+b w_2^2-2c w_1w_2,
\]

where

\[
a=\sinh(2yu_1),
\qquad
b=\sinh(2yu_2),
\qquad
c=\sinh(y(u_1+u_2)).
\]

The determinant is negative:

\[
ab-c^2<0.
\]

Hence the form is indefinite even though both source amplitudes are positive.

## Exact amplitude-ratio gate

Put (r=w_2/w_1). The orientation is negative precisely between the two roots

\[
r_\pm
=
\frac{c\pm\sqrt{c^2-ab}}{b}.
\]

Thus the same two labels, positions, affine origin, reciprocal sector action, center phase, and Maslov grade admit both Krein signs. Only the amplitude ratio changes.

For the explicit geometry

\[
u_1=1,
\qquad
u_2=2,
\qquad
y=\frac15,
\qquad
x=\pi,
\]

positive ratios exist on both sides of the sign boundary.

## Consequence

Neither labelled support nor metaplectic crossing data orients the physical boundary form. The exact theta coefficients are load-bearing. A successful source theorem must constrain amplitudes and phases together, not merely count crossings or preserve label order.

This gives a sharper target than generic modularity:

1. derive the exact amplitude ratio transported between every potentially negative label pair;
2. compare it with the local forbidden interval ((r_-,r_+));
3. retain all cross-label contributions when more than two atoms interact;
4. identify a modular recursion that prevents the completed coefficient vector from entering the global negative cone;
5. test the same law on hostile self-dual sources with altered amplitudes.

## Scope boundary

The two-atom hostile does not show that the actual theta amplitudes enter a negative interval. It proves that every theorem using only support, positivity, affine origin, reciprocal symmetry, or Maslov grade is insufficient.

The remaining source law must be coefficient-sensitive. This aligns with the broader Marici rule that meaning and comparison live in typed coefficients, not merely in carrier geometry.

## Verification

The checker `research/grothendieck/checkers/two_label_krein_amplitude_gate.py` verifies indefiniteness, computes the forbidden amplitude-ratio interval, and exhibits positive-amplitude choices of both Krein signs on one fixed geometry.
