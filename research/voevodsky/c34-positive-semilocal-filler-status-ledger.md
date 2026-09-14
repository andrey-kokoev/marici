# `C_34` positive semilocal filler status ledger

## Purpose

This ledger supersedes informal status summaries for the positive semilocal `C_34` construction. It separates:

1. exact finite-cutoff projection algebra;
2. analytic results on the Bruhat--Schwartz core;
3. source-normalization assumptions;
4. claims explicitly withdrawn by later audits.

## Exact finite-cutoff algebra

### Four-leg projection dilation

For Tate and reference projections `Q_T,Q_0`,

\[
\Psi x
=
\frac1{\sqrt2}
(Q_Tx,
(I-Q_T)x,
Q_0x,
(I-Q_0)x)
\]

satisfies

\[
\boxed{
\Psi^*\Psi=I,
\qquad
\Psi^*J_4\Psi
=Q_T-Q_0.
}
\]

Status: **exact**.

### Eight-leg ordered-placement dilation

Doubling in the observer-placement coordinate gives a positive feature with readouts

\[
\boxed{
\frac12
(P\Delta Q+
\Delta QP)
}
\]

and

\[
\boxed{
\frac1{2i}
[P,
\Delta Q].
}
\]

Status: **exact**.

### Hadamard common/difference rotation

With

\[
C
=
\frac12(F_T+F_0),
\qquad
D
=
\frac12(F_T-F_0),
\]

one has

\[
\boxed{
C^*C+D^*D=I,
}
\]

\[
\boxed{
C^*J_2D+D^*J_2C
=Q_T-Q_0,
}
\]

\[
\boxed{
D^*D
=
\frac12
(Q_T-Q_0)^2.
}
\]

Status: **exact**.

### Dyadic refinement

Every projection/complement row admits sign-preserving dyadic defect splitting. Transition maps satisfy

\[
\boxed{
R_n^*R_n=I,
\qquad
R_n^*J_{n+1}R_n=J_n.
}
\]

Status: **exact functional calculus**.

### Halmos typing

The inside and outside generic contractions are unitarily equivalent through the polar part of `(I-P)QP`. Exact atoms are:

\[
P_{\{1\}}(PQP)
=P_{H_{11}},
\]

\[
P_{\{1\}}((I-P)(I-Q)(I-P))
=P_{H_{00}}.
\]

The standard Sonin space is `H_00`, not `H_11`.

Status: **exact projection-pair algebra**.

## Executable algebra audit

The checker

`research/voevodsky/checkers/check_relative_c34_positive_dilation.py`

verifies on an explicit noncommuting projection pair:

- four-leg isometry and signed readout;
- Hadamard identities;
- eight-leg Hermitian and skew placements;
- first dyadic defect split.

Materialized result:

`research/voevodsky/checkers/relative-c34-positive-dilation-v1.json`

Result: **passed**, maximal residual below `4e-16`.

## Exact cutoff covariance

For common cutoff phase

\[
U_L
=M_{e^{2iLs}},
\]

\[
\Delta Q_L
=U_L\Delta Q_0U_L^*.
\]

Observer Mellin multipliers commute with `U_L`, so the recentered difference row is exactly stationary:

\[
\boxed{
(U_L\oplus U_L)^*
D_LM_mU_L
=D_0M_m.
}
\]

Status: **exact characterwise identity**.

## Exact physical-regulator alignment

The physical cutoff, Fourier cutoff, observer, and finite regulator can be transported by the characterwise unitary `mathcal U_chi`. The transported outer regulator is

\[
\widetilde Z
=
\mathcal U_\chi
Z^{physical}
\mathcal U_\chi^*.
\]

Finite trace identities are preserved without replacing `widetilde Z` by a convenient Mellin window.

Status: **exact unitary transport**, conditional only on using the declared source carrier and character decomposition.

## Analytic trace-ideal results

### Difference row

For a regular Tate phase with polynomially controlled derivatives and a Schwartz observer,

\[
\Delta Q_0M_m
\in
\mathcal S_2.
\]

Hence the recentered Hadamard difference row is Hilbert--Schmidt.

Status: **proved by divided-difference kernel estimate on the stated core**.

### Two-sided relative operator

After two-sided Schwartz localization,

\[
M_{m_h}^*
\Delta Q_0
M_{m_g}
\in
\mathcal S_1.
\]

The same holds for the ordered Hardy placement under the stated Sobolev/smoothing assumptions.

Status: **proved by Schwartz-kernel/harmonic-oscillator factorization**, with endpoint index split off.

### Outer-regulator removal

For trace-class localized operators and strongly exhausting transported projections,

\[
\widetilde Z_RT\widetilde Z_R
\to T
\]

in trace norm.

Status: **standard trace-ideal theorem; proved by finite-rank approximation**.

### Placement commutator

Moving the translated Hardy projection outside the observer sandwich leaves

\[
\mathcal C_L(g,h)
=
\operatorname{Tr}
([M_{m_h}^*,\Pi_L]
\Delta Q_0M_{m_g}).
\]

Both factors are Hilbert--Schmidt. Their kernel pairing is `L1` and acquires modulation `exp(-2iL(s-t))`. Riemann--Lebesgue gives

\[
\boxed{
\mathcal C_L(g,h)
\to0.
}
\]

Status: **proved under the stated Schwartz/characterwise Hilbert--Schmidt hypotheses**.

## Tate boundary identification

The uncompressed localized relative projection trace is

\[
\boxed{
\operatorname{Tr}_{rel}
(M_{m_h}^*
\Delta Q_0
M_{m_g})
=
\frac1{2\pi i}
\int
\overline{m_h}
m_g\partial_s\log\gammads
+
e_{end}(g,h).
}
\]

The local Tate distribution identity identifies its angular sum with `W_S(g*h*)`.

Status: **standard relative projection/Tate identity**, requiring exact source normalization and endpoint branch convention.

Combined with placement-commutator decay, the ordered Hermitian eight-leg readout has the same boundary form; the skew readout tends to zero.

Status: **proved in the iterated regulator order once the standard Tate identity is admitted**.

## Mellin normalization

With Plancherel measure `ds/(2pi)`, the cutoff phase derivative gives

\[
\boxed{
\frac L\pi
\sum_\chi
\int|m_{g,\chi}|^2ds
=2Lh(1).
}
\]

Thus the Hardy spectral-flow coefficient matches Connes's `2 log Lambda h(1)` term for `L=log Lambda`.

Status: **exact normalization calculation**, with orientation selected accordingly.

## Conductor filtration

Ramified epsilon factors contribute

\[
w_{v,\chi}^{cond}
=\pm f(\chi)\log q_v.
\]

No uniform Plancherel semibound exists over unrestricted conductor. At conductor budget `F`, common-edge positivity requires schematically

\[
\log\Lambda
\ge
F+C_S.
\]

The admissible `(L,n,F)` region is directed, and conductor projections commute with the Tate multiplier and boundary legs.

Status: **exact filtration geometry plus standard epsilon-factor dependence**; constants/sign require source convention.

## Relative positive completion

The completed object is the tuple

\[
\boxed{
\mathfrak F_{34,S}
=(C_S,D_S,J_2,\operatorname{Tr}_{rel})
}
\]

with ordered-placement doubling when matching Connes's product.

It has:

1. ordinary positivity at every finite regulator;
2. a bounded common module row;
3. a Hilbert--Schmidt difference row;
4. a trace-class cross readout;
5. exact cutoff recentering of the difference row;
6. strict dyadic and conductor refinement.

Status: **constructed**.

## Norm-limit obstruction

The four-leg feature is isometric, so raw eight-leg norms preserve divergent source volume. Therefore raw positive legs do not converge strongly as the outer regulator is removed.

Status: **exact no-go**.

The correct terminal type is relative/pro-Hilbert, not an ordinary finite-norm Hilbert feature.

## Feature-slot count

At finite dyadic depth `n`, the formal slot count is

\[
\boxed{
8(n+1).
}
\]

The complete microscopic carrier is countable. Slots are parallel feature summands, not simplicial edge nodes.

Status: **exact presentation count**.

No final edgewise tetrahedron count is defined.

## Withdrawn claims

The following claims are explicitly withdrawn:

1. bare semilocal transition traces are finite;
2. the exact eigenvalue-one atom of `PQP` is the Sonin sector;
3. the projection meet alone is the full asymptotic near-one bulk;
4. extremal eigenvalue depth sets the boundary-effective depth;
5. hard and soft bulk removal are automatically equivalent;
6. raw dyadic residual legs converge to `|A_S|` after only volume removal;
7. the pure translated Hardy strip is the first generic dyadic defect;
8. a bare transition Cauchy--Schwarz estimate proves `O(sqrt(log Lambda))` sewing;
9. strong convergence of the translated Hardy projection passes through observer multiplication without a commutator;
10. trace-class membership alone makes the left-compressed trace equal the uncompressed projection-pair trace.

## Remaining stronger questions

The relative `C_34` filler does not answer:

1. simultaneous rather than iterated `(L,R,N)` convergence;
2. a minimal ordinary Hilbert realization with Gram `|A_S|`;
3. source-derived positive common-bulk quotient uniform in conductor;
4. observer-weighted Landau--Widom laws for physical generic-angle modes;
5. a finite ordinary edgewise subdivision count;
6. positivity of the Weil form.

These are stronger than existence of the regulator-relative positive filler.

## Current disposition

Within the Bruhat--Schwartz observer core and iterated regulator order, the positive semilocal `C_34` construction is complete as a relative positive feature:

\[
\boxed{
\text{finite positive dilation}
+
\text{stationary Hilbert--Schmidt difference}
+
\text{trace-class cross boundary}
+
\text{strict filtered refinement}.
}
\]

Its signed boundary observation is the Tate logarithmic-derivative/Weil form, while its raw common positive row remains regulator-relative and volume divergent.
