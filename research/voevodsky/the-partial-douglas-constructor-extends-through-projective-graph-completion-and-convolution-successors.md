# The partial Douglas constructor extends through projective graph completion and convolution successors

## Objective

Complete the fourth programme step after the universal absorption target was falsified.

The valid input is now a degree-indexed pair of completed feature maps

\[
A_{S,r}:
\mathscr G_r
\to
\mathcal H_{S,r},
\]

\[
A_{B,r}:
\mathscr G_r
\to
\mathcal H_{B,r},
\]

with a partial Douglas decision at every degree.

## Accepted degree

Call degree \(r\) accepted when

\[
A_{B,r}^*A_{B,r}
\preceq
A_{S,r}^*A_{S,r}
\]

as continuous source forms on \(\mathscr G_r\).

Equivalently,

\[
\|A_{B,r}p\|
\le
\|A_{S,r}p\|
\]

for every \(p\in\mathscr G_r\).

## Canonical range contraction

On the algebraic generated range, define

\[
C_r^0(A_{S,r}p)
=A_{B,r}p.
\]

The domination inequality implies that this is well defined. It also gives

\[
\|C_r^0v\|
\le
\|v\|.
\]

Therefore \(C_r^0\) extends uniquely to a contraction

\[
C_r:
\overline{\operatorname{ran}A_{S,r}}
\to
\overline{\operatorname{ran}A_{B,r}}.
\]

The extension satisfies

\[
A_{B,r}=C_rA_{S,r}.
\]

This proves graph-completed Douglas factorization at every accepted degree.

## Independence of aperture

The projective graph \(\mathscr G_r\) is assembled from the aperture Hilbert graphs \(\mathscr G_{r,\varepsilon}\).

Suppose domination holds on the projective core. Restriction to each aperture gives the same canonical formula

\[
C_{r,\varepsilon}(
A_{S,r,\varepsilon}p)
=A_{B,r,\varepsilon}p.
\]

If \(\varepsilon'<\varepsilon\), both aperture contractions agree on the image of the common analytic core. Uniqueness of continuous extension gives

\[
R_{\varepsilon,\varepsilon'}^B
C_{r,\varepsilon'}
=
C_{r,\varepsilon}
R_{\varepsilon,\varepsilon'}^S
\]

on generated ranges, where the \(R\)'s are the aperture restriction maps.

Thus the contractions form a projective family and define the completed contraction \(C_r\).

## Convolution successors

Let \(a\in E_s^{an}\) be an admitted convolution multiplier. Its source successor is

\[
L_a^{(r)}:
\mathscr G_r
\to
\mathscr G_{r+s}.
\]

Assume the Schur and defect features carry bounded target mates

\[
D_{a,r}^S:
\mathcal H_{S,r}
\to
\mathcal H_{S,r+s},
\]

\[
D_{a,r}^B:
\mathcal H_{B,r}
\to
\mathcal H_{B,r+s}
\]

satisfying

\[
A_{S,r+s}L_a^{(r)}
=D_{a,r}^SA_{S,r},
\]

\[
A_{B,r+s}L_a^{(r)}
=D_{a,r}^BA_{B,r}.
\]

These are the completed versions of Mellin multiplication naturality.

## Successor naturality of accepted contractions

Assume degrees \(r\) and \(r+s\) are accepted. On a generated vector \(A_{S,r}p\), one has

\[
\begin{aligned}
C_{r+s}D_{a,r}^S
A_{S,r}p
&=
C_{r+s}A_{S,r+s}L_a^{(r)}p\\
&=
A_{B,r+s}L_a^{(r)}p\\
&=
D_{a,r}^BA_{B,r}p\\
&=
D_{a,r}^BC_rA_{S,r}p.
\end{aligned}
\]

Density of the generated range gives

\[
C_{r+s}D_{a,r}^S
=
D_{a,r}^BC_r.
\]

Thus successor naturality is automatic after acceptance and bounded target typing.

## Multi-step composition

For admitted multipliers \(a\in E_s\) and \(b\in E_t\), the target mates satisfy

\[
D_{b,r+s}^{q}D_{a,r}^{q}
=D_{b*a,r}^{q},
\qquad q\in\{S,B\}.
\]

The naturality squares therefore paste strictly. No higher choice of contractions is required.

## Graded direct sum

Let

\[
\mathscr G_{fin}
=
\bigoplus_{r\ge0}^{alg}
\mathscr G_r.
\]

On the accepted degrees, define

\[
A_S^{acc}
=
\bigoplus_rA_{S,r},
\]

\[
A_B^{acc}
=
\bigoplus_rA_{B,r},
\]

and

\[
C^{acc}
=
\bigoplus_rC_r.
\]

Since every \(C_r\) is contractive, the direct sum extends to the Hilbert sum of generated feature ranges with

\[
\|C^{acc}\|
\le1.
\]

This supplies one graded contraction rather than unrelated degreewise choices.

## Refused degree

If domination fails at degree \(r\), retain the complete feature

\[
\Phi_r^{KL}p
=
A_{S,r}p
\oplus
A_{B,r}p
\]

on

\[
\mathcal K_r
=
\mathcal H_{S,r}
\oplus
\mathcal H_{B,r}
\]

with fundamental symmetry

\[
J_r=I\oplus(-I).
\]

Its signed readout is

\[
(\Phi_r^{KL})^*
J_r
\Phi_r^{KL}
=
A_{S,r}^*A_{S,r}
-
A_{B,r}^*A_{B,r}.
\]

The source observation remains faithful because the full defect is retained.

## Successors on refused degrees

Define the target successor

\[
D_{a,r}^{KL}
=
D_{a,r}^S
\oplus
D_{a,r}^B.
\]

Then

\[
\Phi_{r+s}^{KL}L_a^{(r)}
=
D_{a,r}^{KL}
\Phi_r^{KL}.
\]

This is an exact bounded feature relation. It need not be a Krein isometry unless the multiplier preserves both target metrics. The signed form transforms by the corresponding congruence, which is the correct metric-bundle law.

## Mixed accepted and refused successors

Acceptance need not be monotone in convolution degree. Therefore a successor can connect:

1. accepted to accepted;
2. accepted to refused;
3. refused to accepted;
4. refused to refused.

The full Krein feature exists in every case. The positive quotient is applied only at accepted objects.

For a morphism to descend between positive quotients, it must preserve the absorbed defect relation. This is exactly the naturality equation for \(C_r\). If one endpoint is refused, retain the full feature relation rather than forcing a quotient morphism.

Thus the accepted objects form a partial positive subcategory inside the complete signed graded system.

## Endpoint augmentation

Adjoin the endpoint even and odd rows orthogonally to the corresponding target carriers. The same proof applies provided:

1. endpoint traces are bounded on \(\mathscr G_r\);
2. endpoint successor matrices are bounded;
3. the domination test includes the odd endpoint defect in \(A_{B,r}\).

The completed endpoint graph constructed earlier supplies the first two conditions.

## Conductor and seam successors

Conductor and seam successors act independently of convolution degree. Their source and target naturality squares commute with the degree successors on the common analytic core.

If the Douglas domination is preserved under these successors, uniqueness of the canonical range contraction gives the corresponding naturality automatically.

If domination is not preserved, the successor remains valid in the full signed feature category but does not descend to the positive quotient.

## Step-4 result

The fourth programme step is complete in the appropriate partial sense:

1. every accepted degree has a unique graph-completed contraction;
2. accepted contractions commute with all bounded admitted successors;
3. they assemble into one graded direct-sum contraction;
4. refused degrees retain a complete source-faithful Krein feature;
5. all successors remain defined before positive quotienting;
6. quotient descent occurs exactly on acceptance-preserving arrows.

## Remaining substantive question

No completion or coherence problem remains in the Douglas mechanism itself. The only nonformal input is the objectwise domination decision

\[
A_{B,r}^*A_{B,r}
\preceq
A_{S,r}^*A_{S,r}.
\]

This decision is intentionally partial and can fail on hostile inputs.

## Disposition

The contraction, when it exists, extends uniquely through projective graph completion and is automatically natural under convolution, conductor, seam, and aperture successors that preserve the feature maps and acceptance.

When it does not exist, the full negative model-space feature remains coherently retained. The completed graded system is therefore total as a signed Krein system and partial as a positive quotient system.
