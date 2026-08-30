# Two-adjoint gauge-clock obstruction (WP433)

## Candidate constructor

WP432 identifies flavor gauge Higgsing as the closest conditional route to a
mediator-to-clock relation. WP128 already contains two Hermitian fields (A,D)
transforming in the adjoint of the shared (U(3)_Q) flavor group. Gauging that
group gives the gauge-boson mass quadratic form

$$
G_{ab}=g_F^2\left(
\operatorname{Tr}[T_a,A]^\dagger[T_b,A]
+\operatorname{Tr}[T_a,D]^\dagger[T_b,D]
\right).
$$

This relation is source-derived from the adjoint kinetic terms. It descends
under simultaneous weak-basis conjugation and supplies a genuine candidate
spectral shape.

## Exact central kernel

The central generator (T_0=I_3) commutes with every adjoint background:

$$
[I_3,A]=[I_3,D]=0.
$$

Consequently the (U(1)) gauge direction is an exact zero mode of (G) for
all choices of the two adjoints. No potential, vacuum alignment, or numerical
fit involving only conjugation adjoints can remove it. The center acts
trivially on these fields.

An exact generic benchmark demonstrates that this is the only algebraic
breaking defect rather than a failure of the nonabelian construction. For

$$
A=\operatorname{diag}(0,1,3),
\qquad
D=\begin{pmatrix}2&1&1\\1&-1&1\\1&1&0\end{pmatrix},
$$

the mass Gram has rank eight on the nine-generator (U(3)) basis, while its
restriction to the eight traceless generators has nonzero determinant and rank
eight. Thus a generic pair completely Higgses (SU(3)_Q) but never the central
(U(1)).

## Scale authority remains absent

Restricting the proposal to (SU(3)_Q) removes the central zero mode, but its
nonzero masses still scale as

$$
M_a^2=g_F^2 f^2 \lambda_a(\widehat A,\widehat D).
$$

The normalized adjoint shapes determine mass ratios; the continuous product
(g_F f) sets the absolute clock. WP128 supplies neither an independently
observed (g_F) nor a source-selected (f/v). Therefore the construction can
rigidify a spectral shape without selecting its absolute location.

## Additional theory obligations

Gauging the chiral quark flavor group also requires a separately declared
anomaly-free fermion content and Standard Model portal. Those obligations are
not inferred from the mass Gram and are not solved here. Adding a center-charged
fundamental or bifundamental scalar could Higgs the (U(1)), but it enlarges the
state domain and introduces another vacuum scale.

## Verdict and falsifier

The two WP128 adjoints provide a viable generic (SU(3)_Q) breaking shape, not
a complete observed flavor-gauge clock. For (U(3)_Q), the smallest exact
falsifier is any claimed full-rank mass Gram built only from commutators with
adjoint backgrounds; the identity row and column must vanish. Reopening
requires a center-charged field or an explicitly (SU(3)_Q)-only theory,
anomaly cancellation, and independent measurements or source laws fixing
(g_F f/v).

Run `uv run --with sympy python
research/flavor/checkers/wp433_two_adjoint_gauge_clock_obstruction.py` to
regenerate the JSON result.
