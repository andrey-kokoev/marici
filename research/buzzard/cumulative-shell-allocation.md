# Cumulative Weyl shell allocation: Lean packet

## Source boundary

This increment formalizes the integer allocation core of Grothendieck's
`cumulative-weyl-shell-rank-allocation.md`. It does not choose the continuous
Weyl counting function or its constant term.

## Formal objects and assumptions

`count : ℕ → ℤ` is an already declared cumulative integer count. The shell
rank is its forward difference

\[
m_k=count(k+1)-count(k).
\]

Monotonicity of `count` is the only assumption needed for nonnegative ranks.

## Theorems and hostile

- `cumulativeShellRank_nonnegative` proves every increment is nonnegative for
  a monotone cumulative count.
- `cumulativeShellRank_telescopes` proves the exact endpoint formula from
  zero to `n`.
- `cumulativeShellRank_window` proves the shifted-window version.
- `local_zero_ranks_do_not_reconstruct_growth` is a finite hostile showing
  that arbitrary local integer assignments do not inherit the cumulative
  endpoint law.

## Missing interfaces

The source specialization `count(k)=floor(F(k))` needs a real-valued Weyl law,
floor typing, and proof that the relevant range is monotone. Comparing the
floor endpoints with `F` needs the standard bounded fractional-part estimate.
The coefficient `1/(2*pi)`, the linear term, and especially the constant
`7/8` require an independently derived spectral counting theorem and boundary
or Maslov correction. Cumulative allocation transports that constant but does
not derive it.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/CumulativeShellAllocation.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
