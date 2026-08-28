# The Nested Brunnian Hostile Is Fillable, Not a Homotopy Residue

## Audit target

The family

\[
\beta_n=[C_{n-2},P^{-1}]
\]

is nontrivial and killed by every deletion map. Does it represent the
irreducible class in \(\pi_{n-1}(S^2)\)?

## Correction

No. The word is constructed as an iterated commutator using every peripheral
deletion-kernel subgroup. It therefore lies in the symmetric-commutator
subgroup that forms the kernel of the spherical Brunnian-to-homotopy map.

Consequently

\[
\beta_n\ne1
\quad\text{in the raw braid group},
\qquad
[\beta_n]=0
\quad\text{in the homotopy-residue quotient}.
\]

## What remains true

The family proves that literal reconstruction of the full braid from all
proper marginals fails at every arity. It does not prove that a new primitive
homotopy port is needed at every arity. Under a grammar that identifies
authorized higher fillings, \(\beta_n\) is fillable.

The two objectives must remain distinct:

```text
literal braid faithfulness       must retain beta_n
faithfulness modulo fillings     may quotient beta_n
```

## New open constructor

To exhibit a genuine next-level residue, one must construct an explicit
spherical Brunnian braid whose class is nonzero under

\[
\operatorname{Brun}_n(S^2)\longrightarrow\pi_{n-1}(S^2).
\]

For \(n=5\), the target is \(\pi_4(S^2)\cong\mathbb Z/2\), but the nested
commutator already constructed is not its generator.

## Verification

```powershell
uv run python research/strominger/checkers/nested_brunnian_is_fillable_not_residual_checks.py
```
