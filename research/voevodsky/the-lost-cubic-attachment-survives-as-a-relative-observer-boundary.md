# The lost cubic attachment survives as a relative observer boundary

## Result

The adjacent cubic attachment does not disappear without a trace when its pushout into the corrected observer transition kernel becomes zero.

There are two precise recoveries:

1. A relative fibre of the source-to-observer map carries a NONZERO lift of the original adjacent class and maps to the original residual receiver.
2. Inside the finite observer kernel K, the extension

       0 -> im(f) -> K -> K/im(f) -> 0

has a nonzero scalar pushout. Pulling that boundary class back along the quotient of the explicit nullhomotopy recovers the original scalar cubic attachment.

Both constructions are compatible with admitted corrected frame isomorphisms. They retain the source-marked submodule and nullhomotopy data; they do NOT apply a derived functor to the already-zero pushed-forward class and claim to recover it.

Inputs:
- `the-corrected-observer-kills-the-adjacent-cubic-class-but-retains-the-full-extension.md`
- `two-residual-gaps-detect-the-adjacent-cubic-attachment.md`
- `common-flag-models-supply-coherent-nullhomotopies-at-every-finite-horizon.md`

## 1. Fixed objects and the information that was lost

Use the declared corrected stage-three observer tower, with unchanged O_2. The previous construction also permits the ideal full-optimal cubic observer and the two private-coordinate augmentation, provided their specified source actions and correction maps are retained.

Write

    B=G_3=J_3/J_4, A=J_2/J_4, G=G_2=J_2/J_3,
    0 -> B --i--> A --q--> G -> 0,
    K=ker(O_3^sharp -> O_2).

The source extension has connecting class e:G->B[1]. Its observed coefficient map is f:B->K. The preceding theorem supplied the bounded source-equivariant extension

    H:A->K, H i=f.

Explicitly H is source evaluation minus the lifted old graded-line component. Hence f[1]e=0, although f is nonzero on the cubic witness v_3.

Let T be the ORIGINAL shifted three-seam residual receiver, whose bottom degree is -1, and let

    j:B[1]->T

be the actual D3 cycle map. Its adjacent class j e is nonzero by the established finite projective restriction and positive residual-gap witness.

There cannot be a derived comparison r:K[1]->T with r f[1]=j: it would imply j e=r f[1]e=0. This rules out recovering the original receiver by an unproved direct map from the saturated kernel. A relative construction is necessary.

## 2. Explicit relative fibre and lifted class

Define the two-term complex

    R=[B --f--> K], degrees 0,1.

It is a fibre model for B->K, with the standard cone identification adjusted to this displayed differential convention. Its shift is

    R[1]=[B --(-f)--> K], degrees -1,0.

Represent G by the usual strict extension roof

    P=[B --i--> A], degrees -1,0.

Define a chain map

    e_tilde_H:P -> R[1]

by identity on B in degree -1 and -H on A in degree zero. The chain identity is exactly

    (-f) id=(-H)i.

Projection pi_R:R[1]->B[1] gives pi_R e_tilde_H=e. Composing further with j gives the original NONZERO receiver observation. Thus e_tilde_H is nonzero in the same strict derived category.

In particular the witness need not lie in ker(f). Indeed f(v_3)!=0. The relative representative uses both degrees and the equation H i=f; replacing it by the ordinary kernel of f would lose the mechanism.

## 3. An actual relative comparison with the original receiver

The span

    T <-j- B[1] -f[1]-> K[1]

has a homotopy pushout. An explicit cochain model is

    Z=Cone((j,-f[1]):B[1]->T direct_sum K[1]).

Thus Z has B in degree -2, T^(-1) direct_sum K in degree -1, and the remaining T degrees above that. Its new differential is

    d_Z^(-2)(b)=(j(b),-f(b)).

The original class becomes null after inclusion T->Z. On P, a nullhomotopy has components

    degree -1: B -> Z^(-2), identity,
    degree  0: A -> Z^(-1), a |-> (0,H(a)).

In degree -1, the homotopy equation is

    (j,-f)+(0,H i)=(j,0).

This explicitly identifies where the new comparison discards the old class.

Conversely, the fibre of T->Z is equivalent to R[1]. For a concrete sign convention, model this fibre by

    F^n=T^n direct_sum Z^(n-1),
    d_F(t,z)=(d_T t, inclusion(t)-d_Z z).

The map R[1]->F sends

    b in degree -1 to (j(b),b),
    k in degree 0 to (0,(0,-k)).

Its retraction reads the B component in degree -1 and minus the K component in degree zero. The retraction kernel has the form

    T^n direct_sum T^(n-1),
    d(t,z)=(d_T t,t-d_T z),

with contraction (t,z)|->(z,0). It is a bounded contractible identity-cone complex. Projection F->T recovers j pi_R.

Thus R[1] is not merely a formal extra copy of the source: it is an explicit relative fibre of the receiver's actual homotopy-pushout comparison. It is not, however, a newly admitted physical measurement channel.

## 4. A finite observer-internal boundary detecting the scalar class

The full D3 receiver need not factor through im(f), but the RETAINED scalar cubic functional does.

Let L_0 be the one-dimensional source corner module at the fixed six-event endpoints, with all positive-length path actions zero. Let

    lambda:B->L_0

be the original ideal cubic functional, in the fixed linear convention. It is source-equivariant: a contributing I^3 input has at least six events, so a positive-length context cannot fit into this detector's fixed six-event corner. Its value on v_3 is the strictly positive residual-gap product.

The class lambda[1]e is nonzero. On the finite packet, a hypothetical source-equivariant nullhomotopy A->L_0 would send v_3=a b c to a times the value on bc, hence to zero because I annihilates L_0. This contradicts lambda(v_3)>0. The same finite projective restriction used for the original roof makes this a derived nonvanishing statement.

Put

    L=im(f) subset K, C=K/L.

K is finite-dimensional, so L is closed and all quotients here are strict. Since the original scalar row is retained in O_3^sharp, ker(f) is contained in ker(lambda). Therefore lambda factors through a bounded source-module map

    lambda_bar:L->L_0.

This remains true if separate private-coordinate rows enlarge L; it does not require L to be one-dimensional.

Now take the extension

    0 -> L -> K -> C -> 0

and push it out along lambda_bar. Its class is

    chi:C -> L_0[1].

An explicit middle module is

    (K direct_sum L_0)/{(l,-lambda_bar(l)):l in L}.

This is a finite source-module extension, not a response norm or a fitted scalar form.

## 5. The recovery equation

Since H i=f has image in L, the composite A->K->C kills B and descends to a bounded source map

    H_bar:G->C.

There is an actual commuting extension diagram

    0 -> B -> A -> G -> 0
         |      |H    |H_bar
    0 -> L -> K -> C -> 0,

where the left arrow is f corestricted to L. Naturality of degree-one extensions gives the exact equation

    lambda[1] e = chi H_bar
        in Hom_D(G,L_0[1]).

The left side is nonzero. Hence chi is nonzero and its pullback along H_bar is nonzero. This is the finite relative boundary carrying the lost scalar attachment.

There is also a direct obstruction to extending lambda_bar to an equivariant map K->L_0. The source identity and equivariance of H give

    f(v_3)=H(a b c)=a H(bc) in I K,

whereas lambda_bar(f(v_3))=lambda(v_3)>0. Every equivariant map K->L_0 kills I K. Thus no such extension exists, exactly as the nonsplit pushout class chi requires.

The map f into the ENTIRE K killed the original source Ext1 class because H extended it. The inclusion of its image L into K records the obstruction to extending the scalar readout instead. These are different maps and different coefficient modules, so there is no contradiction.

## 6. Nullhomotopy choice and frame compatibility

If H' is another equivariant extension of f, then

    H'-H=u q

for a bounded source map u:G->K. The corresponding relative lifts differ by the map -u through the degree-zero K component of R[1]. Projection to B[1], and therefore to the original receiver, kills this ambiguity.

Likewise H_bar'-H_bar is the composite G->K->C. The connecting class chi vanishes after pullback to K, so

    chi H_bar'=chi H_bar.

Thus recovery of the scalar class is independent of the chosen extension H, even though the displayed relative lift need not be unique. This is an explicit ambiguity statement, not a claim of unique Toda data.

For admitted corrected frame isomorphisms, let t_K:K^f->K^g be the induced kernel map. Source compatibility gives

    t_K f_f=f_g,
    t_K H_f=H_g

for the supplied old-line-lift construction. It induces the chain isomorphism diag(id_B,t_K) between the R models, and the corresponding cone isomorphism between the Z models, fixing T. These maps satisfy the frame cocycle strictly.

They also identify L^f with L^g and C^f with C^g, preserve lambda_bar and chi, and transport H_bar. Hence the recovery equation is frame-compatible. Common noninvertible observer refinements give natural diagrams as well; no isomorphism of the raw uncorrected towers is asserted.

At a fixed cubic stage, the established larger source roofs obtained by quotienting J_2 and J_3 by J_N map to P with their identity-complex kernels. Precomposing the displayed maps by those actual quotients preserves all formulas. This is compatible finite-horizon refinement, not an assertion of a uniformly bounded infinite source resolution.

## 7. What this does and does not recover

Recovered:
- a nonzero relative lift detected by the FULL original D3 receiver;
- a finite observer-internal extension chi recovering the original SCALAR adjacent attachment by pullback;
- explicit homotopies, signs, ambiguity and corrected-frame compatibility.

Not claimed:
- a direct factorization of the original receiver through K[1]; that is impossible here;
- recovery by applying a functor to the zero class f[1]e;
- reconstruction of the source from arbitrary observer states;
- a new ordinary scalar measurement on K extending lambda_bar;
- numerical realization or noise bounds for the derived quotient/connecting map;
- new higher Ext degrees beyond these degree-one and relative-cone constructions.

The essential retained information is the SOURCE-MARKED image L inside K and its quotient extension, not merely the zero pushed-forward class or a list of scalar values. The source-realization certificate supplies genuine inputs, but does not replace this relative module data.

Audit clarification: `audit-the-relative-boundary-is-intrinsic-to-the-labelled-source-module-not-to-state-values.md` proves that L is recoverable from the declared ideal action as I^2 O_3, and identifies the smaller intrinsic extension with middle module ker(O_3->O_2) intersect I O_3. Thus L need not be supplied as additional source-evaluation data when the module action and ideal are known. Identifying the resulting boundary's pullback with the normalized original source class still requires the source evaluation.

## Verification

    uv run --with sympy python research/voevodsky/checkers/check_relative_cubic_attachment_recovery.py

The exact checker verifies the fibre-lift signs, the homotopy-pushout nullhomotopy, the explicit fibre retraction, a nonsplit image/cokernel extension fixture, the nullhomotopy ambiguity formula and frame transport.

Actual source nonvanishing is the already proved positive cubic attachment. The needed bounded H and its applicability to the full-optimal observer are established by the preceding exact source-context checks, not inferred from this matrix fixture.
