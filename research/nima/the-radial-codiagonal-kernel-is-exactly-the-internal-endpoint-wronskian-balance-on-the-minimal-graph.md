# The radial codiagonal kernel is exactly the internal endpoint–Wronskian balance on the minimal graph

## Question

What is the kernel of the fixed bilateral codiagonal on the doubled rapid radial graph, before imposing additional theta-source relations?

## Claim boundary

On the minimal graph defined only by rapid decay, half-line support, wall matching, and

\[
D_t\rho_\pm=e_\pm-\frac12w_\pm,
\]

the codiagonal vanishes exactly when both oriented derivative sources vanish. Rapid decay then forces both radial states and wall values to vanish, while each internal pair may retain

\[
e_\pm=\frac12w_\pm.
\]

Thus the codiagonal forgets the balanced endpoint–Wronskian channel. Whether the actual completed-theta source intersects this kernel nontrivially requires an additional source identity.

## Oriented derivative sources

Set

\[
q_+=e_+-\frac12w_+,
\qquad
q_-=e_--\frac12w_-.
\]

Fold them into the whole-line rapid function

\[
q(t)=
\begin{cases}
q_+(t),&t>0,\\
q_-(t),&t<0.
\end{cases}
\]

The sewn wall condition excludes an independent point-supported source at \(t=0\).

The fixed codiagonal is the bilateral Laplace transform

\[
D J_{\rm or}(z)
=
\int_{\mathbb R}e^{-zt}q(t)\,dt.
\]

## Kernel calculation

Suppose

\[
D J_{\rm or}(z)=0
\]

for every \(z\). Restricting to \(z=i\xi\) gives a zero Fourier transform of \(q\). Fourier injectivity on the rapid whole-line source yields

\[
q=0.
\]

Since the two half-lines have disjoint interiors,

\[
q_+=0,
\qquad
q_-=0.
\]

Therefore

\[
e_+=\frac12w_+,
\qquad
e_-=\frac12w_-.
\]

The graph laws reduce to

\[
D_t\rho_+=0,
\qquad
D_t\rho_-=0.
\]

Rapid decay at the two exterior ends forces

\[
\rho_+=0,
\qquad
\rho_-=0,
\qquad
\rho(0)=0.
\]

Conversely, any admissible rapid feature pair satisfying

\[
\rho_\pm=0,

e_\pm=\frac12w_\pm
\]

lies in the codiagonal kernel. Hence on the minimal graph,

\[
\ker(DJ_{\rm or})
=
\left\{
(0,e_+,2e_+;0,e_-,2e_-)
\right\},
\]

with the entries understood in the two oriented feature spaces.

## Meaning of the kernel

The kernel is not a failure to observe the radial derivative source. The codiagonal observes

\[
q=D_t\rho
\]

faithfully. It forgets how that source was decomposed into endpoint and Wronskian contributions.

Therefore the reduced codiagonal state is naturally the derivative-source class

\[
[e,w]\longmapsto e-\frac12w.
\]

Retaining the full six-coordinate packet remembers the decomposition; applying the codiagonal quotients by balanced internal redistributions.

## Actual theta-source restriction

For completed-theta shells, \(e\) and \(w\) are not arbitrary rapid functions. They are separately derived endpoint and Wronskian currents. The minimal-graph kernel intersects the actual source range nontrivially only if a nonzero shell packet satisfies

\[
e_\pm=\frac12w_\pm
\]

as complete function-valued identities.

No existing source theorem establishes such an identity. Pointwise equality at one spectral parameter or on the Xi divisor is insufficient.

## G4 conformance consequence

If G4 uses the codiagonal as its Green feature, its declared radical should be compared with this balanced internal channel. It must then state whether:

1. the full endpoint/Wronskian decomposition is gauge;
2. only the derivative source is physical;
3. the actual theta-source range meets the balanced kernel;
4. quotienting preserves the separately required wall and multiplicity-jet data.

If G4 instead treats endpoint and Wronskian channels as distinct physical ports, it must retain the full faithful feature and cannot quotient by this kernel.

## Direction rescore

- Minimal-graph codiagonal kernel: completed exactly.
- Faithfulness on the derivative source \(q\): completed.
- Intersection with the completed-theta source range: 8/10; requires an endpoint–Wronskian identity audit.
- Identification with G4 radical: interface-blocked.

## Disposition

The codiagonal radical is now typed: it is the freedom to redistribute a zero derivative source between endpoint and Wronskian channels with coefficient \(1/2\). The remaining local question is whether the actual completed-theta feature range contains a nonzero balanced packet. No RH or G4 quotient conclusion is authorized without that audit.
