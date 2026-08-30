# Reciprocal Bivector Doubling Has a Normalization Anomaly

For a fixed source `f`, consider

\[
G_s(q)=\int_q^\infty e^{s(v-q)}f(v)\,dv,
\qquad W_s=\Omega\wedge G_s.
\]

Each sheet obeys

\[
2\operatorname{Re}(s)E_s=B_s-2F_s,
\]

where `E_s` is the integrated bivector energy, `B_s` its endpoint norm, and
`F_s` its source-forcing overlap.

## Exact fixed-source audit

Take real `s`, a decay rate `lambda>s`, and

\[
f(q)=e^{-\lambda q}v,
\qquad \langle\Omega,v\rangle=0.
\]

Writing `D` for the squared norm of `Omega wedge v`, one obtains

\[
E_s=\frac{D}{2\lambda(\lambda-s)^2},\qquad
B_s=\frac{D}{(\lambda-s)^2},\qquad
F_s=\frac{D}{2\lambda(\lambda-s)}.
\]

The Green identity holds exactly. The reciprocal sheet `1-s` has the same
form with `s` replaced by `1-s`, but its energy, boundary, and forcing terms
do not agree with those of the first sheet.

## The normalization trap

Define the normalized state

\[
\widetilde W_s=(\lambda-s)W_s=e^{-\lambda q}\Omega\wedge v.
\]

This makes the sheet energies and endpoints identical. It does not make their
Green laws identical: the same normalization transports the forcing term.
Reciprocal subtraction gives

\[
2(2s-1)\widetilde E
=-2(\widetilde F_s-\widetilde F_{1-s}),
\]

and both sides equal `(2s-1)D/lambda`.

Thus reciprocal doubling alone does not confine a scalar-null state. The
candidate proof works only if a source-derived sewing theorem removes this
normalization anomaly without fitting the sheet weights.

## Multi-tower consequence

The forward and backward witness towers are insufficient by themselves. Their
mate/equalizer tower must transport not only states but the complete Green
pairing, including its forcing coefficient. Equality of normalized states is
weaker than equality of source-typed currents.

The next gate is to derive the reciprocal mate on the complete current packet
and test whether primitive, square, seam, and archimedean channels absorb the
forcing anomaly. If no independently constructed channel absorbs it, this
conservation route closes.

