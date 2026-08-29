# Source energy selects the realizable restricted inverse limit

## Essential correction

Stable observation does not imply realization of the raw algebraic inverse limit.

Let
\[
\Phi:E_\infty\longrightarrow\varprojlim_F E_F
\]
send a completed effective source residue to its compatible finite shadows. Even when the joint frame is an isometry, the raw inverse limit can contain compatible families of infinite source energy.

The target of the realization theorem must therefore be fixed by the source topology and aggregation constructor before any source state is inspected.

## Three distinct objects

For a frozen cofinal finite inventory system, distinguish:

1. the raw algebraic inverse limit
   \[
   L_{\mathrm{alg}}=\varprojlim_F E_F;
   \]
2. the bounded-energy restricted inverse limit
   \[
   L_{\mathrm{en}}
   =
   \{x=(x_F)\in L_{\mathrm{alg}}:\mathcal E(x)<\infty\};
   \]
3. the completed source image
   \[
   L_{\mathrm{src}}=\Phi(\widehat E_\infty).
   \]

The correct source-realization theorem is
\[
L_{\mathrm{src}}=L_{\mathrm{en}},
\]
not \(L_{\mathrm{src}}=L_{\mathrm{alg}}\).

The energy functional \(\mathcal E\) is part of the frozen instrument specification. It cannot be reverse-engineered from which compatible families happen to be source-realizable.

## Nested orthogonal quotients

Suppose
\[
E_m\cong R_m,\qquad
R_m\subset R_{m+1},
\]
with orthogonal restriction maps. For a compatible family \(x=(x_m)\), define
\[
\mathcal E(x)=\sup_m\|x_m\|^2.
\]
Then completeness gives:

> A compatible family is represented by a unique vector in the completed source space exactly when \(\sup_m\|x_m\|<\infty\).

The finite shadows form a bounded Cauchy-compatible net in the increasing reachable sectors. Their limit reconstructs the source vector.

## General Gram systems

For nonorthogonal observers, each finite inventory carries a source-derived positive quadratic form
\[
q_F(x_F)=\langle Q_Fx_F,x_F\rangle.
\]
The restriction maps must satisfy energy monotonicity or a declared coherent comparison law. Define
\[
\mathcal E(x)=\sup_{F\in\mathfrak F}q_F(x_F)
\]
or the corresponding frozen weighted aggregation when the system is not nested.

The realization theorem now has two independent parts:

1. **energy completeness:** every compatible family with finite \(\mathcal E\) is represented by a completed source residue;
2. **stable inversion:** the source norm and frozen observation energy are uniformly equivalent on \(G_\infty^\perp\).

The first removes bounded-energy surplus. The second controls the reconstruction condition number. Neither implies the other without proof.

## Hostile I: perfect conditioning with raw surplus

Take \(N=\ell^2(\mathbb N)\),
\[
G_m=\{n:n_1=\cdots=n_m=0\},
\qquad
E_m\cong\mathbb C^m.
\]
The raw inverse limit is
\[
L_{\mathrm{alg}}\cong\mathbb C^{\mathbb N},
\]
all scalar sequences. The completed source image is only
\[
L_{\mathrm{src}}\cong\ell^2(\mathbb N).
\]

With unweighted coordinate observation, the global frame operator is
\[
A=I.
\]
Conditioning is perfect, yet \(\Phi\) is not onto \(L_{\mathrm{alg}}\). The bounded-energy restriction
\[
\sup_m\sum_{k=1}^m|x_k|^2<\infty
\]
selects exactly \(\ell^2\), so
\[
L_{\mathrm{en}}=L_{\mathrm{src}}.
\]

This is pure raw inverse-limit surplus without topology loss.

## Hostile II: weighted topology loss

Use weights \(a_k=1/k\). The observation energy becomes
\[
\sum_{k\ge1}\frac{|x_k|^2}{k^2},
\]
and the frame operator on the original source norm satisfies
\[
Ae_k=\frac1{k^2}e_k.
\]
Now \(\ker A=0\) but \(\inf\sigma(A)=0\). Observation separates source vectors, while stable inversion fails and the source image is not closed in the weaker observation norm.

This is topology loss. It is distinct from the unavoidable raw surplus of all unrestricted scalar sequences.

If the weighted energy is declared as the new source topology and completed, the source object itself changes. That may be legitimate only through an explicit authority transition; it cannot silently repair the original realization theorem.

## Correct finite-inventory comparison theorem

Fix:

- the observer-theory version;
- a cofinal inventory family;
- aggregation weights;
- target topology;
- source quadratic energy;
- completion functor.

Then prove:

1. \(\Phi\) embeds the completed source quotient into \(L_{\mathrm{alg}}\);
2. its image is exactly \(L_{\mathrm{en}}\);
3. the joint observer frame has uniform lower and upper bounds on the source quotient;
4. the bounds are uniform in cutoff and compact \(s\)-sets;
5. theory extension transports both the energy restriction and the effective residue system.

An isometry identifies source energy and observer energy exactly. A frame equivalence gives a bounded topological isomorphism. Neither licenses surjectivity onto \(L_{\mathrm{alg}}\).

## RH interface

The categorical RH tower now has three completion gates:

1. **source realization:** finite compatible shadows satisfy the frozen bounded-energy condition and reconstruct one completed source residue;
2. **observer stability:** reconstruction has a uniform frame margin;
3. **spectral stability:** the realized Birman–Schwinger family remains uniformly separated from generalized eigenvalue \(1\).

Raw inverse-limit surplus is not itself an RH defect; it consists of formal shadows outside the declared source-energy class. The defect is a bounded-energy compatible shadow without a source realization, or a realized shadow whose reconstruction margin collapses.
