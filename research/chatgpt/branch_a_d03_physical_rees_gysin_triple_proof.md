# Branch A: physical D03 Rees/Cartier specialization of the complete filling triple

Date: 2026-09-07.

## Verdict

The source's fixed-nonzero-beta formal comparison for the long normal 03 makes the recorded filling cycle Omega an explicit boundary. This holds before localizing any occurrence, Rees, or other monodromy parameter.

The complete transported data have the normal form

\[
dS=\Omega',\qquad
W'_u=\lambda X_{03}S,\qquad
W'_\mu=\mu S+Z,\qquad
\Theta'=\lambda X_{03}Z,\qquad dZ=0.
\]

Here lambda is the source-supplied invertible physical normal factor. The prime denotes transport of the original recorded chains, including all lower terms. It is not substitution into their homology modules.

The ordinary supported Koszul-Hom class of `(Omega',W'_u)` vanishes. The corresponding compatibility class also vanishes. Their retained first-normal comparison symbol is different: the first symbol of Theta is `[u03] tensor Z_D`, where `Z_D` is primitive and nonzero on `X03=0`. This first-symbol readout does not factor through the ordinary supported-Hom cohomology just shown to vanish.

The two endpoint terms of Z and all four Q components are explicit below. No endpoint correction is discarded. No identification with the physical conductor--Morse Delta_J is asserted.

## 1. The physical base change is supplied by the source

The immutable input is Marici commit
`d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`.

Entry 106 and `check_d03_formal_support_purity.rs` prescribe the long-normal comparison in characteristic-zero completion, at fixed invertible beta:

\[
u_{03}=e^{\beta X_{03}}-1=\lambda X_{03},
\qquad
\lambda=\beta\sum_{n\ge0}\frac{(\beta X_{03})^n}{(n+1)!},
\qquad \lambda(0)=\beta\ne0.
\]

This is an exact formal-series identity. The series after beta has constant term one, so it is a unit. The proof does not infer the identity from a finite Taylor check.

We apply this **local D03 graph** while retaining the other Rees variables and the two other long normals independently. We do not set the six Rees parameters to zero, identify them with scalar units, or apply an unprovided global physical kinematic quotient.

A convenient algebraic model before evaluation of lambda is

\[
B'=\mathbb Z[\lambda^{\pm1},X_d,t_s,u_{14},u_{25}]/
(X_eX_o:e\in S_-,o\in S_+),
\]

with

\[
S_-=(02,04,24),\qquad S_+=(13,15,35).
\]

Its map to the physical completed coefficient ring sends lambda to the displayed series. The original 430-state complex is termwise free, so its termwise base change computes its derived tensor product, including the comparison chains. No flatness of this coefficient specialization is asserted or needed for that computation.

In particular, the previous normal-subring annihilator is not simply pulled back as a homology presentation. New chain primitives can appear under this base change; one is constructed below.

## 2. Exact normal-frame isomorphism and support preservation

The state set is unchanged:

\[
[F,H,\epsilon],\qquad H\subseteq F,\qquad \epsilon\in\{0,1\},
\]

of homological degree `3-|F|+|H|+epsilon`. The final bit remains the separate occurrence factor with boundary `X35`. It is not combined with the native 35-circle.

After the graph pullback the 03-circle boundary is `lambda*X03`. Use the source's supported Koszul unit change of frame

\[
\mathsf U[F,H,\epsilon]
=\lambda^{\mathbf1_{03\in H}}[F,H,\epsilon]_X.
\]

The target has the same radial boundary, the same other normal boundaries, and the normalized 03 boundary

\[
dh_{03}^X=X_{03}p_{03}.
\]

All other short normals still satisfy `u_s=t_s*X_s`, and `u14,u25` remain independent. The 03 unit is not globally replaced by a scalar: its power is explicitly retained in the transport of every chain.

For a source coefficient monomial, its power of lambda after transport is its old `u03` exponent plus the number of marked 03 normals in the basis state. The code checks the full chain equation on all 430 basis columns. This includes every radial/normal mixed square and the separate occurrence differential.

Because this change is diagonal in the face and mark labels, it preserves both endpoint packets, the complete short boundary, and the full fourteen-state Q quotient. The checker verifies the endpoint connecting block as well as inclusions and quotients. These are the genuine support objects, not the rejected isolated three-edge projection.

The ordered normal line is retained. On the Cartier divisor,

\[
[u_{03}]=\beta[X_{03}],\qquad
[u_{03}]^\vee=\beta^{-1}[X_{03}]^\vee.
\]

Thus changing from the u-normal to the X-normal without transporting the dual line would introduce an erroneous beta factor. The source's logarithmic convention equivalently has `dlog(u03)=dlog(X03)+dlog(lambda)`, with the last term regular.

## 3. Recover and transport the actual input chains

The checker independently rebuilds the old 430-state model and the four relevant homogeneous contractions. Its resulting Omega, W_u, W_mu, and Theta are compared bytewise through canonical hashes with the four chains in the preceding certificate. It does not rerun the unrelated 512-pattern census.

Let

\[
w=t_{02}t_{04}t_{13},\qquad
\mu=t_{15}t_{24}u_{14}u_{25},\qquad
A=t_{02}t_{04}t_{13}t_{15}t_{24}.
\]

The input identities are

\[
d\Omega=0,\qquad dW_u=u_{03}\Omega,\qquad
dW_\mu=\mu\Omega,\qquad
\Theta=u_{03}W_\mu-\mu W_u.
\]

The transported lambda powers are respectively `0,1,0,1`. Every coefficient of the lambda-stripped W_u is divisible by X03. Factoring this **already divisible chain** produces a fifteen-term polynomial chain S, with no new inverse:

\[
\mathsf U\phi(W_u)=\lambda X_{03}S.
\]

The differential checks directly that `dS=Omega'`. Thus this assertion does not depend only on cancelling X03 from an equation. The underlying freeness also makes that cancellation legitimate because X03 is a nonzero divisor in the chosen normalization ring.

### Complete fifteen-term primitive S

| Face | Normal marks | Separate occurrence partner | Coefficient |
|---|---|---:|---|
| `02` | `02` | 0 | `t04*t13` |
| `03` | `03` | 0 | `t02*t04*t13` |
| `04` | `04` | 0 | `t02*t13` |
| `13` | `13` | 0 | `t02*t04` |
| `35` | `` | 1 | `t02*t04*t13` |
| `02,03` | `02,03` | 0 | `t04*t13` |
| `02,35` | `02` | 1 | `t04*t13` |
| `03,04` | `03,04` | 0 | `t02*t13` |
| `03,13` | `03,13` | 0 | `t02*t04` |
| `03,35` | `03` | 1 | `t02*t04*t13` |
| `04,13` | `04,13` | 0 | `t02` |
| `02,03,04` | `02,03,04` | 0 | `-t13` |
| `02,03,35` | `02,03` | 1 | `-t04*t13` |
| `03,04,13` | `03,04,13` | 0 | `-t02` |
| `03,13,35` | `03,13` | 1 | `-t02*t04` |

Every term has degree three. None is an endpoint state. Its Q component is

\[
\pi_QS=w h_{03}^X.
\]

The transformed comparison gives

\[
Z=W'_\mu-\mu S,
\qquad dZ=0,
\qquad \Theta'=\lambda X_{03}Z.
\]

Z has 45 terms, all exported. The equality is verified on the full polynomial chains, not only on Q or on homology.

## 4. The actual supported Gysin complex and its values

Put `x=X03` and express the supported construction in the normalized x-normal frame. In a homological cone convention, the complete complex representing `RHom(K(x),C')` has

\[
\mathscr H_n=C'_n\oplus C'_{n+1},
\qquad
D(a,b)=(da,xa-db).
\]

This is the standard Hom complex after multiplying its second component in degree n by `(-1)^n`. Its counit and purity map are

\[
\epsilon(a,b)=a,\qquad
\operatorname{pur}(a,b)=b\bmod x
\quad\text{in }C'_D[-1]\otimes N_{D/B'}.
\]

The normal dual is represented by the fixed normal basis; it is not discarded. The shifted target differential is `-d`, as required by the displayed map. The checker constructs all 860 basis states and verifies the differential, counit, and purity equations on every column. Since x is a regular parameter and C' is bounded free, this is the usual Cartier supported-duality model.

For the original supported filling pair, after the necessary source normal-frame change, the cycle is

\[
(\Omega',xS)=D(S,0).
\]

It is exact in this ordinary supported Hom model. Its purity image is literally zero.

The compatibility comparison is also computed, not inferred:

\[
(0,xZ)
=D(W'_\mu,0)-\mu(\Omega',xS)
=D(Z,0).
\]

It too is exact in the ordinary supported Hom model and has zero purity image.

These statements do not prove that a category fixing additional comparison cochains regards the same homotopies as admissible. They do establish the values of the explicit ordinary supported Gysin calculation. In particular, a nonzero class cannot be obtained here by multiplying separately normalized unit residues.

## 5. The retained first-normal symbol is not the ordinary purity image

There is a second, differently typed map:

\[
(I_x/I_x^2)^\vee\otimes\operatorname{gr}_{I_x}^1 C'
\longrightarrow C'_D,
\qquad
[x]^\vee\otimes[xa]\longmapsto\bar a.
\]

This is the coefficient-level first-symbol evaluation. The checker verifies it is a chain map on every generator of `xC'`. Before evaluating the normal line, its outputs are

\[
\operatorname{gr}_{u_{03}}^1 W'_u=[u_{03}]\otimes S_D,
\qquad
\operatorname{gr}_{u_{03}}^1\Theta'=[u_{03}]\otimes Z_D.
\]

The equations retained on the divisor are

\[
dS_D=\Omega_D,\qquad dZ_D=0,
\qquad W'_{\mu,D}=\mu S_D+Z_D.
\]

This map reads the first symbol of the **recorded comparison chains**. It does not descend to a map sending the ordinary supported-Hom class of `(0,xZ)` to `[Z_D]`: that class is a boundary by Section 4. Forgetting the primitive Z and then claiming a nonzero ordinary Gysin image would therefore be incorrect.

The distinction is operational: the coefficient specialization of W_u and Theta at x=0 is zero, whereas their first symbols can be read only with the normal line retained. No scalar division on an arbitrary chain is used.

## 6. The primary cycle is also trivial with endpoint/Q-zero primitive on the divisor

After restricting to x=0, Omega lies entirely in the short-boundary subcomplex. The complete homogeneous short-boundary calculation produces this six-term chain L:

| Face | Normal marks | Separate occurrence partner | Coefficient |
|---|---|---:|---|
| `02` | `02` | 0 | `t04*t13` |
| `04` | `04` | 0 | `t02*t13` |
| `13` | `13` | 0 | `t02*t04` |
| `35` | `` | 1 | `t02*t04*t13` |
| `02,35` | `02` | 1 | `t04*t13` |
| `04,13` | `04,13` | 0 | `t02` |

It satisfies

\[
dL=\Omega_D,\qquad
\pi_QL=0,\qquad
\operatorname{pr}_{V_+}L=\operatorname{pr}_{V_-}L=0.
\]

The endpoint connecting components are zero as well, because both the primitive and its boundary have zero endpoint terms. Every Rees and occurrence weight is preserved. Thus this particular primary class has a primitive in the natural target-side endpoint/Q-relative complex, not merely in the full ordinary complex.

The two primitives `S_D` and L differ by a closed degree-three chain with Q component `w*h03^X`. That difference is primitive in its homogeneous component. L is supplied by the explicit short-boundary contraction; it has not been independently identified with a physical conductor homotopy.

## 7. The surviving first symbol retains the full Q cycle and both endpoints

The Q projection of Z, before or after x=0, is

\[
\pi_QZ=A\left[
 u_{14}u_{25}(T-h_{03}^X)
 -X_{14}u_{25}h_{14}
 -X_{25}u_{14}h_{25}
\right].
\]

All four components are retained. They satisfy the Q differential exactly. The remaining 41 terms have short support and their boundary cancels the full lower attachment of these four Q terms.

The endpoint terms are

\[
Z_{V_-}=t_{13}t_{15}u_{14}u_{25}
 [\{02,04,24\},\{02,04,24\},0],
\]

\[
Z_{V_+}=t_{02}t_{04}t_{24}u_{14}u_{25}
 [\{13,15,35\},\{13,15\},1].
\]

They have the positive signs inherited from the original matrices. The last bit in the positive term is the separate occurrence circle; it is not replaced by the native 35-circle.

Let `Z_E` be its endpoint-quotient part and `Z_V` these two terms. With the actual connecting map kappa obtained from the endpoint block of the differential,

\[
\kappa(Z_E)=-d_VZ_V.
\]

Both sides have six terms, three from each endpoint packet. Removing Z_V therefore makes the alleged cycle fail its differential equation. The certificate exports the six connector columns and all lower corrections.

In the original normal/Rees weight of `w*mu`, after the D03 graph but before the Cartier quotient, the relevant degree-three homology has rank one. After x=0 it has rank two. In the integer bases from the exact reductions, the Z_D coordinates are `(1,1)`, hence primitive.

A simpler nonvanishing detector is the coefficient of the prescribed monomial `w*mu` on the top basis state T. It evaluates Z_D to one. No degree-four state exists in this homogeneous component, so no homogeneous boundary can alter it. A nonhomogeneous formal primitive would have to contain such a component and is ruled out by the same argument. Extension to the stipulated characteristic-zero physical coefficients preserves this conclusion.

The rank-two Cartier result is not a claim that the source selects a unique physical line among all possible degree-three classes.

## 8. Which statements are fixed by the input triple

The original W_mu is retained. The source's pre-specialization calculation had no degree-three ambiguity at its weight. After the D03 graph, a new closed chain Z appears at that weight. Replacing the specialized W_mu by `W_mu-Z=mu*S` would preserve its boundary but erase the compatibility cycle.

This is not the prescribed source triple. It explains why the fixed comparison's first symbol is meaningful as retained data but is not an invariant of the two annihilator equations alone. A stronger physical framing must determine which changes of comparison chains it admits; the present calculation does not manufacture that selection.

The local physical test therefore gives:

- an explicit primary nullhomotopy after the source-defined graph;
- zero classes in the explicit ordinary supported Koszul-Hom Gysin model;
- an independently typed, nonzero first normal symbol of the fixed compatibility;
- all lower short-boundary terms and both nonzero endpoint corrections;
- no scalar unit Q-map, global mixed-variance realization, or physical Delta_J identification.

It does not replace the graph by the different Rees special fibre `t_i=0`. It does not identify the 430-state original-normal complex with the distinct 245-state native-exceptional model. It does not impose a D3 action on the fixed occurrence factor without transporting that factor through the family.

## 9. Reproduction

Run:

```sh
python branch_a_d03_physical_rees_gysin_triple_checker.py \
  --output branch_a_d03_physical_rees_gysin_triple_certificate.json
```

Only the Python standard library is required. No network access or other local checker is required. The script reconstructs the original four witnesses, verifies their recorded hashes, and independently constructs the graph, supported-Hom, first-symbol, and endpoint/Q comparisons.

An isolated `python -I` replay reproduced the certificate byte-for-byte. The run verifies 35,047 exact identities. Its certificate includes the old four witness hashes, every normalized target differential column, the whole transported chains, the fifteen- and six-term primitives, the forty-five-term comparison symbol, endpoint connector terms, all relevant homogeneous cancellation logs, and explicit scope flags.

The certificate's content SHA-256, excluding its own hash field, is:

```text
66b068b29d4151fd4a1ff0bc57073c0166959cb3fd663084f064da8b2810aab9
```

## Sources

Immutable project inputs at the commit stated above:

1. `research/voevodsky/check_d03_formal_support_purity.rs`, especially its initial physical-graph/unit-conjugacy specification.
2. `src/ledger/20260814-106 Marked Log Gallery Secondary Class and the Global Yoneda Gap.md`, section “Physical normal evaluation”. It gives the local fixed-beta scope and expressly leaves the global pull-push identification separate.
3. `research/voevodsky/check_absolute_unlocalized_support_pc.rs`, for the finite signed radial/normal differential.
4. `src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md`, for the two-sheet coefficient ring.
5. `branch_a_d03_rees_filling_and_resonance_proof.md` and its certificate, for the recorded input triple and its auxiliary W_mu. The new checker reconstructs their required chain representatives rather than executing that prior file.

Conventions and general theorems:

- Stacks Project, Koszul functoriality and invertible change of generators, https://stacks.math.columbia.edu/tag/0621.
- Stacks Project, bounded above flat complexes are K-flat, https://stacks.math.columbia.edu/tag/064K.
- Stacks Project, Hom complexes, https://stacks.math.columbia.edu/tag/0A8H.
- Stacks Project, Cartier supported duality and its normal line, https://stacks.math.columbia.edu/tag/0B4B.
- Stacks Project, homology connecting morphisms, https://stacks.math.columbia.edu/tag/0117.

The formal power-series unit argument and every new polynomial chain identity are proved in this note and checked as described; the references do not supply an uncomputed physical selector.
