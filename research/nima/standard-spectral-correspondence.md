# Standard-real interpretation of the operational spectral whole return

## Claim and verification boundary

Let C be the existing `MetricCompletionCandidate`. Use the canonical interpretation
`rho([x]) = lim_n i_Q(approximation x n)` from `standard-pi-identification.md`, and its componentwise complex extension rho_C. The operational witness constructed in `TickOperationalWholeReturnKernel.agda` interprets as the particular standard spectral witness in `uniform-local-core-proof.md` and `spectral-whole-return-proof.md`.

The semantic argument here is written ordinary classical mathematics, **not an Agda theorem about an imported classical-real type**. The operational algebra, dynamics, metric interval/path, and retained-record laws are independently safe Agda theorems. This new written correspondence is separate from the previously operator-accepted standard-pi identification. It needs its own explicit acceptance if used to close the target at a mixed verification level. A consumer requiring kernel semantic correspondence must keep that formalization obligation open.

## 1. Canonical interpretation is a bijection and preserves algebra

A regular rational sequence has `|x_m-x_n| <= 2^-m+2^-n`, so it has a unique real limit. The actual equivalence relation identifies sequences whose eventual differences are at most every dyadic precision. Taking limits proves rho is well-defined; conversely, equal limits imply eventual differences smaller than each precision. Thus rho is injective. These facts were already proved in section 1 of `standard-pi-identification.md`.

For every ordinary real r choose rational q_n with `|q_n-r| < 2^-(n+2)`. Then `|q_m-q_n| < 2^-(m+2)+2^-(n+2) <= 2^-m+2^-n`. Hence q is regular and rho([q])=r. This proves surjectivity in classical real mathematics. The resulting inverse is unique by injectivity; neither rho nor its inverse depends on which approximations witness existence. This is a semantic completeness argument, not a new operational scalar backend.

The actual addition uses samples `x_(n+1)+y_(n+1)`, and negation uses `-x_n`; their limits are respectively rho(x)+rho(y) and -rho(x). Constants interpret as their rational values.

Operational multiplication is the quotient of the bounded scheduled rational product. Its samples are products of samples of the two original representatives at input depths tending to infinity. The canonical product input depth is above the output depth; thus both factors converge to their original real limits. Continuity of real multiplication gives rho(x*y)=rho(x)rho(y), independently of the selected bound or schedule. This also follows from the checked rational-approximant convergence, rational multiplication preservation and moving-product convergence theorem: apply the sound convergence interface from section 2 of the pi proof to the product sequence. Therefore rho is a unital ring isomorphism. Its componentwise extension preserves the implemented complex addition, multiplication, conjugation and squared modulus.

## 2. Actual completion balls and the closed order

If `CompletionWithin(a,b,k)` holds, its existential representatives are eventually at distance at most 2^-k. Taking limits gives `|rho(a)-rho(b)| <= 2^-k`. This is soundness, not an assumption that a fixed-radius representative predicate descends.

Conversely, if `|rho(a)-rho(b)| < 2^-k`, let the positive difference between the radius and this distance be delta. Any representatives converge to their limits, so eventually the sum of their two approximation errors is smaller than delta. Their eventual difference is then at most 2^-k, supplying a witness for the actual `CompletionWithin`. **No converse at equality of distance and radius is needed or claimed.** These two implications prove that rho and its inverse are continuous for the usual metric topology.

`CompletionNonnegative(a)` says that at every k some representative is eventually bounded below by -2^-k. Its real limit is therefore nonnegative. Conversely, if rho(a)>=0, each chosen representative eventually differs from rho(a) by less than 2^-k, hence is bounded below by -2^-k. It supplies the required witness at every precision. Thus the cone agrees exactly with ordinary real nonnegativity. By algebra preservation,

`CompletionLE(a,b) iff rho(a)<=rho(b)`.

The implemented strict order in `TickSpectralOpenPieces` is a truncated witness k with `a+embed(2^-k)<=b`. Its interpretation implies rho(a)<rho(b), since 2^-k is strictly positive. Conversely, if rho(a)<rho(b), choose k with 2^-k <= rho(b)-rho(a) and use closed-order reflection. Consequently this strict order agrees exactly with ordinary real strict order.

The completion subtypes `UnitInterval`, `ReturnInterval`, `FirstOpenPiece`, and `SecondOpenPiece` therefore interpret bijectively as [0,1], [0,2], (0,1), and (1,2), respectively. Their order proofs are propositional, so they create no extra points. Their inherited balls give the standard interval subspace topology by the preceding strict-radius argument.

## 3. Metric continuity and derivative certificates are semantically sound

For a complex-valued operational curve f, define its ordinary complex interpretation
`F(r)=rho_C(f(rho^-1(r)))`.

The actual continuity certificate says that at each center and output dyadic precision k, some input depth l controls both output components whenever the input is in the completion ball of depth l. If `|r-s| < 2^-l`, section 2 supplies that ball. Its output components differ by at most 2^-k, hence the complex distance is at most sqrt(2)*2^-k. Choosing k arbitrarily large proves ordinary continuity. This argument uses the actual local modulus, not topology of Agda path equality.

Suppose `HasMetricDerivative f t v`. At precision k its witness l controls every completion increment h in the ball about zero, with

`normSquared(f(t+h)-f(t)-scaleComplex(h,v)) <= 2^(-2k) * h^2`.

Interpret algebra and closed order using sections 1–2. For every real increment eta with `|eta| < 2^-l`, take its unique completion preimage h. The strict-radius ball implication applies. If eta is nonzero, the interpreted inequality gives

`|(F(r+eta)-F(r))/eta - rho_C(v)| <= 2^-k`,

where r=rho(t). For any positive error tolerance choose k with 2^-k below it. This is precisely the ordinary derivative F'(r)=rho_C(v). No division by a completion increment occurs internally; division is only in this ordinary-real consequence at nonzero eta. At eta=0 the checked bound remains valid and is not used to divide. For finite vectors the same argument applies componentwise using the single checked vector modulus.

This also validates the checked derivative certificates on strict subintervals, because section 2 identifies their domains with the ordinary open intervals. It makes no derivative claim at the switching time.

## 4. All-time operational phase equals the standard exponential

For a fixed completion scale p let `Z_p(r)=rho_C(phase p (rho^-1(r)))` and let alpha=rho(p). The checked phase-start theorem gives Z_p(0)=1. The full operational phase derivative certificate, interpreted by section 3 and algebra preservation, gives at every real r

`Z_p'(r)=(-i*alpha) Z_p(r)`.

Define `W(r)=exp(i*alpha*r) Z_p(r)`. The ordinary complex product rule and derivative of the standard exponential yield W'(r)=0. Apply the real mean-value theorem separately to the real and imaginary parts on any finite real interval: W is constant. Since W(0)=1,

`Z_p(r)=exp(-i*alpha*r)` for every real r.

This is an all-time identification, not endpoint matching, a norm-based guess, or a sampled calculation. It invokes ordinary real calculus at the reference witness's written-proof level. The checked phase derivative is the operational premise; the interpretation soundness needed to use it is established above.

The accepted pi identification gives rho(machinPi)=standard pi. Hence the **same** implemented phase at machinPi interprets as `exp(-i*pi*r)`, with the sign used by the exported witness.

## 5. Native free linearization, local matrices and factor laws

Vectors in the implementation are functions on Bool×Bool with `ComplexCompletion` entries. Interpret them componentwise. The operational delta basis is sent exactly to the orthonormal standard delta basis, and the checked native basis-action theorems identify the coordinate flips with `P_L=X tensor I` and `P_R=I tensor X`. Thus these are the source-linearized native maps, not unrelated matrices chosen to have the same endpoints.

`TickSpectralWitnessCorrespondence` proves the exact coefficient matrices and Hamiltonian matrices. Algebra preservation and section 4 interpret them as

`Q_j=(I-P_j)/2`, `H_j=pi Q_j`, `U_j(r)=(I-Q_j)+exp(-i*pi*r) Q_j`.

The conjugate-transpose theorem identifies the implemented inverse matrix with the usual local adjoint matrix; the Hamiltonian is self-adjoint. The operational factor lifts are the usual 2x2 matrix actions on one coordinate while leaving the other coordinate fixed. Every ordinary complex factor matrix has an operational preimage by section 1. Therefore the checked arbitrary-factor laws imply all the exported factor-algebra conjugation/preservation laws, not only laws on pure tensors or rational matrix fixtures. The two local legs commute at every ordinary real time.

Likewise the checked reindexing naturality gives covariance for any relabeling with the intertwining equation. The explicit identity/flip family contains both permutations of each Bool factor: a bijection sending false to false must send true to true, and one sending false to true must send true to false. This is a finite two-case mathematical argument, not an assumption of arbitrary completion decidability. The factor-exchange theorems identify the exchanged operators, source and schedule.

## 6. Global return is the exported positive reversed schedule

For forward schedule r let (a,b) be its reversed native operations, and let `v=P_R P_L e_s`. The actual global formula is

`U_b(secondTime(t)) U_a(firstTime(t)) v`,

where `secondTime(t)=positiveCompletion(t-1)` and `firstTime(t)=t-secondTime(t)`.

The positive-part operation is rational nonexpansive and quotient-descended. Its rational values are max(0,q); continuity and rational density imply its standard interpretation is max(0,r). Thus on [0,2] the time coordinates are max(0,t-1) and min(t,1). Alternatively, the checked restriction formulas give the following equalities directly on each of the ordinary real closed pieces, whose union covers [0,2]:

- for 0<=t<=1, gamma_(r,s)(t)=U_a(t)v;
- for 1<=t<=2, gamma_(r,s)(t)=U_b(t-1)P_a v.

These are exactly the exported formulas, including **positive** phase continuation rather than inverse-phase time reversal. The seam agrees in both formulas. The checked global continuity, endpoints, unit norm and open-piece Hamiltonian derivatives interpret as the reference witness's corresponding claims. No C1 claim at the seam is introduced.

## 7. Entire retained records and faithful correspondence

The interpreted pair of source-bound return paths is obtained from the full retained Tick's ordered tags, using the exact operational interpretation already defined in `TickSpectralRetainedReturn`. Its full-record reconstruction and schedule-swap equalities are kernel theorems and remain equalities under interpretation.

At the seam the two schedules give the distinct delta vectors `e_(leftIndex s)` and `e_(rightIndex s)`. They stay distinct under the injective component interpretation. Equality of ordinary interpreted paths therefore forces equality of schedule tags; equality of path pairs forces equality of both tags. The checked full retained-record tags-injectivity theorem then gives equality of entire Ticks. Thus fixed-source faithfulness survives interpretation; it is not weakened to a one-way coherence statement.

## Conclusion and admission policy

Sections 1–7 identify the assembled operational witness with the **pinned exported standard spectral witness**, at the ordinary classical mathematical level used by that export. Operational certificates remain safe Agda evidence; the canonical interpretation, ordinary completeness/calculus and this semantic identification remain written evidence.

The final scientific target is **not automatically promoted by this document**. The verifier must bind this proof and its prerequisites, validate the imported export, and distinguish written semantic correspondence from kernel correspondence. Closing at this additional mixed level requires explicit operator acceptance; otherwise the remaining gate is kernel formalization of the standard-real interpretation and its soundness. The existing acceptance of pi identification alone is insufficient.
