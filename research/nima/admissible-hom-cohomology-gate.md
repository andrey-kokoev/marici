# Coherence must be computed in the admissible Hom subcomplex

## Refinement

The vanishing of ordinary

\[
H^{-j}\operatorname{Hom}(C,\bar C)
\]

is not sufficient to flatten authority-bearing coherence.  The Hom
complex contains algebraic maps that may violate support, resource,
temporal, modality, or fault-model constraints.

Let

\[
\operatorname{Hom}_{\rm adm}^k(C,\bar C)
\subseteq
\operatorname{Hom}^k(C,\bar C)
\]

contain exactly the comparison cells admitted by the active contracts.
Before cohomology is meaningful, admissibility must be stable under the
Hom differential:

\[
\boxed{
\partial\operatorname{Hom}_{\rm adm}^k
\subseteq
\operatorname{Hom}_{\rm adm}^{k+1}.
}
\]

Safe first-level flattening then requires

\[
\boxed{
H^{-1}\operatorname{Hom}_{\rm adm}(C,\bar C)=0,
}
\]

not merely vanishing in the unrestricted complex.

## Minimal hostile witness

Over (mathbf F_2), take the unrestricted segment

\[
H^{-2}=\langle u\rangle
\xrightarrow{\partial_{-2}=1}
H^{-1}=\langle z\rangle
\xrightarrow{\partial_{-1}=0}
H^0.
\]

Unrestricted cohomology vanishes because (z=\partial u).

Now impose a support or fault contract that forbids (u) while allowing
(z).  The admissible segment becomes

\[
0\longrightarrow\langle z\rangle\xrightarrow{0}H^0,
\]

so

\[
\dim H^{-1}_{\rm adm}=1.
\]

The same path ambiguity is algebraically fillable but not admissibly
fillable.  Ordinary cohomology produces a false flattening certificate.

## Two distinct rejection modes

1. **Not a subcomplex.** An admitted cell has a differential that is not
   admitted.  The policy typing is incoherent and cohomology must not be
   computed.
2. **Nonzero admissible cohomology.** The admissible spaces form a
   subcomplex, but an ambiguity has no admissible higher filler.

```json
{
  "code": "admissible_coherence_obstructed",
  "ordinary_dimension": 0,
  "admissible_dimension": 1,
  "excluded_filler": "u",
  "exclusion_basis": "fault_or_support_contract"
}
```

## Sector consequences

- A Byzantine-domain comparison cannot use a filler whose proof assumes
  crash-only non-equivocation.
- A source-wall direct image cannot use a gradient-pivot homotopy outside
  the admitted wall complex.
- A logical schedule equivalence cannot use a physical transition that
  exceeds the declared common-cause support.
- An operator comparison cannot use scalar trace directions erased by
  its source-local typing.

## Compiler protocol

1. Build the full typed Hom matrices.
2. Intersect each degree with the active admissibility predicates.
3. Verify differential closure.
4. Compute cohomology ranks only in that subcomplex.
5. Name every excluded filler and the contract excluding it.
6. Require separate source authority for the final flattening action.

This prevents algebraic transport from manufacturing authority.

