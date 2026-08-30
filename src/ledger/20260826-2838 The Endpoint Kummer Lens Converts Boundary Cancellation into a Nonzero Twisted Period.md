# 2838 — The Endpoint Kummer Lens Converts Boundary Cancellation into a Nonzero Twisted Period

> Retracted by Entry 2840. The endpoint Kummer cover is source-derived, but the separable factor \(d\xi/\sqrt{1-\xi^2}\) is not the full strict-transform source measure. The value \(\pi\) is a toy rank-one period and must not be interpreted as the cosmological physical readout.

## Typing correction

Entry 2836 computes the unweighted oriented boundary packet

\[
(-1,+1)
\]

and its zero coarse sum. That is a correct incidence-level statement. It is not the source-normalized coefficient readout on the exceptional Cayley–Menger face.

The frozen face contributes the rank-one Kummer factor

\[
\frac{d\xi}{\sqrt{1-\xi^2}}
\]

on the physical interval \(-1<\xi<1\).

## Endpoint coefficient data

Both endpoints have local exponent

\[
-\frac12
\]

and local monodromy

\[
-1.
\]

They are branch points of a coefficient local system, not two ordinary scalar residue points to which arbitrary finite weights may be assigned.

## Twisted physical readout

Set

\[
\xi=\cos\theta.
\]

On \(0<\theta<\pi\), the square root and Jacobian cancel, yielding

\[
\int_{-1}^{1}\frac{d\xi}{\sqrt{1-\xi^2}}
=
\int_0^\pi d\theta
=
\pi.
\]

Thus the primitive source-normalized Kummer period is nonzero even though the unweighted coarse boundary sum vanishes.

## Architectural consequence

The three-stage readout must preserve coefficient type:

\[
\text{occurrence-resolved incidence}
\longrightarrow
\text{sector-specific coefficient local system}
\longrightarrow
\text{physical twisted pairing}.
\]

Forgetting occurrences too early produces the zero boundary sum. Forgetting the Kummer coefficient type then incorrectly promotes that zero to a period statement.

Entry 2836 is therefore retained with its stated scope: it distinguishes cancellation from route loss at the boundary-incidence level. The present entry supplies the next layer and forbids interpreting that cancellation as vanishing of the Kummer period.

## Narrow conclusion

The Carrier controls the two endpoint occurrences and their orientations. The cosmological coefficient lens equips them with square-root monodromy. The physical current pairs with that combined typed object and yields \(\pi\) in the primitive one-dimensional model.

This does not evaluate the full three-site loop period; spectator variables and the remaining coefficient blocks are not included.

## Durable artifacts

- `research/benincasa/check_endpoint_kummer_readout_typing.py`
- `research/benincasa/endpoint-kummer-readout-typing.json`
