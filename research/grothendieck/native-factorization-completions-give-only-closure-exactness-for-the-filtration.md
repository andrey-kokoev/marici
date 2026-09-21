# Native factorization completions give only closure exactness for the filtration

## Result and relation to the common-path theorem

**Fixed-scale obstruction, with a strictly exact induced-norm replacement.** Applying the existing r-factor presentation norm to I^r before passing to its associated quotient gives natural Banach spaces E_r. At fixed scale the sequence

0 -> E_(r+1) -> E_r -> X_r -> 0

is NOT exact at E_r. The first map is injective but its image is only dense in the quotient kernel, not equal to that kernel.

The strictly exact sequence instead uses the next ideal with the norm INHERITED from E_r. This agrees with the distinction in Voevodsky's common-path extension theorem, rather than contradicting it. In particular, independently stronger layer/factorization norms cannot silently replace the terms of that theorem.

This note answers the kernel-versus-closure test. It constructs the connecting roof for the induced-norm sequence in a declared exact category; it does not claim a completed analytical derived base-change theorem.

## 1. Specify the two norms before completing

Fix r>=1 and s,b>=1. At a stabilized finite endpoint corner c of event length n, let P^r_c be the r-factor relation presentation used in the associated-source construction, with its unweighted marked-path-tuple l1 norm. Multiplication maps it onto (I^r)_c.

Let mu_r be the quotient norm on (I^r)_c under this multiplication. This quotient removes the actual multiplication kernel, but does NOT yet kill I^(r+1). Put

W_r(n)=(2 lambda s)^r r! (1+n)^r (b a)^n,

E_r = l1 direct_sum_c ((I^r)_c, W_r(n) mu_r).

These E_r are the natural extension of the earlier presentation-norm convention from associated layers to ideal powers. They are explicitly defined here, not presumed to have been completed previously.

Let F_(r+1|r) be the l1 sum of (I^(r+1))_c with the RESTRICTION of W_r mu_r. It is a closed subspace of E_r: coordinate membership is closed and endpoint projections are bounded. It is exactly the closure of the algebraic I^(r+1) in E_r.

Successive quotient norms give canonically

E_r / F_(r+1|r) = X_r,

where X_r is precisely the earlier weighted associated-layer completion at this fixed s,b. On a finite corner both sides are P^r_c modulo the preimage of I^(r+1). The l1 quotient identification follows by choosing coordinate lifts with summable errors.

Consequently

0 -> F_(r+1|r) -> E_r -> X_r -> 0

is strictly exact, with isometric first arrow and quotient last arrow. This requires no uniformly bounded linear splitting.

## 2. The native next-power norm is stronger

Merge the first two relation factors of an (r+1)-factor presentation. Their product still lies in I. On marked-path tuple expansions this is l1-contractive, so

mu_r(v) <= mu_(r+1)(v),  v in I^(r+1).

The weighted ratio is

W_r(n)/W_(r+1)(n) = 1/[2 lambda s (r+1)(1+n)].

Thus inclusion extends to an injective bounded map

E_(r+1) -> F_(r+1|r),

and in every corner its operator norm is at most the displayed ratio. Injectivity follows from the identity on finite endpoint coordinates. The image contains all finite-support corners and is therefore dense.

The factor tending to zero with n already warns that closedness is impossible if nonzero next-power corners occur at arbitrarily large lengths. The following source witness proves that directly and certifies the relevant quotient norms exactly.

## 3. Exact source norm certificates

Choose r+1 consecutive forgotten diamond relations q_1,...,q_(r+1), each on a fresh two-event block. Follow them by a fixed all-forgotten suffix w, bringing the total event length to n>=2(r+1). Put

v_n=q_1 ... q_(r+1) w.

This is an actual element of I^(r+1), not a class inferred from an observed Gram matrix. Its expansion has 2^(r+1) distinct paths, each with coefficient +1 or -1.

Multiplication of path tuples is l1-contractive, so the actual path norm is a lower bound for every factorization quotient norm. An (r+1)-factor lift is

q_1 tensor ... tensor (q_(r+1) w),

and an r-factor lift is obtained by merging the first two factors. Both lifts have coefficient norm 2^(r+1). Hence

mu_r(v_n)=mu_(r+1)(v_n)=2^(r+1).

Normalize x_n=v_n/[2^(r+1) W_(r+1)(n)]. Then

||x_n||_(E_(r+1))=1,

||x_n||_(F_(r+1|r))=1/[2 lambda s (r+1)(1+n)] -> 0.

Thus the injective native inclusion is not bounded below. An injective map between Banach spaces with closed image would have a bounded inverse onto that image. Its image is therefore nonclosed.

## 4. An explicit kernel element without a native lift

Choose distinct endpoint corners with lengths

n_j=2^j+2(r+1).

Use x_(n_j) from section 3. The series

z=sum_(j>=1) x_(n_j)

converges in F_(r+1|r), since its norm is bounded by a constant times sum 2^(-j). It is therefore an element of ker(E_r -> X_r).

Any preimage in E_(r+1) would have to have exactly these finite endpoint coordinates. Its native l1 norm would be sum 1=infinity. There is no such preimage.

Accordingly,

image(E_(r+1) -> E_r) is a proper dense subspace of ker(E_r -> X_r),

closure(image)=ker(E_r -> X_r).

This is failure of algebraic exactness of the proposed Banach sequence, not merely a missing proof of a bounded splitting. It is a norm mismatch at fixed scale, not the analytical receiver's separate forgotten-suffix inverse obstruction.

## 5. The common norm retains the source extension

Let A_r be the completed path algebra with weight

h_r(n)=(1+n)^r (b a)^n.

It is a Banach algebra because h_r(n+m)<=h_r(n)h_r(m). Source action on an r-factor presentation is implemented by multiplication into its first or last factor. The unweighted norm is bounded by the path l1 norm of the acting element, and the weight inequality gives bounded A_r actions on E_r. They preserve F_(r+1|r) and descend to X_r.

Work in the exact category of Banach A_r-bimodules with strict short exact sequences. The sequence of section 1 defines its extension class. Its connecting morphism has the standard roof

X_r <- [F_(r+1|r) -> E_r] -> F_(r+1|r)[1],

with the two-term complex in degrees -1 and 0. The left arrow is the quotient quasi-isomorphism; strict exactness makes its cone strictly acyclic. The right arrow is the connecting projection. Neither map requires a splitting or inverse analytical feature map.

Every stabilized finite endpoint restriction recovers the algebraic source extension and its connecting morphism. No global hereditary or projectivity theorem for the completed algebra is inferred from finite path-algebra projectivity.

At r=1, mu_1 is just the inherited path l1 norm. Thus E_1 and F_(2|1) are, up to the common constant 2 lambda s, the common-path completions J_1 and J_2 with polynomial exponent p=1. Quotienting further by the closed J_3 gives exactly Voevodsky's strictly exact first truncated extension

0 -> J_2/J_3 -> J_1/J_3 -> J_1/J_2 -> 0.

Its finite forgotten-diamond witness remains source-nonsplit. The positive common-path theorem and the native-norm obstruction concern different norms on the next-power term.

## 6. Subsequent closures and remaining boundaries

1. **All-radius exactness is now proved.** Nima's universal-form Fox lifts supply the previously missing uniform exponential source factorization bounds, including depth-graph control. Voevodsky's transfer theorem adds simultaneous finite-corner quotient lifts to prove strict exactness on the intersections. Thus the native and inherited domains agree there with explicit radius loss, while the fixed-stage counterexample above remains valid. An independent first-step check and bound mu_2(v)<=3(2^n-1)||v||_path are recorded in `a-terminal-normal-form-retraction-gives-an-exponential-two-factor-lift.md`.

2. **Analytical attachment and higher levels.** Voevodsky has now supplied the first truncated extension's bounded nonzero balanced attachment in a common path topology: the ordered two-cut derivative D2 has at most binomial(n,2) terms, annihilates I^3, and is controlled by the common weight (1+n)^2 A^n. This is the direct path estimate needed, rather than an inference from the stronger factorization norm. Its roof is nonzero by finite source restriction; completed projectivity is not assumed. The p=1 induced norm here can pay the extra polynomial factor by enlarging its radius, but this is not a same-radius identification. Voevodsky subsequently supplies compatible attachments at every finite filtration level and transports them through the Fox norm comparisons. Completed derived tensor comparisons and unrestricted inverse-limit realization remain separate.

3. **General homology under completion.** The canonical roof above is for this strictly exact sequence. It does not establish arbitrary differential-range closure, exactness of completed tensoring, or commutation of analytical homology with completion.

The first analytical construction now does use the common-norm extension explicitly. Subsequent constructions must likewise avoid the falsely exact native sequence.

## Verification

`python research/grothendieck/checkers/check_filtered_completion_norm_gap.py`

Passed 285 exact source norm certificates, including equal path lower bounds and factorization-lift upper bounds, plus 24 terms of the explicit missing-lift series estimate. The infinite conclusion follows from the geometric upper bound and endpoint l1 norm identity in section 4.

References:

- `research/voevodsky/endpointwise-separation-and-bounded-differentials-close-the-fixed-depth-l1-receiver.md`;
- `research/grothendieck/the-completed-associated-source-is-multiplicative-with-controlled-scale-loss.md`;
- `research/voevodsky/the-first-filtered-extension-is-strictly-exact-and-source-nonsplit.md`;
- `research/voevodsky/the-completed-first-filtered-extension-has-a-nonzero-balanced-attachment.md`;
- `research/grothendieck/packet-refinement-preserves-the-relation-tower-but-coarse-seams-lose-higher-products.md`;
- `research/nima/universal-form-fox-lifts-control-the-completed-ideal-power-topologies.md`;
- `research/voevodsky/fox-lifts-transfer-the-compatible-filtered-tower-to-presentation-scales.md`.
