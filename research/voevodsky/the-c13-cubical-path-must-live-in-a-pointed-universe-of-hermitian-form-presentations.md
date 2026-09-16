# The C13 cubical path must live in a pointed universe of Hermitian-form presentations

## Question

What universe can contain both the source and spectral endpoints of the C13 comparison and support cubical path inversion?

## Claim boundary

A typed candidate universe can be defined. Membership of the spectral endpoint requires the still-unverified premise that the source-to-spectral comparison is a natural isometric equivalence, not merely equality of selected scalar evaluations.

Fix the observer category \(\mathsf{Obs}_S\) and let \(\mathsf{Herm}\) be the category of Hermitian-form objects and isometries. A presentation is a functor

$$
P:\mathsf{Obs}_S\longrightarrow\mathsf{Herm}.
$$

Fix the source presentation \(\mathcal Q_1\). Define the pointed presentation universe

$$
\mathsf{HPres}_S
=
\sum_{P:\mathsf{Obs}_S\to\mathsf{Herm}}
\operatorname{IsoNat}(\mathcal Q_1,P).
$$

An object is therefore a presentation functor together with a natural isometric identification from the source presentation. A morphism from \((P,\theta)\) to \((P',\theta')\) is a natural isometry \(u:P\Rightarrow P'\) satisfying

$$
u\circ\theta=\theta'.
$$

The source endpoint is

$$
(\mathcal Q_1,\operatorname{id}_{\mathcal Q_1}).
$$

The spectral endpoint would be

$$
(\mathcal Q_3,\eta_{13}),
$$

but this expression is an object of \(\mathsf{HPres}_S\) only if

$$
\eta_{13}:\mathcal Q_1\xRightarrow{\simeq}\mathcal Q_3
$$

is a natural isometric equivalence on the declared observer carrier.

Intermediate nodes must likewise be presentation functors \(P_r\), each equipped with a natural isometry from \(\mathcal Q_1\). Derived data such as polarization, Mellin vectors, canonical/dual pairing, scattering phase, and logarithmic connection may decorate \(P_r\); they do not become new universe nodes unless the resulting decorated presentation remains naturally isometrically equivalent to \(\mathcal Q_1\).

If seven such objects and equivalences are constructed,

$$
(P_0,\theta_0)\simeq(P_1,\theta_1)\simeq\cdots\simeq(P_7,\theta_7),
$$

univalence turns them into seven composable universe paths, and path inversion supplies the seven reverse segments.

## First gate

The existing compact formula

$$
C_{13}(g)=(\Omega_S^+g,\Omega_S^-g)
$$

does not by itself prove membership of the spectral endpoint in \(\mathsf{HPres}_S\). The required theorem must state the common source domain, both weighted codomains, naturality in observers, preservation of the complete Hermitian form including boundary convention, and invertibility or a unitary inverse.

## Source test

Connes--Consani--Moscovici, arXiv:2310.18423, gives a unitary canonical transform into \(L^2(\mathbb R,dm_S)\), a dual transform into the opposite weighted space, and an unweighted cross pairing corresponding to the original semilocal Hilbert product. Theorem 4.6 makes semilocal amplification a Hilbertian isomorphism, and Proposition 4.7 preserves the Hilbert product under the paired Euler changes. This constructs a natural isometric equivalence for the undifferentiated Hilbert presentation.

The cited source section does not identify the differentiated cross pairing, with endpoint row, with the complete source Weil form. Therefore it does not construct the required equivalence between the declared complete \(\mathcal Q_1\) and \(\mathcal Q_3\).

## Complete-form comparison

On the compact-support observer core, the derived source identity gives

$$
\mathcal Q_1(g_1,g_2)
=
E_{\mathrm{end}}(g_1,g_2)
+
\int_{\mathbb R}
\overline{m_{g_2}(s)}m_{g_1}(s)V_{\mathrm{loc},S}(s)\,ds.
$$

Define the right-hand side to be \(\mathcal Q_3(g_1,g_2)\). The reflected logarithmic contour differential proves that its continuous gamma--prime term and endpoint residues are parts of one completed spectral current. Hence

$$
\mathcal Q_1=\mathcal Q_3
$$

as Hermitian forms on that core. The identity map on the observer carrier is therefore the natural isometry between these two form presentations. The paired canonical--dual transform supplies its spectral factorization; it is not the underlying observer map.

This equality extends to the declared logarithmic Fourier-form closure by the continuity argument in `compact-support-weil-source-identity-derived-instance.md`. Independent external verification of the centered source formula remains an authority gate.

## Seven-slot factorization test

One equivalence does not canonically determine seven nondegenerate equivalences. A valid degenerate seven-slot factorization is

$$
P_0=P_1=\cdots=P_6=\mathcal Q_1,
\qquad
P_7=\mathcal Q_3,
$$

with

$$
e_0=\cdots=e_5=\operatorname{id}_{\mathcal Q_1},
\qquad
e_6=\eta_{13}.
$$

Its composite is \(\eta_{13}\), and its reverse consists of \(\eta_{13}^{-1}\) followed by six identity equivalences. Moving the unique nonidentity segment to another slot gives six further degenerate factorizations. The endpoint equivalence supplies no canonical choice among them and no seven nontrivial intermediate presentations.

For each placement \(j\in\{0,\ldots,6\}\), define

$$
P_r^{(j)}=
\begin{cases}
\mathcal Q_1,&r\le j,\\
\mathcal Q_3,&r>j,
\end{cases}
$$

and

$$
e_r^{(j)}=
\begin{cases}
\operatorname{id}_{\mathcal Q_1},&r<j,\\
\eta_{13},&r=j,\\
\operatorname{id}_{\mathcal Q_3},&r>j.
\end{cases}
$$

These are all seven one-nondegenerate-arrow choices. For every \(j\),

$$
e_6^{(j)}e_5^{(j)}\cdots e_0^{(j)}=\eta_{13}.
$$

Adjacent placements differ only by one unit equation:

$$
\eta_{13}\operatorname{id}_{\mathcal Q_1}
=
\operatorname{id}_{\mathcal Q_3}\eta_{13}.
$$

Consequently all seven choices have the same normalized nerve: deleting identity degeneracies leaves the single nondegenerate edge \(\eta_{13}\). They provide six unit-coherence comparisons but no new semilocal constructor, intermediate form, or analytic invariant.

The seventh edgewise subdivision of the indexing simplex does not manufacture analytic intermediate objects or seventh roots of \(\eta_{13}\). A nondegenerate semilocal realization requires six independently typed intermediate Hermitian-form presentations.

## Disposition

At internal derived-source strength, the complete C13 endpoint is admitted in \(\mathsf{HPres}_S\): its natural isometry is the identity on the common observer carrier because the source and completed spectral Hermitian forms agree. A formal seven-slot path exists only degenerately. The seven previously displayed analytic formulas do not supply the six missing intermediate presentation objects.