# Branch A: coherent endpoint/Q framing and primary-fixed comparisons

Date: 2026-09-07.

## Result and scope

The computed regulator obstruction survives a precisely specified homotopy-coherent frame. That frame retains the full fourteen-state Q quotient and the two genuine endpoint-top quotient complexes, including their occurrence partners. Its homotopy fibre is explicitly equivalent to a 412-state subcomplex of the complete 430-state coefficient complex.

In the complete occurrence-weight-zero component, over `Lambda = Z[beta]`, the framed kernel has

\[
H_1=(\Lambda/(\beta))^8,\qquad
H_2=\Lambda^4\oplus(\Lambda/(\beta))^{12},\qquad
H_3=0.
\]

The previously computed attaching class `chi_beta` is a primitive, split free summand of the displayed H2. Forgetting the endpoint-top frame sends its cyclic submodule to `Lambda/(beta^2)` in the ordinary short boundary.

The coherent supported-map space has twelve degree-zero homotopy classes. All twelve change the primary class. For a specified primary admitting a lift, the space of coherent endpoint/Q-framed lifts is contractible in this component. The previously attempted primary `-beta chi_beta` has no such lift.

These are results in the explicitly defined coefficient-frame category. They do not construct the independent physical conductor homotopy or identify the physical Delta_J. A stronger frame retaining further comparison cells must be specified and tested separately; this calculation does not classify frame-only classes that such extra data might introduce.

## 1. Source coefficients and complete state space

Use

\[
R=\mathbb Z[\beta,X_d:d\in\mathscr D]/(X_eX_o:e\in S_-,\ o\in S_+),
\]

\[
\mathscr D=(02,03,04,13,14,15,24,25,35),\quad
S_-=(02,04,24),\quad S_+=(13,15,35).
\]

The normalized native normal differential is `beta X_d`. The independent occurrence-35 differential is `X35`. The exponential frame units are not used to cancel beta. Substitution of the actual exponential units remains characteristic-zero formal algebra; its geometric purity theorem in the inspected source assumes fixed nonzero beta.

The complete source has states

\[
[F,H,\epsilon],\qquad H\subset F,\quad\epsilon\in\{0,1\},
\qquad |[F,H,\epsilon]|=3-|F|+|H|+\epsilon.
\]

The differential is

\[
\begin{aligned}
d[F,H,\epsilon]={}&
\sum_{a\in A(F)}(-1)^{\#\{b\in F:b<a\}}X_a[F\cup\{a\},H,\epsilon]\\
&+(-1)^{3-|F|}\sum_{h\in H}(-1)^{\operatorname{pos}(h)}\beta X_h
[F,H\setminus\{h\},\epsilon]\\
&+\epsilon(-1)^{3-|F|+|H|}X_{35}[F,H,0].
\end{aligned}
\]

Here A(F) is the set of diagonals that can be inserted while keeping the dissection noncrossing. The supplied cellular model has 430 states, its short boundary B has 416 states, and the two endpoint subcomplexes V have 32 states. The actual quotient Q=C/B has fourteen states.

Provenance is pinned to commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61` in `andrey-kokoev/marici`:

- `research/voevodsky/check_absolute_unlocalized_support_pc.rs`: signed radial/native differential and actual support subcomplexes.
- `research/voevodsky/check_d03_pabs_morse_pullback.rs`: separate occurrence correction.
- `research/voevodsky/check_d03_formal_support_purity.rs`: formal exponential graph and fixed-nonzero-beta geometric scope.
- Entry 93: alternating normalization ring.

The preceding endpoint/Q-transgression verifier was rerun independently and reproduced its certificate byte-for-byte. The new checker is standalone and reconstructs the necessary chains structurally; it does not import a previous checker or require its certificate.

## 2. A genuine boundary map, including endpoint comparison homotopies

Coordinate projection onto the entire endpoint subcomplex is generally not a chain map. It is not used here.

For each endpoint F=S_- or S_+, retain precisely its fully native-marked top and the same top with its occurrence partner. They form a quotient

\[
E_F^{\mathrm{top}}=[Rq_{F,4}\xrightarrow{-X_{35}}Rq_{F,3}]
\]

in homological degrees four and three. Projection onto these two rows is a chain map. No radial arrow can enter a fully marked endpoint from a proper face, and normal differentials remove marks. Its only internal incoming arrow is the occurrence differential displayed above.

Set

\[
\mathcal D=Q\oplus E_-^{\mathrm{top}}\oplus E_+^{\mathrm{top}},\qquad
\rho=(\pi_Q,\pi_-,\pi_+):C\longrightarrow\mathcal D.
\]

This is an eighteen-state, degreewise surjective chain-map boundary. It fixes the full Q object and these two specified endpoint-top normal grades. All other endpoint states remain in C; they have not been replaced by scalar residues.

Let

\[
\mathcal K=\ker\rho.
\]

It has 412 states: the 416 short-boundary states, except the four endpoint-top states recorded as boundary data. The full differential preserves this kernel.

### Explicit coherent fibre

Use the homological fibre convention

\[
\mathcal F_n=C_n\oplus\mathcal D_{n+1},\qquad
\partial_{\mathcal F}(c,h)=(dc,\rho c-d_{\mathcal D}h).
\]

The additional components are the retained comparison homotopies. The full fibre has 448 states.

Let j be the labelled graded section of rho and put

\[
\alpha=d_Cj-jd_{\mathcal D}:\mathcal D_n\longrightarrow\mathcal K_{n-1}.
\]

Then

\[
\Pi(c,h)=c-j\rho c-\alpha h,\qquad
I(k)=(k,0),\qquad H(c,h)=(jh,0)
\]

satisfy

\[
\Pi I=1,\qquad
\partial_{\mathcal F}H+H\partial_{\mathcal F}=1-I\Pi.
\]

The projection and inclusion are chain maps. These identities are checked on all 448 fibre basis states and all 412 kernel basis states. No coefficient is inverted. The formula is the termwise-split mapping-cone contraction; it retains the endpoint/Q homotopies rather than replacing them by strict zero without a comparison.

Thus the homotopy-coherent frame is equivalent to the strict kernel for this actual surjective chain map. This is not an assumption that every physical frame can be strictified in the same way.

## 3. Complete polynomial normal forms

Assign occurrence degree

\[
\deg_X[F,H,\epsilon]=-
\sum_{d\in F}\varepsilon_d+\sum_{d\in H}\varepsilon_d+\epsilon\varepsilon_{35}.
\]

In occurrence weight zero, the coefficient monomial is forced. A state contributes exactly when

\[
m_{F,H,\epsilon}=
\prod_d X_d^{\mathbf1_{d\in F}-\mathbf1_{d\in H}-\epsilon\mathbf1_{d=35}}
\]

has nonnegative exponents and survives the mixed-sheet ideal. The coefficient of this basis vector is an arbitrary polynomial in beta.

The resulting free Lambda-complexes have sizes 231 for C, 224 for B, and 222 for K. The boundary has nine states in this component. No bound on beta degree is imposed.

Every differential entry is an integer times a monomial

\[
\beta^{n_H(j)-n_H(i)}.
\]

Here j is the source state and i the target state. The checker constructs explicit polynomial changes of basis with determinant one. At each step, a minimal-power coefficient plus or minus one divides the entries needed for elimination. The quotient powers are nonnegative. Blocks with nonunit differential beta or beta squared are retained as two-state complexes; they are never contracted.

This is an explicit construction over Z[beta], not an appeal to a Smith-form theorem over a principal ideal domain. All inverse matrices and chain equations are checked again using literal polynomial powers.

The homology is:

| Complex | H1 | H2 | H3 |
|---|---|---|---|
| C | `(Lambda/(beta))^6` | `Lambda^3 + (Lambda/(beta))^12` | `Lambda^2` |
| B | `(Lambda/(beta))^8` | `Lambda^3 + (Lambda/(beta))^12 + Lambda/(beta^2)` | `Lambda` |
| K | `(Lambda/(beta))^8` | `Lambda^4 + (Lambda/(beta))^12` | `0` |

All other homology groups vanish. A plus sign in this table denotes a direct sum. The certificate exports every normal-form block, both change-of-basis matrices, and all elementary operations.

## 4. The transgression is a split free framed class

In the actual Q component let

\[
\varphi_Q=\beta T-h_{03}-h_{14}-h_{25}.
\]

Lift those four labelled terms to C and define

\[
\chi_\beta=d\widetilde\varphi_Q.
\]

This is the eighteen-term short-boundary cycle from the previous computation. It has zero joint boundary rho, so it is a cycle in K.

The structural full top cycles are

\[
\Psi_\beta=\sum_F(-1)^{|F|(|F|+1)/2}\beta^{3-|F|}[F,F,0],
\]

\[
Z_-=P_\beta\Psi_\beta,\qquad Z_+=\Psi_\beta-Z_-.
\]

The operator P_beta replaces a native 35 mark by beta times the separate occurrence partner and kills a state containing both. Direct computation gives

\[
\pi_QZ_-=\beta^2\varphi_Q,\quad\pi_QZ_+=0,\quad
(\pi_-,\pi_+)(Z_-)=(1,0),\quad
(\pi_-,\pi_+)(Z_+)=(0,1)
\]

on the native endpoint-top coordinates in occurrence degree zero.

The old primitive

\[
W_\beta=\beta^2\widetilde\varphi_Q-Z_-,\qquad
 dW_\beta=\beta^2\chi_\beta
\]

has endpoint-top boundary value -1 at the negative endpoint. It is not in K.

The new normal form supplies a polynomial cochain

\[
\ell:\mathcal K_{(0)}\longrightarrow\Lambda[2],\qquad
\ell d=0,\quad\ell(\chi_\beta)=1.
\]

Its twelve coefficients are exported, with the corresponding face/mark states. Thus

\[
\Lambda[\chi_\beta]\cong\Lambda
\]

is an explicitly split summand of H2(K). In particular, both beta chi and beta squared chi remain nonzero in the coherent endpoint/Q-frame.

Forgetting the endpoint-top frame maps this cyclic submodule to Lambda/(beta squared) in H2(B). The old annihilating homotopy removes the cycle only by changing its specified endpoint comparison. The coherent fibre calculation does not admit that as a homotopy with the same retained frame.

### Consequence for the prior attempted lift

The supported difference, after its Q-nullhomotopy was removed, had components

\[
p\longmapsto-\beta\chi_\beta,\qquad e\longmapsto-W_\beta,
\quad de=\beta p.
\]

A framed replacement with the same primary homology class would require an upper chain Y in K satisfying

\[
dY=-\beta^2\chi_\beta.
\]

Applying ell yields 0=-beta squared in Lambda. Hence no such lift exists. Allowing the endpoint/Q comparison homotopies does not remove the obstruction: the explicit fibre/kernel equivalence includes those homotopies already.

This is nonexistence of that proposed framed lift, not a nonzero physical Delta_J.

## 5. Twelve coherent supported maps, all with nonzero primary changes

Retain

\[
S_\beta=[Re\xrightarrow{\beta}Rp],\qquad |e|=3,\quad|p|=2.
\]

Since this is bounded free,

\[
\operatorname{RHom}_R(S_\beta,\mathcal F)
\simeq\operatorname{Hom}_R(S_\beta,\mathcal K).
\]

The full occurrence-weight-zero internal Hom has 444 generators over Lambda. Its exact normal form gives

\[
H^0=(\Lambda/(\beta))^{12},\qquad
H^1=(\Lambda/(\beta))^{24},\qquad
H^2=(\Lambda/(\beta))^8,
\]

with all other cohomology zero. Negative cohomology vanishes, so the space of degree-zero maps has no higher homotopy groups. The positive cohomology groups above are extension groups, not higher homotopy groups of that space.

For each of the twelve nonendpoint triangulations F, define

\[
E_F=[F,F,0],\qquad
B_F=\sum_{j=1}^3(-1)^{j-1}X_{a_j}[F,F\setminus\{a_j\},0],
\quad F=(a_1<a_2<a_3).
\]

Then

\[
dE_F=\beta B_F,\qquad dB_F=0,
\]

and

\[
\Gamma_F(p)=B_F,\qquad\Gamma_F(e)=E_F
\]

is a supported map into K. Both images have zero full Q and zero endpoint components. These maps form the entire H0 above; the matrix of their normal-form homology coordinates has determinant +1.

Their primary images form the entire beta-torsion subgroup of H2(K). A second integer coordinate matrix has determinant +1. Therefore

\[
H^0\operatorname{RHom}(S_\beta,\mathcal F)_{(0)}
\longrightarrow H_2(\mathcal K)_{(0)}[\beta]
\]

is an isomorphism.

Thus all twelve directions alter the primary class. They are not twelve competing trivializations of one fixed primary.

## 6. Fix the primary homotopy-coherently

Let P=R[2] be the actual bottom subcomplex of S_beta. Define the primary-fixed deformation complex by the homotopy fibre

\[
\mathcal T=\operatorname{fib}\left(
\operatorname{RHom}(S_\beta,\mathcal F)
\longrightarrow\operatorname{RHom}(P,\mathcal F)
\right).
\]

This definition retains a specified comparison homotopy on the primary, rather than requiring equality of its chosen chain representative.

The termwise-split source inclusion has quotient S_beta/P=R[3]. Consequently,

\[
\mathcal T\simeq\operatorname{RHom}(R[3],\mathcal K).
\]

In occurrence weight zero,

\[
\pi_n\operatorname{Map}(R[3],\mathcal K)=H_{3+n}(\mathcal K)_{(0)}=0
\qquad(n\geq0).
\]

The zero map supplies a point. Hence this deformation space is contractible. Every nonempty fibre over another fixed primary has the same homotopy type by translation.

This statement does not promise existence for every primary. The class -beta chi fails the necessary beta-annihilation equation and gives an empty fibre, as shown above.

At beta zero, new top cycles can appear after nonflat specialization; the family computation is not a substitution of generic homology into that fibre. The result concerns actual polynomial families over Lambda. It does not extend a geometric purity theorem to beta zero.

## 7. Reproduction and remaining physical comparison

Run

```sh
python branch_a_coherent_endpoint_q_primary_frame_checker.py \
  --output branch_a_coherent_endpoint_q_primary_frame_certificate.json
```

The standalone checker performs 70,670 exact checks. It includes full polynomial differential and fibre identities, four independent normal-form computations, literal polynomial verification of the basis changes, the free transgression detector, and the two unimodular twelve-class coordinate matrices.

Certificate SHA-256:

```text
f1d1c28ce850fd87fcdd90804bf2a65d772fb35d093cd6e92c35ca409c523faf
```

The source-defined regulator coefficient problem is now determined for the stated frame and occurrence component. The physical conductor-to-Morse transport is still not supplied by these calculations. Its comparison must state the boundary functor and the primary it fixes; matching scalar residues cannot replace those maps. Additional lower-normal or geometric comparison cells could define a different framed deformation problem and must be included explicitly before making a claim about the physical Delta_J.

## Mathematical references

- Stacks Project, Hom complexes, tag 0A8H: https://stacks.math.columbia.edu/tag/0A8H
- Stacks Project, Cones and termwise split sequences, tag 014D: https://stacks.math.columbia.edu/tag/014D
- Stacks Project, the connecting homomorphism for a short exact sequence of complexes, tag 0117: https://stacks.math.columbia.edu/tag/0117

- Stacks Project, bounded projective complexes compute derived morphisms, tag 064B: https://stacks.math.columbia.edu/tag/064B
- Kerodon, mapping spaces from differential graded Hom complexes, tag 00SC: https://kerodon.net/tag/00SC
