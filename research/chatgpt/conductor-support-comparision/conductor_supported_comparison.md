# Conductor-supported comparison of the polynomial boundary

Date: 2026-09-06  
Source repository: `andrey-kokoev/marici`  
Pinned commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

## Result and scope

The formal nodal coefficient model in our preceding boundary construction admits a canonical extraordinary conductor restriction. Its value is one orientation-odd line in cohomological degree one. Its adjunction counit has the normalization module as its mapping cone. These statements retain all polynomial coefficients and are natural under the existing coefficient localizations.

The integral cone has no prime torsion. The constant-coefficient reflection-equivariant extension nevertheless has exact order two. This recovers Marici's existing conductor Bockstein obstruction, rather than asserting a new physical obstruction.

This computes a conductor-supported comparison for the explicit split-node model. It does **not** identify that conductor immersion with Marici's complete endpoint-relative, support-PC, or proper Rees/DNC correspondence. In particular, a normalized supported line does not by itself prove that branch-polynomial information can be discarded from the physical packet.

## 1. Source operations and what they retain

The fetched normalization-conductor kernel is the difference of evaluations on two polynomial branches. Its source checker explicitly retains the entire node kernel after tensoring with the absolute unit and relative interval. The generic logarithmic Thom trace has coefficient one on the interval generator; it supplies no additional operator on the branch polynomials. [S1, S2]

The integration checker compares a finite signature of the distinguished primitive object. It does not serialize a chain map on arbitrary polynomial inputs from the conductor diagram to the four-term physical complex. Consequently that signature equality is not used here as proof of a full coefficient comparison. [S3]

For one of the existing coefficient rings let

\[
R=R_L,\qquad A=R[x,y]/(xy),\qquad
N=R[x]\oplus R[y].
\]

In words: keep the source's localized coefficient ring; the two branches of the node have coordinates x and y; N contains independent polynomials on the two normalization branches. Here x and y replace the earlier names z-plus and z-minus.

The conductor immersion and source complex are

\[
i:\operatorname{Spec}R\hookrightarrow\operatorname{Spec}A,
\qquad R=A/(x,y),\qquad
Q=[N\xrightarrow{\delta}R_{\mathrm{or}}],
\quad \delta(f,g)=f(0)-g(0).
\]

In words: the conductor is the closed locus where both branch coordinates vanish. Q is placed in degrees zero and one. Sheet exchange swaps the two summands of N and negates its conductor quotient; the subscript records that orientation character.

There is an exact sequence

\[
0\longrightarrow A\xrightarrow{\nu}N
\xrightarrow{\delta}R_{\mathrm{or}}\longrightarrow0.
\]

In words: node functions are precisely pairs of branch functions with equal conductor values. Therefore the inclusion of A into Q is an equivariant quasi-isomorphism. No positive branch coefficient is killed by this quasi-isomorphism. [S1]

## 2. Compute the extraordinary restriction

For a closed immersion, the right adjoint of pushforward is derived Hom from its quotient algebra. [M1] Thus

\[
i^!Q\simeq\operatorname{RHom}_A(R,A).
\]

In words: calculate the conductor-supported coefficient object by resolving the conductor module over the node ring. This is a different operation from extracting a constant coefficient.

An explicit free resolution of R starts with

\[
\cdots\longrightarrow A^2
\xrightarrow{\operatorname{diag}(x,y)}A^2
\xrightarrow{\operatorname{diag}(y,x)}A^2
\xrightarrow{(x\;y)}A\longrightarrow R\longrightarrow0.
\]

In words: after the first map, the two diagonal maps alternate indefinitely. Their exactness follows from the two annihilator identities

\[
\operatorname{Ann}_A(x)=(y),\qquad
\operatorname{Ann}_A(y)=(x).
\]

In words: a node polynomial killed by one branch coordinate is supported on the other branch. These identities hold coefficientwise over every ring R used in the construction.

Applying Hom into A gives

\[
A\xrightarrow{(x,y)^T}A^2
\xrightarrow{\operatorname{diag}(y,x)}A^2
\xrightarrow{\operatorname{diag}(x,y)}A^2\longrightarrow\cdots.
\]

In words: this is the cochain complex computing the extraordinary restriction. Its degree-zero kernel is zero. All its cohomology above degree one vanishes by the displayed annihilator identities.

A degree-one cocycle has the form

\[
(xa(x),\;yb(y)),\qquad
\operatorname{res}(xa(x),yb(y))=a(0)-b(0).
\]

In words: divide each component by its branch coordinate and subtract the two resulting constant terms. A boundary has the form (xf,yf), so its residue is zero.

Conversely, if the residue is zero, a(x) and b(y) have equal constants and define one node polynomial f. The cocycle is then the boundary (xf,yf). The class of (x,0) has residue one. Hence

\[
\operatorname{Ext}^q_A(R,A)=
\begin{cases}
R_{\mathrm{or}},&q=1,\\
0,&q\ne1,
\end{cases}
\qquad i^!Q\simeq R_{\mathrm{or}}[-1].
\]

In words: the supported object has one primitive line, in degree one, and changes sign under sheet exchange. This includes the full infinite free resolution; it is not a conclusion extrapolated from a finite truncation.

The residue map above is A-linear **on cocycles modulo boundaries**, with A acting on R through the conductor quotient. Extending the coefficient formula to all arbitrary degree-one cochains would not give the required A-linear map. One rigorous model is the good truncation consisting of A in degree zero and the degree-one cocycles in degree one. Its quotient to the displayed Ext group and its inclusion in the full Hom complex are quasi-isomorphisms.

### Branch multiplication on the supported class

For the generator e represented by (x,0),

\[
x e=[(x^2,0)]=0,\qquad y e=0.
\]

In words: multiplication by either branch coordinate kills this Ext class. The first equality has the explicit boundary witness f=x; the second vanishes because xy is zero. These equations concern the supported class. They do not say that x or y was a boundary in the original node-function module A.

The residual coefficient dependence on R survives unchanged. Applying this supported functor changes the coefficient object. It does not assert a map that sends every earlier integer-linear marking of Q to a supported marking: applying the A-linear functor also requires a specified A-module source, and transforms that source as well. In particular, distinct earlier branch markings have not been declared homotopic.

## 3. The canonical comparison and its cone

The canonical adjunction map points from the supported object into the node object:

\[
\eta:i_*i^!Q\longrightarrow Q.
\]

In words: this is the counit for the conductor immersion. It is not a trace from arbitrary node polynomials to an integer.

Under the previous identifications, its distinguished triangle is the normalization-conductor sequence:

\[
R_{\mathrm{or}}[-1]\xrightarrow{\eta}A
\xrightarrow{\nu}N\xrightarrow{\delta}R_{\mathrm{or}}.
\]

In words: the cone of the supported-to-node comparison is exactly the normalization module. The extension has the primitive Ext generator computed above: lift one in the conductor quotient to (1,0) in N; its x and y relations lift to the cocycle (x,0).

An explicit model for the domain and comparison is

\[
P=[A\xrightarrow{\nu}N],\qquad
\eta^0=\operatorname{id}_A,\qquad \eta^1=0,
\]

where P has degrees zero and one.

In words: P is another model of the supported line in degree one, and its degree-zero identity represents the counit.

With the usual cohomological cone convention, [M2]

\[
\operatorname{Cone}(\eta)=
[A\xrightarrow{a\mapsto(a,-\nu a)}A\oplus N],
\qquad \pi(a,n)=\nu a+n.
\]

In words: the two terms lie in degrees minus one and zero. The displayed projection onto N is a quasi-isomorphism. Its section sends n to (0,n), and its contraction sends (a,n) to a. These give an integral, coefficient-natural, reflection-equivariant contraction of the cone onto N.

Consequently

\[
H^0\operatorname{Cone}(\eta)=R[x]\oplus R[y],
\qquad H^q\operatorname{Cone}(\eta)=0\quad(q\ne0).
\]

In words: the normalization data remain in the comparison cone. Since the actual R rings are polynomial/Laurent rings over the integers, the cone has no ordinary integer torsion. Its ordinary integral Bocksteins vanish.

### Ordinary restriction is a different comparison

There is also the conductor-value map

\[
c:A\longrightarrow R,\qquad
\operatorname{Cone}(c)\simeq
\bigl(xR[x]\oplus yR[y]\bigr)[1].
\]

In words: evaluating node functions at the conductor deletes their positive branch terms; those deleted terms reappear, shifted, in this different cone. This ordinary restriction is not the extraordinary counit. Neither cone is zero, and neither contains ordinary prime torsion in the formal model.

## 4. Assemble the comparison over the octagon boundary

Apply the construction to every existing localized ring R-L and every existing localization arrow. The node relations, normalization maps, residue, and the two-term model P all commute with these maps. In particular the local calculation supplies an actual natural transformation of diagrams, not a list of equal numerical readouts.

Let

\[
T_A=\operatorname*{lim}_{J_U}A_L,\qquad
T_P=\operatorname*{lim}_{J_U}P_L,\qquad
T_N=\operatorname*{lim}_{J_U}N_L.
\]

In words: these are derived sections of the three complete coefficient diagrams on the previously defined boundary index. T-A is equivalent to the earlier unreduced conductor totalization T-Q.

Derived limits in a stable category preserve fibre and cofiber sequences. Therefore

\[
\operatorname{Cone}(T_P\xrightarrow{\eta_U}T_A)\simeq T_N.
\]

In words: the entire boundary comparison cone is the derived normalization diagram, with no omitted coefficient degrees.

For each branch monomial, the scalar localization calculation is the same 903-support calculation performed for the previous boundary model. The new checker rebuilds every equal-degree vertex-to-edge matrix with exact integer unit-pivot reductions. It agrees with all 903 entries of the preceding certificate. Its nonzero Smith factors are one. Thus every cohomology group of T-N is free as an abelian group, and

\[
H^0(T_N)=R_0[x]\oplus R_0[y].
\]

In words: the boundary cone still has all unlocalized branch polynomials in degree zero; Laurent-support effects occur in its higher cohomological degrees. Counting one monomial per support is not a finite-rank computation of the entire polynomial module.

To view the supported object in the earlier marking convention, shift its supported degree to zero and retain the compensating orientation line:

\[
F_L=(i_L^!Q_L)[1]\otimes o_L\simeq R_L,
\qquad T_!=\operatorname*{lim}_{J_U}F_L.
\]

In words: the odd supported line is tensored with the odd orientation factor, producing an even coefficient line in degree zero. This is an explicitly specified convention, consistent with the source's relative orientation calculation; it is not an independently proved identification with every physical orientation map.

The scalar support computation gives H-zero equal to R-zero and no negative cohomology. Accordingly

\[
\operatorname{Map}_{D(\mathbb Z)}(\mathbb Z,T_!)\simeq(R_0)_{\mathrm{disc}},
\qquad
\operatorname{hofib}_{1}\bigl((R_0)_{\mathrm{disc}}
\xrightarrow{\operatorname{id}}(R_0)_{\mathrm{disc}}\bigr)\simeq *.
\]

In words: normalizing the **full polynomial** supported coefficient to one gives a contractible marking space. Normalizing merely one selected scalar coefficient would leave additional polynomial markings. The degree-zero coefficient readout here is not a claim that all of T-exclamation is quasi-isomorphic to R-zero.

## 5. The order-two class is equivariant, not ordinary cone torsion

The constant-coefficient part retains the source sequence

\[
0\longrightarrow\mathbb Z\xrightarrow{a\mapsto(a,a)}
\mathbb Z^2_{\mathrm{swap}}\xrightarrow{(a,b)\mapsto a-b}
\mathbb Z_{\mathrm{or}}\longrightarrow0.
\]

In words: sheet exchange swaps the middle basis and negates the quotient. This is Marici's existing sequence in entry 141. [S4]

An equivariant section would send one to (a,-a), requiring

\[
2a=1.
\]

In words: an integral unit cannot be lifted equivariantly. Twice the unit does lift, via (1,-1). The obstruction lies in

\[
\operatorname{Ext}^1_{\mathbb Z[C_2]}
(\mathbb Z_{\mathrm{or}},\mathbb Z)\cong\mathbb Z/2.
\]

In words: it is an order-two extension class in the reflection-equivariant category, despite the ordinary integral cone being torsion-free.

For reflection exponents g and h in {0,1}, the explicit connecting cocycle is

\[
c(g,h)=\frac{g+h-((g+h)\bmod2)}2,
\qquad c(1,1)=1.
\]

In words: composing two reflections supplies the nonzero comparison residue. Its double is the coboundary of the integer cochain g, while any normalized integral coboundary takes an even value on the reflection pair. The checker verifies the cocycle, connecting, and order-two identities.

This calculation recovers a known coefficient obstruction. It does not choose the endpoint-relative physical defect to which that obstruction must be applied. The source explicitly distinguishes those two tasks. [S4]

## 6. What remains unconstructed

The explicit conductor immersion now has its full polynomial extraordinary restriction, canonical counit, localization-natural assembly, and integral cone computation. The result uses the source's node ring, rather than a rank-one replacement of it.

The remaining physical identification requires a comparison from this specific conductor-supported functor to the source's complete relative endpoint/PC functor, retaining its generic Q leg, both endpoint connectors, support/Cartier data, and prescribed readout. Equality of a finite primitive signature does not provide this comparison on arbitrary coefficients. Also, the affine split node used here is not the different Rees chart with relation u=Xt that appears in the source's direct-trace no-go. [S3, S5]

No cone for that still-unspecified **full physical comparison** is claimed. No conclusion about RH follows from these local coefficient computations.

## Verification

Run:

```sh
python check_conductor_supported_comparison.py --output conductor_supported_comparison_certificate.json
```

The checker passes 17,022 exact assertions. It uses sparse untruncated node polynomials; checks dual differentials and their reflection/base-localization compatibility through cochain degree twelve; checks explicit residue reductions and higher boundary witnesses on polynomial modes through branch degree eight; checks the canonical cone contraction; performs integral finite-mode Smith reductions; rebuilds all 903 scalar support cases; and verifies the reflection connecting cocycle. Arbitrary-degree results follow from the displayed exact-sequence and annihilator proofs, not finite testing alone. This is not proof-assistant verification.

## Sources

[S1] `research/voevodsky/check_normalization_conductor_bimodule_kernel.py`, blob `2982163ca939dd1e09bb0b66b4229e31430e3c30`; associated ledger filename `20260817-627 The Conductor Difference Complex Is the Universal Mixed-Variance Kernel.md` (its internal metadata identifies entry 433).

[S2] `research/voevodsky/check_generic_log_dnc_thom_trace.py`, blob `95fd466d144bafea6838cfeacc4aaf485b124275`.

[S3] `research/voevodsky/check_global_mixed_variance_transform.py`, blob `3b23d8a71a374435e8f54d4fe9451a08cb8ab98e`.

[S4] `src/ledger/20260814-141 Conductor Bockstein Transgression and the Endpoint-Defect Reduction.md`, blob `5d10a833f7c77b8a9ba98e63dbcd15a7c10a1e95`.

[S5] `src/ledger/20260815-186 Direct Affine-Node Endpoint Descent No-Go and the Extraordinary Trace Gate.md`, blob `1b34c0f62b08195f18951108792a70a498f0b2fe`.

[M1] Stacks Project, *Right adjoint of pushforward for closed immersions*, tag `0A74`, and *Properties of upper shriek functors*, Lemma 48.17.4, tag `0ATZ`: `https://stacks.math.columbia.edu/tag/0A74` and `https://stacks.math.columbia.edu/tag/0ATZ`.

[M2] Stacks Project, *Cones and termwise split sequences*, tag `014D`: `https://stacks.math.columbia.edu/tag/014D`.

Earlier generated input: `coefficient_marked_boundary.md` and its executable certificate. The two different indexing/projection coefficient models remain distinguished throughout.
