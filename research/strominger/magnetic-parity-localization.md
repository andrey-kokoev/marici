# Odd magnetic transport localizes to its endpoints

Stable support cycles behave differently in the two reflection parities.

Let `a=2k` be the newly admitted pole depth.  The minus Hall endpoint has
weight

\[
e_-=(-1)^{g+1}(a+g+q-1)a^{\overline g}.
\]

For odd `q`, the plus Hall endpoint has weight

\[
e_+=(-1)^g(a+g-q-1)a^{\overline g}.
\]

Their product is exactly the stable determinant character:

\[
e_-e_+
=-(a^{\overline g})^2
 (a+g-q-1)(a+g+q-1).
\]

Thus odd-depth alternating cycles are present in the support graph but become
determinant-invisible after elimination.  No internal state survives in the
exterior character.

For even `q`, the selected plus endpoint is the adjacent coefficient `-B1`.
Writing

\[
X=g(a-4)(m_++1)+(a+g-1)(m_+-g),
\qquad m_+=1-g+q-a,
\]

the stable character satisfies

\[
R_{g,q}(a)=e_-e_+\frac{qg(g+3)}{X}.
\]

The correction is not identically one.  Even-depth cycles therefore carry a
genuine Schur response, although the final determinant still compresses to a
scalar character.

This parity split explains the grade-two `q=7` exception particularly cleanly.
It occurs when the odd plus-endpoint factor vanishes:

\[
a+g-q-1=0
\quad\text{at}\quad(a,g,q)=(6,2,7).
\]

But an odd stable step has `a>=q+3`, hence

\[
a+g-q-1\ge g+2>0.
\]

The exceptional circuit is therefore forced to be an initialization event;
it cannot recur after stable transport begins.

The endpoint identities are symbolic.  The equality with exact growing
determinant ratios is cross-checked for 350 stable steps with grades through 8
and depths through 11.
