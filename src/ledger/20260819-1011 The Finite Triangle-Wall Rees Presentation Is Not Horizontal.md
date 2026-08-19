# The Finite Triangle-Wall Rees Presentation Is Not Horizontal

## Source-derived connection gate

Entry 1008 shows that dual-number flatness cannot choose a connection on the
rank-seven exact-valuation object.  The full rational-form machinery does
contain a candidate external operator: differentiating

\[
K^{\gamma-k}\prod_i q_i^{-l_i}a^m b^n
\]

raises the appropriate \(K\)- or \(q_i\)-pole and supplies the exact
parameter derivative of its defining polynomial.  This operator is defined
before any quotient or pivot choice.

For a raw relation row \(r(X)\), horizontality of the retained presentation
requires

\[
\partial_T r+rA_T\in\operatorname{rowspan}R
\]

for each wall tangent \(T\).  This was tested at

\[
(X_1,X_2,X_3)=(2,3,5)
\]

over \(\mathbf F_{32003}\), using the complete degree-ten presentation with
11520 ambient columns and 15256 raw relation rows.

## Exact failure census

For the \(X_1\) wall tangent \(\partial_{X_1}+\partial_{X_3}\),

\[
13704/15256
\]

covariant relation derivatives have nonzero normal form.  Their family
distribution is

\[
(264,1792,2640,2640,2640,2640,1088).
\]

For the independent \(X_2\) tangent
\(\partial_{X_2}+\partial_{X_3}\), the total is again

\[
13704/15256,
\]

with distribution

\[
(264,1792,2640,2640,2640,1088,2640).
\]

The entries are ordered as

\[
(d_{\rm dR},K,q_1,q_2,q_3,q_{23},q_{31}).
\]

Changing the global sign convention does not repair the gate: 7496 rows
still fail in each tangent direction.  Thus the obstruction is not a sign
choice or a single marked-divisor anomaly.

## Meaning

The finite Rees presentation used in Entries 994, 1003, and 1006 is a valid
fiberwise rank object, but it is not closed under the source external
connection:

\[
\boxed{
\text{finite Rees flatness}\not\Rightarrow
\text{horizontal finite Rees complex}.
}
\]

This does not falsify the full untruncated rational-form connection.  The
operator raises pole and degree sectors, while the finite presentation
discards precisely the neighboring data needed to express covariant
derivatives as relations.  The result is therefore another truncation gate,
parallel to Entry 878's failure of the projected rank-twenty-one block.

In particular, no connection may be projected onto \(E_2\) from the current
degree-ten packet.  Doing so would silently discard the measured residuals.

## Correct next construction

Retain a connection-stable filtered total complex first.  Concretely, enlarge
the pole/degree window together with its boundary relations and test whether
the covariant residuals move outward with the cutoff.  The decisive options
are:

1. stabilization in the direct limit, giving a genuine source connection
   which can then be passed through exact valuation;
2. persistent finite-degree residuals, identifying a missing Čech/Gysin or
   principal-coherence block.

Only after this closure test should the induced connection on the seven-plane
be computed.

## Durable verification

- checker: `research/nima/check_triangle_wall_external_connection_gate.py`;
- packet: `research/nima/triangle-wall-external-connection-gate.json`;
- allocator claim: `seqclaim-bc36edc891e31845f68d0042`.
