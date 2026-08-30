# Connected Transport Rank

## Candidate precursor

Let a typed operation supply a finite linear kernel

\[
K:V_{\rm present}\longrightarrow V_{\rm future}.
\]

A completely separable transition factors through a line and has rank one.
The first algebraic witness of connected future structure is

\[
\boxed{\bigwedge^2K.}
\]

It vanishes exactly when \(\operatorname{rank}K\le1\).  A coarse numerical
capacity is

\[
c_0(K)=\max(0,\operatorname{rank}K-1).
\]

This has the required first gates:

1. invertible changes of present and future frames preserve it;
2. appending an independent spectator vector gives
   \(K\otimes s\) with \(\operatorname{rank}(K\otimes s)=\operatorname{rank}K\);
3. sequential composition obeys
   \[
   \operatorname{rank}(LK)\le
   \min(\operatorname{rank}L,\operatorname{rank}K),
   \]
   an algebraic data-processing inequality;
4. after positive normalization, rank one is the determinantal independence
   locus for a joint probability table, while mutual information supplies its
   metric refinement.

Thus \(\bigwedge^2K\) is a plausible pre-probabilistic support for connected
information.  It detects whether dependence is possible without assigning a
probability magnitude.

## Carrier gate

The bounded cross-sector test also gives a negative result.  Coefficients are
essential.  A generic fully supported incidence relation is represented by an
all-ones support matrix of rank one even when its coefficient-bearing
transition matrix has higher rank.  The exact flavor example

\[
\begin{pmatrix}
9/25&16/25&0\\
16/25&9/25&0\\
0&0&1
\end{pmatrix}
\]

has rank three; forgetting its weights can erase the connected structure.

Therefore the candidate does not currently live on a bare unweighted Carrier.
It lives on a typed transport kernel:

\[
\boxed{
\text{Carrier port}
+\text{coefficient adapter}
\longrightarrow K
\longrightarrow\bigwedge^2K.
}

Positive state/effect readout then refines this algebraic dependence locus to
mutual information or channel capacity.

## Interpretation

This is consistent with the ports-and-adapters architecture.  The Carrier
declares which present and future spaces may be related.  The sector adapter
supplies the actual transport coefficients.  Connected future capacity is an
invariant of their composite, not of either layer alone.

It also supplies a precise meaning for the coherence channel: exterior powers
of transport record multi-directional dependence that cannot pass through a
single scalar line.

## Next falsifier

Construct a source-defined transport kernel in one mature sector before its
positive readout, and test whether the source-selected state/effect pairing is
faithful on its determinantal support:

\[
I(X;Y)>0
\quad\Longrightarrow\quad
\bigwedge^2K\ne0,
\]

and whether \(\bigwedge^2K\ne0\) produces \(I(X;Y)>0\) for the particular
physical state rather than merely making it possible.  The converse cannot
hold for every state: a rank-two channel fed on only one input direction can
have zero mutual information.  The scattering Cut/helicity kernel is the
sharpest existing candidate for this faithfulness test, together with
spectator and base-change naturality.

Certificate:
`research/nima/checkers/check_connected_transport_rank.py`
