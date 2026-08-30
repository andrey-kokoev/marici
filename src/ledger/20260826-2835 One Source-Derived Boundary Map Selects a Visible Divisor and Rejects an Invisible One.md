# 2835 — One Source-Derived Boundary Map Selects a Visible Divisor and Rejects an Invisible One

## Matched physical test

Use the previously derived weighted \(X_1\)-soft \(q_{G12}\)-residue current. Its exceptional physical coordinate is

\[
\xi\in[-1,1],
\]

with oriented chain

\[
\Gamma_\xi=[-1,1],
\qquad
\partial\Gamma_\xi=[1]-[-1].
\]

No comparison map is changed between the two marked divisors.

## Visible marked divisor

After removing the common \(X_1\) normal, the source gives

\[
q_{g1}/X_1=\xi+1.
\]

It vanishes at the negative endpoint \(\xi=-1\). Therefore the oriented boundary pairing is

\[
\langle\partial\Gamma_\xi,q_{g1}\rangle=-1.
\]

This is a nonzero source-normalized supported chain map.

## Invisible marked divisor

On the same exceptional current,

\[
q_{g23}|_{X_1=0}=2p,
\qquad p>0.
\]

It is a unit throughout the chain and has no endpoint zero. Hence

\[
\langle\partial\Gamma_\xi,q_{g23}\rangle=0.
\]

## Selection law

The same source-derived physical boundary map distinguishes the two coefficient supports:

\[
\text{support met with orientation}
\longmapsto
\text{nonzero readout},
\]

\[
\text{support a unit on the chain}
\longmapsto
0.
\]

This supplies the positive counterpart requested after Entry 2833. The physical lens is not a universal eraser: it selects one existing supported class and rejects another through incidence with one fixed chain.

## Scope

The theorem concerns the supported endpoint/boundary map. It does not evaluate the complete bulk period, nor does it claim that every nonempty support intersection gives a nonzero integrated observable. Higher-dimensional intersections can still cancel by orientation, monodromy, or exactness.

## Durable artifacts

- `research/benincasa/check_matched_physical_divisor_selection.py`
- `research/benincasa/matched-physical-divisor-selection.json`
