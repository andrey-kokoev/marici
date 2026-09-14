# Two-sided Schwartz localization makes the regular relative Hardy kernel trace class

## Regular phase assumptions

Fix one angular character `chi` and cutoff `L`. Write

\[
\sigma_{L,\chi}(s)
=e^{2iLs}
\gamma_\chi(s).
\]

After separating endpoint/winding jumps, assume the regular phase satisfies:

1. `gamma_chi` is smooth and unimodular on the real axis;
2. every derivative has polynomial growth:
   \[
   |\partial_s^k\gamma_\chi(s)|
   \le
   C_{k,\chi}
   (1+|s|)^{d_k};
   \]
3. observer Mellin coefficients `m_(g,chi)` and `m_(h,chi)` are Schwartz.

These are the standard regular Tate-symbol conditions on a fixed character sector away from explicitly extracted poles/index channels.

## Relative Hardy projection kernel

Let

\[
Q_\sigma
=M_\sigma
\Pi
M_\sigma^*.
\]

The distribution kernel of `Q_sigma` differs from that of `Pi` by cancellation of the diagonal delta term. Off the diagonal,

\[
\boxed{
(Q_\sigma-\Pi)(s,t)
=
\frac1{2\pi i}
\frac{
\sigma(s)
\overline{\sigma(t)}-1
}{s-t}.
}
\]

Because `|sigma|=1`, the numerator vanishes at `s=t`. The quotient extends smoothly across the diagonal with value proportional to

\[
\partial_s
\log\sigma(s).
\]

For the Tate/reference difference after common translation,

\[
\Delta Q_L
=Q_{e^{2iLs}\gamma}
-Q_{e^{2iLs}},
\]

the same cancellation gives a smooth divided-difference kernel whose derivatives have polynomial growth for fixed `L,chi`.

## Two-sided observer localization

Define

\[
\boxed{
T_{L,\chi}^{regular}(g,h)
=
M_{m_{h,\chi}}^*
\Delta Q_L^{regular}
M_{m_{g,\chi}}.
}
\]

Its kernel is

\[
\boxed{
K_{g,h}(s,t)
=
\overline{m_{h,\chi}(s)}
\Delta q_{L,\chi}^{regular}(s,t)
m_{g,\chi}(t).
}
\]

A polynomially bounded smooth divided difference multiplied by Schwartz functions in both variables is a Schwartz function on `R^2`:

\[
\boxed{
K_{g,h}
\in
\mathcal S(\mathbb R^2).
}
\]

All weighted mixed derivatives lie in `L2(R^2)`.

## Trace-class lemma for Schwartz kernels

Let `T_K` be the integral operator with Schwartz kernel `K(s,t)`. Let

\[
H_{osc}
=-\partial_s^2+s^2
\]

be the one-dimensional harmonic oscillator and set

\[
D
=1+H_{osc}.
\]

The inverse `D^(-1)` is Hilbert--Schmidt because its eigenvalues have order `1+n`:

\[
\boxed{
D^{-1}
\in
\mathcal S_2.
}
\]

Since `K` is Schwartz, the operator

\[
DT_KD
\]

has a Schwartz kernel and is bounded, indeed Hilbert--Schmidt. Factor

\[
\boxed{
T_K
=D^{-1}
(D T_KD)
D^{-1}.
}
\]

The product of two Hilbert--Schmidt operators with a bounded middle factor is trace class. Hence

\[
\boxed{
T_K
\in
\mathcal S_1.
}
\]

Moreover,

\[
\boxed{
\|T_K\|_1
\le
\|D^{-1}\|_2^2
\|D T_KD\|.
}
\]

The final norm is bounded by finitely many weighted `L2` seminorms of `K`.

## Application to the relative kernel

The Schwartz-kernel lemma gives

\[
\boxed{
M_{m_h}^*
\Delta Q_L^{regular}
M_{m_g}
\in
\mathcal S_1
}
\]

for every fixed `L,chi` and every Schwartz observer pair.

Thus strongly convergent transported outer regulators may be removed in trace norm for this symmetric relative projection placement.

## Additional left Hardy projection

The exact ordered product contains

\[
M_{m_h}^*
\Pi
\Delta Q_L^{regular}
M_{m_g}.
\]

The Hardy projection is a zeroth-order singular integral bounded on every Sobolev space. Composition by `Pi` on the left preserves smoothing after two-sided Schwartz localization in the following sense:

\[
D
M_{m_h}^*
\Pi
\Delta Q_L^{regular}
M_{m_g}
D
\]

is bounded. This follows by commuting `D` through the left Schwartz multiplier, using Sobolev boundedness of `Pi`, and using arbitrarily high weighted Sobolev regularity of `Delta Q M_(m_g)`.

Therefore the same factorization yields

\[
\boxed{
M_{m_h}^*
\Pi
\Delta Q_L^{regular}
M_{m_g}
\in
\mathcal S_1.
}
\]

This is the exact Schatten condition required by the transported-regulator lemma.

## Unequal regulator placements

At finite physical regulator, cyclicity may produce different left and right observer factors. The argument only requires each side to be Schwartz/smoothing in its own variable. Equality of the two multipliers is unnecessary.

Hence polarized observer pairs and transported left/right regulator placements are covered by the same kernel criterion.

## Trace evaluation

Since the regular localized operator is trace class, its trace is the integral of its continuous diagonal kernel:

\[
\operatorname{Tr}
T_{L,\chi}^{regular}(g,h)
=
\int_\mathbb R
K_{g,h}(s,s)ds.
\]

The diagonal divided difference is the logarithmic derivative anomaly. Therefore

\[
\boxed{
\operatorname{Tr}
T_{L,\chi}^{regular}(g,h)
=
\frac1{2\pi i}
\int
\overline{m_{h,\chi}(s)}
m_{g,\chi}(s)
\partial_s
\log\gamma_\chi(s)ds
}
\]

with orientation-dependent sign.

The common exponential derivative cancels between Tate and reference projections.

## Endpoint/index channel

If `gamma_chi` has winding, a branch jump, or a pole crossing associated with the endpoint normalization, split

\[
\boxed{
\Delta Q_L
=
\Delta Q_L^{regular}
+
\Delta Q_L^{index}.
}
\]

The index part is a finite-rank spectral-flow projection or a separately declared endpoint graph channel. It is trace class after observer localization and contributes

\[
e_{end,\chi}(g,h).
\]

The Schwartz-kernel argument applies to the regular part; finite rank handles the index part.

## Angular/conductor assembly

A Bruhat--Schwartz observer at each finite place is invariant under some compact open subgroup. Its angular transform therefore has finite conductor support. For each fixed observer pair, only finitely many ramified character sectors contribute.

At archimedean places there are finitely many parity sectors, and the Mellin functions are Schwartz in `s`.

Hence on the ordinary Bruhat--Schwartz observer core,

\[
\boxed{
\sum_\chi
\|T_{L,\chi}(g,h)\|_1
<\infty
}
\]

without requiring a global uniform bound over all conductor levels.

For larger smooth completions with infinite angular support, rapid character decay plus polynomial seminorm bounds gives the corresponding dominated sum.

## Transported-regulator removal

Let

\[
\widetilde Z_{R,\chi}
\xrightarrow[s]{R\to\infty}
I.
\]

Trace-class localization now gives

\[
\boxed{
\widetilde Z_{R,\chi}
T_{L,\chi}(g,h)
\widetilde Z_{R,\chi}
\longrightarrow
T_{L,\chi}(g,h)
}
\]

in trace norm.

After finite/summable angular assembly,

\[
\boxed{
\lim_{R,N}
\operatorname{Tr}
(\widetilde Z_{R,N}
T_{L,S}(g,h)
\widetilde Z_{R,N})
=
\sum_\chi
\operatorname{Tr}
T_{L,\chi}(g,h).
}
\]

Thus the exact transported outer regulator disappears without needing to know its Mellin geometry.

## Dependence on `L`

For each fixed `L`, derivatives of the exponential phase contribute finite powers of `L` to Schwartz seminorm estimates. This is enough for the iterated order

\[
R,N\to\infty
\quad
\text{before}
\quad
L\to\infty.
\]

A simultaneous diagonal limit requires estimates uniform in `L`; this note does not claim them.

The projection-pair trace after reference subtraction is independent of `L`, but the trace norm of a chosen kernel representation need not be uniformly bounded in `L`.

## Exact scope

The proof applies when:

1. endpoint/index singularities are split off;
2. the regular gamma phase is smooth with polynomial derivative bounds;
3. observer Mellin factors are Schwartz in the radial variable;
4. regulator limits are taken in the iterated order;
5. the left Hardy projection is handled on the declared Sobolev core.

These conditions match the standard Bruhat--Schwartz semilocal observer domain.

## Disposition

For each fixed cutoff, character, and Bruhat--Schwartz observer pair,

\[
\boxed{
M_{m_h}^*
\Pi
(Q_{L,\chi}^T-Q_L^0)
M_{m_g}
\in
\mathcal S_1
}
\]

after separating the finite endpoint/index channel. Therefore exact transported outer regulators converge in trace norm, angular assembly is finite/summable on the observer core, and the relative trace equals the Tate logarithmic-derivative pairing. The remaining limitations concern simultaneous cutoff/regulator limits and physical generic-angle refinement, not iterated `C_34` regulator convergence.
