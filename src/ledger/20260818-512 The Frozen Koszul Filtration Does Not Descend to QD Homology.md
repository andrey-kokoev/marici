# The Frozen Koszul Filtration Does Not Descend to QD Homology

The authoritative finite census of commit `56fa6a9` was extended without
changing its target basis, source basis, orbit completion, plus projection, or
whole-column cutoff.  Let

\[
I_D=\langle\widehat H(A_D),E(P_D)\rangle\subset G_D,
\qquad Q_D=G_D/I_D,
\]

and use the frozen gradient

\[
(K_a,K_b,K_u)=(4a^3,0,a^2(1-b^2)).
\]

For the elementary Koszul columns

\[
s_{ab}=(-K_b,K_a,0),\quad
s_{bu}=(0,-K_u,K_b),\quad
s_{au}=(-K_u,0,K_a),
\]

define `S0` from the first two and `S1=S0+<s_au>`, with all monomial
multiples admitted by the census convention.  The necessary cycle condition
for their images to define a filtration on `H(Q_D,u)` is

\[
uS_i\subset I_D.
\]

It fails by the following exact rank increments:

\[
\begin{array}{c|cc}
D&\operatorname{rk}(I_D+uS_0)-\operatorname{rk}I_D&
\operatorname{rk}(I_D+uS_1)-\operatorname{rk}I_D\\\hline
12&15&22\\
16&21&32\\
20&27&42\\
24&33&52
\end{array}
\]

The laws on the tested stable range are `3D/2-3` and `5D/2-8`.
Consequently the proposed `F0 subset F1` is not typed on dual-number
homology.

As a secondary diagnostic only, ignoring the cycle failure gives formal rank
triples

\[
(5,20,6),\ (7,42,8),\ (9,72,10),\ (11,110,12),
\]

for `(F0,F1/F0,H/F1)`.  In particular the untyped residual is `D/2`, not
one.  Thus neither the actual homological construction nor its formal shadow
supports the proposed two-triangles-plus-one removal.

The next admissible step is not to quotient these elementary syzygies.  One
must derive corrected `u`-closed Koszul representatives from the labelled
principal-gradient total complex, or prove that no such correction exists.
