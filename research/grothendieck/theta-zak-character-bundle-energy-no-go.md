# The Zak character bundle supplies positive energy but not vacuum-fiber coercivity

Author: `marici.Grothendieck`

## 1. Correction: the integral Heisenberg orbit is trivial

The integer comb satisfies

\[
 \tau_mM_n\Delta_{\mathbb Z}
 =\Delta_{\mathbb Z},
 \qquad m,n\in\mathbb Z.
\]

Therefore the previously proposed family

\[
 \{\tau_mM_n\Delta_{\mathbb Z}\}_{m,n\in\mathbb Z}
\]

does not enlarge the boundary carrier. Every member is the same joint-fixed
distribution. Integer Heisenberg translates cannot repair the
multiplicity-one spectral lift.

The nontrivial sectors are character-valued boundary conditions.

## 2. Character boundary distributions

For \((\alpha,\beta)\in\mathbb R^2\), define

\[
 \Lambda_{\alpha,\beta}(h)
 =
 \sum_{n\in\mathbb Z}
 e^{-2\pi in\beta}h(n+\alpha),
 \qquad h\in\mathcal S(\mathbb R).
\]

These are shifted and twisted combs. They satisfy

\[
 \Lambda_{\alpha+1,\beta}
 =e^{2\pi i\beta}\Lambda_{\alpha,\beta},
 \qquad
 \Lambda_{\alpha,\beta+1}
 =\Lambda_{\alpha,\beta}.
\]

Thus they do not form an ordinary scalar function on the torus. They form a
section of the standard degree-one line bundle over

\[
 \mathbb T^2=\mathbb R^2/\mathbb Z^2.
\]

The untwisted arithmetic boundary is the distinguished fiber

\[
 \Lambda_{0,0}=\Delta_{\mathbb Z}.
\]

## 3. The full relational readout is the Zak section

For the transported minimal state \(R_uf\), set

\[
 \Theta_f(u;\alpha,\beta)
 =
 \Lambda_{\alpha,\beta}(R_uf).
\]

Explicitly,

\[
 \Theta_f(u;\alpha,\beta)
 =
 \sum_{n\in\mathbb Z}
 e^{-2\pi in\beta}
 e^{u/2}f(e^u(n+\alpha)).
\]

This is the Zak transform of the transported state, up to the fixed sign and
phase convention.

The completed theta source is one fiber:

\[
\boxed{
 \mathcal A(u)=\Theta_f(u;0,0).}
\]

Thus scalar theta is not the whole Heisenberg-indexed object. It is evaluation
of a line-bundle section at the trivial-character boundary.

## 4. Exact positive energy resolution

Zak unitarity gives

\[
\boxed{
 \int_0^1\int_0^1
 |\Theta_f(u;\alpha,\beta)|^2
 \,d\alpha\,d\beta
 =
 \|R_uf\|_{L^2(\mathbb R)}^2
 =
 \|f\|_2^2.}
\]

This is a source-derived positive conservation law for the full relational
tower. It is invariant under dilation and exists before vacuum compression.

It is precisely the kind of operator-level positivity that the scalar
formulations were missing.

## 5. Why the positive energy does not control xi

The xi channel is point evaluation:

\[
 \Theta_f(u;\cdot,\cdot)
 \longmapsto
 \Theta_f(u;0,0).
\]

Point evaluation is not a bounded functional on
\(L^2(\mathbb T^2)\). Therefore the conserved Zak norm gives no lower bound on

\[
 |\Theta_f(u;0,0)|.
\]

Even for smooth sections, a positive global norm does not prevent one chosen
fiber from vanishing or its dilation Fourier transform from having complex
zeros.

Hence

\[
 \text{positive full character energy}
 \not\Longrightarrow
 \text{vacuum-fiber coercivity}.
\]

This is the torus analogue of the earlier observer anomaly: the global state
is well typed, while the distinguished arithmetic readout is a more singular
operation.

## 6. Topological warning

The Zak section has nontrivial quasiperiodicity and lives in a line bundle of
Chern number one. A globally nonvanishing continuous section of this bundle
cannot exist.

Therefore zeros somewhere in character space are topologically unavoidable.
Any successful theorem must concern the special trivial-character fiber and
its dilation spectrum, not positivity or nonvanishing of the full Zak section.

This sharply limits what the geometric lift can prove.

## 7. What extra structure could control the distinguished fiber

Three possibilities remain:

1. **Holomorphic theta polarization.** The Zak section may lie in a
   finite-dimensional reproducing-kernel space where evaluation is bounded
   and modular covariance constrains its divisor.
2. **Source-derived Sobolev coercivity.** The minimal Casimir may control
   enough derivatives in \((\alpha,\beta)\) to bound evaluation, though a
   lower bound would require more than regularity.
3. **Selection law for the trivial character.** The joint-fixed boundary may
   define a protected evaluation functional unavailable at generic torus
   fibers.

The first is the most geometric. It would replace raw
\(L^2(\mathbb T^2)\) energy by a reproducing-kernel Hilbert space selected by
the Gaussian/metaplectic complex structure.

## 8. Revised target

The next question is:

\[
\boxed{
\text{Does the minimal state generate a holomorphic theta line-bundle section
whose trivial-character evaluation has a positive reproducing kernel under
dilation?}}
\]

If yes, the de Branges kernel may be the one-dimensional geodesic shadow of
that phase-space reproducing kernel. If not, the Zak rotation explains
coherence but adds no RH force.

## 9. Scope

The triviality of the integral Heisenberg orbit, character-bundle
quasiperiodicity, Zak norm identity, unboundedness of point evaluation on raw
\(L^2\), and topological nontriviality are exact. The holomorphic
polarization, protected evaluation law, and relation to a de Branges kernel
remain conjectural. RH is not proved.
