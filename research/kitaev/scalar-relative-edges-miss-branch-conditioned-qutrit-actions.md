# Scalar relative edges miss branch-conditioned qutrit actions

Owner: `marici.Kitaev`

## Bounded question

Do three scalar branch-coherence edges plus one Choi-complete root-branch
anchor determine a branch-preserving controlled qutrit unitary?

## Verdict

No. The root Choi test fixes the qutrit action on one branch, while scalar
relative fringes tested on one data state constrain only that state's branch
phases. Other branches may carry different qutrit unitaries that fix the test
state.

The repaired unitary theorem requires:

```text
one Choi-complete root-branch test
+ three Choi-complete coherent edge comparisons
```

The `3+1` port count survives, but none of the four ports is merely scalar.
Each relative edge must compare the full branch-conditioned data process.

## Exact hostile unitary

Let the four branch labels be `0,1,2,3`, and let the qutrit basis be
`A_L,B_L,C_L`. Take branch zero as the common-mode anchor.

For real angles `theta_i`, define

\[
G_i
=
\operatorname{diag}
(1,e^{i\theta_i},e^{-i\theta_i}),
\]

with

\[
G_0=I
\]

and at least one nonzero `theta_i` for `i>0`.

The branch-preserving hostile is

\[
U_{hostile}
=
\sum_{i=0}^3
|i\rangle\langle i|_F
\otimes G_i.
\]

It is unitary, preserves every branch label, has no leakage, and needs no
environment beyond a common ray.

## Why the proposed tests pass

### Root Choi anchor

On branch zero, `G_0=I`. A complete Choi test of that branch reports the ideal
identity process exactly.

### Scalar spanning-tree edges

Prepare the qutrit anchor state `A_L` during each branch-interference test.
Every `G_i` fixes that state:

\[
G_i|A_L\rangle=|A_L\rangle.
\]

Therefore every edge visibility and phase on a spanning tree is ideal. The
returned environment is common, so the scalar environment-Gram test also
passes.

### Yet the instrument differs

On branch `i`, the state

\[
\frac{|B_L\rangle+|C_L\rangle}{\sqrt2}
\]

acquires relative phase `2 theta_i`. The implementation is a genuine
branch-conditioned qutrit operation, not the target common process.

This is the requested cross-factor correlated hostile: it lives jointly in
the relative branch factor and the nonanchored data subspace.

## Geometry of the missed subspace

The root Choi test constrains the complete data algebra at one branch. Scalar
edge tests constrain the complete branch tree at one data ray. Their union
does not constrain the tensor-product corner

```text
nonroot branch differences
tensor
data directions orthogonal to the scalar anchor
```

That corner contains the hostile controlled phases above.

This is a general tomography rule: complete marginals on two factors do not
determine their correlations unless a product or independence theorem has
already been proved.

## Choi-complete edge repair

Let `R` be a qutrit reference and prepare

\[
|\Omega\rangle
=
\frac1{\sqrt3}
\sum_{e=A,B,C}|e_L\rangle_V|e_L\rangle_R.
\]

For an edge joining branches `i,j`, coherently prepare the two branches while
the data-reference pair is in `Omega`. The two branch-conditioned output
vectors are

\[
(G_i\otimes I_R)|\Omega\rangle
\]

and

\[
(G_j\otimes I_R)|\Omega\rangle.
\]

Unit visibility with the declared relative phase holds exactly when

\[
G_j^*G_i
\]

is the required scalar multiple of the identity. Thus one Choi-complete edge
comparison identifies the entire relative unitary between its endpoint
branches.

A connected tree of three such edges propagates the root process to all four
branches. The root Choi test then fixes the common process itself.

## Exact repaired theorem for branch unitaries

Assume:

1. the operation is block diagonal in the four declared branches;
2. each branch block is a qutrit unitary;
3. there is no leakage or unreturned environment;
4. one root branch is Choi-certified against the target;
5. every edge of a connected branch tree is Choi-interferometrically certified
   against the target relative phase.

Then every branch block equals its target up to one common global phase, and
the complete controlled unitary is correct projectively.

The proof is propagation. The root fixes `G_0`. Each certified edge fixes
`G_j` relative to an already fixed neighboring block. Connectivity reaches
all branches.

## General-channel boundary

For noisy branch channels, ordinary Choi states of each diagonal branch do not
necessarily determine coherent off-diagonal branch maps. A controlled
instrument contains cross maps between branch sectors, not only four reduced
channels.

The full repair then requires process-tensor or superchannel tomography of the
edge coherence blocks. The unitary vector-interference theorem above is the
minimal exact case, not a theorem for arbitrary instruments.

This distinction matters when an environment carries coherent branch data
without changing the individual diagonal channels.

## Revised interpretation of three plus one

The tower counts incidence positions:

- one root position establishes the common constructor;
- three tree-edge positions establish its transport across four branches.

It does not count scalar observations. Each position inherits the coefficient
complexity of the object transported through it.

For qutrit unitaries, that object is a Choi vector. For general channels, it is
a complete process block. For scalar environment rays, it reduces to one
complex overlap.

The same branch geometry supports different coefficient lenses, and the lens
sets the tomography burden.

## Immediate programme consequence

The earlier three scalar fringes remain sufficient for environment-ray closure
only after the source proves that branch-conditioned action factorizes as

\[
U_{branch}\otimes G_{common}.
\]

Without that product theorem, the finite compiler must use Choi-complete edge
tests or explicitly retain the untested cross-factor kernel.

Thus the next microscopic calculation should first ask whether locality,
topological charge, or the frozen interaction Hamiltonian enforces product
factorization between branch and qutrit action. If not, upgrade the edge ports.

## Falsifiers

- The hostile `U_hostile` changes branch labels or leaks.
- Its root branch fails an identity Choi test.
- Its scalar edge fringes on `A_L` reveal any `theta_i`.
- It acts identically on `B_L/C_L` superpositions for nonzero `theta_i`.
- A Choi edge comparison has unit visibility when `G_j*G_i` is non-scalar.
- A connected tree plus fixed root fails to determine all unitary branch
  blocks up to common global phase.
- The unitary proof is promoted to arbitrary noisy instruments without testing
  off-diagonal process blocks.

## Claim boundary

This packet falsifies the mixed-strength certificate consisting of one
complete root anchor and three scalar edges. It repairs it exactly for
branch-preserving unitary blocks with no leakage or environment.

The new remaining question is whether the physical `D(S3)` constructor has a
source-derived product-factorization theorem that permits scalar edges, or
whether its relative ports must be Choi-complete.

No build, checker, or Git operation was used.
