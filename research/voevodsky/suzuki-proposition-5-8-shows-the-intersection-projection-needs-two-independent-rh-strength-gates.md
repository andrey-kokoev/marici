# Suzuki Proposition 5.8 shows the intersection projection needs two independent RH-strength gates

## Primary-text correction

The unconditional intersection

\[
V(0)=L^2(0,\infty)\cap K L^2(0,\infty)
\]

and its alternating-projection constructor are genuine. But Suzuki's own Proposition 5.8 gives the exact audit of what remains. The proposition states that RH is equivalent to **both**:

1. the Weil/norm identity on `V(0)`;
2. an interpolation/completeness condition allowing `V(0)` to isolate every zero coordinate with uniform decay on the others.

Thus merely constructing or proving nontriviality of the intersection is substantially insufficient.

## Gate one: arithmetic isometry

Suzuki's first condition is, in his normalization,

\[
2\|\phi\|_{L^2(\mathbb R)}^2
=
\langle\phi,\phi\rangle_W
\qquad(\phi\in V(0)).
\]

The left side is positive by construction. The equality identifying it with the Weil form is not obtained from

\[
\phi\in H_+\cap KH_+.
\]

It is an additional arithmetic assertion. Therefore projecting a source vector into `V(0)` kills Hardy leakage but does not prove that its positive ambient norm is the completed endpoint--gamma--prime pairing.

This directly blocks the proposed shortcut

\[
Q_W(f,g)
\stackrel{?}{=}
\langle P_VA_{src}f,P_VA_{src}g\rangle.
\]

The question mark is exactly Proposition 5.8(1).

## Gate two: zero-coordinate interpolation

For each zero coordinate `gamma` and each `epsilon>0`, Suzuki requires a vector in `V(0)` whose transform equals one at the selected coordinate and is bounded at every other zero by a uniformly summable localization envelope of the form

\[
|\widehat\phi(-\rho)|
\le
|\gamma-ho|^{-1-\epsilon}.
\]

This condition prevents the intersection from being a small positive subspace blind to hostile zero directions. It is the concrete faithfulness requirement missing from the alternating-projection construction.

Even if `P_V` is nonzero, or infinite-dimensional, it need not satisfy this interpolation property. A positive subspace can avoid every negative orbit simply by failing to observe it.

## How the converse works

If RH fails, choose a nonreal zero `gamma_0`. Condition (2) provides two localized vectors selecting the conjugate pair. Their sum is arranged so that the Weil form receives

\[
-m_{\gamma_0}+O(\epsilon),
\]

which is negative for sufficiently small `epsilon`. Condition (1) would identify this with a positive `L^2` norm, giving a contradiction.

This is precisely the off-axis `(1,1)` block obstruction, now verified in Suzuki's primary theorem rather than inferred abstractly.

## Consequence for an exact fixed-vector attempt

An exact fixed vector of

\[
A=PQP
\]

only proves membership in `V(0)`. It proves neither:

\[
2\|\phi\|_2^2=\langle\phi,\phi\rangle_W,
\]

nor the interpolation property. Hence constructing one source-fixed eigenvector at eigenvalue one cannot yield universal positivity. At minimum one needs a family of fixed vectors that is simultaneously:

- arithmetically isometric;
- zero-separating;
- uniformly localized;
- complete for the Weil test topology.

These requirements are much stronger than a nonzero endpoint atom for `PQP`.

## Corrected role of alternating projections

The projection

\[
P_V=s\!\!\lim(PQP)^n
\]

solves only the geometric support intersection. It does not solve either arithmetic gate in Proposition 5.8. The complete architecture is

\[
\text{boundary involution}
\longrightarrow
V(0)
\xrightarrow{\text{arithmetic isometry}}
H_W
\xrightarrow{\text{interpolation faithfulness}}
\text{zero confinement}.
\]

Only the first arrow is unconditional.

## New narrowed constructor target

The next source object should not be another projection or isolated fixed vector. It must be a family `phi_gamma` in the intersection together with a source-side proof of

\[
\langle\phi_\gamma,\phi_\eta\rangle_W
=
2\langle\phi_\gamma,\phi_\eta\rangle_{L^2}
\]

and a uniform interpolation matrix close to the identity on zero coordinates.

Constructing this family by naming the zeros is circular for the present programme. A source-valid replacement would be a resolvent or reproducing family indexed by a continuous spectral parameter, with the discrete interpolation statement derived afterward.

## Disposition

Suzuki's Proposition 5.8 prevents overinterpreting the unconditional intersection projection:

\[
\boxed{
P_V\text{ exists and is contractive, but RH still requires}
\begin{cases}
\text{Weil--}L^2\text{ isometry on }V(0),\\
\text{zero-separating interpolation by }V(0).
\end{cases}
}
\]

The first missing identity is exactly the requested endpoint--gamma--prime Green identity; the second is the faithful-completion gate. Neither follows from alternating projections.
