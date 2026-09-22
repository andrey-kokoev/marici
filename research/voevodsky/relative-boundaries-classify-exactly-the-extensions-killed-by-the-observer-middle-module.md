# Relative boundaries classify exactly the extensions killed by the observer middle module

## Relative completeness theorem

In the declared finite-stage source-bimodule category, let

    0 -> L --i--> N --q--> C -> 0,
    I N=L,

be the intrinsic observer sequence, with C=N/L. Let V be a finite source module with I V=0. Then pushout of this sequence induces a canonical linear isomorphism

    Hom_(S-S)(L,V)
      ~= ker[ q^*:Ext1_(S-S)(C,V) -> Ext1_(S-S)(N,V) ].

It is not merely injective. Every extension of C by V that splits after pullback to N is the boundary of one UNIQUE equivariant covector L->V.

For the actual fixed-corner observer and scalar corner target V, the retained top readouts span these covectors. Hence they account for ALL degree-one classes lost under this particular pullback. No assertion of completeness for the full Ext1(C,V), the entire source evaluation, or stable scalar acquisition is made.

Inputs:
- `audit-the-relative-boundary-is-intrinsic-to-the-labelled-source-module-not-to-state-values.md`
- `the-lost-cubic-attachment-survives-as-a-relative-observer-boundary.md`
- `../nima/vacuum-attachment-readouts-are-direct-but-residual-readouts-need-stronger-tail-priors.md`

## 1. Fix the category and the actual sequence

Use the finite-dimensional source-bimodule modules supporting the specified stage-three observer. All maps are continuous in their declared finite-stage topologies. Strict exactness agrees here with ordinary exactness of finite-dimensional modules, and all finite linear isomorphisms are bounded.

The actual intrinsic sequence is

    E=O_3, K=ker(O_3->O_2),
    L=I^2 E,
    N=K intersect I E,
    C=N/L.

The audit proved L=im(f) and I N=L. The latter uses the checked equivariant lift of the old graded line. Its support verification covers the specified private, full-optimal and vacuum augmentations. It is not silently asserted for arbitrary new protocols.

All these modules have finite convex source support. Extensions of finite-dimensional endpoint modules are themselves finite-dimensional; endpoint idempotents absent on both ends are also absent on the middle. Thus the argument stays within a common finite convex source restriction and is valid in the corresponding strict completed setting. No projectivity of completed ideals is needed.

Ext1 below means ordinary equivalence classes of these strict source-bimodule extensions, identified with their degree-one derived morphisms. The theorem concerns this finite-stage category, not an unspecified category of infinite observer sequences.

## 2. The boundary construction

For alpha:L->V, form

    E_alpha=(N direct_sum V)/{(i(l),-alpha(l)):l in L}.

It fits into

    0 -> V -> E_alpha -> C -> 0,

where v maps to [0,v] and [n,v] maps to q(n). Denote its class by delta(alpha).

Pulling this extension back along q:N->C gives a split extension: the map n|->[n,0] lifts q. Therefore

    delta(alpha) belongs to ker(q^*).

Pushout and Baer sum make delta linear. These are the same boundary classes constructed in the previous observer audit.

## 3. Construct the inverse without an unspecified resolution

Take an arbitrary extension

    0 -> V --j--> Z --p--> C -> 0

whose pullback along q splits. Such a splitting is equivalent to a bounded source-module lift

    s:N->Z, p s=q.

For l in L, p s i(l)=0, so there is a unique alpha(l) in V with

    j alpha(l)=s i(l).

This defines an equivariant bounded alpha:L->V.

Now define

    Phi:E_alpha -> Z,
    Phi([n,v])=s(n)+j(v).

It is well defined because s i=j alpha. It is onto: first match the image in C using q, then correct by j(V). It is injective: if s(n)+j(v)=0, then q(n)=0, so n=i(l), and v=-alpha(l), precisely the relation in the pushout.

Phi is an isomorphism of extensions, acting as the identity on V and C. Its bounded inverse is automatic in this finite-dimensional setting. Therefore the original class equals delta(alpha).

This proves surjectivity onto the relative kernel constructively, rather than by an unqualified appeal to a long exact sequence in an unspecified completion.

## 4. Why the covector is unique and choice-independent

If s' is another lift, then

    s'-s=j h

for an equivariant h:N->V. Since I V=0 and I N=L,

    h(L)=h(I N)=I h(N)=0.

Thus restricting s or s' to L gives the SAME alpha. An isomorphism of the original extensions preserves this construction, so the inverse depends only on the extension class.

Likewise delta(alpha)=0 precisely when alpha extends to an equivariant map N->V. Every such extension kills L, so only alpha=0 can have zero boundary.

This proves both uniqueness and injectivity. The result is a canonical classification of the specified kernel, although neither the splitting s nor the middle-module representative Z is canonical.

## 5. Naturality and corrected frames

The construction is natural in an I-annihilated target V: a map V->W takes alpha to its composite and the associated boundary to the pushout class. Restriction of a pulled-back splitting gives the same composite covector.

It is also natural under isomorphisms of the observer sequence (L,N,C). Corrected frame isomorphisms preserve the declared source action, ideal and transition. Hence they transport L=I^2 O_3 and N=ker(pi) intersect I O_3, and induce exactly these sequence isomorphisms.

The relative completeness is therefore frame-compatible for the admitted corrected frames. It does not create an isomorphism between the previously distinguished raw uncorrected source-marked towers.

## 6. Exact consequence for the retained cubic readouts

For the specified stage-three protocols, L is supported at the single six-event corner and all positive-length paths act trivially on it. Take V to be its scalar corner module. Then every linear covector of L is equivariant, and

    dimension of the relative Ext1 kernel = dim L.

The audited top readout ranks therefore give:

- scalar cubic frame family alone: relative kernel dimension 1;
- scalar cubic family plus vacuum: dimension 2;
- both separately retained private coordinates without vacuum: dimension 2;
- both private coordinates plus vacuum: dimension 3.

The named retained covectors span the dual of L in each case. Their boundary classes consequently form a basis of THIS relative kernel. These dimensions do not count additional higher degrees or the full Ext1 group.

This is the promised completeness theorem for the comparison. It strengthens the prior independence statements to exhaustion of the classes killed by pullback along q:N->N/L.

## 7. Keep the comparison distinct from source recovery

The classified map is

    q^*:Ext1(N/L,V)->Ext1(N,V).

It is not the map pushing the source adjacent class along G_3->K, nor the full observer evaluation of sources. The relation to that adjacent class still uses the actual source-calibrated map

    H_bar:G_2->N/L,
    H_bar^* delta(alpha)=lambda_alpha[1] e_2.

Relative completeness does not reconstruct H_bar from observer-state values and does not establish faithfulness of H_bar^* on arbitrary targets or classes. The existing product witnesses justify the stated scalar source nonvanishing.

Likewise, algebraic exhaustion is not a uniform measurement theorem. The vacuum covector is directly stable in its acquisition norm; the residual covector needs the stronger path-tail priors proved by Nima. No norm on the entire Ext group or numerical conditioning for this classification is inferred.

## 8. Why this need not exhaust the full Ext1 group

An exact illustrative fixture takes S=k[t], N=J_2 direct_sum k, L=tN, C=N/L=k^2 and V=k, where J_2 is the two-dimensional nilpotent Jordan module.

Extensions of C by V have two coordinates (a,b), specifying the t-action from the two quotient generators into V. Pullback along N->C splits exactly when b=0. The boundary covector L->V is a.

Thus the relative kernel is one-dimensional while Ext1(C,V) is two-dimensional. This is not a computation of the full actual observer Ext group; it demonstrates why the relative theorem must not be promoted to that stronger statement.

## Verification

    uv run --with sympy python research/voevodsky/checkers/check_relative_boundary_completeness.py

The checker verifies the constructive inverse, splitting-choice independence, equivariant pushout isomorphism, linearity and injectivity, and a proper relative kernel in the exact fixture. The theorem for the actual observer modules is the finite-stage module proof above together with the already audited identity I N=L.
