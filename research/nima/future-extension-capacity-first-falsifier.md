# Future-Extension Capacity: First Falsifier

## Conjecture under attack

The Operator proposed that, when several developments remain possible, reality
selects the path allowing the greatest number of future trajectories.

The literal branch-count formulation is false.  Adding a null or purely
presentational branch changes cardinality without changing any physical
effect.  Moreover, two nonzero quantum outcomes can have Born weights
\(9/10\) and \(1/10\), whereas unweighted branch counting assigns \(1/2\) to
each.  Branch number is neither presentation invariant nor a probability law.

## Surviving object

The existing effect-algebra and Shannon-refinement results supply a canonical
replacement once a source defines:

* a finite exhaustive family of physical effects;
* positive normalized weights \(p_i\);
* admitted future refinements of each outcome.

For a finite horizon, define recursively

\[
\boxed{
C_T(h)
=H(p(\cdot\mid h))
+\sum_i p_i\,C_{T-1}(h_i).
}
\]

This is not raw trajectory count.  It is the Shannon entropy of the complete
typed future tree.  The checker verifies exactly that:

1. recursive evaluation equals leaf evaluation;
2. null refinement changes branch count but not \(C_T\);
3. independent future trees add their capacities, so
   \(N_{\rm eff}=e^{C_T}\) is multiplicative.

Thus \(C_T\) is a legitimate presentation-invariant candidate for
``effective future multiplicity'' wherever Marici already supplies a physical
effect algebra.

## Crucial correction

The capacity functional does not yet imply a selection law.  There are three
different assertions:

\[
\begin{array}{ll}
\textbf{A.} & \text{Typed future trees carry the capacity }C_T.\\
\textbf{B.} & \text{Physical dynamics favors actions with larger }C_T.\\
\textbf{C.} & \text{Individual outcomes are selected by their future capacity.}
\end{array}
\]

Our exact refinement calculus supports A.  B is an open causal-entropic
conjecture.  C is presently disfavored: outcome probabilities must descend
from the conjugate-doubled positive state/effect pairing and agree with Born
weights, not with branch counts.

A possible form of B is

\[
P(a\mid h)\propto W_{\rm source}(a\mid h)
\exp\!\bigl(\lambda C_T(h\circ a)\bigr),
\]

but \(\lambda\), the action space, the horizon, and even the exponential bias
are not derived and must not be fitted after inspection.

## Sharp next tests

1. **Scattering:** compute \(C_T\) from a source-defined sequence of Cut and
   detector-effect refinements; test whether it adds information beyond Born
   weights or merely repackages them.
2. **Flavor:** compute it on physical spectral-projector refinements, not
   sparse texture charts.
3. **Cosmology:** the conjecture remains untyped until an exhaustive physical
   effect family exists.
4. **Dynamics:** find two equally source-weighted admissible actions with
   unequal \(C_T\).  A reproducible transition bias toward the larger value,
   without fitting \(\lambda\), is the first evidence for B.

The surviving Deutsch–Popperian conjecture is therefore:

> Source dynamics may favor actions that preserve a larger invariant Shannon
> measure of coherently extendable physical effects, while individual outcome
> weights remain fixed by the positive state–effect pairing.

Certificate:
`research/nima/checkers/check_future_extension_capacity.py`
