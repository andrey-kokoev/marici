# The polarized pair kernel has a canonical linear crossing to the bordered radial response

## Question

Can the modularly oriented pair current be mapped source-derivatively to the bordered radial packet \((\rho(0),E,W,R)\), rather than defining the map by the desired scalar cancellation?

## Claim boundary

Yes on the projective ordered-pair test carrier. Shell localization, oriented half-density transport, correlation, endpoint evaluation, Wronskian differentiation, and Laplace readout compose to a continuous linear map. Radial Stokes then forces the bordered response \(R+2E\). This constructs the analytic pair-to-bordered crossing; identification of its target with the Aspect-owned arithmetic G4 adjoint remains an external declaration.

## Pair carrier

Let \(\mathscr T_\theta\) be the rapid completed-theta label space. For the analytic-transpose Evans lane form

$$
\mathscr P_\theta^{\rm an}
=\mathscr T_\theta
\widehat\otimes_\pi
\mathscr T_\theta.
$$

An elementary tensor \(f\otimes g\) retains ordered slots, and the construction below is bilinear in \((f,g)\), hence linear on this tensor product. The Hermitian Green lane instead uses \(\mathscr T_\theta\widehat\otimes_\overline{\mathscr T_\theta}\) and inserts complex conjugation in the second slot. These two variance lanes must remain distinct.

## Shell-local radial features

For a shell \([a,b]\), define on elementary tensors

$$
\rho_{f,g}^{[a,b]}(t)
=\int_a^b f(x)g(x+t)\,dx,
$$

$$
e_{f,g}^{[a,b]}(t)
=\frac12\left[
 f(b)g(b+t)
-f(a)g(a+t)
\right],
$$

and

$$
w_{f,g}^{[a,b]}(t)
=\int_a^b
\left[
 f'(x)g(x+t)
-f(x)g'(x+t)
\right]dx.
$$

These operations are continuous on the rapid projective pair space and preserve theta pair, shell, prime, and grade labels.

## Bordered Laplace packet

Set

$$
R_{f,g}(z)=\int_0^\infty e^{-zt}\rho_{f,g}(t)\,dt,
$$

$$
E_{f,g}(z)=\int_0^\infty e^{-zt}e_{f,g}(t)\,dt,
$$

$$
W_{f,g}(z)=\int_0^\infty e^{-zt}w_{f,g}(t)\,dt.
$$

Define

$$
\mathcal T_{\rm pair\to border}^{[a,b]}
(f\otimes g)
=
\left(
\rho_{f,g}(0),E_{f,g},W_{f,g},R_{f,g}
\right).
$$

By the universal property of the projective tensor product, this extends uniquely to a continuous linear map on \(\mathscr P_\theta\).

## Stokes intertwining

Integration by parts gives, for every ordered pair,

$$
\partial_t\rho_{f,g}
=e_{f,g}-\frac12w_{f,g}.
$$

Therefore the image of the crossing lies in the closed bordered relation

$$
zR-\rho(0)=E-\frac12W.
$$

The combined return readout

$$
\mathcal J_{\rm RL}(\rho_0,E,W,R)
=R+2E
$$

is consequently equivalent to

$$
\mathcal J_{\rm RL}
=
\frac{\rho_0+E-W/2}{z}+2E,
$$

with the divided term understood by its removable extension at \(z=0\).

No coefficient is selected from Xi zeros or shell cancellation.

## Modular orientation

Before forming the pair tensor, oriented radial half-density transport applies the Jacobian factor \(r^{1/2}\) to each leg. On labels this turns \(K(n,m)\) into

$$
K_{1/2}(n,m)=\sqrt{nm}K(n,m).
$$

Thus the crossing inherits

$$
K_{1/2}(pn,pm)=pK_{1/2}(n,m)
$$

and the correct additive-to-multiplicative Haar orientation.

## Slot reversal

Exchanging \(f\) and \(g\), together with radial reflection, exchanges the correlation slots and reverses the Wronskian sign. Hence the crossing retains the ordered reciprocal/linking orientation rather than passing to a symmetric scalar pair current.

## Cutoffs and jets

Shell differences concatenate exactly, finite label cutoffs commute with every operation, and

$$
\partial_z^jR(z)
=(-1)^j\int_0^\infty t^je^{-zt}\rho(t)\,dt
$$

with analogous formulas for \(E,W\). Rapid theta decay gives continuity for every fixed jet order and projective completion.

## Explicit composite

The crossing is the source composite

$$
\boxed{
\mathcal T_{\rm pair\to border}
=
\operatorname{Laplace}
\circ
(\rho_0,e,w,\rho)
\circ
\operatorname{Loc}_{[a,b]}
\circ
(C_{1/2}\widehat\otimes C_{1/2})
}
$$

in the analytic-transpose lane. The Hermitian lane uses

$$
C_{1/2}\widehat\otimes\overline{C_{1/2}}
$$

and conjugates the second-slot feature formulas.

Every arrow is independently defined before applying the Evans residual.

## External boundary

This constructs the map formerly denoted

$$
T_{\theta\to{\rm cyc2},p}
\quad\text{followed by}\quad
T_{\rm end}
$$

when the cyclic-square target is represented by the polarized pair density rather than an output-only scalar grade.

It does not prove that the existing Aspect-owned conservative G4 block uses \(\mathcal J_{\rm RL}\mathcal T_{\rm pair\to border}\) as its arithmetic adjoint return. Declaring that equality is the remaining chain-placement theorem.

## Disposition

The pair-current-to-bordered-radial crossing is analytically constructed as a continuous linear map on the polarized projective pair carrier, with modular orientation, Stokes relation, shell naturality, and all jets exact. The sole remaining issue is external G4 block identification, not construction of the crossing itself.