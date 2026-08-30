# 1946 — The Cyclic Scalar Sees Only the Invariant (D_4) Logarithmic Block

## Question

Entry 1945 constructs five labelled logarithmic blocks.  Which part is seen
by the frozen cyclic scalar period, and what is its local connection residue?

## Occurrence decomposition

The labelled vanishing space is

\[
V_{\rm occ}=\mathbb Q[C_5]
\simeq
\mathbb Q_{\rm triv}\oplus I_{\rm aug},
\]

where (I_{\rm aug}\simeq\mathbb Q(\zeta_5)) has dimension four over
(mathbb Q).

The source scalar readout is the equal-weight augmentation covector

\[
\epsilon=(1,1,1,1,1).
\]

It obeys

\[
\epsilon(1,1,1,1,1)=5,
\]

while it vanishes on the basis

\[
e_0-e_1,quad e_1-e_2,quad e_2-e_3,quad e_3-e_4
\]

of (I_{\rm aug}).

Therefore the physical cyclic scalar sees exactly the trivial-character line
and kills the four-dimensional nontrivial-character sector.

## Invariant local connection

Let

\[
R=\sum_i r_i,qquad V=\sum_i v_i.
\]

Then

\[
N(R)=V,qquad N(V)=0,
\]

so in the ordered basis ((R,V)),

\[
\boxed{
N_{\rm inv}=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix},qquad
\operatorname{rank}N_{\rm inv}=1,qquad
N_{\rm inv}^2=0.
}
\]

Use the convention

\[
\nabla
=d-\frac{N_{\rm inv}}{2\pi i}\,d\log\tau.
\]

A positive loop around (	au=0) has monodromy

\[
T=\exp(N_{\rm inv})=I+N_{\rm inv}.
\]

The two local exponents are ((0,0)); their nontrivial extension, rather than
a semisimple exponent difference, produces the logarithm.

## Result

\[
\boxed{
\text{The frozen scalar period carries one rank-one unipotent }D_4
\text{ block.}
}
\]

The augmentation sector is real labelled coefficient data, but it is not
visible to this scalar observable.  Claiming a Fourier-weighted or other
nontrivial-character observable requires an independently derived
occurrence-sensitive source functional; it cannot be introduced merely to
retain those four directions.

## Next falsifier

Search the frozen five-site source for an already defined occurrence-sensitive
observable or residue vector whose readout covector has a nonzero component
on (I_{\rm aug}).  If none exists, classify the augmentation sector as
coefficient memory erased by the scalar port rather than additional physical
output.

## Evidence

- `research/benincasa/marici-gm/src/bin/five_site_d4_readout_decomposition.rs`
- `research/benincasa/results/five-site-d4-readout-decomposition.json`
- Entries 1883 and 1945
- allocator claim: `seqclaim-959924f122245634ac17eb66`

