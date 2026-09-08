# Branch A: D03 Rees filling classes and their resonance compatibility obstruction

Date: 2026-09-07.

## Result and scope

The previous uniqueness of the corrected Morse filling holds in its fine-weight-zero component. It does not extend to all nonnegative normal/Rees degrees of the same unlocalized coefficient complex.

The new calculation constructs an integral degree-two cycle `Omega03`, of normal weight `t02*t04*t13`, with zero coefficients on both complete endpoint packets. Its image in the full short-boundary quotient is exactly `t02*t04*t13*X03*p03`. The class is primitive and nonzero. Consequently it gives a genuine change of a based filling that leaves its full boundary unchanged, and its quotient class has zero short-boundary connecting class.

Over the nine-variable normal/Rees polynomial subring its exact annihilator is

\[
(u_{03},\ t_{15}t_{24}u_{14}u_{25}).
\]

Explicit chains kill these two multiples. Their compatibility is a primitive nonzero degree-three cycle, not a removable higher boundary. Thus the cycle cannot be replaced by its isolated annihilator quotient module through a homogeneous Koszul lift with the same bottom class.

All statements concern the corrected **430-state finite cellular coefficient complex** and its actual endpoint/short-boundary/14-state-Q support diagram. This is the target of the preceding 2338-state pulled-back-normal support equivalence. It is not the different 245-state native-exceptional-normal complex. No physical conductor homotopy, physical `Delta_J`, global extraordinary comparison, or identification with the earlier supported `tau` is asserted.

## Cross-branch inputs and retrieval boundary

The recovered Branch B report `equivariant_physical_lift.md` is dated September 6. It distinguishes the order-six obstruction to a strict invariant unit from the contractible space of homotopy-coherent normalized states in its endpoint coefficient model. It retains the node, tags, and top relation; it does not claim the complete support-PC/generic-Q comparison. The preceding `source_defined_branch_comparison.md` retains branch polynomials in the source and removes their tails only through explicit node boundaries.

The latest Branch C nonlinear artifact recoverable in this review was the September 5 `term2_nonlinear_source.md`. It distinguishes the valid raw connected-component multinerve from a normalization-component diagram that lacks face maps, and distinguishes an ordinary homotopy retract from an equivariant, stratum-preserving one. Newer September 6–7 Branch C chat turns were not recovered; this report does not claim a complete synchronization with them.

These results justify testing the **whole graded coefficient complex**, rather than extrapolating a single homogeneous contraction or equating a linear homology calculation with a nonlinear realization. Neither cross-branch result is used as an assumed physical identification.

## 1. Ring, actual support, and differential

Write

\[
\mathscr D=(02,03,04,13,14,15,24,25,35),
\quad S_+=(13,15,35),\quad S_-=(02,04,24),
\]
\[
S=S_+\cup S_-,\qquad L=(03,14,25).
\]

Let

\[
\mathcal A=\mathbb Z[t_s\ (s\in S),u_l\ (l\in L)],
\qquad
B=\mathcal A[X_d\ (d\in\mathscr D)]/
(X_eX_o:e\in S_-,o\in S_+).
\]

In words: all Rees parameters and all three long normals remain independent. Only opposite-sheet short occurrence products vanish. For a short diagonal use the supplied graph `u_s=t_s*X_s`; long normals remain `u_l`.

A corrected cellular state is

\[
[F,H,\epsilon],\qquad H\subseteq F,\quad\epsilon\in\{0,1\},
\]

where `F` is a noncrossing hexagon face. Its homological degree is

\[
|[F,H,\epsilon]|=3-|F|+|H|+\epsilon.
\]

The final bit records the **separate occurrence** Koszul factor with `d h_occ=X35 p_occ`. It is not the native `35`-normal circle.

The differential is

\[
\begin{aligned}
d[F,H,\epsilon]
={}&\sum_{a\in\operatorname{Add}(F)}
 (-1)^{\#\{b\in F:b<a\}}X_a[F+a,H,\epsilon]\\
&+\sum_{h\in H}(-1)^{3-|F|+\operatorname{pos}_H(h)}
 u_h[F,H-h,\epsilon]\\
&+\epsilon(-1)^{3-|F|+|H|}X_{35}[F,H,0].
\end{aligned}
\]

Here the conditions on the first sum mean that adding `a` gives a noncrossing face of size at most three. The checker implements these conditions combinatorially and verifies the complete polynomial square-zero identity on all 430 states.

The support diagram is

\[
\widehat V\subset\widehat B\subset\widehat C,
\qquad
\widehat Q=\widehat C/\widehat B.
\]

The endpoint summands have `F=S_+` or `F=S_-`. The short-boundary summands have `F` containing at least one short diagonal. Their ranks are

\[
32\subset416\subset430,\qquad |\widehat Q|=14.
\]

These are actual differential-stable submodules. In particular, the quotient is not the rejected three-edge projection. The 430 basis states and all differential columns match the preceding support-equivalence certificate after the declared short-normal graph substitution; that equality was independently checked during this calculation.

## 2. Infinite weight range reduces to 512 cases

Every one of the eighteen variables has its own fine degree. The weight of a state is

\[
\operatorname{wt}[F,H,\epsilon]
=-\sum_{d\in F}e_{X_d}
+\sum_{h\in H}\operatorname{wt}(u_h)
+\epsilon e_{X35}.
\]

Consider all weights whose nine occurrence coordinates are zero and whose nine coordinates in

`(t02,t04,t13,t15,t24,t35,u03,u14,u25)`

are nonnegative integers. A state contributes to a homogeneous component if its uniquely required coefficient exponent vector `w-wt(state)` is nonnegative and its occurrence monomial survives the opposite-sheet ideal. Its contribution is a free rank-one abelian group generated by that coefficient monomial times the state.

Each state has weight zero or one in every normal/Rees coordinate. Therefore eligibility depends on whether each of those coordinates of `w` is zero or positive, not on the size of a positive integer. Multiplication by a normal variable is an isomorphism **between the two homogeneous components** when that coordinate is already positive: both have identical state sets and integer differential matrices, and their chosen monomials differ by that variable. This does not invert the variable in the coefficient ring.

It follows that all nonnegative normal weights in this occurrence slice are covered by the `2^9=512` zero/positive patterns. This is an all-exponent proof, not a numerical test at a degree cutoff. The checker additionally verifies the implemented identity of every pattern with a representative having larger positive exponents.

For each pattern and each of the four support objects, an integral unit cancellation produces maps

\[
pi=1,\qquad di=0,\qquad pd=0,\qquad dH+Hd=1-ip.
\]

The residual differential is zero in every case. Thus every reported homology group is free over the integers. The certificate contains all cancellation sequences and residual bases; the checker constructs and verifies every displayed projection, inclusion, and homotopy identity. No rank inference from a list of primes is used.

## 3. Complete weight census

The following counts are counts of degree-support patterns, not ranks of a global polynomial module.

| Property | Number of patterns |
|---|---:|
| `H2(full)` is nonzero | 320 |
| `H3(full)` is nonzero | 9 |
| `H3(Q)` is nonzero | 64 |
| `ker(H2(Q) -> H1(short))` is nonzero | 58 |

Every short-boundary attachment image in this census is saturated. The attachment matrix is computed by lifting each actual quotient cycle, applying the full differential, and projecting into the computed short-boundary homology. The gcd of its maximal-rank minors is one; its rank is at most two.

Examples are:

| Positive weight coordinates | `H2(full)` | `H3(full)` | `H2(Q)` | Attachment kernel |
|---|---|---|---|---|
| none | 0 | 0 | Z^2 | 0 |
| `t02,t04,t13` | Z | 0 | Z^2 | Z |
| `t04,t35,u03` | 0 | 0 | Z | 0 |
| `u03,u25` | Z | 0 | 0 | 0 |
| all nine | Z^3 | Z^2 | 0 | 0 |

The last two examples illustrate why full filling variations and quotient filling variations must not be identified. A nonzero full cycle can lie entirely in short support; conversely, higher Q comparisons can have nontrivial lower attachment.

At zero weight the calculation reproduces the previous result:

\[
H_2(\widehat C)_{0}=0,
\qquad
H_2(\widehat Q)_{0}=\mathbb Z^2,
\qquad
\ker\partial_0=0.
\]

The previous proposed `t04*t35*u03` weight also has no full degree-two class. The new class below is not an identification or revival of the old `tau` candidate.

## 4. A primitive endpoint-zero D03 variation

Set

\[
w=t_{02}t_{04}t_{13},\qquad \omega=\deg w.
\]

In this weight the full chain ranks in homological degrees zero through three are `(8,38,37,9)`. The computed homology is

\[
H_1(\widehat C)_\omega=\mathbb Z^3,
\qquad H_2(\widehat C)_\omega=\mathbb Z,
\]
\[
H_1(\widehat B)_\omega=\mathbb Z^4,
\qquad H_2(\widehat Q)_\omega=\mathbb Z^2.
\]

In the computed quotient and short-boundary bases, the connecting matrix is

\[
\partial_\omega=
\begin{pmatrix}1&-1\\0&0\\0&0\\1&-1\end{pmatrix}.
\]

Its kernel is primitive of rank one. After orientation is fixed by the positive `03` quotient component, the constructed full cycle satisfies

\[
d\Omega_{03}=0,\qquad
\operatorname{pr}_{V_+}\Omega_{03}=
\operatorname{pr}_{V_-}\Omega_{03}=0,
\qquad
\pi_Q\Omega_{03}=wX_{03}p_{03}.
\]

Here `p03=[{03},empty,0]` is the long-facet base state in homological degree two. No occurrence factor is removed. Positivity is a choice of integral orientation of this computed class, not a claim that it is a physical residue unit.

The cycle has the following 21 terms. A final-bit value of one means tensoring with `h_occ35`.

| Face F | Marks H | Occurrence partner | Coefficient |
|---|---|---:|---|
| `02` | `` | 0 | `X02*t02*t04*t13` |
| `03` | `` | 0 | `X03*t02*t04*t13` |
| `04` | `` | 0 | `X04*t02*t04*t13` |
| `13` | `` | 0 | `X13*t02*t04*t13` |
| `35` | `` | 0 | `X35*t02*t04*t13` |
| `02,04` | `02` | 0 | `-X04*t04*t13` |
| `02,04` | `04` | 0 | `X02*t02*t13` |
| `02,24` | `02` | 0 | `-X24*t04*t13` |
| `02,25` | `02` | 0 | `-X25*t04*t13` |
| `04,14` | `04` | 0 | `-X14*t02*t13` |
| `04,24` | `04` | 0 | `-X24*t02*t13` |
| `13,14` | `13` | 0 | `-X14*t02*t04` |
| `13,15` | `13` | 0 | `-X15*t02*t04` |
| `13,35` | `` | 1 | `X13*t02*t04*t13` |
| `13,35` | `13` | 0 | `-X35*t02*t04` |
| `15,35` | `` | 1 | `X15*t02*t04*t13` |
| `25,35` | `` | 1 | `X25*t02*t04*t13` |
| `02,03,04` | `02,04` | 0 | `X03*t13` |
| `02,25,35` | `02` | 1 | `-X25*t04*t13` |
| `03,13,35` | `13` | 1 | `-X03*t02*t04` |
| `04,13,14` | `04,13` | 0 | `X14*t02` |

A derivation of this representative is included in the checker. Start with the degree-two residual inclusion from the unit contraction; remove its two endpoint components by two explicit degree-three unit boundaries; subtract the resulting cycle from the boundary of `w*T`. The result has the single specified Q component and no endpoint coefficients.

For a homogeneous chain `v`, write `c_g(v)` for its **integer coefficient in the uniquely prescribed weight-omega monomial basis**. The detector

\[
\begin{aligned}
\ell(v)={}&c_{[03,\varnothing,0]}(v)
-c_{[35,\varnothing,0]}(v)\\
&+c_{[13,35;\varnothing,1]}(v)
-c_{[13,15,35;13,1]}(v)
\end{aligned}
\]

satisfies

\[
\ell(dv)=0,\qquad \ell(\Omega_{03})=1.
\]

The checker tests the first equation on every degree-three boundary column. This proves integral primitiveness and nonvanishing. A nonhomogeneous polynomial primitive is impossible as well: its weight-omega component would contradict the same detector. The detector is a componentwise coefficient functional, not an occurrence-variable inverse or a claimed B-linear map to a scalar line.

Write `b03=Omega03-w*X03*p03`. Then

\[
b_{03}\in\widehat B_2,
\qquad
db_{03}=-d(wX_{03}p_{03}).
\]

Thus the lower attachment is coherently filled by an explicit 20-term short-boundary chain. It is not simply declared to vanish.

For the previously constructed cellular image

\[
\Gamma=X_{03}[03,35;\varnothing,0]
       +X_{13}[13,35;\varnothing,0],
\qquad
h_{\rm ref}=-w\,\Gamma h_{\rm occ},
\]

both `h_ref` and `h_ref+n*Omega03` have the same complete differential and the same zero endpoint components. Distinct integers `n` give nonhomotopic full homogeneous fillings. The Q classes differ by `n*w*X03*p03`, whose lower attachment class is zero.

This proves nonuniqueness for the stated based-filling/attachment problem in this normal weight. A stronger physical frame fixing the lower correction **pointwise**, or imposing additional mixed-variance operators, is a different problem. No such unprovided restrictions are assumed here.

## 5. Exact annihilator over the normal polynomial subring

The annihilator assertion is over `A=Z[t_s,u_l]`, acting on the full coefficient homology. It is not a classification of all annihilators involving occurrence variables, nor of a stronger physically framed homotopy group.

The exact result is

\[
\operatorname{Ann}_{\mathcal A}[\Omega_{03}]
=(u_{03},\mu),\qquad
\mu=t_{15}t_{24}u_{14}u_{25}.
\]

To prove completeness, multiply the actual cycle by every subset of the six normal coordinates absent from `w`. There are 64 cases. The computed homology image vanishes exactly when that subset contains `u03` or contains all four of `t15,t24,u14,u25`. The certificate records every homology image, not just the vanishing Boolean.

Any further power of an already positive coordinate acts by the homogeneous chain isomorphism proved in Section 2. Therefore these 64 cases classify every monomial multiplier. Distinct monomials have distinct fine degrees, so their images cannot cancel across degrees. Every component is integer-torsion-free, so an integer multiple adds no further annihilator. These facts prove the displayed ideal for every polynomial in `A`.

Equivalently the generated graded cyclic module is

\[
\mathcal A[\Omega_{03}]
\cong \mathcal A/(u_{03},\mu)\langle\omega\rangle,
\]

where the last notation records the generator's fine degree, not a chain shift. Its support in the normal-parameter spectrum is `V(u03,mu)`. Inverting `u03` kills it; inverting the product `mu` also kills it. No such inversion occurs in this construction.

The generic normal region therefore does not carry this class. It is supported at exceptional resonance and at least one of the four additional normal/Rees divisors. It is not a generic scalar Q unit.

## 6. The annihilating homotopies have a nonzero next comparison

The full polynomial matrices supply a 15-term chain `W_u` and a 30-term chain `W_mu` with

\[
dW_u=u_{03}\Omega_{03},\qquad
dW_\mu=\mu\Omega_{03}.
\]

Both are exported in the certificate. `W_u` has zero endpoint components. `W_mu` has two endpoint components; those are retained, not deleted or asserted physically admissible.

Since multiplication by `u03` is injective on every underlying free B-state, its short exact coefficient sequence has the connecting map

\[
\partial_{u_{03}}[\overline W_u]=[\Omega_{03}].
\]

In words: reduce the primitive modulo `u03`; its lift has boundary `u03*Omega03`; extract that known factor. This is the homological connecting map into the integral coefficient complex. It is not division of an arbitrary coefficient, and `u03` is not an integer prime.

Retain the compatibility between these two annihilations:

\[
\Theta_{03}=u_{03}W_\mu-\mu W_u,
\qquad d\Theta_{03}=0.
\]

Its normal weight is

\[
\omega'=\deg(t_{02}t_{04}t_{13}t_{15}t_{24}u_{03}u_{14}u_{25}).
\]

In this component

\[
H_3(\widehat C)_{\omega'}=\mathbb Z,
\qquad [\Theta_{03}]=1
\]

in the exported oriented basis. The cycle has 45 terms. There are no degree-four states in this weight, so its nonzero closed chain cannot be a boundary.

The relevant ambiguity groups are zero:

\[
H_3(\widehat C)_{\omega+\deg u_{03}}=0,
\qquad
H_3(\widehat C)_{\omega+\deg\mu}=0.
\]

Hence replacing either annihilating primitive does not remove the displayed class; the usual possible changes `u03` times a cycle in the second weight and `mu` times a cycle in the first are boundaries. Changing the representative of `Omega03` by a boundary and changing both primitives compatibly also leaves the class unchanged.

Its Q component is

\[
\pi_Q\Theta_{03}
=t_{02}t_{04}t_{13}t_{15}t_{24}\,\theta_Q,
\]

where

\[
\theta_Q=u_{03}u_{14}u_{25}T
-X_{03}u_{14}u_{25}h_{03}
-X_{14}u_{03}u_{25}h_{14}
-X_{25}u_{03}u_{14}h_{25}.
\]

In words: the new compatibility reaches the **complete** top/three-normal Q cycle, not the false isolated degree-one edge. The polynomial prefactor and the two endpoint terms are retained.

An attempted homogeneous map from the isolated quotient's Koszul resolution would have to send its bottom generator to `Omega03`, its two first generators to annihilating primitives, and its top generator to a degree-four chain with boundary `Theta03`. That last chain does not exist. Thus replacing the whole construction by the isolated module `A/(u03,mu)` loses essential comparison data. This is a source-resolved failure at the next homotopy degree, not a reason to alter a differential to force a filler.

## 7. Relation to Branch B, Branch C, and the physical target

All 512 integer homology calculations are torsion-free. Therefore no integer-prime Bockstein is produced merely by these coefficient slices. This does not rule out equivariant torsion: Branch B's strict order-six obstruction belongs to a different equivariant lifting problem. Nor does it remove Branch C's nonlinear sphere torsion: these additive chain models do not compute that nonlinear homotopy type.

The new supported class and its primitive secondary compatibility are derived from the full signed native-normal states already in the finite cellular coefficient model. No new formal cells have been adjoined to force either result.

The original weight-zero Morse filling remains unique under its computed attachment condition. The present result falsifies only the extension of that claim to all normal/Rees weights. In particular:

- `Omega03` has degree two and nonzero Rees weight; it is not the physical `H_cond-e_F*h_Morse` by definition.
- `Theta03` is the comparison between two independently computed parameter-annihilating primitives in this same complex; it is not yet the independently selected physical conductor–Morse comparison.
- The old `t04*t35*u03` homogeneous component remains rigid in degree two. No equality with the previous supported `tau` is asserted.
- No D3 action on the fixed `K_occ(X35)` source is invented. A physical rotation changes the distinguished occurrence factor and requires a family comparison.
- The endpoint-zero statement concerns `Omega03` and `W_u`; the nonzero endpoint terms of `W_mu` and `Theta03` must be included in any subsequent physical-frame test.
- The native 245-state exceptional model, derived-localization variants, and inhomogeneous monodromy-unit localizations are outside this particular computation.

The next physical comparison has explicit input: determine the source-defined image or admissibility of the triple `(Omega03,W_u,Theta03)` with its known normal support, exact lower corrections, and endpoint terms. A generic localization that inverts `mu` necessarily kills `Omega03`; a unit residue argument cannot undo that fact without a separately typed supported functor.

## 8. Reproduction and provenance

Run:

```sh
python branch_a_d03_rees_filling_and_resonance_checker.py \
  --output branch_a_d03_rees_filling_and_resonance_certificate.json
```

The checker has no external Python dependencies. It reconstructs every face, marked state, coefficient differential, fine-degree slice, and support quotient. It verifies all 512 integral contractions and attachment matrices and the full polynomial identities for `Omega03`, `W_u`, `W_mu`, and `Theta03`. The certificate includes all 512 pivot sequences, homology bases and attachment matrices, the 64 annihilator images, and the four explicit polynomial chains.

An isolated rerun with `python -I` reproduced the certificate byte-for-byte. The certificate contains 826,810 exact checks. The check count does not replace the all-exponent, annihilator, and support arguments given above.

Certificate content SHA-256 (the hash excludes its own hash field):

```text
c3d401f7dd1a66335806314893f89d6df865c9da282db697a9b3a6fe844310c7
```

Primary source rules were read at commit `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61` of `andrey-kokoev/marici`:

- `research/voevodsky/check_d03_pabs_morse_pullback.rs`: complete corrected Morse and separate occurrence factor.
- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`: finite signed normal/radial differential and target-only scope.
- `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`: the alternating-sheet monomial quotient.
- `src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md`: the complete endpoint/short-boundary/Q support diagram.

The preceding local artifacts used to compare models are `morse_pulledback_normal_support_equivalence_proof.md` and its certificate, and `morse_q_filling_torsor_and_attachment_proof.md` and its certificate. This new standalone checker does not depend on executing their code.

Mathematical conventions and facts:

- Stacks Project, Hom complexes, tag `0A8H`, `https://stacks.math.columbia.edu/tag/0A8H`: the graded differential and comparison of chain maps.
- Stacks Project, long exact sequence in homology, tag `0117`, `https://stacks.math.columbia.edu/tag/0117`: the support attachment and coefficient connecting map.
- Stacks Project, Koszul complex, tag `0621`, `https://stacks.math.columbia.edu/tag/0621`: the two-parameter compatibility equation.
- Stacks Project, Dold–Kan, tag `019D`, `https://stacks.math.columbia.edu/tag/019D`: the additive filling-space interpretation. It does not identify these spaces with Branch C's nonlinear geometric source.
