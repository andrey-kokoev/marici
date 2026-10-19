# One-dimensional selection: pointed axis succeeds, unmarked full-heat sum does not

Definition: `research/conjecture_net/contracts/marked-channel-selection.v1.json`.
Checker: `research/voevodsky/checkers/check_marked_channel_selection.py`.
Receipt: `research/voevodsky/results/marked-channel-selection-v1.json`.

## Scoped result and source change

There is a concrete one-dimensional selection for the explicitly **pointed universal channel-lattice source** (L_n,j), with L_n=Z^{D_n} and a supplied diagonal occurrence j. This is NOT a canonical selection from the unmarked geometric source, nor a physical preparation. The mark and domain restriction are additional declared inputs, not a hidden normalization fitted to zeta.

Two candidate nodes preserve this distinction: `symmetric-full-heat-selection` is rejected; its explicit successor `marked-axis-source-selection` is constructed at the pointed/axis scope. The enclosing `one-dimensional-source-selection` review accepts this conditional selection policy, not the rejected unmarked quotient or a forced native choice. Channel/carrier binding and physical continuation comparison still need to use exactly the same mark and admitted domain.

## What the existing source actually supplies

Nima's canonical construction has a basis for every polygon diagonal and maps a triangulation T to delta_{v_T}, v_T=sum_{d in T} e_d. The universal lattice and its local reciprocal relabelling-invariant regulator Q(n)=sum n_d^2 are supplied mathematical carriers. Neither source selects a distinguished diagonal. Prior hydration expressly removed an unsupported selected rank-four channel orbit; it must not be reinstated implicitly.

A fixed axis cannot be selected equivariantly under unmarked channel permutations when D>=2: a permutation moving that axis contradicts invariance. We instead supply a mark j and transport it with the source. The rule is a covariant family of pointed objects, not an invariant preferred channel.

This domain distinction matters for the actual geometric packets: a triangulation of an n-gon has n-3 distinct diagonal entries. For n>=5 its incidence atom lies off EVERY single axis, so the axis restriction below reads it as zero. Its full source record survives. The construction therefore does not turn every original Catalan basis atom into the zeta seed. At n=4 a single marked diagonal is a genuine axis atom. General axis multiples and negative integers belong to the declared universal lattice completion, not an assertion about a primitive triangulation or laboratory preparation.

## Actual selection, reconstruction and licensed operations

Define E_j b on L by extending b on Z by zero outside the axis; R_j c(k)=c(k e_j). Then R_j E_j=I and

    c=E_j R_j c+N_j c, N_j=I-E_j R_j.

On l2 these are the orthogonal axis projection and its retained complement, both continuous. On finite packet algebra the axis image is a convolution subalgebra. On the whole source, R_j does NOT preserve arbitrary binary convolution: for k!=j, both delta_{e_k} and delta_{-e_k} read zero, but their product is delta_0 and reads one.

The allowed task operations are axis shifts, character multipliers, convolution with an axis packet, diagonal local heat, dyadic bonding and relabelling WITH the mark. Each preserves the selection kernel and transports its action. In particular convolution by an axis packet a satisfies R_j(E_j a*c)=a*R_j c. Off-axis translations or unreviewed archival restoration are not licensed by the coarse reader. Keeping their data does not make those operations descend.

For a permutation sigma,

    R_{sigma(j)} sigma_* = R_j.

Holding j fixed restricts symmetry to its stabilizer. The checker retains a permutation hostile showing what fails when the mark is frozen instead of transported.

## Fourier, mesh and heat are compatible at this scope

On finite characters,

    F_D(E_j b)(theta)=F_1 b(theta_j).

The source embedding is an l2 isometry, and the character-side map g(theta_j) is an L2(T^D) isometry with normalized transverse Haar measure. Hence this square extends by Fourier-Plancherel; it is not pointwise restriction of an arbitrary L2 torus function to a measure-zero subtorus.

At mesh h, the real atom embedding is T -> T tensor delta_0 on transverse coordinates. Its Fourier image is F_1 T tensor 1. Thus the four ambient real Fourier charts alternate transverse delta_0 and constant 1. Applying F_D twice returns reflection and the original transverse delta port. The axis comb is NOT self-Fourier as a D-dimensional distribution when D>1.

Dyadic bonding n->2n commutes with R_j and E_j, and h->h/2 leaves physical atom positions unchanged. Q(k e_j)=k^2 gives exactly the restricted source heat coefficients exp(-pi t h^2 k^2) under the already declared heat-time convention. No new source form or rescaling of the full multichannel energy is inserted. On other directions Q is retained, not pulled back through the selection.

At h=1 the unit axis comb paired with exp(-pi t ||x||^2) gives theta_1(t). In the odd Fourier chart the transverse constant contributes t^{-(D-1)/2}; combined with the D-dimensional Fourier-Gaussian factor, it yields the one-dimensional reciprocity exponent -D/2+(D-1)/2=-1/2. The existing zero-atom/constant boundary pair, Gaussian Mellin completion, pole packet and xi endpoint constant then apply to the SELECTED one-dimensional target. They are not a claim of D-dimensional axis-comb self-sewing. The unit comb/Gaussian/measure remain declared inputs, consistent with the bounded package's scalar c normalization policy.

## Retained exclusion: the symmetric coordinate-sum quotient

Sigma(n)=sum n_d is permutation-invariant, additive, and commutes with dyadic bonding. On finitely supported packet algebra, pushforward along Sigma preserves convolution and is dual to restriction of finite characters to the diagonal torus. These are genuine positive properties, not grounds for discarding it without review.

But for D>=2 the vector e_1-e_2 maps to zero while Q(e_1-e_2)=2 and Q(0)=0. Thus the independently specified source quadratic heat is not a function of Sigma(n). No heat-semigroup intertwining through the pushforward exists on the whole packet domain. On triangulations Sigma(v_T)=n-3, so it also forgets the entire diagonal pattern at a fixed degree.

The coefficient pushforward is not bounded l2(L)->l2(Z): a packet equal to one on M distinct points of the sum-zero fibre has source squared norm M and image squared norm M^2, giving norm ratio sqrt(M). The full unweighted D-dimensional comb has infinite mass at every sum fibre; its pushforward is not the ordinary one-dimensional comb. Formal Poisson summation in one variable cannot fix that failure.

A weighted Gaussian fibre integral, conditional expectation, altered regulator or narrowed source could define a different candidate, but those are new choices requiring their own source/domain/normalization review. None is silently used here.

## Verification and remaining work

Exact finite tests cover D=2,3,20,54 (the last two are the diagonal counts for n=8,12), convolution and its hostile, reconstruction, rational Fourier phases, mark covariance, heat restriction and four nested scales. Unbounded-fibre examples and the transverse Gaussian exponent are regression controls; the infinite Fourier/continuity and theta claims rest on the above mathematical arguments and the existing analytic completion witness.

The rejected symmetric candidate is retained with its counterexample. The pointed successor does not close `channel-carrier-source-map`, Weil-form repair or physical selection. For downstream same-source work the mark, axis-domain policy and retained complement are mandatory comparison parameters; a route requiring the full geometric incidence or a different mark cannot use this witness without a new binding review. No RH truth, positive Weil pullback or laboratory realization is claimed.
