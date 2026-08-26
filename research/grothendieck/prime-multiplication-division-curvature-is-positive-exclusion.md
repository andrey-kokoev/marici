# Prime multiplication/division curvature is positive exclusion

## Bounded question

What remains when Gaussian heat sampling, discrete prime labels, and reciprocal
transport are retained in one mixed coherence square?

## Source-labelled multiplication

On the integer-label Hilbert module with orthonormal basis \(e_n\), define

\[
T_pe_n=e_{pn}.
\]

The Gaussian heat atom obeys

\[
g_n(k\log p)=g_{np^k}(0),
\]

so \(T_p^k\) is not an arbitrary shift: it is the label operation implemented
by evaluation of the Gaussian scale orbit at the prime-power jump.

## Reciprocal partial division

The Hilbert adjoint is

\[
T_p^*e_m=
\begin{cases}
e_{m/p},&p\mid m,\\
0,&p\nmid m.
\end{cases}
\]

Thus reciprocal transport is partial division. Its failure at valuation zero
is retained rather than silently filled.

## Exact mixed curvature

Multiplication followed by division is everywhere defined:

\[
T_p^*T_p=I.
\]

Division followed by multiplication sees only the divisible labels:

\[
T_pT_p^*=P_{p\mid n}.
\]

Consequently

\[
[T_p^*,T_p]
=I-P_{p\mid n}
=P_{p\nmid n}.
\]

The mixed-square residual is exactly the positive projection onto the
primitive exclusion sector for \(p\).

For prime powers,

\[
[T_p^{*k},T_p^k]
=P_{v_p(n)<k}.
\]

The full valuation filtration therefore appears as nested positive boundary
curvatures.

## Joint faithfulness of all prime exclusions

If a coefficient packet \(c\) satisfies

\[
P_{p\nmid n}c=0
\]

for every prime \(p\), then \(c=0\). Indeed, for any fixed integer label \(n\)
there exists a prime not dividing \(n\); the corresponding exclusion
projection reads the coefficient \(c_n\).

Equivalently,

\[
\bigcap_p\operatorname{Ran}T_p=\{0\}.
\]

Thus the all-prime family is jointly faithful even though no individual
exclusion port is faithful.

## Why this is genuinely stronger than the universal seam cocycle

The identity depends on the discrete multiplication/division structure of
integer labels and on the Gaussian sampling law that realizes multiplication
at \(k\log p\). A generic continuous translated source has no corresponding
partial-division operator or valuation-zero projection.

This is therefore the first source-labelled, positive, hostile-rejecting mixed
curvature found after the scalar cutoff cocycle was closed.

## Current boundary

Positive exclusion curvature does not yet confine scalar zeros. The missing
bridge is

\[
X(z)=0
\Longrightarrow
P_{p\nmid n}c_z=0
\quad(\forall p),
\]

for a canonically constructed zero-state packet \(c_z\).

No such implication has been proved. If it were source-derived, joint
faithfulness would force \(c_z=0\), contradicting nontriviality of the
zero-state off the allowed interface. If a hostile zero packet has nonzero
exclusion energy, it gives the sharp rejection witness.

## Next gate

Construct the labelled coefficient packet attached to the doubled-tail
zero-state without dividing by \(X\). Then compute whether the completed Green
boundary identity makes its total exclusion energy vanish. Failure at one
prime is the smallest falsifier; success for every prime closes the label
state before any limiting positivity argument.
