# The two one-wall tails supply the missing v_alg covector

## Source-derived comparison

After the first normal jet removes the \(e_6\) coordinate, the remaining primitive source plane is rank two. The frozen two-wall model supplies a canonical ordered route basis:

\[
(w_{101},w_{110}),
\]

represented by transport from the two one-wall extensions \(l_1=b+x\) and \(l_2=a+y\).

Ledger entries 294 and 296 give universal exact tails

\[
T_{101}=-\frac{v_0}{4x^3y^3(x+y)},
\qquad
T_{110}=+\frac{v_0}{4x^3y^3(x+y)},
\]

where \(v_0=v_{\rm alg}(0)\). Clearing the common nonzero kinematic factor yields the primitive integral covector

\[
\boxed{
q_{v_{\rm alg}}(w_{101},w_{110})=(-1,+1).
}
\]

Its image is saturated and its kernel is

\[
\boxed{
K_{\rm route}=\mathbb Z\langle w_{101}+w_{110}\rangle.
}
\]

Thus the physically retained algebraic response is wall-route difference, while coherent wall-route sum is null.

## Relation to the pyramid odd plane

The normal-jet computation identified

\[
\ker q_{e_6}=\mathbb Z\alpha_{13}\oplus\mathbb Z\alpha_{14}.
\]

The two one-wall transports give an ordered basis of the source-relative wall plane. What is still not serialized is the integral marking from that wall plane to the Picard complement \(\langle\alpha_{13},\alpha_{14}\rangle\).

If that marking sends \(w_{101},w_{110}\) to \(\alpha_{13},\alpha_{14}\), up to simultaneous overall sign and interchange, then

\[
K_{\rm route}=\mathbb Z\langle\alpha_{13}+\alpha_{14}\rangle
\]

and the full comparison is

\[
Q=\begin{pmatrix}-1&0&0\\0&-1&1\end{pmatrix}.
\]

Without this final wall-to-Picard marking, the unconditional result is the primitive covector \((-1,+1)\) and sum-kernel in the labelled wall-route basis.

## Integral normalization

The odd eigenvector \(w_{110}-w_{101}\) maps to \(2v_0\) after clearing the kinematic factor. The individual wall routes map to units \(\pm v_0\). Hence no division by two is needed or authorized.

## Information flow

\[
\{d_i\}
\to
A_1^3
\xrightarrow{q_{e_6}}
\mathbb Z e_6
\quad\text{and}\quad
\langle w_{101},w_{110}\rangle
\xrightarrow{(-1,1)}
\mathbb Z v_{\rm alg},
\]

with the coherent sum wall route killed. This realizes the de Rham half of the missing comparison; only the integral identification of the labelled wall routes with the two Picard routes remains.

Verification:

- `research/voevodsky/checkers/check_one_wall_valg_covector.py`
- `research/voevodsky/results/one_wall_valg_covector.json`
