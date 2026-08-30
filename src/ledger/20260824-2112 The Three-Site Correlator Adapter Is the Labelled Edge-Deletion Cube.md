# 2112 — The Three-Site Correlator Adapter Is the Labelled Edge-Deletion Cube

## Question

Entry 2110 typed the wavefunction-to-correlator comparison and proved that it
kills global state-line phase.  Determine the finite source object through
which the three-site one-loop coefficient system must pass before asking what
happens to its nonsplit algebraic extension or to \(\mathcal Q\).

## Frozen source rule

Benincasa--Dian, arXiv:2401.05207, proves that a correlator associated to a
graph with \(n_e\) edges is represented by the \(2^{n_e}\) wavefunction graphs
obtained by all labelled edge erasures.  The erased edge is replaced by its
inverse two-point factor \(1/y_e\), and its endpoint site weights are shifted
by \(y_e\).  The same comparison is encoded by an orientation-changing
subdivision of the weighted cosmological polytope.

For the three-site loop, retain the edge occurrences

\[
E=\{12,23,31\}.
\]

The adapter sectors are all subsets \(S\subseteq E\):

\[
\varnothing;
\quad
\{12\},\{23\},\{31\};
\quad
\{12,23\},\{12,31\},\{23,31\};
\quad
E.
\]

Thus its graded dimensions are

\[
\boxed{1\to3\to3\to1.}
\]

The exact labelled incidence packet contains twelve oriented cube edges with
the standard occurrence/Koszul signs.

## Carrier classification

Every pre-integration operation is source-declared:

- retain a wavefunction graph;
- erase a labelled edge occurrence;
- insert \(1/y_e\);
- shift the two endpoint site weights by \(y_e\);
- change the orientation/weight of an existing subdivision cell.

No new polynomial divisor is introduced by this finite adapter.  In
particular,

\[
\boxed{
\mathcal Q\text{ cannot enter here as a new correlator Carrier divisor.}
}
\]

This does not say that integrated correlator periods are \(\mathcal Q\)-free.
It types where any such dependence would have to live.

## Narrow result

\[
\boxed{
\text{three-site wavefunction-to-correlator comparison}
=
\text{labelled Boolean deletion adapter on the existing subdivision Carrier}.
}
\]

The weighted correlator geometry is not an ad hoc new Carrier: it is an
orientation/weight lens on a source-defined subdivision of the wavefunction
geometry.  Any surviving role for \(\mathcal Q\) must arise after applying
sector-specific coefficient integration or extension transport through this
adapter.

## Next falsifier

Attach to each of the eight sectors its actual relative Gauss--Manin
coefficient object and derive the twelve deletion maps.  Then compute the
totalized extension class.  The first bounded pilot should compare the full
three-edge sector with the three single-deletion sectors and test whether the
known algebraic/elliptic extension restricts, cancels, or creates supported
cohomology.

## Durable evidence

- `research/benincasa/checkers/three_site_weighted_correlator_adapter.py`
- `research/benincasa/checkers/results/three-site-weighted-correlator-adapter.json`
- arXiv:2401.05207v1, equations (2.29) and (4.71)
- Ledger allocation: `seqclaim-c2eebf3a5696ed1bf6c9d36a`

