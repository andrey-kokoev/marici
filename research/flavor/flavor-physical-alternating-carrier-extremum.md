# The physical alternating carrier does not select observed CP

Work package: WP611  
Owner: marici.Figueiredo

## Faithful alternating carrier

For ordered nondegenerate Yukawa spectral projectors, the elementary
CP-sensitive quartet is

\[
\Omega_{ij;kl}=\operatorname{Im}
\operatorname{Tr}(P_i^uP_j^dP_k^uP_l^d).
\]

For distinct adjacent indices it equals the Jarlskog invariant (J), up to
the fixed ordering sign. It is invariant under common weak-basis conjugation
and has a charged-current CP-asymmetry instrument. This is the natural
physical alternating carrier on `physical16`.

It is not the same object as a formal alternating tensor on three abstract
port labels. It contains relative quantum phases and requires four spectral
projectors.

## Failure on exact matching support

For any permutation-valued spectral overlap, paired up and down projectors
coincide and all mixed projector quartets are real. Therefore

\[
J=0.
\]

The physical alternating carrier vanishes on both (P_+) and (P_+^T). It
cannot distinguish the two exact WP609 matching presentations or supply the
missing orientation while those supports are retained.

## Coefficient-free extremum audit

In the standard three-angle parametrization,

\[
J=s_{12}c_{12}s_{23}c_{23}s_{13}c_{13}^2\sin\delta.
\]

The first two sine-cosine products are at most (1/2). Writing
(x=s_{13}^2), the remaining squared factor is (x(1-x)^2), whose maximum
is (4/27) at (x=1/3). Hence

\[
J^2\le {1\over108}.
\]

Fourier mixing saturates this bound. The two coefficient-free monotone uses
of the carrier therefore select only endpoints:

- minimizing (J^2) selects the CP-conserving locus;
- maximizing (J^2) selects maximally democratic CP violation.

Neither describes the fitted flavor domain. All 1,210 stored sheets have
nonzero (J), while every sheet is far below the maximal value.

## Interior selection requires new source information

A potential such as

\[
V=(J^2-c)^2
\]

has an interior minimum at (J^2=c). But the number (c) is precisely the
missing source prediction. Reading it from the fitted ensemble would encode
the desired answer. The alternating carrier distinguishes CP-sensitive
physical points; it does not determine which nonzero magnitude nature should
choose.

This preserves the selector/readout distinction:

- (Omega) is a faithful physical readout and probe;
- an independently derived action involving (Omega) could become a
  selector;
- the carrier alone is not that action.

## Experimental criticism

Charged-current CP asymmetries already provide an independently executable
test. They falsify both endpoint laws: observed nonzero (J) rejects the
minimum, and strongly nonmaximal (J) rejects universal maximization.

Any new alternating mediator channel must be separately resolved and matched
to the same projector ports. Inferring it from the already measured (J)
would not establish a source operation. Its prediction must include an
independently fixed interior scale and survive the complete fitted ensemble.

## Disposition

Nima's alternating-carrier requirement is correct at the relational level,
but its faithful flavor realization adds a new obstruction. The physical
carrier vanishes on exact matching supports, and its coefficient-free extrema
miss observed flavor. A successful architecture must relax permutation
support and derive an interior CP scale from additional dynamics or geometry.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp611_physical_alternating_carrier_extremum.py

The generated result is
research/flavor/results/wp611_physical_alternating_carrier_extremum.json.
