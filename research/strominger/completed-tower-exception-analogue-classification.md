# Physical analogues of towers, E1, and E2 are typed quotient phenomena

## Verdict

None of the named finite Laurent kernel vectors is constructed by the
source-derived completed puncture module. The completed physical engine does
contain three mechanisms that resemble them only after their types are stated:

1. a parity-projector family, one electric alias for every source jet;
2. declared Green/gauge/period zero modes at initialization or quotient;
3. collision-moment circuits whose primitive coefficients depend on tangent
   geometry.

They are not three instances of the old finite Laurent kernel mechanism.

## 1. Towers

The invariant centered point source has exterior support

\[
 m=2-a,\qquad a\geq4,
\]

with locked negative-binomial coefficients. The formal magnetic tower at
grade `g` lies on

\[
 m=-(g+a-1).
\]

These diagonals would intersect only if `g=-1`; therefore they are disjoint
for every physical `g>=2`. Moreover a nonzero finite coefficient sequence
cannot satisfy the source recurrence and terminate. Hence no magnetic tower
is a completed point-source state.

The physical replacement is the universal electric projector kernel

\[
 \mathcal H_{Q=+1}=\ker\Pi_M.
\]

It forms a source-jet family, but it is restored by the complementary electric
port and is not a zero of transport or of the magnetic principal symbol.

## 2. E1

The grade-two vector `E1=1-bar(z)^(-2)` is neither on the coherent source
support nor compatible with its recurrence. Its nearest physical analogues
are finite-dimensional initialization/quotient modes:

- the constant mode removed by normalized Laplacian inversion;
- the `l=0,1` scalar kernel of spin-two reconstruction;
- exact one-forms removed before contour periods;
- a one-chart determinant zero at `xi=0`, repaired by the other chart.

Only the first three are genuine physical quotients. The last is merely an
atlas boundary. None has the support or primitive vector of `E1`.

## 3. E2

The grade-two three-term circuit

\[
 E2=\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6}
\]

has no source preimage, and the magnetic grade-three symbol is injective on
every finite point-supported jet. Therefore no distinct-puncture or same-point
finite-jet transport circuit of `E2` type exists.

At a collision specialization, a truncated moment map can have the primitive
kernel `(1,-3,2)`. For tangent offsets `(0,1,3/2)`, it is forced by

\[
 \sum c_i=\sum t_ic_i=0.
\]

This is a supported label-difference born at collision. Moving the offsets
changes the circuit, and retaining the second moment removes it. It is a
physical collision analogue of the coefficient pattern, not survival of the
engine class.

## 4. Distributional enlargement

The symbol factors as

\[
 p^4-q^4=(p-q)(p+q)(p^2+q^2).
\]

Larger function or infinite-order distribution spaces may support solutions
on these characteristic directions. The authorized completed source category
contains only finite point-supported jets, represented by polynomials, where
the integral-domain proof forbids such annihilators. Adding characteristic
solutions would be a new constructor extension, not completion of the present
source.

## Typed classification

| apparent analogue | first nonfaithful arrow | restored by |
|---|---|---|
| electric jet family | magnetic parity projection | complementary `E` port |
| constant and `l<=1` modes | Green/spin reconstruction quotient | chosen zero-mode record |
| higher-pole exact class | de Rham/period quotient | local principal-part port |
| `(1,-3,2)` collision stencil | truncated collision moment map | sufficient moments or labels |
| one-chart zero | chart boundary | second chart |
| characteristic solution | unauthorized source enlargement | not present in current category |

## Evidence

`checkers/completed_tower_exception_analogue_checks.py` verifies diagonal
disjointness for arbitrary physical grade, finite-recurrence impossibility,
support exclusion of `E1/E2`, projector restoration, collision-stencil
dependence, and absence of polynomial characteristic annihilators.
