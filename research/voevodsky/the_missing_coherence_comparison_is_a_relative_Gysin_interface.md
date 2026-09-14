# The missing coherence comparison is a relative Gysin interface

## Final structural identification

The accumulated exact calculations separate three objects that had previously been conflated.

### 1. Absolute fixed-pencil Picard lattice

The four oriented split-fiber component differences generate, after primitive closure,

\[
L_b\cong A_1^3
=
\mathbb Z\alpha_{12}
\oplus\mathbb Z\alpha_{13}
\oplus\mathbb Z\alpha_{14}.
\]

The first normal-jet comparison supplies the primitive absolute response

\[
q_{e_6}=(-1,0,0),
\]

so \(\alpha_{12}\) is the shared \(e_6\) direction and

\[
L_b^{\rm route}=\ker q_{e_6}
=
\langle\alpha_{13},\alpha_{14}\rangle.
\]

### 2. Relative two-wall extension lattice

The two labelled one-wall extensions form a separate lattice

\[
W=\mathbb Zw_{101}\oplus\mathbb Zw_{110}.
\]

Their universal algebraic tails give the primitive response

\[
q_{v_{\rm alg}}^W=(-1,+1),
\qquad
\ker q_{v_{\rm alg}}^W
=
\mathbb Z\langle w_{101}+w_{110}\rangle.
\]

Thus wall-route difference is visible and wall-route sum is physically null in the source-derived relative extension calculation.

### 3. Absolute chamber transport

Site exchange and smooth physical-chamber Gauss--Manin return preserve the ordered split-fiber labels. Their matrix on \(L_b\) is the identity. Therefore they do not identify the relative wall basis with the two fixed-pencil route axes.

## The missing arrow

The required comparison is exactly an integral relative-to-absolute Gysin interface

\[
\boxed{
J:W\longrightarrow L_b^{\rm route}.
}
\]

It must satisfy:

1. **integrality:** \(J\) has integral columns;
2. **primitivity:** its image is saturated if it is to carry unit-normalized routes;
3. **orientation compatibility:** it transports the source wall orientation local system;
4. **response compatibility:**
   \[
   q_{v_{\rm alg}}^{L_b}\circ J=q_{v_{\rm alg}}^W;
   \]
5. **null descent:**
   \[
   J(w_{101}+w_{110})\subseteq K_{\rm route}.
   \]

This is not an ordinary Picard continuation, a boundary residue, or an identification with the conductor \(A_2\) lattice.

## Information flow

The complete typed flow is

\[
\{d_i\}
\longrightarrow
L_b=A_1^3
\xrightarrow{q_{e_6}}
\mathbb Ze_6,
\]

and independently

\[
(w_{101},w_{110})
\xrightarrow{(-1,+1)}
\mathbb Zv_{\rm alg}.
\]

The missing interface joins them:

\[
W
\xrightarrow{J}
L_b^{\rm route}
\longrightarrow
L_b/K_{\rm route}
\longrightarrow
\langle e_6,v_{\rm alg}\rangle
\longrightarrow
\text{physical period readout}.
\]

## Residual ambiguity

If \(J\) is an integral isometry of the two \(A_1^2\)-type route frames, only one orientation bit remains. The fixed-pencil kernel is one of

\[
\mathbb Z\langle\alpha_{13}+
\alpha_{14}\rangle,
\qquad
\mathbb Z\langle\alpha_{13}-
\alpha_{14}\rangle.
\]

The relative wall kernel is already known; only its signed image under \(J\) is not.

## Decision datum

One labelled signed Gysin column, such as \(J(w_{110})\) in the \((\alpha_{13},\alpha_{14})\) frame, decides the final bit. No full Picard matrix or new period integration is necessary.

Verification:

- `research/voevodsky/checkers/check_relative_Gysin_interface_synthesis.py`
- `research/voevodsky/results/relative_Gysin_interface_synthesis.json`
