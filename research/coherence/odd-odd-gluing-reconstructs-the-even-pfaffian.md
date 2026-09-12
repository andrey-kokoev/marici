# Odd boundary states glue to the even Pfaffian amplitude

## Setup

Split an ordered chain into two contiguous odd blocks of sizes \(2m+1\) and \(2n+1\). Its antisymmetric chain matrix has block form

\[
M=
\begin{pmatrix}
A&B\\
-B^T&C
\end{pmatrix},
\]

where \(A\) and \(C\) are odd antisymmetric matrices.

Let their canonical cofactor states be

\[
u_i=(-1)^i\operatorname{Pf}(A_{\widehat i}),
\qquad
v_j=(-1)^j\operatorname{Pf}(C_{\widehat j}).
\]

Then \(Au=0\) and \(Cv=0\).

## Why the sewing kernel has rank one

Every left point precedes every right point. For the exponential half-line kernel,

\[
B_{ij}=e^{-t(b_j-a_i)}
=e^{ta_i}e^{-tb_j}.
\]

Thus

\[
\operatorname{rank}B=1.
\]

This is the Markov/separation property supplied by the ordered interval between the two boundary configurations.

## Gluing identity

Pfaffian expansion of \(M\) could contain one, three, or more edges crossing between the blocks. Every contribution with more than one cross edge vanishes because the relevant minor of \(B\) has rank one. Exactly one cross edge remains. Summing its possible endpoints gives

\[
\boxed{
\operatorname{Pf}M=u^TBv.
}
\]

There is no residual normalization or sign in the declared contiguous orientation.

Therefore the two odd null lines are not merely analogous to states. Their boundary contraction exactly reconstructs the even amplitude:

\[
\boxed{
\text{odd state}\otimes\text{odd state}
\xrightarrow{\ B\ }
\text{even Pfaffian amplitude}.
}
\]

## Matching semantics

Each odd cofactor state records every possible unpaired primitive in its block. The rank-one sewing kernel pairs one left residual with one right residual. Pfaffian cancellation then leaves the adjacent matching of the combined ordered chain.

The global even closure is therefore assembled from local odd residuals without selecting representatives of their null lines.

## Consequence

This proves the key parity gluing law for contiguous ordered configurations. It upgrades the even/odd formulas from parallel identities to a compositional structure:

- even configurations assign scalar amplitudes;
- odd configurations assign one-dimensional state lines;
- interval sewing supplies the pairing between state lines;
- odd--odd sewing returns the even amplitude.

This is the minimal algebraic core expected of a one-dimensional fermionic boundary theory.

It does not yet establish a full bordism functor. Remaining coherence tests include associativity of repeated sewing, even--odd module transport, units, and compatibility with the varying Green trace fibers.

## Verification

The exact-rational checker tests 84 cases with odd block sizes from one through five. Every cross block has rank one and every case satisfies the gluing identity with sign \(+1\).

Run:

```text
python research/coherence/check_odd_odd_pfaffian_gluing.py
```

Artifacts:

- `check_odd_odd_pfaffian_gluing.py`
- `odd-odd-pfaffian-gluing.v1.json`
