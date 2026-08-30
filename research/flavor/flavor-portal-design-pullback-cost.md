# Portal design pullback-cost gate

Work package: WP579  
Owner: marici.Figueiredo

## Question

WP578 identifies orthogonal unit perturbations in invariant \((r,q)\) space as
the optimally conditioned two-setting design under its frozen Euclidean
budget. Are those settings uniformly feasible on the portal source
coordinates \((z,\lambda_s)\), with the inherited viability condition
\(\lambda_s>0\)?

## Exact pullback

For

\[
r=z,
\qquad
q={\lambda_s z^2\over\lambda_H},
\]

the WP576 source Jacobian and its inverse are

\[
A=
\begin{pmatrix}
1&0\\
2\lambda_s z/\lambda_H&z^2/\lambda_H
\end{pmatrix},
\qquad
A^{-1}=
\begin{pmatrix}
1&0\\
-2\lambda_s/z&\lambda_H/z^2
\end{pmatrix}.
\]

The physical-parameter perturbations that realize the invariant unit settings
are therefore

\[
A^{-1}e_r=(1,-2\lambda_s/z)^T,
\qquad
A^{-1}e_q=(0,\lambda_H/z^2)^T.
\]

In the Euclidean \((z,\lambda_s)\) metric, their squared costs are

\[
C_r=1+{4\lambda_s^2\over z^2},
\qquad
C_q={\lambda_H^2\over z^4}.
\]

The pure-\(q\) setting cost diverges at zero mixing for every
\(\lambda_H>0\). The pure-\(r\) cost also diverges when
\(\lambda_s\ne0\). Hence the orthogonal unit design is pointwise available
for \(z>0\) but not uniformly bounded on the full nonzero-mixing domain.

## Bounded-setting reach

If the admitted physical source perturbation obeys
\(|\delta\lambda_s|\le B\), a unit pure-\(q\) setting requires

\[
{ \lambda_H\over z^2}\le B,
\qquad
z^2\ge{\lambda_H\over B}.
\]

Equivalently, under the unit bound \(B=1\), the largest pure-\(q\) response is

\[
|\delta q|_{\max}={z^2\over\lambda_H}.
\]

At the rational hostile \(z=1/2\), \(\lambda_H=1\), a unit invariant
\(q\)-perturbation needs \(\delta\lambda_s=4\). A unit-bounded source setting
can produce at most \(|\delta q|=1/4\).

Both finite endpoints must also retain \(\lambda_s>0\); differential reach
alone does not certify that viability condition.

## Typing consequence

WP576's rank-two statement is local algebraic faithfulness. WP578's
orthogonal design is optimal only in its declared invariant metric. WP579
shows that pulling this metric back to physical portal parameters produces a
singular cost near \(z=0\).

A physical calibration must therefore state:

- the admitted source-setting norm and maximum perturbation;
- the portal point or compact domain on which settings are feasible;
- the induced invariant design matrix rather than an idealized unit design;
- uncertainty and nonlinear-remainder bounds for finite settings.

This is a reach gate, not a selector or rigidifier. Full weak-basis descent
passes because both coordinate systems are invariant. No reference port
repairs insufficient source-setting reach; exposure can preserve a generated
rate response but cannot enlarge the attainable source perturbation.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp579_portal_design_pullback_cost.py

The generated result is
research/flavor/results/wp579_portal_design_pullback_cost.json.
