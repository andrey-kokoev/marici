# The compact-sandwich product limit is compatible with endpoint, conductor, and convolution-successor channels

## Regular and endpoint splitting

Write

\[
\Delta Q_0
=
\Delta Q_0^{\mathrm{reg}}
+
\Delta Q_0^{\mathrm{ind}},
\]

where the endpoint/index term is finite rank. Set

\[
H_g^{\mathrm{reg}}
=
\Delta Q_0^{\mathrm{reg}}M_{m_g},
\qquad
H_g^{\mathrm{ind}}
=
\Delta Q_0^{\mathrm{ind}}M_{m_g}.
\]

The phase-energy estimate gives \(H_g^{\mathrm{reg}}\in\mathcal S_2\). Since a bounded multiplier composed on the right of a finite-rank operator remains finite rank,

\[
H_g^{\mathrm{ind}}\in\mathcal S_2.
\]

For

\[
K_h=[M_{m_h}^*,\Pi]\in\mathcal S_2,
\]

the regular and index placement remainders are both compact sandwiches:

\[
R_L^{\mathrm{reg}}
=U_L^*K_hU_LH_g^{\mathrm{reg}},
\qquad
R_L^{\mathrm{ind}}
=U_L^*K_hU_LH_g^{\mathrm{ind}}.
\]

Weak decay of \(U_L\) therefore gives

\[
\|R_L^{\mathrm{reg}}\|_1
+
\|R_L^{\mathrm{ind}}\|_1
\longrightarrow0.
\]

Thus the endpoint channel does not require a separate oscillatory argument. Its finite rank is stronger than the required Hilbert--Schmidt hypothesis.

## Conductor restrictions

Let \(Z_F\) be a conductor projection. Radial Mellin modulation is independent of angular character and hence

\[
[Z_F,U_L]=0.
\]

The Tate/reference projection pair is block diagonal in angular characters, so

\[
[Z_F,\Delta Q_0]=0.
\]

Restricting the compact sandwich gives

\[
Z_FR_LZ_F
=
U_L^*(Z_FK_hZ_F)U_L(Z_FH_gZ_F).
\]

Orthogonal compression does not increase Hilbert--Schmidt norm. Therefore every finite conductor level inherits the same trace-norm convergence.

On the Bruhat--Schwartz core, the finite-place angular transform has finite conductor support, so conductor assembly is finite. For an infinite smooth completion, it is enough that

\[
\sum_\chi
\|K_{h,\chi}\|_2
\|H_{g,\chi}\|_2
<\infty.
\]

Then

\[
\sum_\chi\|R_{L,\chi}\|_1\to0
\]

by dominated convergence.

## Convolution successors

For semilocal convolution, Mellin transformation changes convolution into multiplication:

\[
m_{g_1*g_2,\chi}(s)
=
m_{g_1,\chi}(s)m_{g_2,\chi}(s).
\]

The Schwartz class is an algebra. Consequently convolution successors retain:

1. radial Schwartz decay;
2. rapid angular decay;
3. the Hardy commutator condition;
4. finite observer-weighted Tate phase energy.

For bounded observer packets, standard Schwartz seminorm estimates give

\[
p_{M,K}(g_1*g_2)
\le
C_{M,K}
\sum_{M_1+M_2\le M\atop K_1+K_2\le K}
p_{M_1,K_1}(g_1)p_{M_2,K_2}(g_2).
\]

Thus the Hilbert--Schmidt majorants for \(K_h\) and \(H_g\), and hence their summable product majorant, are stable under convolution successors.

## Pullback functoriality

All operations used in the limit commute with the declared block restrictions:

- unitary Mellin transport;
- angular and conductor projection;
- regular/index direct sum;
- observer multiplication;
- finite-rank endpoint inclusion.

Therefore the limiting product is natural under restriction:

\[
Z_F
\left(
\lim_{L\to\infty}^{\mathcal S_1}T_L(g,h)
\right)
Z_F
=
\lim_{L\to\infty}^{\mathcal S_1}
Z_FT_L(g,h)Z_F.
\]

The same statement holds characterwise and after any summable angular direct sum.

## Completion statement

On the Bruhat--Schwartz observer core, and on bounded smooth packet completions satisfying the recorded angular majorants, the minimal product route is compatible with:

- the regular/index decomposition;
- endpoint finite-rank channels;
- conductor restriction and successor maps;
- convolution successors;
- angular direct sums.

Hence both semilocal sewing completion routes now have the required endpoint, conductor, bounded-packet, and convolution compatibility. The only remaining qualification is that the positive strong route completes the relative difference feature, not the divergent physical common row.
