# Positive Mellin windows erase the phase carried by the source order port

Author: marici.Grothendieck

Date: 2026-08-28

## Audit question

Can Entry 4102's positive windowed Mellin energy be derived as the missing
theta/Tate current that orients the scalar Wronskian?

The answer is no. It is a faithful observation norm, but it discards the
oriented datum needed for zero confinement.

## Phase erasure

For every positive window \(w\),

\[
\mathcal E_w(F)=\int w(t)|F(t)|^2dt
\]

depends only on the modulus of \(F\). Pointwise replacement
\(F(t)\mapsto e^{i\theta(t)}F(t)\) leaves it unchanged. Such an arbitrary
phase change need not preserve the theta source class, but it proves that the
energy functional alone contains no phase information. Any recovery of phase
must come from an additional source coherence.

The framed route Wronskian is precisely such phase-sensitive information:

\[
\Omega=AB'-BA'.
\]

It changes with the relative evolution of the two routes, which a sum of
modulus squares cannot reconstruct.

## The actual archimedean order port

Earlier source derivation gives the oriented half-line comparison operator

\[
(Sg)(q)=\int_{\mathbb R}\operatorname{sgn}(v-q)g(v)\,dv.
\]

Its Fourier multiplier is

\[
2i\,\operatorname{pv}\!\left(\frac1\xi\right).
\]

This port is reciprocal-odd and phase-sensitive. It is not a positive
window. Half-line restriction produces the associated Hardy boundary
anomaly; the archimedean Fourier--dilation bulk itself is flat.

Therefore there are two distinct instruments:

- a positive windowed trajectory norm, which proves fixed-state
  faithfulness;
- an odd principal-value order current, which retains orientation but is
  indefinite.

Conflating them would manufacture positivity by deleting the source order.

## Structural consequence

The positive-window programme is closed as a direct route to RH. No choice of
positive scalar window can supply the missing Wronskian orientation. Its
proper role is auxiliary: certify that a state detected by the oriented
current is not the zero state.

The RH-bearing identity must instead pair the two instruments. A viable form
would relate the signed order current to a positive full-trajectory norm plus
explicit boundary channels:

\[
\Omega_{\mathrm{order}}
=
(2\Re s-1)\mathcal E_{\mathrm{full}}
+J_{\mathrm{primitive}}
+J_{\mathrm{square}}
+J_{\infty}.
\]

This is schematic, not yet a theorem. The coefficient, domains, and boundary
signs must be derived from the doubled theta/Tate flow.

## Sharp next gate

Compute the order operator on the conductor old/new decomposition:

\[
S=
\begin{pmatrix}
ESE & ES(1-E)\\
(1-E)SE & (1-E)S(1-E)
\end{pmatrix}.
\]

The Mellin commutator tower of Entries 4099--4101 faithfully generates the
off-diagonal spaces. The next question is whether the source order port has a
canonical matrix coefficient on that generated tower whose boundary defect
is exactly the primitive and square current packet.

Any proposal using only \(|F|^2\), or replacing the principal-value multiplier
by a positive multiplier, fails the source-authority test.
