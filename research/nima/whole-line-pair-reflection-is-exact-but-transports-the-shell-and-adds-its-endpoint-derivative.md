# Whole-line pair reflection is exact but transports the shell and adds its endpoint derivative

> **Status update.** The successor folding calculation constructs the missing
> carrier comparison and shows that its gluing coordinate is the bilateral
> Laplace transform of the whole source. The reflection theorem below remains
> valid, but the proposed universal-cancellation use is rejected for every
> nonzero source.

## Question

Does the real-separation completed-theta pair kernel define the negative-support reciprocal source required by free-tail cancellation while retaining finite-shell localization?

## Claim boundary

Yes as a whole-line pair identity, but not as fixed-shell slot swap. Reflecting separation transports the shell by the same variable and exchanges the ordered labels. Differentiating the reflected family therefore includes the moving-shell endpoint derivative. The existing moving-seam and complete endpoint bundle can type this transport; the fixed-shell doubled half-line carrier cannot.

## Exact reflected pair identity

For

\[
\rho_{nm}^{[a,b]}(t)
=\int_a^b\Phi_n(u)\Phi_m(u+t)\,du,
\]

change variables \(v=u-t\) to obtain

\[
\rho_{nm}^{[a,b]}(-t)
=\int_{a-t}^{b-t}\Phi_m(v)\Phi_n(v+t)\,dv
=\rho_{mn}^{[a-t,b-t]}(t).
\]

Thus reflection performs three operations together:

1. \(t\mapsto-t\);
2. ordered-label swap \((n,m)\mapsto(m,n)\);
3. shell transport \([a,b]\mapsto[a-t,b-t]\).

The third operation prevents identification with a same-shell scalar phase.

## Reflected radial forcing

Let

\[
f_{nm}^{[a,b]}(t)=D_t\rho_{nm}^{[a,b]}(t).
\]

Define

\[
Q_{mn}(t)=\rho_{mn}^{[a-t,b-t]}(t).
\]

The reflected identity gives

\[
f_{nm}^{[a,b]}(-t)=-D_tQ_{mn}(t).
\]

Leibniz differentiation resolves the right side into a fixed-integrand derivative and moving endpoints:

\[
D_tQ_{mn}(t)
=\int_{a-t}^{b-t}\Phi_m(v)\Phi_n'(v+t)\,dv
+\Phi_m(a-t)\Phi_n(a)
-\Phi_m(b-t)\Phi_n(b).
\]

Therefore the negative-support reciprocal forcing is not merely the swapped interior derivative. It includes the complete two-endpoint transport with its forced signs.

## Compatibility with the existing source bundle

The repository already has unitary moving-seam transport and a rank-two endpoint pushforward satisfying a metric naturality square. That machinery has the correct architecture for the reflected shell family:

\[
\text{pair bulk}
\longrightarrow
\text{moving shell}
\longrightarrow
\text{complete endpoint pair}.
\]

It does not yet identify this separation-indexed shell motion with G4's radial source incidence. The required comparison must preserve the object-indexed endpoint metric; replacing the moving fibers by one fixed Euclidean port would erase the exact transport.

## Folding obstruction

Folding the negative physical half-line by \(r=-t\) turns \(\partial_t\) into \(-\partial_r\), which explains the doubled differential \(\partial_r\oplus(-\partial_r)\). But the source readout must also be folded. Reusing the second positive-half-line functional

\[
\ell_{-z}(g_-)=\int_0^\infty e^{zr}g_-(r)\,dr
\]

without the physical-coordinate pullback recreates the support obstruction. The whole-line construction therefore requires a comparison cell between physical negative-support Laplace pairing and the folded reciprocal channel. Carrier folding alone is insufficient.

## Revised direction score

- Whole-line reflected pair source as a source object: 10/10; it is explicit.
- Fixed-shell two-copy realization: 0/10; shell transport is unavoidable.
- Folded comparison into the conservative double: completed by the successor packet; it does not cancel a nonzero source.
- G4 boundary-feature route: 10/10; it uses the same moving endpoint packet if folding fails.

## Disposition

The real-separation pair kernel supplies the required reflected source before folding. The unresolved arrow is now precise: construct the metric comparison from the moving-shell whole-line pair bundle, including its endpoint derivative, to the folded reciprocal radial carrier and prove that its Laplace pairing reproduces the negative-support transform. No RH conclusion is authorized.
