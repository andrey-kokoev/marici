# The Seam Cocycle Has a Universal Resolvent Homotopy but It Is a Bulk, Not Modular, Repair

## Resolvent form of the tail

Write the positive-chart tail propagation abstractly as

\[
R_z=(D-z)^{-1}
\]

on its outgoing graph domain, with conventions chosen so that endpoint
evaluation gives

\[
A(z)=\operatorname{ev}_0R_zf.
\]

The mate-square seam residual from the previous result is the endpoint of the
resolvent difference:

\[
C_f(z)
=
\operatorname{ev}_0(R_{-\overline z}-R_{\overline z})f.
\]

## Canonical second-order homotopy

The resolvent identity gives

\[
R_{-w}-R_w
=
-2wR_{-w}R_w.
\]

Therefore

\[
C_f(z)
=
-2\overline z\,
\operatorname{ev}_0R_{-\overline z}R_{\overline z}f.
\]

This constructs the missing comparison cell without choosing a Hilbert pivot
or integrating an observed scalar residual afterward.  It is canonical from
the two tail propagators themselves.

## Why this does not close the RH route

The identity is universal.  It holds for every source for which the two
resolvents exist, including hostile even sources with off-critical zeros.  It
therefore contains no theta arithmetic or modular selection law.

More importantly, the correction is not supported only at the seam.  The
homotopy state

\[
K_z=R_{-\overline z}R_{\overline z}f
\]

occupies the full scale half-line.  Its endpoint gives `C_f`, but its Green
derivative introduces a genuine second-order bulk channel.  Treating the
endpoint value alone as a modular boundary current discards the interior state
whose propagation produced it.

For `f(q)=exp(-alpha q)`,

\[
K_z(q)
=
\frac{e^{-\alpha q}}
{(\alpha-\overline z)(\alpha+\overline z)},
\]

and

\[
C_f(z)
=
-2\overline zK_z(0).
\]

The homotopy is visibly nonzero throughout the bulk.

## Coherence-tower meaning

The mate-square residual does admit a next coherence cell, but that cell is
itself a new state tower rather than a scalar equality witness:

```text
two unilateral tail functors
        |
        v
resolvent-difference 2-cell
        |
        v
second-order bulk homotopy K_z
        |
        v
seam endpoint C_f(z)
```

This is exactly the operator's warning that the coherence cell across towers
may itself have a tower.  The new rung is forced, but it does not terminate
the explanation.

## Sharp modular question

Theta/Poisson structure must now do more than reproduce the universal
endpoint residual.  It must either:

1. identify `K_z` with an already declared primitive, square, connected, or
   archimedean state channel;
2. supply an opposite-oriented reciprocal homotopy whose full bulk Green
   contribution cancels it;
3. prove that the anti-diagonal zero-state annihilates the entire homotopy,
   not only its endpoint.

Any proposed modular current that matches `C_f(z)` while leaving the bulk
`K_z` untyped fails the mate-square audit.

## Result

The seam cocycle is canonically null-homotopic through the universal
second-order resolvent state.  This is a real construction, but not an RH
mechanism.  It moves the obstruction from the endpoint into a new bulk
coherence tower.  The next source-specific gate is whether theta arithmetic
identifies or cancels that entire homotopy state.

