# Resolved infinity-Gysin Čech matrix contract

This packet fixes the input and output conventions for the matrix calculation
following ledger Entries 727–733.  It does not prescribe local bases.

## Fields and involutions

Use

\[
K_{12}=\mathbb Q[z]/(z^2-z+1),\qquad \sigma_{12}(z)=1-z,
\]

\[
K_{13}=\mathbb Q[w]/(w^2+w-1),\qquad \sigma_{13}(w)=-1-w,
\]

and \(K_{23}=\mathbb Q\).  Calculations over a split field must retain the
two involution matrices; ordering the two roots is not structure.

## Local input

For each ordered incidence \(i\to ij\), supply a matrix

\[
r_{i,ij}:V_i\otimes K_{ij}\longrightarrow E_{ij}.
\]

The matrix packet must contain:

- the source and target basis labels;
- the coefficient field and its involution matrix;
- the exact matrix of \(r_{i,ij}\);
- the local frame-change matrices on both charts;
- the orientation sign used in the Čech differential;
- for \(E_{23}\), the stack-chart involution and the unnormalized trace.

The full nonresonant \(E_{23}\) object is retained.  No exceptional-resonance
generator may be appended there.

## Differential

With orientations \(1\to2\), \(1\to3\), and \(2\to3\), assemble

\[
d(v_1,v_2,v_3)=
\bigl(r_{2,12}v_2-r_{1,12}v_1,\;
r_{3,13}v_3-r_{1,13}v_1,\;
r_{3,23}v_3-r_{2,23}v_2\bigr).
\]

The last component includes the unnormalized finite trace from the stack
chart.  On an even section it is multiplication by two; on an odd section it
is zero.

## Character projectors

After extension to the compositum
\(L=\mathbb Q(\sqrt{-3},\sqrt5)\), let \(g_{-3}\) and \(g_5\) be the two
commuting involutions.  Use

\[
P_{\epsilon,delta}
=\frac14(1+\epsilon g_{-3})(1+\delta g_5),
\qquad \epsilon,\delta\in\{+1,-1\}.
\]

The rational invariant block is \(P_{+,+}dP_{+,+}\).  Also compute the
\((-+),(+-),(--)\) blocks.  The mixed \((--)) block is expected to vanish for
the present incidence carrier; a nonzero block must be traced to coefficient
monodromy rather than silently discarded.

## Verification gates

1. Verify \(dg=gd\) for both involutions.
2. Verify \(d^2=0\) if internal coefficient differentials are included.
3. Verify independence under every declared local basis change:
   \(d' = B_1dB_0^{-1}\).
4. Report domain dimension, target dimension, rank, kernel dimension, and
   cokernel dimension in each character block.
5. Compute the invariant cofiber before any physical interpretation.

The pairwise-resonant-divisor route remains open only if the invariant cofiber
is nonzero.  A nonzero dimension is not yet a physical class: its generator
must additionally be stable under basis changes and compatible with the
physical Gysin orientation.
