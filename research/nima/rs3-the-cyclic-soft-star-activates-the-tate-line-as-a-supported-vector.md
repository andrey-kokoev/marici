# The cyclic soft star activates the Tate line as a supported vector

Date: 2026-08-23

A single unequal-energy path breaks the \(C_3\) isotropy at the equal-energy
point, so it cannot by itself transport the cyclic Tate quotient.  The
source-canonical geometry is instead the cyclic saturation of the path:

\[
\gamma_i(\eta):
\quad X_i=\eta,
\qquad X_j=1\ (j\ne i),
\qquad i=1,2,3.
\]

The three arms meet at \(\eta=1\) and terminate on the three labelled soft
divisors at \(\eta=0\).  Their label module is the regular module

\[
A=\mathbf F_3[C_3].
\]

Each arm has the same source-normalized soft Gysin multiplicity one.  Before
scalar summation, the combined endpoint map is therefore

\[
G_{\rm soft}:A_{\rm arms}\longrightarrow A_{\rm endpoints},
\qquad
G_{\rm soft}=1_A.
\]

This orientation input is independently frozen by Benincasa Entry 1125:
cyclic relabelling preserves both the external-normal and loop-edge residue
orientations, the three generators all have unit Gysin coefficient and deck
character \(-1\), and their transition is the regular three-cycle.  Thus the
identity matrix above is derived from the cyclic atlas rather than chosen.

It is \(C_3\)-equivariant and induces a nonzero rank-one map

\[
\boxed{
I/(g-1)I
\xrightarrow{\ \overline G_{\rm soft}\ }
I/(g-1)I.
}
\]

For the oriented generator \([g-g^{-1}]\), this induced map is the identity.
Thus the unequal-energy Tate coefficient is activated as a vector of
supported endpoint classes.

The construction lifts integrally.  On
\(I_{\mathbb Z}=\ker(\mathbb Z[C_3]\to\mathbb Z)\), the matrix of
\(g-1\) has Smith invariants \((1,3)\).  Since the endpoint Gysin is the
integral identity on the three labelled generators, it induces

\[
I_{\mathbb Z}/(g-1)I_{\mathbb Z}
\xrightarrow{\;1\;}
I_{\mathbb Z}/(g-1)I_{\mathbb Z}
\cong\mathbb Z/3.
\]

The supported vector is therefore an integral order-three class, not an
artifact manufactured by reduction modulo three.

The final scalar augmentation still vanishes:

\[
\varepsilon\,G_{\rm soft}|_I=0.
\]

There is therefore no contradiction with the frozen all-positive scalar
period.  The information is present at the supported coefficient/readout
interface and disappears only when the three labelled endpoints are summed
to an unsplit scalar.

A projection onto one chosen soft endpoint fails the cyclic naturality
square.  This negative control shows why one arm could not supply the
canonical map: source canonicity appears only after the full cyclic star is
retained.

## Architectural consequence

RS-3 now distinguishes three levels exactly:

\[
\text{generic scalar readout}=0,
\qquad
\text{single-arm specialization}=	ext{noncanonical},
\qquad
\text{cyclic supported vector readout}\ne0.
\]

The latent Tate datum is neither generically physical nor absent.  It becomes
observable at an existing carrier boundary through an equivariant
vector-valued supported readout.

## Durable evidence

- Benincasa Entry 1125 and epistemic event 834;
- research/benincasa/checkers/rank12_u2_v0_physical_soft_tate_pairing.py;
- research/nima/checkers/check_rs3_cyclic_soft_star_tate_specialization.py;
- research/nima/results/rs3-cyclic-soft-star-tate-specialization.json.
- research/nima/checkers/check_rs3_integral_soft_star_tate_descent.py;
- research/nima/results/rs3-integral-soft-star-tate-descent.json.
