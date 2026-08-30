# Defect velocity is a positive \(S\sinh(yS)\) weight with oscillatory \(D\)-readout

## 1. Fixed completed source

Let \(\rho\) be the normalized even completed theta density and

\[
  A(z)=\int_{\mathbb R}\rho(u)e^{izu}\,du.
\]

For \(z=x+iy\),

\[
  |A(z)|^2
  =
  \iint
  \rho(u)\rho(v)
  e^{-y(u+v)}
  \cos\bigl(x(u-v)\bigr)\,du\,dv.
\]

The sine term vanishes by interchange of the two source copies.

## 2. Exact defect-velocity formula

Differentiate with respect to \(y\):

\[
  \partial_y|A(x+iy)|^2
  =
  -\iint
  (u+v)e^{-y(u+v)}
  \cos\bigl(x(u-v)\bigr)
  \rho(u)\rho(v)\,du\,dv.
\]

Pair \((u,v)\) with \((-u,-v)\) and use evenness of \(\rho\). With

\[
  S=u+v,
  \qquad
  D=u-v,
\]

one obtains

\[
  \boxed{
  \partial_y|A(x+iy)|^2
  =
  \frac12
  \iint
  S\sinh(yS)\cos(xD)
  \rho\!\left(\frac{S+D}{2}\right)
  \rho\!\left(\frac{S-D}{2}\right)
  \,dS\,dD.}
\]

The radial weight is nonnegative:

\[
  S\sinh(yS)\ge0
  \qquad(y\ge0).
\]

All remaining sign ambiguity lies in the relative-coordinate oscillation
\(\cos(xD)\).

## 3. Conditional form

Define the positive fixed-sum measure

\[
  d\nu_S(D)
  =
  \frac12
  \rho\!\left(\frac{S+D}{2}\right)
  \rho\!\left(\frac{S-D}{2}\right)dD,
\]

and its cosine readout

\[
  C_S(x)=\int\cos(xD)\,d\nu_S(D).
\]

Then

\[
  \partial_y|A(x+iy)|^2
  =
  \int_{\mathbb R}S\sinh(yS)C_S(x)\,dS.
\]

This is the exact scalar shadow of the labelled two-copy defect current.

## 4. What must be proved

The source supplies a positive measure in \((S,D)\), but a positive measure
need not have a positive cosine transform. Nor can one require

\[
  C_S(x)\ge0
\]

for every \(S,x\) without imposing a much stronger, generally false
fixed-sum Fourier-positivity condition.

Therefore the required orientation is intrinsically nonlocal in \(S\):

\[
\boxed{
\text{negative relative-coordinate bands must be repaired across
sum-coordinate and arithmetic labels}.}
\]

This is exactly where modular sewing must act. A proof performed separately
at each \(S\) discards the available completion current.

## 5. Boundary curvature

At \(y=0\), evenness forces

\[
  \partial_y|A(x)|^2=0.
\]

The first nontrivial outward coefficient is

\[
  \left.\partial_y^2|A(x+iy)|^2\right|_{y=0}
  =
  \frac12
  \iint
  S^2\cos(xD)
  \rho\!\left(\frac{S+D}{2}\right)
  \rho\!\left(\frac{S-D}{2}\right)
  \,dS\,dD,
\]

which also equals

\[
  2\bigl((A'(x))^2-A(x)A''(x)\bigr).
\]

Thus the first Laguerre curvature is the boundary acceleration of the same
full-sector defect whose first outward velocity controls the
Hermite--Biehler inequality.

## 6. Explanatory compression

The chain is now exact:

\[
\boxed{
\begin{aligned}
\text{unitary vacuum defect}
&\longrightarrow |A(x)|^2,\\
\text{complex quarter-turn}
&\longrightarrow \partial_y|A(x+iy)|^2,\\
\text{two-copy source}
&\longrightarrow S\sinh(yS)\cos(xD),\\
\text{boundary acceleration}
&\longrightarrow \text{Laguerre curvature}.
\end{aligned}}
\]

The Green, Kähler, de Branges, and Laguerre formulations are therefore
different coordinate expressions of one coupled defect current.

## 7. Next source theorem and falsifier

The next theorem must decompose the exact labelled theta product measure so
that the weighted integral of the negative cosine bands is paired with
positive bands through reciprocal/prime transport, uniformly in \(x\) and
\(y>0\).

The smallest falsifier is an exact labelled block for which the canonical
transported negative contribution exceeds its positive partner. Pairings
chosen after inspecting \(x\) are inadmissible.

## 8. Scope

The two-copy formula, nonnegative radial weight, conditional decomposition,
and boundary-curvature identity are exact. They locate but do not solve the
oscillatory sign problem. No modular cross-\(S\) transport inequality,
Hermite--Biehler theorem, or RH result is established.
