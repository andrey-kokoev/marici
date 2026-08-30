# No finite six-port can be the completed source intertwiner

## Question

Can the now-ordered Pearson carrier be mapped into a finite six-port boundary
object that also carries reciprocal Fourier–Poisson sewing?

## Two different naturality levels

The source supplies a valid finite labelled square. A preparation coefficient
attached to a label is seen as the same coefficient in the logarithmic chart.
This incidence commutes with diagonal labelled preparation and with its
adjoint.

Fourier–Poisson sewing has a different type. It is defined on the completed
global source and does not preserve a finite Euler cutoff. If \(P_X\) is a
cutoff projection and \(F\) is global Fourier sewing, the residual is

\[
\mathfrak A_X=P_XF(I-P_X).
\]

The existing exact four-mode witness has

\[
\operatorname{rank}\mathfrak A_X=1.
\]

Thus the Beck–Chevalley square already fails at the smallest nontrivial finite
model.

## Consequence for the six-port programme

The ordered finite Pearson carrier is legitimate, and its dual pairing is
legitimate. But no finite six-dimensional object can simultaneously be:

- the source-complete arithmetic carrier;
- stable under global Fourier–Poisson sewing;
- compatible with Euler cutoff as a source subobject;
- and the physical six-port controller.

The conflict is not dimension alone. It is the order of operations. Global
sewing must occur before diagnostic projection. A finite controller may model
the resulting comparison, but it cannot be the source object on which the
completed sewing was constructed.

## Correct categorical architecture

The required chain has three separately typed arrows:

```text
global restricted-product source
    -> completed rigged boundary correspondence
    -> finite diagnostic projection
    -> controlled optical realization
```

The first arrow carries Pearson/de Rham incidence and its contragredient. The
second retains the seam created by one-sided translation. The third is a
projection after sewing. The fourth compiles a finite experiment with an
explicit calibration relation.

Reversing the middle order would treat the cutoff projection as if it were a
Fourier-stable source subobject. The leakage residual disproves that move.

## DPC verdict

Closed: the search for a finite \(6\times6\) matrix that is simultaneously the
completed arithmetic source map and the optical controller.

Open: a global operator-valued correspondence whose finite projections can be
calibrated against the optical controller.

This retypes the missing incidence. It is not a bijection between six names
and six ports. It is a natural transformation from a global rigged source
functor to a family of finite diagnostic functors, with a declared leakage
cell whenever projection is moved before sewing.

## Finite falsifier

Any proposed finite source intertwiner must make
\(P_XF(I-P_X)=0\). The exact four-mode witness gives a nonzero rank-one
residual, so one such failure rejects the proposal without any continuum
limit argument.

## Verification

The checker `check_no_finite_completed_source_intertwiner.py` verifies the
finite labelled naturality square and the nonzero rank-one Fourier cutoff
residual using exact integer arithmetic.

