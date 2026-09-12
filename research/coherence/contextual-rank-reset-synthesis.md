# Contextual rank reset: current synthesis and claim ledger

## Core statement

A presented structure is reduced relative to an admitted context family. Contractible relations contribute a torsion certificate; persistent homology inherits incoming and outgoing interfaces. The resulting typed residual is reusable exactly to the extent that its complete contextual behavior factors through those interfaces.

```text
presented structure
-> contextual defect
-> contractible part + residual
-> torsion certificate + typed interface
-> minimal reusable realization
```

This is atemporal. The arrows express factorization and dependence, not physical succession.

## Three independent ranks

The word `dimension` must be replaced by three separate ranks.

| Rank | Meaning | Present example |
|---|---|---|
| constructor rank | independent discrete generators admitted by the source | number of selected prime axes |
| orbit rank | independent continuous symmetry directions seen after representation | one logarithmic translation generator |
| realization rank | minimal state dimension reproducing complete admitted behavior | one for oriented sewing; generically two after reversal |

Prime transport illustrates the distinction:

\[
M(p)=\operatorname{diag}(p,p^{-1})
=\exp((\log p)A),
\qquad A=\operatorname{diag}(1,-1).
\]

Arbitrarily many prime generators map to one continuous orbit direction. The discrete valuation action remains faithful by unique factorization, while stationary incoming/outgoing behavior occupies a two-dimensional carrier.

## Finite mathematical core

For ordered half-line shifts, boundary failure of shift/adjoint cancellation gives

\[
K_{j,i}=R_jS_i-S_iR_j.
\]

Cubical alternation produces

\[
\mathcal F_{ij}=K_{j,i}-K_{i,j},
\]

an operator-valued antisymmetric two-cochain satisfying the finite Bianchi identity.

Endpoint evaluation on exponentials yields the chain kernel

\[
M_{ij}(t)=\operatorname{sgn}(a_j-a_i)e^{-t|a_j-a_i|}.
\]

Its even Pfaffian is the adjacent minimum-matching amplitude; its odd Pfaffian cofactors span the residual line. Exact triangular congruence reduces it to adjacent hyperbolic pairs plus one zero line at odd size.

Thus:

```text
even rank -> Pfaffian torsion
odd rank  -> one residual homology line
```

## Residual recurrence

Writing chain coordinates as \(y_i\), an odd cofactor state \(u\) inherits

\[
q_{\rm out}(u)=\sum_i u_i/y_i,
\qquad
q_{\rm in}(u)=\sum_i u_i y_i.
\]

For contiguous odd blocks,

\[
u_L^TBu_R=q_{\rm out}(u_L)q_{\rm in}(u_R).
\]

Therefore the microscopic block can be replaced, for the frozen sewing protocol, by its bicharged residual line.

This statement is protocol-relative. The complete type is determined by the stabilized two-sided context Hankel matrix

\[
H_X(u,v)=\operatorname{Observe}(uXv).
\]

When finite and context-closed,

\[
\dim T_X=\operatorname{rank}H_X.
\]

A finite rank-one pairing table is only a corner of this complete behavior.

## Context completion

Orientation reversal swaps incoming and outgoing charges. If reversal is typed between oriented fibers, each fiber remains one-dimensional. If reversal must be an endomorphism of one stationary carrier, the generic minimal type doubles:

\[
T=L_{\rm in}\oplus L_{\rm out}.
\]

Translation and reversal act by

\[
M(z)=\operatorname{diag}(z,z^{-1}),
\qquad
R=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

with

\[
R^2=I,
\qquad RM(z)R=M(z)^{-1}.
\]

They preserve the hyperbolic metric and generate the displayed \(O(1,1)\)/Clifford module. Pfaffian reversal of an odd microscopic block descends exactly to this residual charge swap.

## Graph and refinement layer

Signed log-prime shifts do not preserve one locally finite broken-Sobolev line. The correct finite object is a varying graph bundle

\[
B\mapsto(\mathcal D_B,\mathcal T_B,J_B).
\]

Adding a breakpoint is not an equivalence. It is an exact jump extension

\[
0\to\mathcal D_B\to\mathcal D_C
\to\bigoplus_{c\in C\setminus B}\mathbb C_c\to0.
\]

Right extension transports jump triangles exactly and retypes the old endpoint as a new seam jump. Left compression is natural only relatively: crossed seams remain in its declared compression cofiber.

## Categorical skeleton

The finite source is a nonsymmetric ordered metric monoidal category. The target consists of based skew self-dual complexes with:

- incoming and outgoing boundary lines;
- Pfaffian determinant data;
- homological parity;
- exact jump cofibers.

Elimination orders reach the same minimal object. Their canonical comparisons form a thin groupoid: all tested comparison cocycles and loops are strictly trivial. Ambient symplectic topology is not imported without additional path or lift data.

The Cubical Agda module `BoundaryPfaffianRankReset.agda` checks the abstract square

```text
Min ~= Retype o Reconcile o Expose
```

and contextual behavior preservation. It does not instantiate the fields with the finite Pfaffian model or assert automatic self-recursion.

## Claim ledger

### Proved algebraically in the documented finite model

- chain-kernel Pfaffian adjacent-matching identity;
- odd Pfaffian-cofactor null vector;
- adjacent hyperbolic normal form;
- even-cut factorization and unit;
- odd--odd sewing through a rank-one cross block;
- even action on odd residual lines;
- bicharged residual sewing factorization;
- reversal/translation relations and hyperbolic metric preservation;
- Pfaffian reversal intertwining with residual charge swap;
- breakpoint jump exact sequence and surviving-shift jump identities.

### Executably verified finite evidence

- four-prime cubical census and oriented boundary identities;
- nonzero mixed half-line residuals;
- four- and six-rank endpoint matching behavior;
- permutation covariance;
- elimination comparison cocycles;
- trace-fiber and refinement incidence counts;
- context-rank growth under reversal.

### Constructed abstractly but not yet instantiated end-to-end

- ordinary categorical source and skew-boundary target;
- rank-reset validity square in Cubical Agda;
- varying graph diagram as the target of the full Pfaffian sewing operation.

### Open

- stabilization under the complete constructor alphabet;
- infinite-prime and unbounded-depth completion;
- continuity of determinant/Pfaffian lines over that completion;
- an Agda construction of the chain minimalization theorem;
- a universal higher functor including graph recollement;
- any physical realization.

### Rejected or corrected

- identifying powers alone with a simplicial nerve;
- treating the first degree-zero anticommutator as a two-form curvature;
- claiming the six-face P4 compression was a complete intersection pairing;
- treating arbitrary refinement as an equivalence;
- inferring Maslov holonomy from nonidentity symplectic comparison matrices;
- claiming static rank-one sewing behavior determines the complete context type;
- calling the metric, parity-polarized construction an ordinary TQFT.

## Next executable program

Before adding more conceptual layers:

1. define the admitted constructor alphabet explicitly;
2. compute finite context Hankel ranks by depth;
3. test stabilization and congruence under every generator;
4. instantiate `BoundaryPfaffianRankReset.agda` with the finite chain model;
5. only then formulate the stable/higher completion.
