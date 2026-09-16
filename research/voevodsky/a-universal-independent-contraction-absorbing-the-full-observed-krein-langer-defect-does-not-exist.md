# A universal independent contraction absorbing the full observed Krein--Langer defect does not exist

## Step-3 target

The proposed third step asked for an independently constructed contraction

\[
C_r:
\mathcal H_{S,r}
\to
\mathcal H_{B,r}
\]

such that

\[
A_{B,r}
=C_rA_{S,r}
\]

and

\[
\|C_r\|\le1.
\]

Step 2 shows that the source observes the full model-space defect \(K_B\) in every convolution degree. Therefore any universal contraction must absorb every admissible Krein--Langer defect direction.

## Hostile reflected multiplier

Let \(B\) be a nonconstant finite Blaschke product and take the Schur numerator

\[
S=1.
\]

Then

\[
\Theta=B^{-1}S=B^{-1}
\]

is meromorphic with unimodular boundary values.

The Schur kernel of the constant function \(S=1\) is zero:

\[
K_S(z,w)=0.
\]

The Blaschke kernel is nonzero:

\[
K_B(z,w)
\neq0.
\]

Krein--Langer decomposition gives

\[
K_\Theta(z,w)
=
-
\frac{K_B(z,w)}
{B(z)\overline{B(w)}}.
\]

Thus the positive feature \(A_S\) vanishes while the defect feature \(A_B\) does not.

## Source detection

Translated Gaussian observers detect every direction of \(K_B\). Hence for every convolution degree \(r\), there exists \(p\in E_r\) such that

\[
A_{B,r}p
\ne0.
\]

But

\[
A_{S,r}p=0
\]

for every \(p\).

No linear map \(C_r\) can satisfy

\[
A_{B,r}=C_rA_{S,r}.
\]

This fails before contractivity is considered.

## Consequence

There is no universal source operation that absorbs the full Krein--Langer defect for every reflected multiplier in the admitted meromorphic class.

Convolution-degree naturality, endpoint augmentation, and lattice coherence cannot change this fact. The hostile kernel has a genuinely observed negative direction and no positive Schur capacity.

## Partial-constructor formulation

The correct Step 3 is a partial constructor.

Given \((A_S,A_B)\), first test the kernel inclusion

\[
\ker A_S
\subseteq
\ker A_B.
\]

If it fails, no factorization exists.

If it holds, define the canonical range map

\[
C_0(A_Sp)=A_Bp.
\]

This map extends to a contraction exactly when

\[
A_B^*A_B
\preceq
A_S^*A_S.
\]

Thus the constructor either:

1. returns the unique source-labelled Douglas contraction on generated ranges; or
2. refuses with a kernel or norm-domination witness.

It cannot manufacture the norm bound from coherence data.

## Independently contractive special cases

An independent contraction can still exist on a restricted class when an ambient source operation is identified before the kernel comparison.

Examples of admissible mechanisms include:

1. orthogonal projection onto a source-invariant defect sector;
2. conditional expectation onto a reducing subalgebra;
3. a Markov transfer known independently to be contractive;
4. an isometric correspondence whose target projection is the defect feature.

For endpoint-only index one, odd-parity projection is such a candidate. Step 2 shows that it is insufficient when \(K_B\) contains additional observed directions.

## Retained-defect alternative

When the partial constructor refuses, the correct coherent object is not a falsely positive quotient. Retain the defect explicitly:

\[
\Phi_r^{KL}
=
A_{S,r}
\oplus
A_{B,r}
\]

with fundamental symmetry

\[
J=I\oplus(-I).
\]

Its signed readout is exact, its source observation is faithful, and its degree successors remain natural.

This gives a completed Pontryagin/Krein feature even when positive absorption fails.

## Step-3 disposition

Step 3 cannot be completed as a universal construction. It is false on the explicit hostile family

\[
\Theta=B^{-1}
\]

with nonconstant \(B\).

The valid replacement is:

1. a partial Douglas constructor on inputs satisfying source Gram domination;
2. explicit retention of the full negative model-space feature on refused inputs;
3. independent contraction proofs only on source-restricted subclasses where a genuine ambient contraction is available.

## Impact on Step 4

Successor extension is automatic after the partial constructor accepts, because the canonical source-labelled contractions agree on nested generated ranges.

On refused inputs, Step 4 extends the signed Krein feature rather than a positive quotient.

Thus graph completion and successor coherence remain available in both branches, but positive defect absorption is conditional rather than universal.
