# The Two-Prime Source Seams Satisfy an Exact Cocycle

## Translation current

For a positive shift length \(\ell\), define

\[
(T_\ell F)(u)=e^{-\ell/2}F(u+\ell).
\]

For \(\ell=\log p\), this is the independently derived prime Green repair
current of entry 3268. Distinct prime translations commute:

\[
T_\ell T_m=T_mT_\ell=T_{\ell+m}.
\]

## Transform and seam cell

Let

\[
\widehat F(z)=\int_0^\infty F(u)e^{zu}\,du,
\qquad
B_\ell(F;z)=\int_0^\ell F(u)e^{zu}\,du.
\]

Then

\[
\widehat{T_\ell F}(z)
=e^{-(z+1/2)\ell}
\bigl(\widehat F(z)-B_\ell(F;z)\bigr).
\]

The seams obey the exact cocycle

\[
B_{\ell+m}(F;z)
=B_\ell(F;z)
+e^{(z+1/2)\ell}B_m(T_\ell F;z).
\]

Interchanging \(\ell\) and \(m\) gives the other subdivision of the same
interval. Substitution shows that both sequential transforms equal

\[
e^{-(z+1/2)(\ell+m)}
\bigl(\widehat F(z)-B_{\ell+m}(F;z)\bigr).
\]

Thus the source/control part of the two-prime coherence tower closes with
identity transition.

## Scope correction

This is not yet the two-addition determinant cell. A joint colligation can
contain internal coupling, so the feedback increment assigned to the first
edge can depend on which label is eliminated first. Equality of source
translations and total seams does not imply equality of those edge
increments.

The output-tower gate must therefore be performed on one fixed joint
colligation:

1. eliminate \(p\) then \(q\);
2. eliminate \(q\) then \(p\);
3. eliminate the \((p,q)\) block jointly;
4. prove equality of the three determinant sections under one normalization;
5. only then compare that common section with the independently derived
   endpoint Evans section.

The final comparison, not the source seam cocycle, carries possible RH force.

