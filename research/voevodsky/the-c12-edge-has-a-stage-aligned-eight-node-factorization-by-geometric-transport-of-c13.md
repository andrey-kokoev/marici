# The C12 edge has a stage-aligned eight-node factorization by geometric transport of C13

## Objective

Package the seven source-verified \(C_{12}\)-direction transfers adjacent to the factored \(C_{13}\) edge as one autonomous chain of Hermitian-form presentations.

This introduces no new analytic identity. It assembles the segmentwise results of `c13-segmentwise-c12-triangulation-audit.md` into a standalone edge object.

## Common carrier

Fix the observer-generated semilocal carrier and the source-derived Hardy--Titchmarsh unitary

\[
\mathcal T_S:
\mathcal H_{geom,S}
\xrightarrow{\sim}
\mathcal H_{spec,S}.
\]

Every spectral presentation on \(C_{13}\) is transported geometrically by conjugation with \(\mathcal T_S\). Since the transport is unitary, all polarized Gram forms are preserved.

Write

\[
\Sigma_S^\pm
=\mathcal T_S^{-1}\Omega_S^\pm\mathcal T_\infty
\]

for the two source-derived geometric identifications and

\[
\mathscr R_{geom,S}
=(\Sigma_S^+)^*\Sigma_S^-
=\mathcal T_\infty^*M_{J_S^{-1}}\mathcal T_\infty.
\]

## Eight nodes

### Node \(C_{12}[0]\): source observer

\[
\boxed{C_{12}[0]=g.}
\]

### Node \(C_{12}[1]\): represented convolution polarization

Let \(h=g*g^*\). Define

\[
\boxed{
C_{12}[1]
=
\left(U_S(g),
U_S(h)=U_S(g)U_S(g)^*
\right).
}
\]

### Node \(C_{12}[2]\): geometric Mellin boundary presentation

Transport the multiplicative Mellin boundary vector back to the geometric carrier:

\[
\boxed{
C_{12}[2]
=x_g
:=
\mathcal T_S^{-1}\widehat g_\mu.
}
\]

This retains the integrated representation as factorization data.

### Node \(C_{12}[3]\): semilocal Sonin-amplified geometry

Let

\[
x_g^+
=\Sigma_S^+x_g.
\]

Then

\[
\boxed{
C_{12}[3]
=(\mathcal H_{geom,S}^+,x_g^+).
}
\]

Its spectral image satisfies

\[
\mathcal F_\mu w_S(\Sigma_Sf)
=A_S^+\mathcal F_\mu w(f).
\]

### Node \(C_{12}[4]\): dual/canonical geometric pair

Define

\[
x_g^-=\Sigma_S^-x_g.
\]

Set

\[
\boxed{
C_{12}[4]
=(
\mathcal H_{geom,S}^+,x_g^+;
\mathcal H_{geom,S}^-,x_g^-
).
}
\]

### Node \(C_{12}[5]\): geometrically transported source pairing

Define

\[
B_S^{geom}(x_+,x_-)
=
B_S(\mathcal T_Sx_+,\mathcal T_Sx_-).
\]

Then

\[
\boxed{
C_{12}[5]
=(
\mathcal H_{geom,S}^+,
\mathcal H_{geom,S}^-,
B_S^{geom}
).
}
\]

### Node \(C_{12}[6]\): relative geometric scattering operator

Adjoin

\[
\mathscr R_{geom,S}
=(\Sigma_S^+)^*\Sigma_S^-.
\]

Set

\[
\boxed{
C_{12}[6]
=(
\mathcal H_{geom,S}^+,
\mathcal H_{geom,S}^-,
B_S^{geom},
\mathscr R_{geom,S}
).
}
\]

### Node \(C_{12}[7]\): geometric Weil connection

Transport the differentiated relative phase:

\[
V_{geom,S}
=
\mathcal T_\infty^*
M_{V_{loc,S}}
\mathcal T_\infty,
\qquad
V_{loc,S}
=\frac1{2i}\partial_s\log J_{loc,S}.
\]

Define

\[
\boxed{
C_{12}[7]
=(
L^2(X_S)^{K_S},
U_S,F_S,
B_S^{geom},
\mathscr R_{geom,S},
V_{geom,S}
).
}
\]

Forgetting the final three observed structures gives the declared semilocal geometric vertex \(V_2\). Thus the endpoint is an enriched presentation of \(V_2\), not a new fifth vertex.

## Seven arrows

The arrows are:

\[
\sigma_{12}[0]:
 g
\longmapsto
\left(U_S(g),U_S(g)U_S(g)^*\right),
\]

\[
\sigma_{12}[1]:
\text{represented convolution polarization}
\longmapsto
\text{geometric Mellin boundary value},
\]

\[
\sigma_{12}[2]:
 x_g
\longmapsto
\Sigma_S^+x_g,
\]

\[
\sigma_{12}[3]:
 x_g^+
\longmapsto
(x_g^+,x_g^-),
\]

\[
\sigma_{12}[4]:
(x_g^+,x_g^-)
\longmapsto
B_S^{geom},
\]

\[
\sigma_{12}[5]:
B_S^{geom}
\longmapsto
(B_S^{geom},\mathscr R_{geom,S}),
\]

\[
\sigma_{12}[6]:
\mathscr R_{geom,S}
\longmapsto
V_{geom,S}.
\]

Every arrow is the source-derived geometric transport recorded in the segmentwise audit.

## Stagewise face 123

Let \(C_{13}[r]\) be the established source-to-spectral nodes. The Hardy--Titchmarsh realization gives stagewise comparison cells

\[
H_{123}[r]:
C_{23}[r]C_{12}[r]
\Rrightarrow
C_{13}[r].
\]

For \(r=0,\ldots,6\), the square comparing \(\sigma_{12}[r]\) with \(\sigma_{13}[r]\) commutes by one of:

1. the star-representation law;
2. Mellin convolution/multiplication;
3. semilocal Sonin amplification;
4. the two source-derived Hardy--Titchmarsh identifications;
5. transported source duality;
6. unitary conjugation of the relative scattering phase;
7. conjugation of the differentiated Green identity.

Hence the chain is aligned stage by stage with \(C_{13}\).

## Categorical representation

Each node is a Hermitian-form presentation on the same observer category. Each arrow preserves the represented polarized form. The chain therefore defines a factorization

\[
\boxed{
\eta_{12}
=
\sigma_{12}[6]
\circ\cdots\circ
\sigma_{12}[0]
}
\]

in the observer-generated realization category, followed at the endpoint by forgetting the auxiliary pairing, scattering, and connection coordinates.

The auxiliary coordinates are essential for stagewise coherence but do not alter the underlying geometric representation.

## Scope

This construction is:

- source-derived on the observer-generated carrier;
- aligned with all seven \(C_{13}\) stages;
- exact in the signed realization category;
- compatible with the iterated-regulator relative-positive lift already established for the adjacent faces.

It does not assert:

- a simultaneous-regulator ordinary-Hilbert realization;
- uniform completed-space coercivity;
- that unrelated independently chosen \(C_{14}\) stage labels are aligned with this chain.

## Disposition

The previously missing standalone bookkeeping object is now explicit:

\[
\boxed{
C_{12}[0]
\to C_{12}[1]
\to\cdots\to C_{12}[7].
}
\]

It is the geometric transport of the source-backed \(C_{13}\) factorization, with endpoint an enriched semilocal geometric presentation whose forgetful image is \(V_2\).
