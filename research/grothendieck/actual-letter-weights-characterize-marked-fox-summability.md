# Actual letter weights characterize marked Fox summability

## Result and scope

**Exact all-radius domain for the fixed forcing-resolved Fox map.** The maximal coefficient domain is a factorial path scale weighted by the ACTUAL norms of its retained forcing letters. It is generally strictly larger than the sufficient unweighted factorial source, even when restricted to the earlier reconstructed source ideal.

The top jet prevents cancellation from hiding marked path coefficients. What enlarges the domain is attenuation of retained forcings, not cancellation or a change of Green pairing.

Voevodsky's `factorial-fox-summability-has-a-vacuum-necessity-test-and-compatible-filtered-exactness.md` already proves necessity on the forgotten sector. This note addresses the remaining marked sector. The target here is the forcing-resolved projective/cut-l1 carrier, with fixed actual event forcings, positive memory/seam norm multipliers, and all original edge and endpoint labels.

## 1. Actual-letter factorial seminorms

For an elementary event e let f_e=1_(E_e) Phi in H_beta be its actual forcing and put

    gamma_e=sqrt(w_seam) ||f_e||_beta > 0.

The forgotten letter has weight one. For a marked path w define

    Gamma(w)=product_(retained events e of w) gamma_e.

Empty products are one. These weights multiply exactly under composable path concatenation. No independent forcing copies or root states are introduced.

For a coefficient family x=(x_w), retaining its finite endpoint corners, set

    Q_R(x)=sum_c n(c)! R^(n(c)) sum_(w in c) |x_w| Gamma(w),  R>=1.

Let S_Gamma be the intersection of these weighted l1 spaces over integer R>=1. Every gamma_e is positive, so the finite coefficient projections are continuous. Compatible completeness and finite-support density follow as for the earlier path scales.

Write F_(s,b) for the existing all-order forcing receiver, with graph weight (2 lambda s)^k k!, feature radius b, and

    lambda=max(1,tau/sqrt(w_seam)).

The following bounds characterize the domain:

    Q_R(x) <= ||D(x)||_F(R,1),

    ||D(x)||_F(s,b) <= 2 Q_(ceil(2 lambda s b))(x).

First prove them for finite coefficients. They then apply to arbitrary cornerwise coefficient families, allowing infinity, by truncation and the retained coordinate projections.

## 2. Upper bound: every cut retains the same forcing factors

For a word w of length n, each retained event appears either in a memory buffer or as a seam feature. Its forcing norm is present in either case. Moving it from a seam to memory changes the norm multiplier by tau/sqrt(w_seam), at most lambda.

For a k-cut term there are at most n-k such moves. If d(w) is the retained feature count, each term therefore has norm at most

    b^(d(w)) lambda^(n-k) Gamma(w).

There are binomial(n,k) choices of cuts. Put t=2 lambda s. The sum of the graph-weighted bounds is

    Gamma(w) b^(d(w)) sum_(k=0)^n t^k k! binomial(n,k) lambda^(n-k)
      = Gamma(w) b^(d(w)) n! t^n sum_(j=0)^n (1/(2s))^j/j!
      <= 2 Gamma(w) n! (t b)^n.

Here b^(d(w))<=b^n. Triangle inequalities handle collisions between different source words. Summing their absolute coefficient contributions proves the upper bound without assuming positivity of a signed pairing.

## 3. Lower bound: the complete seam route exposes each coefficient

Fix an endpoint corner c of length n. The top jet D_n selects every event. All its buffers are vacuum; its ordered typed seam edges retain the entire underlying path route.

Different routes lie in different labelled cut shapes. Within a route, each seam slot has its vacuum and feature sectors. The projections onto these sectors are contractions for the prescribed positive carrier norm. Their tensor products are contractions also for the forcing projective norm. The feature-degree weights respect these projections.

For a prescribed mark pattern, projecting D_n(x_c) onto those vacuum/feature choices gives the single corresponding coefficient times the tensor of its actual forcing letters. Its norm is exactly

    |x_w| Gamma(w).

There are at most 2^n mark patterns per route. Summing their projection bounds, then the labelled route norms, gives

    sum_(w in c) |x_w| Gamma(w) <= 2^n ||D_n(x_c)||_unweighted.

This conservative bound works even if mark patterns are grouped inside a tensor block rather than individually l1-summed. No lower bound on any gamma_e is used.

At target scale s=R, the top graph multiplier is n!(2 lambda R)^n. Since lambda>=1, it pays the factor 2^n in the last inequality. Finally, the sectors (c,k=n(c)) form a labelled subfamily of the full l1 receiver. Summing over c proves

    Q_R(x) <= ||D(x)||_F(R,1).

Thus cancellation in lower jets cannot enlarge the domain beyond S_Gamma. On the forgotten sector Gamma=1, this reduces to factorial path necessity, in agreement with Voevodsky's exact vacuum probe.

## 4. Precise relation to the earlier source domain

For any cornerwise source coefficient family,

    D(x) belongs to every F_(s,b)  iff  Q_R(x)<infinity for every R.

If the source is required to belong to the earlier common-path reconstructed space S_common, its exact summed-jet domain is

    S_common intersect S_Gamma.

The same statement holds after restricting to the terminal-record ideal. This distinction matters: completion in Q_R alone may admit coefficient families outside S_common. We do not silently identify these spaces.

If A bounds the admitted letters as in Nima's factorial theorem, Gamma(w)<=A^n. Hence its sufficient source S_fact embeds continuously in S_Gamma. That inclusion is strict even inside the reconstructed relation ideal, as the next section proves.

These are coefficient-domain bounds for the fixed actual event forcings. They are not a lower bound for the Clark transform on arbitrary H_beta tensors. In particular they do not recover unweighted path coefficients stably when gamma_e is small.

## 5. A genuine retained-source witness outside S_fact

The global theta forcing on the admitted half-line has finite H_beta norm. Therefore

    ||1_[L,infinity) Phi||_beta -> 0 as L->infinity.

For each n>=2 choose a starting arithmetic vertex far enough out that every event forcing in the chosen n-event interval satisfies

    sqrt(w_seam) ||f_e||_beta <= 2^(-n).

Such vertices exist by the tail bound and unbounded prime labels. Choose distinct endpoint corners. Subsequent monotone event windows stay in that tail.

Let v_n be the local mixed-mark diamond relation

    (p,1)(q,0)+(p,0)(q,1)
      -(q,1)(p,0)-(q,0)(p,1),

followed by a fixed all-retained suffix to total length n. It belongs to I by interval additivity. Its four path coefficients have modulus one, and every path has exactly n-1 retained letters.

Define

    x=sum_(n>=2) v_n/(4 n!).

Its corner path norm is 1/n!. Consequently every old common-path seminorm converges:

    sum_(n>=2) (1+n)^p (b a)^n/n! < infinity.

Closedness of the record kernel places x in the reconstructed source ideal.

But its unweighted factorial seminorm is

    q_R(x)=sum_(n>=2) (R A)^n=infinity,

for the admitted R,A>=1. It is not in S_fact.

In contrast,

    Q_R(x) <= sum_(n>=2) R^n 2^(-n(n-1)) < infinity

for every R. The ratio of successive majorants is R/4^n. Thus the full forcing-resolved jet is summable at every prescribed depth/feature radius.

The four routes/mark patterns remain distinguishable in the top jet. This is an actual retained-forcing attenuation example, not cancellation of the full observation and not a hypothetical choice of vanishing features.

## 6. Operations and currents on the domain

The actual-letter weights are multiplicative under path concatenation. The factorial inequality gives

    Q_R(xy) <= Q_(2R)(x) Q_(2R)(y).

Hence S_Gamma is a complete locally convex coefficient algebra. On its intersection with S_common, retain both families of source seminorms. The Fox convolution law extends by the same absolute-summability argument used in Nima's factorial construction. The zero-seam sector is retained for the full algebra; it vanishes on I.

The existing separately bounded bulk, forcing, and vacuum-incidence currents pull back along D, with their existing shape matching, spectral indices, and compact-interior restrictions. No new cross-degree pairing is introduced.

There is also a jet-order tail bound. If M>=2 lambda s b and L>1, then

    ||sum_(k>N) D_k(x)||_F(s,b)
       <= 2 L^(-(N+1)) Q_(ceil(L M))(x).

Only source lengths n>N contribute, so the proof is the same exponential-radius comparison as before, now with Gamma(w) retained throughout.

## 7. Boundaries

- This characterizes the FORCING-resolved summed map with its fixed actual letters. The analytical output-only domain need not agree with it; Clark transfer gives a continuous forward comparison, not an inverse forcing estimate.
- Unweighted factorial control remains necessary on the forgotten sector and sufficient globally, but is not necessary on general retained source relations.
- The bounds do not transfer the old unweighted Fox factorization estimates to arbitrary Gamma-weighted presentation norms. Those norms have a new within-corner weighting and require their own comparison if used for filtered presentations.
- The formerly open uniform theta substitution gate is now closed by Voevodsky's `relative-theta-tail-control-preserves-the-actual-letter-fox-domain.md`: its relative forcing bound preserves this domain and gives full-jet operator convergence with radius loss. This is not an inverse analytical estimate. The subsequent `actual-letter-normalization-does-not-remove-the-observer-dual-obstruction.md` proves that joint analytical observer pullback remains nonsurjective, even on the inherited actual-letter quotient.
- Root states stay external. No independent prepared states are multiplied or copied.

## Verification

`python research/grothendieck/checkers/check_marked_fox_summability_domain.py`

Passed 1456 exact all-order majorants, 4282 distinct typed top-jet probes, 40 projection/radius checks, and 124 marked-relation weight checks. The existence of the actual late-window witness follows from H_beta integrability, not from choosing numerical Clark samples.

References:

- `research/nima/factorial-path-scales-sum-the-full-fox-jet-family.md`;
- `research/voevodsky/factorial-fox-summability-has-a-vacuum-necessity-test-and-compatible-filtered-exactness.md`;
- `research/voevodsky/the-bounded-filtered-limit-recovers-the-source-and-its-faithful-fox-jets.md`;
- `research/voevodsky/bulk-and-forcing-currents-converge-separately-on-the-forcing-resolved-completion.md`.
