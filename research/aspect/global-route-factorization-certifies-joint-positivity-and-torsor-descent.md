# Global route factorization certifies joint positivity and torsor descent

## Question

Can one source object certify complete joint positivity and test all lift-torsor directions without enumerating principal minors or ambient pairings?

## Global Gram certificate

Let the complete physical joint form factor through one source-derived route map

\[
B:V_{\rm abs}\longrightarrow W,
\qquad
Q=B^*B.
\]

Then for every \(x\in V_{\rm abs}\),

\[
Q(x,x)=\|Bx\|^2\ge0.
\]

This proves positivity at all sector sizes simultaneously. It is not a reconstruction from pairwise overlaps; the map \(B\) must be defined on the complete joint source space with one declared target inner product.

For a torsor direction \(v\),

\[
v\in\operatorname{rad}(Q)
\quad\Longleftrightarrow\quad
Bv=0.
\]

Thus a rank-seven torsor basis requires seven kernel tests against \(B\). The same factorization certifies the positivity premise that made diagonal radical tests valid.

## Exact finite model

Take

\[
B=
\begin{pmatrix}
1&0&1\\
0&1&1
\end{pmatrix},
\qquad
Q=B^*B.
\]

The direction \(v=(1,1,-1)^T\) satisfies \(Bv=0\), hence \(Qv=0\). The direction \(w=(1,0,0)^T\) has \(Bw\ne0\) and positive joint norm. The route map distinguishes radical from nonradical directions without a principal-minor search.

## No fixed local-depth substitute

Voevodsky's equicorrelation family shows that for every fixed overlap cutoff \(k\), all principal restrictions through size \(k\) may be positive while a \((k+1)\)-sector collective mode is negative. Therefore no fixed pair, triple, or higher finite local depth establishes arbitrary joint positivity. A global factorization such as \(Q=B^*B\), or another source-derived all-size theorem, is required.

## Physical source gate

A valid \(B\) must preserve the pre-readout route structure and include every wall, history, tail, and PV-reciprocal component contributing to the physical form. Concatenating independently fitted sector maps into a formal matrix does not prove that their cross terms equal the physical joint pairings.

If the source-relative q_G12 cocycle is only a quotient of route data, the required diagram is

\[
V_{\rm abs}\overset{B}{\longrightarrow}W,
\qquad
V_{\rm abs}\overset{\pi}{\longrightarrow}V_{\rm rel},
\]

with the seven-dimensional kernel of \(\pi\) tested directly under \(B\).

## Verification

`research/aspect/checkers/check_global_gram_torsor.py` verifies the Gram identity, full positivity on exact samples, one radical direction, and one positive-norm direction using rational arithmetic.

## Disposition

The most compressed executable owner request is now a complete route map \(B_p\) and seven images \(B_pv_i\). If all images vanish, the norm descends; if one does not, the relative cocycle cannot determine physical return. Without a global route factorization, local overlap positivity remains noncertifying at every fixed depth.
