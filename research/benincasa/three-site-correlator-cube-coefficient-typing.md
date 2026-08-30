# Three-site correlator cube: coefficient-level typing audit

## Frozen source

Paolo Benincasa and Gabriele Dian, *The Geometry of Cosmological Correlators*, arXiv:2401.05207.

The relevant source statements are:

- equations (2.13)--(2.14): a correlator contribution is a sum over all edge-erased wavefunction graphs;
- equations (2.27)--(2.30): dashing an edge deletes it, multiplies by the inverse two-point wavefunction `1/y_e`, and shifts both endpoint site weights by `y_e`;
- equations (4.66)--(4.71): the same expansion is realized as a weighted-polytope subdivision with weights `(-2)^j` at deletion grade `j`.

## Typed operation

For a graph `G=(V,E)` and a deletion subset `S subset E`, the source defines a separate integrand

\[
\psi_{G\setminus S}
\left(x_v+\sum_{e\in S,\,e\ni v}y_e,\{y_f\}_{f\notin S}\right)
\prod_{e\in S}\frac1{y_e}.
\]

The correlator integrand is the sum of these objects. For the three-edge triangle this gives eight labelled summands arranged combinatorially by the Boolean poset of deletion subsets.

The weighted-polytope representation supplies a second presentation of that sum. It is a subdivision identity among canonical forms, not a source-defined differential between the summands.

## Negative typing result

The frozen source does **not** define, for an inclusion `S subset S union {e}`:

\[
\mathcal M_S\longrightarrow\mathcal M_{S\cup\{e\}}
\]

as a restriction, residue, Gysin, Gauss--Manin, or chain map. In particular, the twelve oriented edges of the triangle's Boolean cube are presently combinatorial incidences only.

Consequently the following inference is prohibited:

\[
\text{signed sum over eight periods}
\not\Rightarrow
\text{totalization of an eight-vertex coefficient complex}.
\]

## Surviving statement

The source-derived wavefunction-to-correlator adapter has:

- a frozen eight-summand labelled carrier packet;
- explicit rational multiplication and endpoint-shift operations within each summand;
- a weighted-polytope subdivision identity for their sum.

It does not yet have coefficient-level arrows between deletion grades. Therefore an extension class coupling the eight period systems is currently **untyped**, not zero.

## Next finite falsifier

For one edge `e`, construct the two adjacent period systems directly from their source integrands and test whether the dash replacement factors through an independently existing localization triangle. The admissible first candidates are:

1. restriction to the edge hyperplane;
2. residue/Gysin along the two-point factor `y_e=0`;
3. pullback by the endpoint-energy translation followed by multiplication by `1/y_e`.

The first candidate that is well typed must satisfy Gauss--Manin horizontality before it can be copied around the labelled cube. Failure of all three candidates leaves the correlator adapter as a source-defined sum rather than a coefficient complex.
