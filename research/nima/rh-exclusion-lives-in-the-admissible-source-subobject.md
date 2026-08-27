# RH exclusion lives in the admissible source subobject

## Linear impossibility theorem

Let `H` be a complex vector space with dimension greater than one, and let

\[
e:H\longrightarrow\mathbb C
\]

be a nonzero linear scalar observer. Then

\[
\dim\ker e=\dim H-1,
\]

so `e` always vanishes on a nonzero state.

This remains true even if a constructor-generated observer family gives an
injective analysis map

\[
C:H\longrightarrow Y.
\]

Writing `e=qC` for a scalar projection `q` does not help. If the image of `C`
has dimension greater than one, it necessarily meets the hyperplane
`ker(q)` nontrivially.

Therefore complete linear observability and scalar zero exclusion are
categorically different properties.

## Exact two-dimensional witness

Take the complete observer analysis map

\[
C=I_2
\]

and the scalar projection

\[
q=(1,1).
\]

The analysis is perfectly conditioned and injective. Nevertheless,

\[
qC(1,-1)^T=0.
\]

No missing observer caused this zero. It is an allowed cancellation inside the
linear state space.

## Where exclusion can live

Let `S` be the source-derived admissible subobject of `H`. Scalar exclusion is
the separate transversality condition

\[
S\cap\ker(e)=\{0\}.
\]

This can hold only because `S` has structure not inherited from the ambient
complex vector space. Examples include:

- a pointed nonlinear cone;
- a distinguished constructor orbit;
- a multiplicative or Fock-semiring image;
- a source variety with an orientation law;
- a complex carrying a canonical contraction;
- a determinant section constrained by an independently derived index law.

The earlier hostile tests already show that ordinary positive measures and
reciprocal symmetry are insufficient choices of `S`.

## Categorical statement

The relevant square is not merely an observer factorization

\[
H\xrightarrow{C}Y\xrightarrow{q}\mathbb C.
\]

It includes an admitted monomorphism

\[
i:S\hookrightarrow H.
\]

The RH-strength property belongs to the pair `(i,e)`: the pullback of the zero
fiber of `e` along `i` must be the zero source state. Full faithfulness of `C`
does not imply this pullback property.

## DPC

For any proposed zero-exclusion mechanism, require:

1. an independently source-derived admissible subobject `S`;
2. proof that its inclusion into the analytic carrier survives completion;
3. an explicit calculation of `S` intersected with the scalar zero fiber;
4. a hostile signed or phase-cancelling source tested before scalar projection;
5. separation of observer completeness from source admissibility.

Reject:

- a claim that enough linear observers make one scalar projection nonzero;
- restriction to `S` defined using the zero set of the scalar;
- division by the completed scalar section;
- a positivity cone that admits the two-atom phase hostile;
- finite-cutoff transversality without completion stability.

## Consequence

The next RH object is not another observer. It is the exact constructibility
image of the labelled theta/Tate source inside the completed analytic state
space. The outstanding theorem must show that this nonlinear image cannot meet
the fixed Evans hyperplane off the seam.

