# 905 — The Six-Point Dense-to-Block Transition Has Balanced Channel Divisor

## Frozen presentations

Entries 903 and 904 use the same left open-string amplitude basis:

\[
L=(123456,124356,132456,134256,142356,143256).
\]

The sparse intersection presentation uses the right basis

\[
B=(153462,154362,152463,154263,152364,153264),
\]

while the standard momentum-kernel presentation of arXiv:1010.3933 uses

\[
D=(562341,562431,563241,563421,564231,564321).
\]

Let \(M_{\rm block}\) be Entry 903's intersection matrix, let

\[
K_{\rm block}=M_{\rm block}^{-1},
\]

and let \(K_{\rm dense}\) be Entry 904's momentum kernel.

Because the left basis is literally identical, the right-basis transition is forced:

\[
\boxed{
T=M_{\rm block}K_{\rm dense}.
}
\]

It obeys

\[
K_{\rm block}T=K_{\rm dense}.
\]

No projection, fitted section, or comparison of unrelated ranks enters this definition.

## Determinant divisor

From Entry 904,

\[
\begin{aligned}
\operatorname{div}\det K_{\rm dense}
={}&2(s_{12}+s_{13}+s_{14}+s_{23}+s_{24}+s_{34}+s_{1234})\\
&+s_{123}+s_{124}+s_{134}+s_{234},
\end{aligned}
\]

where each symbol denotes the divisor of its corresponding sine factor.

From the three labelled blocks of Entry 903,

\[
\begin{aligned}
\operatorname{div}\det K_{\rm block}
={}&2(s_{12}+s_{13}+s_{14})\\
&+(s_{23}+s_{24}+s_{34})\\
&+2(s_{25}+s_{35}+s_{45})\\
&+(s_{235}+s_{245}+s_{345}).
\end{aligned}
\]

Therefore

\[
\begin{aligned}
\operatorname{div}\det T
={}&s_{23}+s_{24}+s_{34}
+s_{123}+s_{124}+s_{134}+s_{234}
+2s_{1234}\\
&-2s_{25}-2s_{35}-2s_{45}
-s_{235}-s_{245}-s_{345}.
\end{aligned}
\]

The pivot channels cancel exactly:

\[
\operatorname{ord}_{s_{12}}\det T
=
\operatorname{ord}_{s_{13}}\det T
=
\operatorname{ord}_{s_{14}}\det T
=0.
\]

The total zero and pole orders are balanced:

\[
\deg(\det T)_+=9,
\qquad
\deg(\det T)_-=9.
\]

## Narrow result

The canonical dense-to-block transition is a degree-zero rational transformation whose determinant divisor is supported entirely on existing factorization channels:

\[
\boxed{
\operatorname{Supp}(\operatorname{div}\det T)
\subseteq
\mathcal A_{\rm channel}.
}
\]

No nonchannel gluing divisor is required.

The checker and packet are

research/benincasa/marici-gm/src/bin/string_six_point_basis_transition_divisor.rs

and

research/benincasa/string-six-point-basis-transition-divisor.json.

## Interpretation

The dense and sparse formulae are not related by a globally regular basis change. Their right-cycle lattices differ by positive and negative modifications on ordinary channel walls. This is the string analogue of a Hecke modification, but all modifications remain on the frozen associahedral carrier.

Thus the correct strengthening of Entry 904 is not

\[
\text{the two coefficient matrices are globally identical},
\]

but

\[
\boxed{
\text{they are rationally equivalent through channel-supported lattice modifications}.
}
\]

## Scope boundary and next falsifier

The determinant divisor does not prove matrix-level residue coherence. The next test must retain the complete transition matrix and compare the two iterated residue maps at a mixed zero/pole corner, for example

\[
s_{23}=0,
\qquad
s_{235}=0.
\]

The order of specialization and the orientation of both residue normals must be frozen. A surviving commutator there would be a genuine coherence obstruction even though the determinant support is ordinary.
