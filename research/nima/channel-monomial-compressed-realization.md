# Channel-monomial compressed Catalan realization

The orbit-tagged construction can be compressed from one seed per triangulation orbit to one generator per polygon channel.

Let `D_n` be the set of polygon diagonals and define the squarefree channel algebra

\[
A_n=\mathbb C[x_d:d\in D_n]/(x_d^2:x\in D_n).
\]

Map a triangulation to its channel monomial

\[
\Phi_n(T)=\prod_{d\in T}x_d.
\]

This is injective because a triangulation is its diagonal set. Cutting into rooted subtrees partitions that set, so gluing becomes multiplication:

\[
\Phi_n(T_L\cup T_R)=\Phi_n(T_L)\Phi_n(T_R).
\]

Quarter rotation acts on generators by

\[
q_n(x_d)=x_{q_nd},
\]

and therefore

\[
\Phi_n(q_nT)=q_n\Phi_n(T).
\]

This is the desired rooted-subtree naturality at the source-algebra level.

## Analytic evaluation

Assign each channel a Mellin atom with algebraically independent code, for example

\[
x_d\longmapsto m_d(z)=\exp(2^{\iota(d)}z).
\]

Then

\[
\Phi_n(T)\longmapsto
m_T(z)=\exp\!\left(z\sum_{d\in T}2^{\iota(d)}\right),
\]

and binary uniqueness makes the evaluation injective on all squarefree channel monomials. Multiplication of Mellin amplitudes realizes subtree gluing as convolution degree.

For strict `C4` equivariance, retain the channel labels in a vector/function-valued history carrier and let the analytic chart operator permute those labels. Scalar exponential evaluation alone remains injective but transports the rotation to a conjugated operator on its image; identifying that conjugated operator with physical Fourier transport is a further comparison.

## Compression

The number of source atoms is only

\[
|D_n|=\frac{n(n-3)}2,
\]

while the number of triangulations is `C_(n-2)`. At `n=12`, 54 channel atoms distinguish all 16,796 facets. Thus no orbit-by-orbit external tagging is required.

`check_channel_monomial_c4_realization.py` verifies injectivity, multiplicativity, and quarter-rotation equivariance at `n=4,8,12`.
