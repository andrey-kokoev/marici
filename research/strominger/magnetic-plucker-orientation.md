# Magnetic Plucker signs have coherent finite-range orientation

Companion to `checkers/magnetic_plucker_orientation_checks.py` (7/7,
exit 0) and `results/magnetic_plucker_orientation.json`.

## Coordinate signs versus orientation

For adjacent row intervals (i,i+1) and column intervals (a,a+1), let

\[
\Delta_{ia}=
\det\begin{pmatrix}
M_{i,a}&M_{i,a+1}\\
M_{i+1,a}&M_{i+1,a+1}
\end{pmatrix}.
\]

The raw signs are not positive: the first mixed-sign component in the tested
lexicographic order is ((g,k,q)=(3,1,2)). The invariant question assigns a
sign (ho_i) to each row interval and (kappa_a) to each column interval,
subject to

\[
\rho_i\kappa_a=\operatorname{sgn}(\Delta_{ia}).
\]

These equations form a bipartite sign graph. They are soluble exactly when
the product of edge signs around every cycle is (+1).

## Finite coherence theorem

The exact scan covers

\[
3\le g\le20,\qquad1\le k\le10,\qquad1\le q\le30.
\]

All 5,400 component graphs are coherent, comprising 62,562 nonzero adjacent
minor constraints. No supported adjacent minor vanishes. Here supported means
that at least one of the two perfect-matching products in its (2\times2)
support is nonzero.

The solved interval signs integrate explicitly to ordinary row and column
signs:

\[
s_0=t_0=1,\qquad s_{i+1}=\rho_i s_i,\qquad
t_{a+1}=\kappa_a t_a.
\]

After this gauge transformation every supported adjacent minor is positive.
This integration is automatic because the ordered row and column intervals
are paths. The only genuine obstruction is therefore cycle holonomy in the
bipartite constraint graph.

## Sharp falsifier

The checker deliberately reverses one edge belonging to a constraint cycle.
The first such test occurs at ((g,k,q)=(3,3,1)), row interval 2 and column
interval 4. The solver rejects the tampered graph, exhibiting the expected
negative-cycle obstruction. Thus the coherence check is capable of failing;
it is not a normalization that forces success.

## Exceptional loci

An independent exact rank scan at grade two over

\[
1\le k\le10,\qquad1\le q\le20
\]

finds defects only at (q=1,7). The (q=7) local singular block annihilates
the primitive vector ((1,-3,2)).

## Boundary of the result

This is a finite-range orientation-coherence theorem, not an arbitrary-grade
proof of total positivity. It establishes neither a closed source-parity
formula for the gauge nor the width-four transfer recurrence. Those are the
two remaining symbolic tasks. Coherence is necessary input to a cone-
preserving transfer proof, but adjacent-minor positivity alone has not yet
been shown sufficient for every maximal Hall minor.

