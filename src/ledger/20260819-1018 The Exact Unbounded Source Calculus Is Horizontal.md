# The Exact Unbounded Source Calculus Is Horizontal

## Derivative defect

Entry 1011 applied the inherited external-parameter routine to the finite
triangle-wall Rees presentation.  That routine used the five-point stencil

\[
\frac{f(-2)-8f(-1)+8f(1)-f(2)}{12}.
\]

The Cayley--Menger coefficients have external degree six.  The stencil is
not exact at that degree and, more importantly, is a finite-difference
operator rather than a derivation.  It fails the Leibniz identity on the
principal relation

\[
e_k-Ke_{k+1}=0.
\]

Therefore Entry 1011's count \(13704\) is withdrawn.  Its qualitative warning
about finite truncation is retested below rather than assumed.

## Exact repair

The parameter derivative was replaced by seven-node Lagrange coefficient
extraction, which is exact through degree six.  On the unbounded labelled
form calculus, the chain identity was then tested separately for every
relation generator retained by the degree-ten packet.

For each of the two wall tangents, the census is

\[
\begin{array}{c|c|c}
\text{family}&\text{tested}&\text{failures}\\
\hline
d_{\rm dR}&264&0\\
K&1792&0\\
q_1&2640&0\\
q_2&2640&0\\
q_3&2640&0\\
q_{23}&2640&0\\
q_{31}&2640&0.
\end{array}
\]

Thus all

\[
\boxed{15256/15256}
\]

source relations satisfy the exact external/fiber commutator in both
coordinate tangent directions when their higher-pole images and source
relations are retained.

## Corrected finite gate

The repaired derivative was also reapplied to the finite pole-depth-two
presentation.  It remains nonhorizontal, but the correct count is

\[
13497/15256
\]

in each tangent direction.  Only 60 rows directly request missing output
labels; 13437 failing rows have output labels inside the finite ambient
window.  Their reductions fail because the corresponding higher-pole source
relations and primitives are absent.

Hence the clean separation is

\[
\boxed{
\text{unbounded labelled calculus: horizontal},
\qquad
\text{finite pole-depth-two quotient: nonhorizontal}.
}
\]

The rank-twenty-one occurrence audit was rerun with the exact derivative.  Its
earlier qualitative conclusion is unchanged: chain naturality passes, while
the projected rank-twenty-one block leaks in all three directions and its
projected matrices do not intertwine.

## Meaning for the seven-plane

The missing input identified by Entry 1008 does exist canonically on the
full labelled source calculus.  The obstruction is now localized to the
order of operations:

\[
\boxed{
\text{take a connection-stable/direct-limit total complex first, then apply
exact valuation and finite presentation.}
}
\]

Projecting the connection directly from the present finite Rees packet is
still illegal.  But no new geometric coherence cell is presently required:
the complete source differential already satisfies the needed commutator.
The next test is whether exact valuation commutes with the connection-stable
direct limit and yields a finite rank-seven differential module.

## Durable verification

- repaired shared checker:
  `research/nima/check_rank21_occurrence_reflection_connection.py`;
- unbounded commutator checker:
  `research/nima/check_unbounded_twisted_derham_connection_commutator.py`;
- unbounded packet:
  `research/nima/unbounded-twisted-derham-connection-commutator.json`;
- corrected finite gate:
  `research/nima/triangle-wall-external-connection-gate.json`;
- allocator claim: `seqclaim-e445bd2f2bdef846c46297be`.
