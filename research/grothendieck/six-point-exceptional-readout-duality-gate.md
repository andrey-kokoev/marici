# Six-point exceptional readout duality gate

Author: `marici.Grothendieck`  
Date: 2026-08-20  
Status: exact underdetermination theorem

## Question

The six-point exceptional shift module has rank eight, strict reflection
covariance, and trivial cyclic holonomy. Do these coefficient-level facts
force the missing physical pairing

\[
\mathcal N_{\rm shift}\otimes\Gamma_{\rm source}
\longrightarrow\mathbb C?
\]

They do not. They constrain one variance of the pairing but provide neither
the other representation nor the comparison map.

## Formal duality is tautological

Let `R_N(g)` be any invertible coefficient representation. One can always
invent the contragredient representation

\[
R_{\rm formal}(g)=R_N(g)^{-T}
\]

and pair it with `N_shift` by evaluation. The identity matrix then satisfies

\[
R_N(g)^T I R_{\rm formal}(g)=I.
\]

This constructs an invariant algebraic pairing for every representation. It
uses no string source cycle, KLT chamber, Betti class, or physical
normalization. Consequently its success contains no evidence that the formal
dual is `Gamma_source`. Installing it would fit the missing datum by hand.

## Exact underdetermination

The companion checker uses an exact rank-eight dihedral control: two cyclic
three-orbits and two fixed directions, with a reflection conjugating the
rotation to its inverse. The frozen coefficient action admits two different
partner completions:

1. the formal contragredient partner with a perfect invariant evaluation
   pairing of rank eight;
2. a trivial partner action, for which covariance restricts every pairing
   column to the four-dimensional invariant subspace, so every covariant
   pairing has rank at most four.

Thus the same coefficient covariance is compatible both with a perfect
pairing and with a rank deficit

\[
\boxed{8-4=4}.
\]

The coefficient module alone cannot choose between them. Reflection
covariance and cyclic holonomy therefore do not determine physical descent.

## Exact missing datum

The next source packet must supply all four items:

1. a global source-derived cycle module `Gamma_source`;
2. its action matrices `R_Gamma(g)` for the same cyclic and reflection
   generators acting on `N_shift`;
3. a source-normalized pairing matrix `P`; and
4. the physically required nonzero or nondegeneracy condition.

Only then is the covariance defect typed:

\[
D_g=R_N(g)^T P R_\Gamma(g)-P.
\]

It suffices to test a generating set. If every `D_g` vanishes and `P` has the
required rank, the induced physical observable can be tested on commutator
generators. A nonzero defect or a physical commutator action falsifies the
exceptional readout shadow.

## Relation to the all-arity disk theorem

The ordinary source-normalized disk-period character already factors through
dihedral abelianization at every arity, including `n=6`. This packet does not
weaken that result. It isolates the separate rank-eight exceptional module,
whose coefficient covariance is richer and whose global pairing remains
unconstructed.

## Verdict

\[
\boxed{
\text{coefficient covariance}
\not\Rightarrow
\text{source-derived physical pairing}.
}
\]

The six-point exceptional commutator quotient remains untyped. The sharp next
action belongs at the source/Betti comparison boundary, not in a formal dual
completion and not in the closed Carrier operation inventory.

Artifacts:

- `research/grothendieck/checkers/six_point_exceptional_readout_duality_gate.py`;
- `research/grothendieck/results/six-point-exceptional-readout-duality-gate.json`.

No ledger entry is claimed.
