# RH rank no-go does not apply to zero-reflection on a pointed cone

## Correction

The previous rank lower bound was stated too broadly.

It correctly proves that one scalar Evans row plus finitely many scalar coherence rows cannot be injective on a linear constructor image whose rank grows without bound.

But RH does not require reconstruction of every carrier state. It requires zero-reflection on the source-admissible set:

\[
\ell(y)=0
\quad\Longrightarrow\quad
y=0
\]

for admissible \(y\).

If the admissible set is a pointed cone rather than a linear subspace, one scalar functional can reflect zero even when the cone spans an arbitrarily large space.

## Exact counterexample to the overstatement

Let

\[
C=\mathbb R_{\ge0}^N
\]

and

\[
\ell(x)=\sum_{i=1}^N x_i.
\]

Then

\[
x\in C,\quad \ell(x)=0
\quad\Longrightarrow\quad
x=0.
\]

The cone has full linear span of dimension \(N\), yet one scalar port is zero-reflecting on it.

The checker verifies this on every nonzero Boolean cone point through dimension eight. The signed vector

\[
(1,-1,0)
\]

shows why the conclusion fails on the linear span.

## Corrected trichotomy

The missing coherence may take one of three forms:

1. an operator-valued linear relation with rank growing alongside the moment module;
2. a source-selected lower-rank orbit;
3. a source-derived pointed cone, polarization, or ordered module on which the Evans functional lies in the interior of the dual cone.

The third option is exactly the orientation route and must not be excluded by linear dimension counting.

## Hard source gates

A cone claim is admissible only if:

- the real structure defining the cone is source-derived;
- the cone is preserved by spectral transport;
- prime shifts and complete seam jets preserve it or transport it covariantly;
- primitive, square, and archimedean currents are included;
- the endpoint functional is strictly positive on every nonzero admissible state;
- completion preserves pointedness and strict dual separation;
- hostile signed prime perturbations fail membership for a source-local reason.

Declaring coefficients positive after scalar projection is not a cone construction.

## Relation to Grothendieck's Green hostile

The universal Green identity lies in the quadratic ideal of the constructor graph and accepts an off-seam zero-state. It therefore supplies neither a new linear row nor a cone orientation.

The surviving nonlinear question is whether modular boundary or reciprocal matching restricts the actual theta states to a pointed subobject that excludes Grothendieck's signed hostile before scalar evaluation.

## DPC verdict

Candidate: finite scalar coherence repairs a growing linear image.

Verdict: rejected by the rank bound.

Candidate: one scalar is therefore always insufficient.

Verdict: retracted; false on a pointed cone.

Surviving candidate: derive a transport-stable pointed cone or ordered module from the labelled source, then test strict endpoint duality and completion stability.

## Finite falsifier

At a finite cutoff, present the cone by source-generated rays or inequalities. Find either:

- a nonzero admissible vector with zero endpoint readout;
- a prime or seam transport taking an admissible ray outside the transported cone;
- a signed hostile incorrectly admitted by the cone;
- a normalized cone sequence whose endpoint readout tends to zero at completion.

Any one closes the proposed orientation.
