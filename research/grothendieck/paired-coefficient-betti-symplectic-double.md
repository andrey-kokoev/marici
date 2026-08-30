# A perfect coefficient--Betti pair canonically supplies a symplectic double

Epistemic-graph event: 1397.

## Algebraic phase space

Let `C` be a finite free coefficient module, `B` a finite free Betti module,
and suppose the source-derived evaluation pairing

`< , >:C x B -> Z`

is perfect.  On

`V=C direct_sum B`

define

`omega((c,b),(c',b'))=<c,b'>-<c',b>`.

Then `omega` is integral, alternating, and nondegenerate.  Both `C` and `B`
are complementary Lagrangian submodules.  No basis or numerical matrix is
required.

For a finite regular fiber `X`, the canonical pair

`C=Fun(X,Z)`, `B=Z[X]`

is perfect, so the coefficient--Betti Mackey object has a canonical integral
symplectic double of rank `2|X|`.  In the pointed rank-one specialization it
is the standard unimodular plane.

## Heisenberg extension

The alternating form canonically defines an integral Heisenberg extension;
at Lie-algebra level its cross commutator is

`[c,b]=<c,b> z`.

Thus the paired formalism does derive the algebraic precursor of conjugate
position and momentum polarizations.  Ledger 1368's statement that no *real*
Heisenberg phase space is currently supplied remains correct: passing to a
Hilbert representation and setting the central generator to `i hbar` require
an archimedean central character and analytic completion.

## What this repairs

The `xp` candidate no longer needs an arbitrary algebraic symplectic form.
The coefficient and Betti legs themselves provide one whenever their pairing
is perfect.  Their unimodular lattices also provide a natural self-duality
constraint on any cutoff lattice.

## What remains missing

The symplectic double does not select:

1. an ordered positive cone in either Lagrangian;
2. real half-line coordinates;
3. the value of `hbar` or a Stone--von Neumann representation;
4. cutoff projectors `x>=ell_x` and `p>=ell_p`;
5. a self-adjoint simultaneous boundary law; or
6. the `1/8` boundary/Maslov correction and fluctuating prime trace.

If the physical coefficient--Betti pairing has a radical, only the quotient
by the radical is symplectic; the earlier radical-repair and physical-chain
gates remain active.

## Verdict

The source-derived phase-space gate is partially positive: a perfect paired
Mackey fiber canonically yields the integral symplectic double required by
dilation dynamics.  The analytic polarization, positivity, quantization, and
dual cutoffs remain new obligations.

## Scope

This is an algebraic theorem.  It does not construct the unavailable physical
relative-chain pushforward or a Hilbert--Polya operator.
