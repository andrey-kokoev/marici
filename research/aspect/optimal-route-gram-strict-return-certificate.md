# Optimal route-Gram strict-return certificate

## Question

What is the optimal strict-return certificate expressed directly through physical route norms and their parity-controlled overlap?

## Gram data

For two physical route amplitudes \(b_+\) and \(b_-\), the return Gram matrix is

\[
G=
\begin{pmatrix}
\|b_+\|^2&\langle b_+,b_-\rangle\\
\langle b_-,b_+\rangle&\|b_-\|^2
\end{pmatrix}.
\]

Assume

\[
\|b_+\|^2\le U,
\qquad
\|b_-\|^2\le V,
\qquad
|\langle b_+,b_-\rangle|\le C.
\]

Gram positivity also imposes Cauchy--Schwarz, so define

\[
C_{\rm eff}=\min(C,\sqrt{UV}).
\]

## Optimal certificate

Monotonicity of the largest eigenvalue in both diagonal entries and the overlap magnitude gives

\[
\lambda_{\max}(G)
\le
\frac{U+V+\sqrt{(U-V)^2+4C_{\rm eff}^2}}{2}.
\]

The bounds certify strict return exactly when their right-hand side is less than one.

This estimate is optimal for the supplied data. The corner matrix

\[
\begin{pmatrix}U&C_{\rm eff}\\C_{\rm eff}&V\end{pmatrix}
\]

is positive and realizes the upper bound. It is itself a Gram matrix of two vectors.

## Exact cases

For

\[
U=V=\frac12,
\qquad C=\frac14,
\]

the largest eigenvalue bound is \(3/4\).

For the rank-one data

\[
U=\frac9{100},
\quad V=\frac{16}{100},
\quad C=\frac{12}{100},
\]

the bound is \(1/4\). Scaling these entries by four yields

\[
U=\frac9{25},
\quad V=\frac{16}{25},
\quad C=\frac{12}{25},
\]

and reaches the terminal value one.

## Improvement over independent Pauli boxes

The Pauli coordinates are

\[
a=\frac{u+v}{2},
\quad z=\frac{u-v}{2},
\quad x=\operatorname{Re}c
\]

under reciprocity. Independent bounds on \(a,x,z\) discard the shared origin of \(a\) and \(z\) in the same route loads \(u,v\), and may combine incompatible extrema. The Gram certificate retains this correlation and automatically enforces positivity.

## Composition with parity defects

The sharp parity-defect estimate supplies a candidate value for \(C\). Bounds on the two physical route norms supply \(U,V\). Their composition therefore gives a sufficient strict-return test without separately reconstructing \(a\) and \(z\).

The result remains conditional: local arithmetic source data currently supplies neither the physical route map nor numerical bounds on \(U,V\).

## Verification

`research/aspect/checkers/check_route_gram_certificate.py` verifies a correlated strict case and strict and terminal rank-one cases with exact rational discriminants.

## Disposition

The optimal two-route Gram certificate is derived. The next executable question is whether normalized parity defects alone imply a nontrivial overlap ratio that can be inserted into this certificate independently of absolute route scale.
