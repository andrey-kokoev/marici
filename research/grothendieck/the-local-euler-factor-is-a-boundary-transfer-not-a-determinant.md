# The Local Euler Factor Is a Boundary Transfer, Not a Determinant

## Relation to Entry 3226

Entry 3226 already identified the bordered colligation

\[
(S_p,e_0,\varepsilon)
\]

and its transfer function. The present result sharpens its typing. Entry
3226's determinant-line language concerns the determinant of the derived
value--flux jet readout, whose scalar is built from the transfer function. It
does not mean that the internal valuation differential (I-aS_p\) has the
Euler factor as its determinant. The calculation below proves that its finite
determinant is identically one.

## Finite valuation truncation

Let (V_{p,N}\) have basis (e_0,\ldots,e_N\), with nilpotent shift

\[
S_{p,N}e_k=e_{k+1},
\qquad
S_{p,N}e_N=0.
\]

For (a=p^{-s}\), set

\[
d_{p,s,N}=I-aS_{p,N}.
\]

This matrix is triangular with every diagonal entry equal to one. Hence

\[
\det d_{p,s,N}=1
\]

for every (a\) and every cutoff (N\). It is always invertible, with

\[
d_{p,s,N}^{-1}
=\sum_{k=0}^{N}a^kS_{p,N}^k.
\]

No local Euler factor is present in its determinant or cohomology.

## Source input and boundary observation

Let the input be the endpoint state (e_0\), and let augmentation be the
observation

\[
\varepsilon_N\left(\sum_{k=0}^{N}c_ke_k\right)
=\sum_{k=0}^{N}c_k.
\]

The boundary transfer function is

\[
Z_{p,N}(s)
=\varepsilon_Nd_{p,s,N}^{-1}e_0
=\sum_{k=0}^{N}a^k
=\frac{1-a^{N+1}}{1-a}.
\]

For \(|a|<1\), the limit is the local Euler factor

\[
Z_p(s)=\frac{1}{1-p^{-s}}.
\]

Thus the local zeta factor is the transfer function of an exact
input--state--output system:

\[
e_0
\xrightarrow{d_{p,s}^{-1}}
v_{p,s}
\xrightarrow{\varepsilon}
Z_p(s).
\]

## Consequence for the zero bridge

The smallest source model rejects the proposed identification between a zeta
zero and cohomology of the valuation differential.

The differential remains invertible while its boundary transfer carries the
Euler factor. After global completion, a scalar zero is naturally a loss of
input--output transmission or destructive boundary interference, not
automatically a kernel of the internal differential.

A cohomological interpretation could still arise from a larger mapping cone
that includes the input and observation maps. But adjoining such a cone after
seeing the scalar transfer would be tautological. Its boundary ports and
differential must be derived independently from the source.

## Revised target

The correct global object should first be a completed conservative system:

1. source-labelled input ports;
2. direct and reciprocal valuation state spaces;
3. the local resolvent dynamics;
4. augmentation and archimedean observation ports;
5. a source-derived scattering or transfer matrix;
6. the scalar completed zeta section as one matrix coefficient.

RH would then require a conservation or minimality theorem showing that this
distinguished transfer coefficient cannot vanish off the simultaneous-loss
wall. Exactness of the internal state complex alone is insufficient.

## Finite falsifier

Any determinant model claimed to be derived from the valuation differential
must reproduce the finite transfer polynomial (1+a+\cdots+a^N\) while the
actual differential determinant remains one. If it inserts that polynomial by
an extra rank-one summand without independently deriving the input and output
ports, it has encoded the desired readout rather than explained it.
