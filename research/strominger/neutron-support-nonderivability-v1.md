# A proof boundary for reference-only neutron contraction

## Which claim can be proved?

The proposed isotope repair needs a guarded P->E operation whose occupied support excludes the intermediate N. We must not insert that operation as an assumption and then call its existence a derivation.

There are three separate claims:

1. The intermediate coefficient variable can be eliminated exactly.
2. The current support-labelled construction laws derive an operation not requiring N.
3. A physical source permits the corresponding isotope assembly.

Claim 1 is a theorem. Claim 2 is false for the specified native path and structural laws below. Claim 3 is not decided by this formalism. The following proofs make the boundary explicit rather than converting the experimental successes into an admission rule.

## Theorem 1: exact coefficient elimination

Let V be the five-coordinate response space and A,B:V->V the native PN and NE maps. Define

```
S = {(p,n,e): n=Ap and e=Bn},
T = {(p,e): e=BAp}.
```

The projection pi:S->T, `(p,n,e) -> (p,e)`, is an isomorphism of linear spaces. Its inverse is

```
(p,e) -> (p,Ap,e).
```

Both compositions are identities by substitution. No invertibility assumption is needed for this elimination theorem: n is already explicitly determined by p. For the actual maps A and B, which are invertible permutations, adding n=0 forces p=e=0.

Therefore omission of the n variable from an endpoint formula is justified. Setting its response to zero is a different operation. Neither assertion changes an occupied-support predicate, which is absent from S and T.

## Theorem 2: native structural laws cannot erase the N obligation

Use the existing witnessed path algebra:

- a reader identity has occupied support consisting of its body site;
- PN has occupied support {P,N};
- NE has occupied support {N,E};
- composition takes the union of occupied supports;
- reversal retains occupied support;
- the permitted structural equations are associativity, left/right identity, reversal of composition and double reversal.

Fix the intermediate body site n. For every arrow a define the Boolean witness

```
chi_n(a) = 1 if n belongs to its required occupied support, otherwise 0.
```

Then

```
chi_n(b after a) = chi_n(a) OR chi_n(b),
chi_n(reverse(a)) = chi_n(a).
```

Every structural equation preserves chi_n:

- associativity is associativity of OR;
- an endpoint identity adds no site absent from the arrow support, since endpoint body sites are already required;
- reversal of composition preserves the same union;
- double reversal changes no support.

Replacing an equal subterm inside a composite or reversed expression also preserves chi_n, by these two equations. Induction on a derivation therefore proves that any expression equivalent to the native PN;NE path under these laws still has chi_n=1.

The proposed contracted arrow with support {P,E}, on three distinct sites, has chi_n=0. Hence **no derivation using those laws equates the native path with the contracted arrow or removes its occupied-N requirement**.

This is an unbounded structural induction, not an extrapolation from thirty examples. The executable checks below audit that the recorded implementation satisfies its premises. The scope is the specified path and these laws; it does not rule out a different native path in another configuration or a larger bounded isotope search.

## Invertible maps are not invertible occupied histories

An important attempted escape is cancellation of an inverse pair. The source also has an inverse-PN coefficient map. For the local history

```
P -> N -> P,
```

the composite coefficient map is identity. But its occupied support is {P,N}, whereas the reader identity at P requires only {P}. Its word also records two operations rather than an empty history.

Thus the coefficient representation sends both histories to the same matrix, but is not faithful on occupied support. The existing supported-path algebra is not made into a groupoid merely because its coefficient matrices are invertible. Declaring this inverse pair equal to the reader identity would itself add a support-erasing quotient law.

The reader-reversing involution is also not silently treated as a dagger fixing objects; the current model explicitly transforms reader roles. The inverse-PN example uses the separately supplied native inverse map on the original reader types, not that identification.

## What would a conditional contraction theorem require?

One can explicitly extend the grammar with:

> A witnessed same-origin PN;NE pair, satisfying the exact shared edge, vacancy, selected-reader boundary and full-reference guards, may be interpreted as a boundary operation with occupied support {P,E} while retaining reference support {P,N,E}.

With that additional rule, the saved finite witnesses establish the four experimental isotope candidates, and the previously checked whole-assembly and coherence conditions apply. This is a valid **conditional admission statement**. It is not a proof of the added rule.

Alternatively, a separately defined operational semantics could identify the two supported histories. Such a semantics must justify why the occupied-body requirement is forgotten, not merely show that endpoint matrices coincide. It must also retain or independently enforce isotope counts, contacts, phase histories, rooted construction and exit conditions. Discarding the occupancy observable by definition cannot establish a claim whose subject is occupancy.

## What remains necessary for physical construction

The missing evidence is an independently sourced definition or mechanism that permits a nonzero reference-mediated response without an occupied neutron carrier. Current coefficient equations, grade zero, inverse recovery and reversal do not supply it.

This proof therefore does **not** admit N-14 or Ne-21 under the unchanged grammar. It also does not prove their physical impossibility. It identifies precisely which premise must change or be supplied before the experimental PE repair can be promoted.

Continuing the native Ne-21 origin-10 search remains logically separate. It could find another construction without making this proposed contraction derivable.

## Executable premise and cancellation audit

```
python research/strominger/checkers/check_neutron_support_nonderivability.py
```

The checker freshly replays the thirty-case coefficient/support audit and the independent isotope witness checks. For each local case it verifies the Boolean support witness, the native inverse-PN cancellation counterexample, identity/associativity/reversal laws and rejection of interpreting a support-erasing coefficient equality as a supported-path identity.

Receipt: `research/strominger/results/neutron-support-nonderivability/verification.json`. This is an exact executable premise audit accompanying a written inductive proof, not a proof-assistant formalization or a physical occupancy derivation. Production and viewer remain unchanged.
