# The source-to-spectral edge has an eight-node factorization from convolution polarization to the dual--canonical connection

## Edge

The conductor edge

\[
C_{13}:
V_1
\longrightarrow
V_3
\]

connects the source test/polarization presentation to the dual--canonical spectral presentation.

Fix a finite place set `S` and a source observer `g`.

## Node `C_(13,0)`: source observer

\[
\boxed{
C_{13,0}=g
\in
\mathsf{Obs}_S.
}
\]

This is the vertex `V_1` presentation before polarization or spectral transport.

## Arrow `d_(13,0)`: form the polarized convolution observer

Define

\[
h=g*g^*.
\]

More generally, retain the sesquilinear polarization

\[
h_{g_1,g_2}
=g_1*g_2^*.
\]

## Node `C_(13,1)`: convolution-square presentation

\[
\boxed{
C_{13,1}
=(g,h=g*g^*).
}
\]

This makes the Hermitian source structure explicit before applying any local factors.

## Arrow `d_(13,1)`: multiplicative Fourier/Mellin transform

Apply the multiplicative Fourier transform after the Radon--Nikodym identification:

\[
\mathcal F_\mu w(g)(s).
\]

## Node `C_(13,2)`: archimedean spectral boundary value

\[
\boxed{
C_{13,2}
=
\widehat g_\mu(s)
:=
\mathcal F_\mu w(g)(s).
}
\]

The convolution polarization becomes pointwise spectral polarization, with conjugation/reflection placed according to the source convention.

## Arrow `d_(13,2)`: apply the dual semilocal Euler transform

The semilocal Sonin/dual transform inserts

\[
A_S^+(s)
=
\prod_{p\in S\setminus\{\infty\}}
L_p(1/2+is)^{-1}.
\]

Set

\[
\widehat g_S^+(s)
=A_S^+(s)\widehat g_\mu(s).
\]

## Node `C_(13,3)`: dual weighted-space presentation

\[
\boxed{
C_{13,3}
=
(H_S^+,\widehat g_S^+),
}
\]

where

\[
H_S^+
=
L^2
\left(
\mathbb R,
|E_S^+(s)|^2ds
\right).
\]

This is one polarity of the semilocal spectral tower.

## Arrow `d_(13,3)`: construct the canonical reciprocal presentation

Use the canonical Hardy--Titchmarsh transform with the conjugate local factors

\[
E_S^-(s)
=
\prod_{v\in S}
L_v(1/2-is).
\]

This produces the canonical vector `widehat g_S^-` in

\[
H_S^-
=
L^2(\mathbb R,dm_S).
\]

## Node `C_(13,4)`: canonical/dual pair

\[
\boxed{
C_{13,4}
=
(H_S^+,\widehat g_S^+;
H_S^-,\widehat g_S^-).
}
\]

The two spaces are now present but have not yet been paired.

## Arrow `d_(13,4)`: apply the source duality pairing

Proposition 4.4 supplies the bilinear pairing

\[
B_S(\xi,\eta)
=
\int_\mathbb R
\xi(s)\eta(s)ds,
\]

which transports the original semilocal Hilbert product.

## Node `C_(13,5)`: paired spectral realization

\[
\boxed{
C_{13,5}
=
(H_S^+,H_S^-,B_S).
}
\]

The Euler amplitudes cancel in the paired norm, while their relative phase remains available to differentiated observations.

## Arrow `d_(13,5)`: form the relative scattering phase

The two unitary spectral identifications have relative operator

\[
\mathscr S_S
=(\Omega_S^+)^*\Omega_S^-
=M_{J_S^{-1}},
\]

where

\[
J_S(s)
=
\prod_{p\in S}
\frac{L_p(1/2-is)}
     {L_p(1/2+is)}.
\]

Include the archimedean ratio `J_infinity` to form `J_loc,S`.

## Node `C_(13,6)`: scattering-phase presentation

\[
\boxed{
C_{13,6}
=
(B_S,J_{loc,S}).
}
\]

This is the multiplicative local-factor phase before differentiation.

## Arrow `d_(13,6)`: differentiate the pairing metric

Define

\[
V_{loc,S}(s)
=
\frac1{2i}
\partial_s
\log J_{loc,S}(s).
\]

For finite primes,

\[
V_p(s)
=(\log p)
\sum_{k\ge1}
p^{-k/2}
\cos(ks\log p),
\]

up to the global orientation convention.

The differentiated Green identity is

\[
B_S(Df,g)
+B_S(f,Dg)
=
-2B_S(V_{loc,S}f,g)
+
\text{boundary}.
\]

## Node `C_(13,7)`: dual/canonical connection realization

\[
\boxed{
C_{13,7}
=
(H_S^+,H_S^-,B_S,V_{loc,S}).
}
\]

This is vertex `V_3`: the completed smooth local Weil current represented as the metric connection of the dual--canonical pairing.

The endpoint residue remains boundary data and is not silently included as a positive coordinate.

## Complete edge factorization

The seven arrows are

\[
\boxed{
\begin{aligned}
d_{13,0}&:
\text{observer}
\to
\text{polarization},\\
d_{13,1}&:
\text{polarization}
\to
\text{Mellin boundary value},\\
d_{13,2}&:
\text{boundary value}
\to
\text{dual Euler transform},\\
d_{13,3}&:
\text{dual transform}
\to
\text{canonical/dual pair},\\
d_{13,4}&:
\text{pair}
\to
\text{source duality pairing},\\
d_{13,5}&:
\text{pairing}
\to
\text{relative scattering phase},\\
d_{13,6}&:
\text{phase}
\to
\text{pairing connection}.
\end{aligned}
}
\]

## Level comparison with `C_24`

The two eight-node edges now have the following roles:

| Level | `C_13` source--spectral | `C_24` geometry--trace |
|---:|---|---|
| 0 | source observer | semilocal geometry |
| 1 | convolution polarization | integrated observer |
| 2 | Mellin boundary value | quotient/orbit kernel |
| 3 | dual Euler transform | product cutoff |
| 4 | canonical/dual pair | scalar cutoff trace |
| 5 | source pairing | relative/renormalized trace |
| 6 | scattering phase | local Weil sum plus error |
| 7 | differentiated connection | local Weil functional |

The levels are not equal objects. Moreover, `C_13` and `C_24` are opposite tetrahedral edges, so they do not bound a single triangular face. Rowwise comparisons between them pass through the tetrahedral interior and belong to the central filler, assembled from the adjacent faces.

## Known and missing row comparisons

- Level 0--1: representation respects convolution squares; source-backed.
- Level 1--2: Mellin transform converts convolution into spectral multiplication, while the geometric path converts it into operator composition.
- Level 2--4: Hardy--Titchmarsh diagrams compare spectral and semilocal Hilbert presentations.
- Level 5: both sides remove Euler amplitude through a relative construction--pairing on `C_13`, Plancherel volume subtraction on `C_24`; equality is not yet proved.
- Level 6--7: the logarithmic phase current must equal the normalized local principal-value trace; this is the missing `C_34` comparison.

## Degeneracy issue

The two edges use genuinely different operations at most levels. Thus a uniform subdivision cannot identify equal-index nodes directly. It needs face-interior comparison objects and homotopies.

No extra edge nodes are yet forced, but seven rowwise comparison layers between these opposite edges would be interior sections of the pyramid. Typing them requires the adjacent faces `123`, `134`, `124`, and `234` to agree through the tetrahedral filler; no single face supplies the comparison.

## Disposition

The source-to-spectral edge has a source-backed eight-node factorization ending in the gamma--prime pairing connection. Together with the eight-node geometry-to-trace edge, it isolates the unresolved upper levels:

\[
\boxed{
\text{source pairing/scattering derivative}
\quad\Longleftrightarrow\quad
\text{volume-renormalized principal-value trace}.
}
\]

Constructing the seven interior row comparisons between these two paths is the next explicit coherence-plane problem.
