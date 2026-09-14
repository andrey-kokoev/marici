# All split-bitangent differences form one norm-minus-six Weyl orbit

Let \(S=\operatorname{Bl}_7\mathbb P^2\), with

\[
K_S=-3H+E_1+\cdots+E_7.
\]

The 56 exceptional curves comprise

\[
7+21+21+7
\]

classes of the forms

\[
E_i,\quad H-E_i-E_j,\quad
2H-E_{i_1}-\cdots-E_{i_5},\quad
3H-2E_i-\sum_{j\ne i}E_j.
\]

For every exceptional curve \(C\), its Geiser partner is

\[
C'=-K_S-C.
\]

Hence the oriented component difference is

\[
d_C=C'-C=-K_S-2C.
\]

This immediately gives the universal congruence

\[
\boxed{d_C\equiv-K_S\pmod{2\operatorname{Pic}(S)}}.
\]

The exact enumeration further verifies

\[
d_C^2=-6,
\qquad
K_S\cdot d_C=0,
\]

and every \(d_C\) is primitive.

Using the standard seven simple reflections

\[
E_1-E_2,\ldots,E_6-E_7,
\qquad H-E_1-E_2-E_3,
\]

the reflection graph on the 56 exceptional curves is connected. Since the Geiser involution commutes with the Weyl action, the 56 oriented differences form one \(W(E_7)\)-orbit. Identifying \(d\sim-d\) yields the 28 bitangent pairs.

The stabilizer has order

\[
\frac{|W(E_7)|}{56}
=\frac{2903040}{56}
=51840
=|W(E_6)|.
\]

Thus C5 and C6 are confirmed:

1. every split-bitangent difference has the canonical mod-two class \(-K_S\);
2. every such primitive norm-\(-6\) difference belongs to one Weyl orbit, with stabilizer of type \(E_6\).

Certificate:

- `research/voevodsky/checkers/bitangent_difference_mod2_weyl_orbit.py`;
- `research/voevodsky/results/bitangent_difference_mod2_weyl_orbit.json`.
