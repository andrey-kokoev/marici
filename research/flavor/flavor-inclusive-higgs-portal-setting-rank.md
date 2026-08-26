# Inclusive-Higgs portal-setting rank

Work package: WP584  
Owner: marici.Figueiredo

## Question

WP583 supplies four exact source-coordinate settings inside a nonempty local
domain. This packet asks which of those settings the largest currently
authorized flavor detector channel can distinguish.

The admitted physical instrument is the inclusive light-Higgs coupling and
production readout

\[
y=\kappa_t^2=1-z.
\]

It is calibrated experimentally, but it contains no dependence on
\(\lambda_s\) in the declared universal mixing model.

## Exact response rank

With source coordinates \((z,\lambda_s)\), the response Jacobian is

\[
J_1=\begin{pmatrix}-1&0\end{pmatrix}.
\]

It has rank one and its Gram determinant is zero. Under the exact WP580
settings, the two \(r\)-branches change the readout by \(\mp h\), whereas
both \(q\)-branches change it by exactly zero. The contextual equivalence
classes therefore fix \(z\) and retain the entire positive
\(\lambda_s\)-fiber.

This kernel occurs at the physical instrument, not at the source map: WP576
already proves that \((z,\lambda_s)\mapsto(r,q)\) has rank two for \(z>0\).

## Smallest exact hostile pair

Use the WP583 interior point

\[
z={1\over4},\qquad \lambda_s=\lambda_H=1,
\qquad h={1\over32}.
\]

The legal pure-\(q\) endpoints are

\[
S_q^- =\left({1\over4},{1\over2}\right),
\qquad
S_q^+ =\left({1\over4},{3\over2}\right).
\]

They are distinct source points with invariant separation \(2h=1/16\), but
both give \(\kappa_t^2=3/4\). Thus executable inclusive-Higgs readout cannot
realize the rank-two conditional detector composition of WP576.

## Classification

The operation is a physical readout. It separates the \(r\)-direction, is
blind to the \(q\)-direction, and is neither a source selector nor a texture
rigidifier. No reference port is involved.

The smallest repair is a publication-bound completed detector channel whose
calibrated response has a nonzero derivative along \(q\) at fixed \(z\).
Sampled \(\kappa_4\) contours on the incompatible \(\kappa_t=1\) slice do not
supply that derivative, as WP564 proves.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp584_inclusive_higgs_portal_setting_rank.py

The generated result is
research/flavor/results/wp584_inclusive_higgs_portal_setting_rank.json.
