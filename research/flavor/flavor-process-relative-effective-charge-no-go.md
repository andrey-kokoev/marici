# Physical Effective Charges Are Process-Relative

## Question

Does replacing a scheme coordinate by an observable-defined effective charge
repair WP829 and make the RG curvature events physical?

## Two physical channel normalizations

Let the same one-dimensional physical orbit be represented by

\[
\dot u=\kappa u(1-u).
\]

Two independently normalized physical records can define effective charges

\[
E_A(u)=u,
\qquad
E_B(u)=u+\frac12u^2(1-u).
\]

They agree at tree level:

\[
E_A(0)=E_B(0)=0,
\qquad
E_A'(0)=E_B'(0)=1.
\]

They also agree on both endpoint values. The second record is strictly
monotone on the physical interval, so neither channel loses the underlying
one-dimensional state. They differ only through a legitimate higher-order
process response.

At the same portal event \(u=1/2\), the records are

\[
E_A=\frac12,
\qquad
E_B=\frac9{16}.
\]

Operational definition has removed arbitrary scheme coordinates, but it has
not selected one process.

## Curvature remains channel-relative

The effective beta function of the second record is the pushforward of the
same physical orbit. Its endpoint critical exponents remain \(+\kappa\) and
\(-\kappa\). Its acceleration extrema satisfy

\[
60u^4-108u^3+45u^2+4u-2=0.
\]

This polynomial has exactly two roots in \((0,1)\). The WP827 anchors give

\[
-\frac13+\frac{\sqrt3}{6},
\qquad
-\frac13-\frac{\sqrt3}{6},
\]

and therefore are not extrema of the second physical record. The polynomial
and its reflection have resultant 53084160, so its internal anchors are not a
reflection pair.

Thus two observable-defined, monotone, tree-normalized effective charges of
the same source trajectory have different portal values and curvature-event
geometry.

## Flavor probe-family interpretation

The admitted flavor programme already distinguishes several source-supported
record types: pole positions, partial widths, positive production rates, and
coherent interference. Each may define an operational running quantity after
its threshold and detector calibration is completed. Nothing currently makes
one of those records the canonical effective charge for the portal.

The largest source-authorized family is therefore a contextual family of
labelled records, not one distinguished scalar. Each monotone channel can
separate points along the toy orbit. Joint faithfulness still does not choose
a channel or a source state.

## Consequence

WP829 cannot be repaired merely by saying “use a physical effective charge.”
The source must additionally provide one of two stronger structures:

1. a unique conserved-current experiment whose normalization and threshold
   completion are forced by the same oriented matter action; or
2. a relation natural across the complete physical probe family, so its value
   is independent of which effective charge presents the orbit.

Absent such a constructor, effective-charge curvature is a process
rigidifier, not a `physical16` selector.

## Smallest exact falsifier

The pair \(E_A(u)=u\) and
\(E_B(u)=u+u^2(1-u)/2\) shares the orbit, endpoints, tree normalization,
monotonicity, and critical exponents. It gives different portal values and
curvature anchors. This is the smallest finite witness that operationality
does not imply canonicality.

## Disposition

Negative canonical-channel result. Observable-defined effective charges are
physical relative to declared instruments, but the current source does not
select one. The next search must target a conserved-current uniqueness theorem
or a probe-natural invariant, not another scalar curvature coincidence.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp830_process_relative_effective_charge_no_go.py
```
