# Derived resolved infinity-Gysin Čech matrix contract

This packet fixes the input and output conventions for the matrix calculation
following ledger Entries 727–735.  Entry 735 supersedes the vector-space-only
reading of Entry 734: internal indicial differentials and source-labelled
principal cells are mandatory.  It does not prescribe local bases.

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

## Local input complexes

For every vertex and edge, supply a finite cochain complex

\[
(V_i^\bullet,\partial_i),
\qquad
(E_{ij}^\bullet,\partial_{ij}).
\]

For each ordered incidence \(i\to ij\), supply a chain map

\[
r_{i,ij}:V_i^\bullet\otimes K_{ij}\longrightarrow E_{ij}^\bullet.
\]

At a simple crossing, the first indicial input is augmented by the actual
source-labelled principal cell:

\[
\widetilde K_i=K_{L_1,i}\oplus\mathbb Q p_i.
\]

The derived corner calculation fixes

\[
r_{i,ij}(X,c)=c\,C_{E,ij};
\]

the homogeneous \(K_{L_1,i}\) directions map to zero.  The principal cell and
its differential must be exported; replacing this augmented complex by its
homogeneous kernel is forbidden.

The matrix packet must contain:

- the source and target basis labels;
- the coefficient field and its involution matrix;
- the exact matrix of \(r_{i,ij}\);
- every internal differential and the degree of the principal cell;
- the local frame-change matrices on both charts;
- the orientation sign used in the Čech differential;
- for \(E_{23}\), the stack-chart involution and the unnormalized trace.

The full nonresonant \(E_{23}\) object is retained.  No exceptional-resonance
generator may be appended there.

## Čech differential and totalization

With orientations \(1\to2\), \(1\to3\), and \(2\to3\), assemble the
degreewise horizontal differential

\[
d(v_1,v_2,v_3)=
\bigl(r_{2,12}v_2-r_{1,12}v_1,\;
r_{3,13}v_3-r_{1,13}v_1,\;
r_{3,23}v_3-r_{2,23}v_2\bigr).
\]

The last component includes the unnormalized finite trace from the stack
chart.  On an even section it is multiplication by two; on an odd section it
is zero.

Let \(C^{p,q}\) have Čech degree \(p\) and internal indicial degree \(q\).
The authoritative object is

\[
\operatorname{Tot}^n C=\bigoplus_{p+q=n}C^{p,q},
\qquad
D=\delta+(-1)^p\partial.
\]

Computing kernels first and then applying an ambient projection is not an
equivalent construction.

## Character projectors

After extension to the compositum
\(L=\mathbb Q(\sqrt{-3},\sqrt5)\), let \(g_{-3}\) and \(g_5\) be the two
commuting involutions.  Use

\[
P_{\epsilon,delta}
=\frac14(1+\epsilon g_{-3})(1+\delta g_5),
\qquad \epsilon,\delta\in\{+1,-1\}.
\]

The rational invariant complex is \(P_{+,+}\operatorname{Tot}(C)\).  Also compute the
\((-+),(+-),(--)\) blocks.  The mixed \((--)) block is expected to vanish for
the present incidence carrier; a nonzero block must be traced to coefficient
monodromy rather than silently discarded.

## Verification gates

1. Verify that every internal differential squares to zero.
2. Verify that every \(r_{i,ij}\) is a chain map.
3. Verify \(Dg=gD\) for both involutions.
4. Verify \(D^2=0\) after totalization.
5. Verify independence under every declared degreewise chain-basis change.
6. Report chain-group dimensions, differential ranks, and homology dimensions
   in each total degree and character block.
7. Compute invariant hypercohomology before any physical interpretation.

The pairwise-resonant-divisor route remains open only if the relevant invariant
total cohomology is nonzero.  A nonzero dimension is not yet a physical class: its generator
must additionally be stable under basis changes and compatible with the
physical Gysin orientation.
