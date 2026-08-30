# The canonical radial Tate lift recovers Fourier but not Weyl phase

## Canonical shell lift

Fix the self-dual additive Haar measure on \(\mathbb Q_p\). Let

\[
B_k=p^k\mathbb Z_p,
\qquad
S_k=B_k\setminus B_{k+1}.
\]

A valuation basis vector has a canonical radial lift

\[
j_{\mathrm{rad}}e_k=\mathbf 1_{S_k}
=
\mathbf 1_{B_k}-\mathbf 1_{B_{k+1}}.
\]

Thus valuation data can be embedded into the radial Schwartz–Bruhat subspace without choosing representatives of unit orbits.

The valuation projection is a left inverse on this radial image after the shell normalization is fixed.

## Exact local Fourier action

For the standard self-dual character convention,

\[
\mathcal F_p\mathbf 1_{B_k}
=
p^{-k}\mathbf 1_{B_{-k}}.
\]

Therefore

\[
\mathcal F_p\mathbf 1_{S_k}
=
p^{-k}\mathbf 1_{B_{-k}}
-
p^{-k-1}\mathbf 1_{B_{-k-1}}.
\]

The local Fourier transform preserves radiality. Hence the spherical Fourier operation does descend to a well-defined operator on the completed shell span.

This repairs one overbroad reading of the valuation no-go: valuation projection erases additive translation and character phase, but it does not erase the entire local Fourier transform on radial vectors.

## What the radial lift cannot recover

For nontrivial \(\eta\),

\[
M_\eta\mathbf 1_{S_k}(x)
=
\psi_p(\eta x)\mathbf 1_{S_k}(x)
\]

is generally nonradial. Likewise, \(T_h\mathbf 1_{S_k}\) is generally a translated shell rather than a radial shell.

Thus the radial subspace is not invariant under the full Weyl pair

\[
T_h,\qquad M_\eta.
\]

The commutator phase

\[
T_hM_\eta
=
\psi_p(\eta h)M_\eta T_h
\]

lives in the nonspherical additive directions omitted by valuation projection.

The radial Fourier matrix is real shell transport. It cannot by itself supply the odd reciprocal phase.

## Minimal nonspherical enlargement

A first phase-sensitive carrier must include character-twisted shells

\[
\psi_p(\eta x)\mathbf 1_{S_k}(x)
\]

and their translated images. Closure under both \(T_h\) and \(M_\eta\) generates an additive Heisenberg orbit, not one extra scalar coordinate.

At finite conductor, one may quotient to a finite additive module and obtain a finite Weyl representation. But its dimension grows with conductor. No cutoff-independent four-dimensional state can carry the complete local Weyl action.

Therefore the earlier four-port Green block must be interpreted as a boundary compression of a larger additive Tate carrier, not as the full finite-place dynamic state.

## Two-stage architecture

The source-native construction now has two levels.

### Infinite or growing local state

Use a Schwartz–Bruhat or finite-conductor additive carrier supporting:

\[
T_h,\quad M_\eta,\quad\mathcal F_p.
\]

This level retains the Weyl phase and additive covariance.

### Fixed boundary port

Apply source-derived incidence and observation maps

\[
U_{\partial}:\mathcal B_4\to\mathcal H_{\mathrm{Tate}},
\qquad
V_{\partial}^*:\mathcal H_{\mathrm{Tate}}\to\mathcal B_4,
\]

where \(\mathcal B_4\) is the wall–jump/even–odd boundary packet.

The effective four-port return is then

\[
G_4(s)
=
V_{\partial}^*(I-S_{\mathrm{Tate}}(s))^{-1}U_{\partial}.
\]

Its finite rank comes from boundary compression, not from a finite-dimensional realization of the local Weyl algebra.

## Completion gate

Finite-conductor truncations must satisfy:

1. exact Weyl covariance before compression;
2. compatibility of conductor bonding maps;
3. convergence of the compressed return \(G_{4,n}(s)\);
4. cutoff-independent boundary dimension;
5. observability of the retained odd phase;
6. annihilation or controlled routing of discarded nonspherical modes.

Entrywise convergence of the \(4\times4\) compression is insufficient if hidden additive states lose closed-range or minimality in the limit.

## Consequence for prime labels

The valuation label \(k\) remains a valid radial coordinate after the additive lift. What changes is the order of operations:

\[
e_{p,k}
\xrightarrow{j_{\mathrm{rad}}}
\mathbf 1_{S_k}
\xrightarrow{\text{Weyl/Fourier orbit}}
\mathcal H_{\mathrm{Tate},p}
\xrightarrow{\text{boundary compression}}
\mathcal B_4.
\]

Projecting back to valuation immediately after \(j_{\mathrm{rad}}\) recovers only the even shell Fourier data and loses the odd phase.

## Hostiles

1. Claim that local Fourier itself never descends to radial shells.
2. Treat the real radial Fourier matrix as the full Weyl representation.
3. Add one odd scalar coordinate and claim closure under all translations and characters.
4. Hold the local state dimension fixed while conductor grows.
5. Obtain a stable \(4\times4\) scalar return while the underlying additive realization is not minimal or compatible.

## Verdict

There is a canonical local additive lift of valuation grades: normalized shell indicators. It is sufficient for spherical Fourier transport but insufficient for the odd Weyl phase.

The required finite-place constructor is therefore a growing additive Tate realization followed by a fixed four-port boundary compression. The next calculation is to derive the incidence and observation maps of that compression from the theta and endpoint source data.
