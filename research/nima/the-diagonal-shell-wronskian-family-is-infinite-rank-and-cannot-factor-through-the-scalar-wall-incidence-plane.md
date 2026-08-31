# The diagonal shell Wronskian family is infinite rank and cannot factor through the scalar wall-incidence plane

## Question

Can the exact diagonal Wronskian shell current be represented by the existing
two scalar coordinates of the retained wall/incidence linking port?

## Claim boundary

No, if those coordinates remain a fixed finite-dimensional plane. Infinitesimal
shells generate an infinite linearly independent family of separation
functions with distinct double-exponential decay rates. Therefore exact
Laplace readout for every shell and every parameter jet requires a
function-valued radial module or an equivalent infinite-dimensional retained
coordinate.

## Local Wronskian density

For one theta label \(n\), define

\[
 w_{n,u}(t)
 =\Phi_n'(u)\Phi_n(u+t)
 -\Phi_n(u)\Phi_n'(u+t).
\]

For a shell \([a,b]\),

\[
 \mathcal W_n^{[a,b]}(t)
 =\int_a^b w_{n,u}(t)\,du.
\]

For an infinitesimal shell,

\[
 \frac1h\mathcal W_n^{[u,u+h]}(t)
 \longrightarrow w_{n,u}(t)
\]

in every compact separation topology and in the rapidly weighted Laplace
spaces used by the Evans readout.

## Distinct large-separation rates

The completed atom has the form

\[
 \Phi_n(x)
 =e^{x/2}P_n(e^{2x})e^{-\pi n^2e^{2x}},
\]

with a nonzero polynomial \(P_n\). For fixed \(u\) and \(t\to\infty\), both
\(\Phi_n(u+t)\) and its derivative carry the decisive factor

\[
 \exp\!\left(-\pi n^2e^{2u}e^{2t}\right).
\]

Hence

\[
 w_{n,u}(t)
 =Q_{n,u}(e^{2t})e^{t/2}
 \exp\!\left(-\pi n^2e^{2u}e^{2t}\right)
\]

for a nonzero polynomial-type coefficient \(Q_{n,u}\).

If \(u_1<\cdots<u_N\), the functions have strictly ordered decay constants

\[
 \pi n^2e^{2u_1}<\cdots<\pi n^2e^{2u_N}.
\]

## Linear independence

Suppose

\[
 \sum_{j=1}^Nc_jw_{n,u_j}(t)=0.
\]

Multiply by the inverse of the slowest double-exponential factor associated
with \(u_1\) and let \(t\to\infty\). Every term with \(j>1\) vanishes relative
to the first. The remaining polynomial-type leading term forces \(c_1=0\).
Repeating proves

\[
 c_1=\cdots=c_N=0.
\]

Thus every finite set at distinct shell locations is linearly independent, and

\[
 \operatorname{span}\{w_{n,u}:u\in\mathbb R\}
\]

is infinite dimensional.

## Finite-port obstruction

The declared wall/incidence linking plane retains only

\[
 \gamma_0f
 \quad\text{and}\quad
 \eta(f).
\]

Any fixed linear factorization through this plane has response rank at most
two before external parameter-dependent data are added. It cannot reproduce
the infinite-rank family \(w_{n,u}(t)\) while preserving all shell locations.

Allowing a fitted coefficient for each shell does not repair the typing: it
inserts the missing function as external data and fails to construct a
cutoff-natural source map.

## Laplace and jet consequence

Laplace transform is injective on this rapidly decaying family. Therefore the
transforms

\[
 \int_0^\infty e^{-zt}w_{n,u}(t)\,dt
\]

also have unbounded finite-set rank as analytic functions. A two-coordinate
port cannot reproduce every shell value and all derivatives in \(z\).

## Required enlargement

The minimal viable G4 interface must retain a radial response module
\(\mathcal H_{\rm rad}\) containing the functions \(w_{n,u}(t)\), together
with maps

\[
 \mathcal G_{\theta,\rm pair}^{[a,b]}
 \longrightarrow
 \mathcal H_{\rm rad}
 \longrightarrow
 \mathcal G_{\rm wall,inc}^{\rm enlarged}.
\]

The scalar wall and incidence traces may remain as boundary coordinates of
this graph, but cannot be its whole response carrier.

## Hostile

Choose three distinct infinitesimal shell locations. Their Wronskian densities
are linearly independent, while any fixed two-dimensional response plane has
rank at most two. This is the smallest finite rank falsifier.

## Disposition

The current scalar wall/incidence linking plane is structurally too small for
the exact diagonal shell family. Candidate one requires an authorized
function-valued radial enlargement of the G4 interface. Until that carrier is
declared and compared with the conservative Green complex, coefficient tuning
cannot close the shell residual. No RH conclusion is authorized.
