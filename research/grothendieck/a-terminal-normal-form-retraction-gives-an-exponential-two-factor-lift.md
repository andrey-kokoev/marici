# A terminal normal-form retraction gives an exponential two-factor lift

## Status and attribution

The requested reverse estimate is positive. Nima's supplied `universal-form-fox-lifts-control-the-completed-ideal-power-topologies.md` proves it uniformly over all powers, and Voevodsky's `fox-lifts-transfer-the-compatible-filtered-tower-to-presentation-scales.md` supplies the simultaneous-lift argument needed for strict exactness on intersections.

This note records an independent first-step derivation and regression check. For the original unweighted marked-path-tuple quotient norm it gives

mu_2(v) <= 3(2^n-1) ||v||_path,  v in (I^2)_(x,y), n=length(x,y).

Thus the inherited and native next-power domains agree on the all-radius intersection. The fixed-Banach-stage nonclosed-image result remains valid. This is source-only lifting, not an inverse to Clark features or a source-module splitting of the filtered extension.

## 1. Terminal normal forms and a degree-sensitive bound

Fix [x,y]. Use terminal-anchored vertex potentials xi_v, v<y, with xi_y=0, so that an event u->v records xi_u-xi_v. These are independent source coordinates: they are the nonzero nested interval forcings from v to y, related invertibly to the actual chamber basis.

The universal-form normal basis is indexed by chains

x <= v_0 < v_1 < ... < v_q=y,

and records the tensor product of xi_(v_i)-xi_(v_(i+1)). Its source lift is the chosen sorted forgotten path x->v_0 followed by the product of the formal single-retained derivatives of the chosen forgotten paths v_i->v_(i+1).

These records span by repeated use of the interval Leibniz identity d(fg)=df g+f dg. They are independent: in the potential-tensor expansion, the coefficient on a strictly increasing chain of q vertices not containing y is exactly its normal-form coefficient. Choosing an upper endpoint in a difference either forces a repeated adjacent vertex later or ultimately chooses xi_y=0. Only the all-lower-endpoint choice survives this coordinate extraction.

This is the terminal-anchored version of the universal-form normal basis proved in Nima's note. Fix the event order globally for compatible convex-corner choices.

Let R=sigma rho:S->S be the resulting endpoint-preserving linear retraction. It preserves retained degree, satisfies rho R=rho, and fixes vertex identities. It is NOT asserted multiplicative.

For a length-n source path with q retained events:

- Its potential expansion has coefficient mass at most 2^q. Extracting the strict-chain coordinates cannot increase that mass.
- A normalized q-form with differentiated block lengths l_i has source lift mass product l_i.
- Since l_i>=1, l_i<=2^(l_i-1), and sum l_i<=n, this mass is at most 2^(n-q).

Consequently

||R(w)||_path <= 2^q 2^(n-q)=2^n.

This is uniform in the endpoint and its arithmetic location. No bound on an inverse analytical feature map occurs.

## 2. A telescoping, right-linear splitting on I

For w=e_1...e_n put

H(w)=sum_(i=1)^n [R(e_1...e_(i-1)) e_i-R(e_1...e_i)] tensor (e_(i+1)...e_n).

Each bracket is in I. Thus H maps S into I tensor_D S. Multiplication telescopes:

mult H(w)=w-R(w).

It is the identity after multiplication on I.

On I the map H is right S-linear. Indeed, for a product u v with u in I, cuts inside u give H(u)v. For cuts beyond u, both retracted prefixes vanish because they factor through rho(u)=0. This proves right linearity directly from the formula, without selecting a relation factorization.

For z in I^2, express z algebraically as a sum of products a b with a,b in I only to prove membership. Right linearity gives

H(ab)=H(a)b in I tensor_D I.

Hence H(z) belongs to the actual two-factor relation presentation and multiplies to z. The formula computing H(z) depends on z itself, not on that auxiliary existence proof.

## 3. Norm of the lift

For one path the i-th bracket has norm at most 2^(i-1)+2^i. Its suffix is a single path of norm one. Therefore

||H(w)||_tuple <= sum_i [2^(i-1)+2^i]=3(2^n-1).

All paths in an endpoint corner have the same length, so linearity gives

||H(z)||_tuple <= 3(2^n-1)||z||_path.

On I^2, H(z) is an admissible presentation. Taking the quotient infimum proves the announced bound.

The tuple norm here is exactly the earlier norm induced from expansion in marked-path tuples. It is not silently replaced by a projective tensor norm on two already completed ideal factors. If one wants an expression consisting termwise of two relations, apply id tensor (1-R) to H(z); on I^2 this leaves H(z) unchanged. Estimating the individual relation factors instead gives the coarser exponential bound 3n 2^n, still sufficient for radius control.

## 4. Restore weights and repair the first kernel comparison

Use the notation of the native-norm obstruction note:

W_r(n)=(2 lambda s)^r r! (1+n)^r (b a)^n,

E_r = completion of I^r with W_r mu_r,

F_(2|1) = completion of I^2 with the inherited E_1 norm.

Here mu_1 is exactly path l1. The upper bound and 1+n<=2^n give

||z||_(E_2(s,b)) <= 12 lambda s ||z||_(F_(2|1)(s,4b)).

The forward merging map was already bounded in the other direction. Finite endpoint truncation extends both identity maps continuously to all-radius intersections, and the coordinates identify their compositions with the identity. In particular the reverse map is onto the native intersection, not merely dense.

The strictly exact induced-kernel sequence consequently becomes the native sequence on these intersections. Surjectivity of its last arrow is not inferred from stagewise surjectivity: choose an unweighted minimizing lift in each finite corner. All radius weights are scalar multiples of that one corner norm, so the same lift works simultaneously at every radius. This is precisely Voevodsky's intersection argument. The Frechet open mapping theorem then gives strictness.

At a fixed radius the extra factor proportional to 1+n still produces the previously proved dense proper inclusion. The repaired comparison has radius loss and does not contradict that example.

## 5. Relation to the supplied all-depth results

Nima's recursive Fox construction gives depth-uniform exponential bounds, including control of the graph weights. It is stronger in scope than the fixed two-factor calculation here. Voevodsky transfers all finite filtered attachment roofs and their common refinements through those comparisons.

Thus the earlier norm-comparison gate is closed, including the first two compatible filtered attachments now supplied by Voevodsky. None of these results proves completed projectivity, a completed tensor-Hom equivalence, or equality of an unrestricted filtration inverse limit with summable source states.

## Verification

`python research/grothendieck/checkers/check_exponential_factorization_lift.py`

Passed:

- 442 exact recorder/retraction/telescoping checks;
- 40 local-product and right-linearity checks;
- 40 nonlocal relation-factor checks, with actual lift/path norm ratios exceeding one;
- a cancelling sum of different product presentations.

The nonlocal factors are constructed as w-R(w), rather than only testing minimal diamond products. All products are reconstructed exactly, and applying the terminal recorder to either lifted factor gives zero. The uniform estimate is the proof above, not an extrapolation from these tests.

References:

- `research/nima/universal-form-fox-lifts-control-the-completed-ideal-power-topologies.md`;
- `research/voevodsky/fox-lifts-transfer-the-compatible-filtered-tower-to-presentation-scales.md`;
- `research/voevodsky/the-first-two-completed-filtered-attachments-form-a-compatible-comparison.md`;
- `research/grothendieck/native-factorization-completions-give-only-closure-exactness-for-the-filtration.md`.
