# Marici Rzk lane

## Scope

This lane formalizes the simplicial categorical shell parallel to, but not
identified with, the Cubical Agda pasting complex. Arithmetic and analytic
semantics require separate derived interpretation maps.

## Current checked increment

`src/01-marici-simplicial-pasting.rzk.md` defines:

- canonical composition in a Segal type;
- its retained two-simplex witness;
- left- and right-associated composites of three arrows;
- associativity derived from the sHoTT three-dimensional filling theorem;
- the corresponding Rezk-type entry point.

`src/02-marici-simplicial-interpretation.rzk.md` defines pointwise action on directed arrows and two-simplex witnesses, then derives preservation of canonical composition from target Segal uniqueness. This is the comparison cell prior to an additive interpretation.

`src/03-marici-nat.rzk.md` begins the independent arithmetic lane with a recursive natural-number type, addition, multiplication, additive zero laws, successor compatibility, commutativity, and closed computation tests.

`src/04-marici-nat-laws.rzk.md` derives additive associativity, both multiplicative zero and unit laws, and left distributivity.

`src/05-marici-nat-semiring.rzk.md` derives prefix interchange, multiplication by a right successor, multiplicative commutativity and associativity, and right distributivity. Together the Nat files now establish the equational commutative-semiring laws.

`src/06-marici-nat-order-subtraction.rzk.md` supplies executable trichotomy data and simultaneous-recursion truncated subtraction. Order laws, cancellation, and sethood remain open.

`src/07-marici-int-normal-form.rzk.md` introduces the quotient-free signed normal form with unique constructor-level zero, natural embedding, involutive negation, comparison-driven addition, and four mixed-sign normalization checks.

`src/08-marici-int-multiplication.rzk.md` derives predecessor multiplication from `(a+1)(b+1)`, defines all sign cases, proves both zero and unit laws, and checks three signed products.

`src/09-marici-int-basic-laws.rzk.md` proves symmetry of the positive-product predecessor, integer multiplication commutativity, both additive inverse laws, and both additive zero laws.

`src/10-marici-int-add-comm.rzk.md` proves integer addition commutativity. The mixed-sign implementation was reduced to one canonical positive-plus-negative normalizer; the opposite order delegates with exchanged magnitudes, so mixed-sign commutativity is definitional rather than dependent on a second comparison proof.

`src/11-marici-nat-int-embedding.rzk.md` proves that the constructor-derived natural embedding preserves zero, one, addition, and multiplication. This is the first checked arithmetic interpretation map between independently defined carriers.

`src/12-marici-comm-semiring-interface.rzk.md` packages carrier-parametric commutative-semiring equations and operation-preserving-map equations, instantiates the former for `MariciNat`, and packages the natural-to-integer map laws. Sethood remains deliberately separate, and the integer carrier is not yet packaged as a ring.

`src/13-marici-int-sign-laws.rzk.md` proves multiplication compatibility with negation in each argument and both arguments, then derives left and right multiplication by negative one from those paths and the unit laws.

`src/14-marici-semiring-map-composition.rzk.md` proves identity and composition closure for operation-preserving maps and checks the generic constructor on the natural-to-integer map followed by the integer identity.

`src/15-marici-simplicial-map-functoriality.rzk.md` connects that ordinary-map identity/composition to pointwise action on directed arrows and retained two-simplex fillers. Both identity and composition laws compute on arrows and fillers.

`src/16-marici-discrete-arithmetic-bridge.rzk.md` identifies the exact realization premise: `is-discrete`, not merely `is-set`. Conditional on discreteness witnesses, it derives Segal and Rezk structures for both arithmetic carriers and proves that the natural-to-integer map preserves canonical directed composition. The file tracks its `ExtExt` assumption explicitly.

`src/17-marici-int-mul-assoc.rzk.md` relates the predecessor encoding to multiplication of successor magnitudes, derives associativity of the encoded positive product from natural multiplication associativity, and proves signed integer multiplication associativity by complete constructor analysis.

`src/18-marici-raw-fractions.rzk.md` opens the rational branch as explicitly raw positive-denominator syntax. It defines negation, cross-multiplied addition, multiplication, and the intended cross-product relation. The checked one-half-plus-one-half example remains four-fourths at constructor level and is only related to one-first through the relation, preventing a silent quotient claim.

`src/19-marici-raw-fraction-relation-laws.rzk.md` proves relation reflexivity and symmetry, involutivity of raw negation, and preservation of the relation by negation. Transitivity stops at the first missing typed theorem: cancellation of a shared positive integer factor. Addition/multiplication congruence also waits for integer distributivity.

`src/20-marici-raw-fraction-mul-laws.rzk.md` proves raw-constructor multiplication commutativity and associativity by combining the checked integer numerator laws with the positive-denominator predecessor laws. These do not promote to quotient multiplication laws without congruence.

`src/21-marici-raw-fraction-units.rzk.md` proves strict left and right multiplicative-unit laws for raw fractions and exposes the normalization gap through the family of related zero representatives at every positive denominator. Raw syntax does not identify those constructors.

`src/22-marici-raw-fraction-zero-laws.rzk.md` proves that every denominator-indexed raw zero is fixed by negation and that left and right multiplication by the chosen zero are annihilating through cross-product equivalence. These cannot be strengthened to raw constructor equality because multiplication retains denominators.

`src/23-marici-raw-fraction-mul-congruence.rzk.md` proves a four-factor interchange law and uses it to establish that raw multiplication preserves cross-product equivalence in both inputs. Thus multiplication is ready to descend once a quotient or equivalent normalization interface exists.

`src/24-marici-raw-fraction-transitivity-if-cancellative.rzk.md` defines the exact positive-factor right-cancellation premise and derives relation transitivity from it via a checked three-factor interchange chain. This does not assume arbitrary integral-domain structure.

`src/25-marici-raw-fraction-descent-interface.rzk.md` packages reflexivity, symmetry, conditional transitivity, and multiplication congruence as the multiplicative descent interface available from positive cancellation. It supplies neither a quotient nor normalization.

`src/26-marici-raw-fraction-add-basic-laws.rzk.md` proves raw addition commutativity and strict left/right zero-unit laws. These use only checked integer commutativity and unit laws; associativity and relation congruence remain downstream of the missing integer additive and distributive laws.

`src/27-marici-raw-fraction-additive-inverses.rzk.md` proves both additive-inverse laws through cross-product equivalence. The raw sums retain squared denominators, so constructor equality with the chosen zero is not asserted.

`src/28-marici-raw-fraction-mul-negation.rzk.md` proves strict constructor-level compatibility of multiplication with left, right, and simultaneous negation by transporting the checked integer numerator laws.

`src/29-marici-raw-fraction-positive-scaling.rzk.md` proves that the positive-denominator embedding preserves denominator products, defines common positive scaling of numerator and denominator, and shows that every such scaling is cross-product equivalent to its source. This is only the forward scaling direction; common-factor selection, removal, and uniqueness remain absent.

`src/30-marici-raw-fraction-scaling-coherence.rzk.md` proves that positive scaling has a strict unit and that iterated scaling agrees strictly with scaling by the positive-factor product. This is coherent forward action, not an inverse normalization action.

`src/31-marici-int-nonnegative-ring-laws.rzk.md` resumes the integer ring interface and proves addition associativity and left distributivity for every triple in the unbounded image of the natural embedding. The proofs transport the checked natural semiring laws through the embedding; they are not finite samples.

`src/32-marici-int-nonnegative-right-distrib.rzk.md` derives right distributivity on the same full nonnegative image from checked left distributivity and global integer multiplication commutativity.

`src/33-marici-int-nonpositive-add-assoc.rzk.md` proves that negation of the natural embedding preserves addition into the nonpositive image, then transports natural associativity to every nonpositive triple. Integer addition associativity now holds on both sign-homogeneous images.

`src/34-marici-int-negative-times-nonnegative-distrib.rzk.md` proves compatibility of a negated embedded factor with multiplication, then derives left distributivity for every nonpositive multiplier and nonnegative pair of addends.

`src/35-marici-int-embedded-mul-sign-coherence.rzk.md` proves the corresponding right-negated embedding law and equality of the two placements of a single minus sign in products of embedded naturals.

`src/36-marici-int-nonnegative-times-negative-distrib.rzk.md` proves left distributivity for every nonnegative multiplier over two nonpositive addends.

`src/37-marici-int-negative-times-negative-distrib.rzk.md` closes the remaining homogeneous-sign family by proving left distributivity for every nonpositive multiplier over two nonpositive addends.

`src/38-marici-int-homogeneous-right-distrib.rzk.md` gives a generic commutativity transport from left to right distributivity and instantiates the three remaining homogeneous-sign right-distributive families. Both orientations now hold for either multiplier sign when the addends share a sign.

`src/39-marici-int-inverse-pair-distrib.rzk.md` enters the opposite-sign frontier by proving both distributive orientations for every arbitrary integer multiplier over an exact inverse pair.

`src/40-marici-int-reversed-inverse-pair-distrib.rzk.md` proves both orientations for the reversed inverse-pair ordering via the left-inverse law. Both equal-magnitude opposite-sign orders are now covered.

`src/41-marici-int-arbitrary-multiplier-homogeneous-distrib.rzk.md` consolidates the four multiplier-sign cases by constructor analysis, giving both distributive orientations for arbitrary normalized multipliers and either homogeneous addend image.

`src/42-marici-int-global-distrib-branch-reduction.rzk.md` defines the remaining positive-negative and negative-positive left-distributive interfaces and proves that they suffice for global left and right distributivity.

`src/43-marici-int-single-mixed-distrib-reduction.rzk.md` uses integer addition commutativity to derive the negative-positive interface from the positive-negative one, then derives both global distributive orientations from that single family. Equal magnitudes are already checked.

`src/44-marici-int-adjacent-magnitude-normalization.rzk.md` proves comparison and mixed-sign addition normalization for every adjacent positive-magnitude pair in both orders: equal recursive prefixes reduce to positive or negative one.

`src/45-marici-int-common-prefix-normalization.rzk.md` proves that comparison and both mixed-sign normalizers are invariant under any common natural prefix, including their integer-constructor forms.

`src/46-marici-int-residual-mixed-normalization.rzk.md` proves all four residual mixed-sign normalization laws when one predecessor magnitude is zero. The result is the natural embedding of the residual magnitude or its negation.

`src/47-marici-nat-subtraction-cancellation.rzk.md` proves cancellation of either summand from a supplied natural additive decomposition and cancellation of one copy from multiplication by a successor factor. These are source-decomposition theorems, not arbitrary subtraction or order reflection.

`src/48-marici-nat-mul-subtraction.rzk.md` proves common-prefix removal for truncated subtraction and that natural multiplication preserves truncated subtraction in its right argument. This supplies scaled residual arithmetic without asserting order reflection or factor cancellation.

`src/49-marici-nat-subtraction-bimodule-law.rzk.md` transports the result through natural multiplication commutativity, proving preservation of truncated subtraction in the left multiplication orientation as well.

`src/50-marici-nat-positive-scale-comparison.rzk.md` proves structurally that multiplication by every successor factor preserves three-way natural comparison. The proof uses successor multiplication, common-prefix comparison invariance, and recursive descent; it assumes no order object.

`src/51-marici-positive-product-compare.rzk.md` transports that theorem to the predecessor encoding used by products of normalized positive integers. Scaled mixed products therefore select the same comparison branch as their source magnitudes.

`src/52-marici-positive-product-successor.rzk.md` proves both successor recurrences for the positive-product predecessor: increasing either positive factor adds one full copy of the other factor.

`src/53-marici-positive-product-residual-base.rzk.md` proves the scaled subtraction residual theorem when the smaller source predecessor is zero, uniformly over every positive scaling factor and residual.

`src/54-marici-positive-product-residual.rzk.md` completes the induction over the smaller predecessor. Given an explicit strictly-greater decomposition, scaled predecessor subtraction returns exactly the positive-product predecessor of the residual. Together with module 51, positive scaling preserves both the comparison branch and its normalized residual.

`src/55-marici-nat-explicit-gap-comparison.rzk.md` proves that a smaller magnitude plus one separating successor and an arbitrary residual compares strictly greater, and that the reversed comparison is strictly less.

`src/56-marici-scaled-mixed-gap-normalization.rzk.md` assembles modules 51, 54, and 55 for the positive-result branch: after positive scaling, an explicit positive-over-negative gap normalizes to the positive-product predecessor of the source residual.

`src/57-marici-scaled-mixed-negative-gap-normalization.rzk.md` proves the exchanged negative-result branch. Both strict mixed-sign branches now normalize compatibly with positive scaling.

`src/58-marici-positive-factor-equal-mixed-distrib.rzk.md` proves the equal-magnitude mixed distributive branch for every positive multiplier by cancellation to zero on both sides.

`src/59-marici-mixed-gap-normalization.rzk.md` proves that an explicit positive-over-negative source gap normalizes directly to its residual.

`src/60-marici-positive-factor-strict-mixed-distrib.rzk.md` proves the reversed source normalization and assembles positive-factor distributivity for both strict mixed-sign branches with explicit residual decompositions. Together with module 58, all three comparison branches are proved in decomposition form.

`src/61-marici-positive-factor-mixed-successor-step.rzk.md` proves the common-successor recursion step for positive-factor mixed distributivity. It removes one common source successor and, after multiplication, one common positive-factor prefix.

`src/62-marici-positive-factor-mixed-distrib.rzk.md` combines that step with the equal and strict zero-edge bases by simultaneous structural recursion. The positive-plus-negative family now distributes for every positive multiplier and arbitrary predecessor magnitudes.

`src/63-marici-zero-factor-mixed-distrib.rzk.md` proves the unrestricted mixed family for the zero multiplier by constructor computation.

`src/64-marici-negative-factor-positive-gap-distrib.rzk.md` proves the positive-residual strict branch for every negative multiplier. Source normalization exposes the residual; product-side addition commutativity exposes module 57's scaled negative-gap normal form.

`src/65-marici-negative-factor-mixed-base-branches.rzk.md` proves the negative-residual strict branch and the equal-magnitude branch for every negative multiplier. All negative-factor zero-edge/equal bases now hold.

`src/66-marici-negative-product-common-successor.rzk.md` proves the product-side common-successor reduction for negative multipliers. Positive-product successor recurrences expose a common positive-factor prefix in the opposed product magnitudes, and reversed mixed normalization removes it.

`src/67-marici-negative-factor-mixed-successor-step.rzk.md` composes that reduction with source common-prefix normalization and the induction hypothesis.

`src/68-marici-negative-factor-mixed-distrib.rzk.md` combines the recursive step with all negative-factor zero-edge bases by simultaneous structural recursion. The positive-plus-negative family now distributes for every negative multiplier and arbitrary predecessor magnitudes.

`src/69-marici-all-factor-mixed-distrib.rzk.md` performs the multiplier constructor split, assembling modules 62, 63, and 68 into the single positive-plus-negative family required by module 43.

`src/70-marici-int-global-distributivity.rzk.md` supplies that family to module 43's reductions. Integer multiplication now distributes over integer addition in both orientations for arbitrary canonical integers.

`src/71-marici-nat-successor-prefix-injectivity.rzk.md` proves successor injectivity by applying predecessor and proves injectivity of adding an arbitrary common natural prefix by induction.

`src/72-marici-nat-zero-successor-disjoint.rzk.md` defines local empty and singleton types, a natural discriminator family, and empty-valued maps from both zero--successor path orientations.

`src/73-marici-nat-positive-factor-cancellation.rzk.md` combines that constructor disjointness with successor and additive-prefix injectivity to prove that left multiplication by every successor natural is injective.

`src/74-marici-nat-positive-factor-right-cancellation.rzk.md` transports this result through natural multiplication commutativity, proving injectivity in the right multiplication orientation.

`src/75-marici-int-constructor-no-confusion.rzk.md` proves injectivity of the positive and negative constructor payloads and pairwise disjointness of zero, positive, and negative integer constructors via type-valued discriminators.

`src/76-marici-positive-product-predecessor-injective.rzk.md` proves injectivity of the positive-product predecessor in either payload when the other positive factor is fixed. Successor transport exposes full natural products, module 73 cancels the factor, and successor injectivity recovers the payloads.

`src/77-marici-int-positive-factor-cancellation.rzk.md` lifts this result through all canonical integer constructor pairs. Equal-sign cases cancel predecessor products; mixed-sign and zero cases are eliminated by module 75's no-confusion maps. Left multiplication by every positive canonical integer is injective.

`src/78-marici-int-positive-factor-right-cancellation.rzk.md` transports the theorem through integer multiplication commutativity. Multiplication by every positive canonical integer is now injective in both orientations.

`src/79-marici-int-mul-swap-right-factors.rzk.md` derives the triple-product coherence path that exchanges two right factors using integer multiplication associativity and commutativity.

`src/80-marici-raw-fraction-relation-transitive.rzk.md` completes raw-fraction relation transitivity. The two supplied cross-product paths are multiplied by the remaining denominators, reordered to align the shared positive middle denominator, and cancelled with module 78. The raw relation is now reflexive, symmetric, and transitive.

`src/81-marici-raw-fraction-scaling-reflection.rzk.md` uses symmetry and transitivity to reverse a supplied positive scaling path and to reflect equivalence after scaling both fractions by the same positive factor. Common factors can therefore be removed at the relation level, but factor selection, coprimality, reduced representatives, and normalization uniqueness remain open.

`src/82-marici-nat-identity-code.rzk.md` defines a recursive natural identity code together with checked path encoding by transport and structural code decoding.

`src/83-marici-nat-identity-decode-encode.rzk.md` proves structurally that decoding the reflexive code yields the reflexive path, including the successor coherence for mapped paths.

`src/84-marici-nat-identity-path-composite.rzk.md` proves uniqueness of singleton inhabitants and, by simultaneous recursion, uniqueness of inhabitants of every natural identity code.

`src/85-marici-nat-identity-decode-encode.rzk.md` transfers code uniqueness conditionally to equality of natural paths when the two path-side decode--encode composite equations are supplied.

`src/86-marici-nat-identity-path-uniqueness.rzk.md` uses the full tuple form of `idJ` to extend reflexive decode--encode to arbitrary natural paths, then combines this composite with code uniqueness to prove that every natural identity type is proposition-valued. This closes natural identity-path uniqueness; decidable equality remains separate.

`src/87-marici-int-identity-code.rzk.md` defines the canonical-integer identity code: zero/zero uses the singleton, equal-sign nonzero constructors use the natural code on predecessor magnitudes, and mixed constructors use the empty type. Its reflexive inhabitant and path encoding by transport check.

`src/88-marici-int-identity-decode.rzk.md` decodes these codes structurally: equal-sign codes map natural decoded paths through the corresponding integer constructor, while mixed codes eliminate from the empty type.

`src/89-marici-int-identity-code-unique.rzk.md` proves every canonical-integer identity code proposition-valued, using singleton uniqueness at zero, natural-code uniqueness for equal signs, and empty elimination for mixed constructors.

`src/90-marici-int-identity-decode-encode.rzk.md` proves the reflexive decode--encode calculation structurally and extends it to arbitrary canonical-integer paths by identity elimination.

`src/91-marici-int-identity-path-unique.rzk.md` maps integer-code uniqueness under decoding and composes with the two decode--encode laws to prove any two parallel canonical-integer paths equal. This closes canonical-integer identity-path uniqueness; decidable equality remains separate.

`src/92-marici-positive-divisibility-witnesses.rzk.md` introduces indexed witnesses for an integer having a right positive factor and for a positive natural having a right positive factor, retaining cofactors and exact multiplication paths. It constructs the unit-factor witness on both axes.

`src/93-marici-raw-fraction-common-factor.rzk.md` pairs numerator and denominator cofactors with two exact right-factor equations sharing one structurally positive factor, and constructs the always-available unit common factor.

`src/94-marici-common-factor-reduced-fraction.rzk.md` extracts the two cofactors as a raw-fraction candidate and checks that extraction from the unit common-factor certificate computes to the original fraction.

`src/95-marici-common-factor-reconstruction.rzk.md` descends the positive denominator equation through successor injectivity, combines numerator and denominator paths by constructor congruence, and proves that positive scaling of the extracted cofactor fraction reconstructs the original raw fraction exactly.

`src/96-marici-common-factor-relation-preservation.rzk.md` transports positive-scaling equivalence along that reconstruction path and applies relation symmetry, proving that removal of any supplied common positive factor preserves raw-fraction equivalence in both orientations.

`src/97-marici-nonunit-common-factor.rzk.md` separates genuine reduction witnesses from the always-present unit factor by requiring the factor predecessor itself to be a successor. It extracts the corresponding reduced candidate and proves removal preserves equivalence.

`src/98-marici-reduced-raw-fractions.rzk.md` defines reducedness as constructive absence of every nonunit common positive factor and packages numerator, positive denominator predecessor, and that evidence as `MariciReducedRawFraction`, with a forgetful map to raw fractions. No reduced inhabitant is asserted without evidence.

`src/99-marici-raw-fraction-normalization-witness.rzk.md` packages a reduced representative together with raw-fraction equivalence to its source, and proves every already-reduced fraction normalizes to itself.

`src/99z-marici-certified-factor-normalization.rzk.md` constructs a normalization witness from supplied numerator and denominator cofactors, exact common-factor equations, and a reducedness proof for the cofactors. The `99z` prefix preserves dependency order under the checker's lexical source ordering.

`src/99za-marici-reduction-decision-interface.rzk.md` defines the exact constructive selector output: either a nonunit common-factor witness or a proof of reducedness. Its next-fraction projection removes the supplied factor in the first branch and retains the source in the second. No selector is asserted.

`src/99zb-marici-reduction-decrease-interface.rzk.md` defines strict natural decrease by a positive additive gap and packages each reducible step with its common-factor equations and a proof that the extracted denominator predecessor is strictly smaller.

`src/99zc-marici-nonunit-factor-decreases-denominator.rzk.md` derives that decrease from every nonunit denominator factor equation: multiplication commutativity exposes a positive additive remainder, successor injectivity removes the outer successor, and the positive-product predecessor supplies the gap. Thus every nonunit common-factor witness yields a decreasing reduction package.

`src/99zd-marici-normalization-recursive-step.rzk.md` proves the recursive normalization algebra: a reduced decision branch normalizes reflexively, while a reducible branch composes relation-preserving nonunit removal with a supplied recursive normalization of the smaller cofactor fraction.

`src/99ze-marici-nat-decidable-equality.rzk.md` constructs a total natural equality decision returning either a path or an empty-valued refutation, using zero/successor disjointness and successor injectivity.

`src/99zf-marici-int-decidable-equality.rzk.md` lifts decidable equality to canonical integers by constructor no-confusion and natural payload decisions. Natural and integer equality tests are now available for bounded divisor search.

`src/99zg-marici-int-magnitude-positive-product.rzk.md` defines canonical-integer absolute magnitude and proves that right multiplication by a positive integer maps to natural multiplication on magnitudes; zero receives a positive-divisibility witness for every factor.

`src/99zh-marici-magnitude-divisibility-lift.rzk.md` reconstructs signed integer right-divisibility from a supplied positive natural factorization of the integer magnitude. Successor injectivity recovers predecessor equality and the source sign selects the cofactor sign.

`src/99zi-marici-bounded-positive-cofactor-search.rzk.md` executes a fuel-bounded descending search over positive cofactors using decidable natural equality; successful results retain the exact multiplication path, and a closed two-times-two search checks.

`src/99zj-marici-traced-cofactor-search.rzk.md` strengthens misses from an untyped marker to a rejection log containing each tested cofactor and its empty-valued equality refutation; hits still retain exact factorization evidence.

`src/99zk-marici-positive-cofactor-bound.rzk.md` defines non-strict natural bounds by additive gaps and proves that every cofactor predecessor in a positive factorization is at most the target predecessor. Thus candidates zero through the target predecessor form a complete search range.

`src/99zl-marici-at-most-successor-split.rzk.md` proves the induction interface for that interval: a bound at a successor endpoint either lowers to the previous bound or identifies the candidate with the new endpoint, and previous bounds lift to the successor.

`src/99zm-marici-bounded-cofactor-decision.rzk.md` uses that split to decide bounded positive cofactors with evidence: the positive branch carries a bounded cofactor and product path, while the negative branch refutes every product path from any cofactor in the interval.

`src/99zn-marici-positive-divisibility-decision.rzk.md` applies the bounded decision at the target predecessor and uses the global cofactor bound to turn bounded absence into universal absence. Positive-natural right divisibility is fully decidable with exact witnesses or refutations, including a closed factor-two/four computation.

`src/99zo-marici-int-positive-divisibility-decision.rzk.md` decides positive right divisibility of canonical integers: zero is always divisible, while nonzero cases decide magnitude divisibility, lift successful cofactors with the source sign, and refute alleged signed cofactors through their induced magnitude equations.

`src/99zp-marici-common-factor-fixed-decision.rzk.md` intersects integer numerator and positive denominator divisibility for one supplied factor. It returns an exact shared-factor certificate when both axes divide, while failure on either axis gives a refutation of every common-factor certificate at that factor.

`src/99zq-marici-common-factor-bound.rzk.md` proves every common positive-factor predecessor is at most the denominator predecessor by swapping factor and cofactor in the denominator equation; the structurally nonunit specialization inherits the bound. This supplies a complete finite range for factor enumeration.

`src/99zr-marici-unit-denominator-reduced.rzk.md` proves that no successor factor predecessor can be bounded by zero, hence every canonical integer over denominator one is constructively reduced and has a normalization witness. Successor-bound descent is also checked for factor-search induction.

`src/99zs-marici-bounded-nonunit-common-factor-decision.rzk.md` decides nonunit common factors over any finite predecessor interval. Hits retain factor index, bound evidence, and the exact common certificate; misses universally refute all certificates in the interval, with transport handling endpoint identification.

`src/99zt-marici-total-reduction-decision.rzk.md` applies that search to every denominator: denominator one uses the direct reducedness theorem, while a successor predecessor searches the complete nonunit interval. Hits become reducibility witnesses; universal bounded absence becomes constructive reducedness via the common-factor bound. Total reduction selection is closed.

`src/99zu-marici-strict-decrease-bounded-recursion.rzk.md` converts strict decrease below `succ n` into the non-strict predecessor bound needed by a structural induction hypothesis at `n`, defines reflexive bounds, and states the bounded normalization family over all component pairs beneath a bound.

`src/99zv-marici-bounded-normalization.rzk.md` constructs that family by structural recursion on the external bound. Fractions in the previous interval use the induction hypothesis; endpoint fractions run the total reduction decision, stop if reduced, or recursively normalize the strictly smaller cofactor denominator and compose factor removal.

`src/99zw-marici-total-raw-fraction-normalization.rzk.md` applies bounded normalization at each fraction's reflexive denominator bound. Every raw fraction now computes a `MariciRawFractionNormalization`, hence a reduced representative together with a checked raw-fraction equivalence proof. Normalization existence is closed.

`src/99zx-marici-unit-denominator-uniqueness.rzk.md` proves the first reduced-uniqueness case: equivalence between two denominator-one fractions reduces by integer right-unit laws to equality of numerators, then component congruence gives equality of raw representatives. The general reduced theorem still requires the coprime cross-product argument. A rational carrier, mixed-sign integer addition associativity, and the integer universal property remain open.

Modules `99zy` through `99zzo` isolate canonicality and the magnitude-Euclid residual, discharge denominator-divisibility antisymmetry, add decidable structural equality and normalized arithmetic, construct sign-aware reciprocal and its raw involution, package the reduced normal-form carrier, and prove canonical-zero results.

`src/99zzp-marici-euclid-unit-magnitude-case.rzk.md` proves denominator divisibility when the left numerator has magnitude one: the magnitude cross product directly exhibits the required quotient, while a zero right numerator contradicts denominator positivity.

`src/99zzq-marici-nonzero-euclid-suffices.rzk.md` repairs the Euclid interface's zero edge. Reduced zero is handled directly through its denominator-one theorem; only structurally nonzero signed numerators invoke magnitude coprimality.

`src/99zzr-marici-nonzero-magnitude-split.rzk.md` constructively classifies every nonzero signed numerator as unit magnitude or magnitude at least two. The unit branch invokes the checked direct theorem, reducing full canonicality to a single large-magnitude coprime Euclid premise.

`src/99zzs-marici-natural-divisibility-calculus.rzk.md` introduces natural divisibility with arbitrary cofactors, including zero, and proves unit divisibility, reflexivity, zero divisibility, transitivity, and conversion from the existing positive witness.

`src/99zzt-marici-general-to-positive-divisibility.rzk.md` proves that a general divisor of a positive value has a positive cofactor, defines nonunit common divisors in the general calculus, and converts them back to the magnitude common-factor certificates refuted by reducedness. This removes the positive-cofactor restriction from the Euclid proof layer without weakening coprimality.

`src/99zzu-marici-standard-euclid-reduction.rzk.md` defines generic nonunit common divisors and natural coprimality, transports reduced positive magnitudes into that form, and proves that standard natural coprime Euclid implies the remaining large-magnitude theorem. All normalization-specific structure is now discharged from the residual.

`src/99zzv-marici-coprimality-divisor-descent.rzk.md` proves coprimality symmetry and descent along a divisor in either coordinate by composing common-divisor evidence through divisibility transitivity. This supplies the coprimality transport needed for a factorization induction proof of natural Euclid.

`src/99zzw-marici-natural-divisibility-products.rzk.md` proves that either product factor divides the product, that divisibility is preserved when multiplying the value on either side, and that divisor and value may be scaled together. Explicit associativity and commutativity paths retain exact cofactor equations.

`src/99zzx-marici-divisibility-positive-scale-cancellation.rzk.md` cancels a common structurally positive scale from general divisibility in either multiplication orientation. Reassociation and commutativity expose the common left factor, then positive multiplication injectivity recovers the unscaled cofactor equation.

`src/99zzy-marici-composite-euclid-step.rzk.md` proves that Euclid for two positive factors implies Euclid for their product. It descends coprimality to each factor, extracts the first factor from product divisibility, cancels it, applies Euclid to the second factor, and reconstructs the product divisor.

`src/99zzz-marici-proper-factor-search.rzk.md` specializes bounded common-factor search to decide proper nonunit factors of every natural value at least three. Hits retain the exact positive factorization; misses universally refute all candidates below the whole-value factor index.

`src/99zzza-marici-proper-factor-recursion-bounds.rzk.md` converts each proper-factor hit into exact recursion data. The searched factor remains in its declared proper bound, while strict denominator decrease places the cofactor predecessor within the previous external recursion stage.

`src/99zzzb-marici-division-state.rzk.md` defines Euclidean division states with quotient, bounded remainder, and exact reconstruction, constructs the zero-value state, and proves the remainder-increment and quotient-carry arithmetic identities needed by the successor update.

`src/99zzzc-marici-division-successor-step.rzk.md` implements the executable successor update for division by any natural divisor at least two. It increments a below-endpoint remainder and carries to the quotient with zero remainder at the endpoint, preserving both the bound and exact reconstruction.

`src/99zzzd-marici-total-nonunit-division.rzk.md` iterates the successor transition by dependent natural induction, constructing total quotient and bounded remainder data for every divisor at least two and every dividend. It also extracts standard natural divisibility from any state whose remainder is zero.

`src/99zzze-marici-bounded-remainder-order-obstructions.rzk.md` proves that a successor cannot be at most its predecessor, that every positive multiple lies at least at its factor, and consequently that a bounded remainder cannot equal a positive multiple of the full divisor. General at-most transitivity and upper-endpoint reindexing are included.

`src/99zzzf-marici-division-equal-quotient-uniqueness.rzk.md` closes the equal-quotient branch of division uniqueness: exact reconstruction against a pure multiple with the same quotient reduces by additive prefix cancellation to zero remainder.

`src/99zzzg-marici-natural-gap-trichotomy.rzk.md` constructs trichotomy for every pair of naturals while retaining an exact positive additive gap in each strict branch. This supplies the quotient comparison evidence required to rewrite strict division-uniqueness branches into order obstructions.

`src/99zzzh-marici-division-smaller-quotient-obstruction.rzk.md` excludes the branch where a bounded-remainder state's quotient is strictly smaller than a pure divisibility quotient. Distributivity and additive cancellation identify the remainder with a positive full-divisor multiple, contradicting its bound.

`src/99zzzi-marici-positive-product-sum-nonzero.rzk.md` exposes a product of two structurally positive naturals plus any remainder as a successor and eliminates any equation identifying that sum with zero. This is the terminal contradiction required by the greater-quotient uniqueness branch.

`src/99zzzj-marici-division-greater-quotient-obstruction.rzk.md` excludes the remaining strict division-uniqueness branch. A positive quotient gap is distributed across the divisor, the smaller quotient prefix is cancelled, and the resulting positive product plus remainder equals zero, contradicting successor disjointness.

`src/99zzzk-marici-divisibility-forces-zero-remainder.rzk.md` assembles explicit quotient trichotomy with the equal and strict branch lemmas. Any standard divisibility witness now forces the remainder of any bounded division state—and in particular the computed nonunit division state—to equal zero.

`src/99zzzl-marici-nonunit-divisibility-decision.rzk.md` decides natural divisibility by every divisor at least two. It computes bounded division, tests the remainder against zero, extracts a witness on equality, and refutes divisibility on inequality via remainder uniqueness.

`src/99zzzm-marici-irreducible-divisor-rigidity.rzk.md` proves that every nonunit divisor of a value with no proper nonunit factor equals the whole value. Zero and unit cofactors are handled directly; a nonunit cofactor forces a proper factor by strict denominator decrease and contradicts irreducibility.

`src/99zzzn-marici-proper-factor-miss-is-irreducible.rzk.md` lifts every exact proper natural factorization to the signed-numerator common-factor certificate used by bounded search. Consequently, the executable search's universal miss supplies the no-proper-nonunit-factor predicate consumed by divisor rigidity.

`src/99zzzo-marici-coprime-excludes-whole-divisor.rzk.md` proves that a structurally nonunit value cannot divide its coprime partner: such a witness, paired with reflexive self-divisibility, would exhibit the whole value as a nonunit common divisor.

`src/99zzzp-marici-divisibility-removes-multiple-prefix.rzk.md` proves, without subtraction, that if a positive divisor divides an explicit multiple of itself plus a residual, then it divides the residual. Quotient-gap trichotomy reduces the cases to a residual multiple, zero residual, or the checked impossible greater-prefix branch.

`src/99zzzq-marici-division-product-remainder-descent.rzk.md` expands a product along a division reconstruction `x=qd+r` into the explicit multiple `(qz)d` plus `rz`, with all distributivity, associativity, and commutativity paths recorded. Removing the multiple prefix proves `d|xz` implies `d|rz`.

`src/99zzzr-marici-irreducible-nondivisor-is-coprime.rzk.md` proves that a residue not divisible by a no-proper-factor value is coprime to it. Divisor rigidity identifies any nonunit common divisor with the whole irreducible value, contradicting the supplied nondivisibility refutation.

`src/99zzzs-marici-coprime-division-remainder-nondivisible.rzk.md` proves divisibility closure under addition and applies it to division reconstruction. If the divisor divided the remainder in `x=qd+r`, it would divide `x`; coprimality with a nonunit divisor refutes this.

`src/99zzzt-marici-divisibility-removes-divisible-summand.rzk.md` generalizes multiple-prefix removal: if a divisor divides one summand and the whole sum, it divides the other summand. Stored cofactors expose the required explicit multiple; the zero-divisor branch is handled without assuming positivity.

`src/99zzzu-marici-bezout-positive-orientation-euclid.rzk.md` defines the two natural-difference orientations of a Bézout certificate and proves the `ux+1=vy` orientation implies Euclid. After scaling by `z`, semiring paths make `y` divide `(ux)z+z`; divisible-summand removal yields `y|z`.

`src/99zzzv-marici-bezout-negative-orientation-euclid.rzk.md` proves the symmetric `vy+1=ux` orientation implies the fixed-pair Euclid conclusion and assembles both constructors of the natural Bézout-difference type. Coprimality is needed only upstream to construct such a certificate.

`src/99zzzw-marici-bezout-lift-left-through-division.rzk.md` proves the first extended-Euclid coefficient update. From `x=qy+r` and `ur+1=vy`, explicit semiring paths derive `ux+1=(v+uq)y`.

`src/99zzzx-marici-bezout-lift-right-through-division.rzk.md` proves the second update: from `x=qy+r` and `vy+1=ur`, it derives `(uq+v)y+1=ux`. Matching both orientations shows the full natural Bézout-difference type is closed under a Euclidean division step.

`src/99zzzy-marici-bezout-symmetry-and-unit.rzk.md` proves coordinate symmetry of natural Bézout differences by exchanging their two orientations and coefficients, and constructs canonical certificates when either coordinate is one.

`src/99zzzz-marici-coprimality-descends-to-remainder.rzk.md` proves that `x= qy+r` transports coprimality of `(x,y)` to `(r,y)` and, by symmetry, `(y,r)`. Any alleged common divisor divides `qy` and `r`, hence `x`, contradicting the original coprimality witness.

`src/99zzzza-marici-bezout-nonunit-bounded-step.rzk.md` proves the nonunit endpoint of bounded extended Euclid. Dividing by `n+2`, a zero remainder contradicts coprimality; a positive remainder has predecessor at most `n`, so the prior bounded certificate for the swapped pair is symmetrized and lifted through division.

`src/99zzzzb-marici-bounded-extended-euclid.rzk.md` proves the zero external-bound base: a positive second-coordinate predecessor bounded by zero equals zero by at-most antisymmetry, so transport supplies the canonical unit Bézout certificate.

`src/99zzzzc-marici-bounded-extended-euclid-successor.rzk.md` proves the successor external-bound constructor. At-most splitting sends lower indices to the prior bound and transports the new endpoint to the checked nonunit extended-Euclid step.

`src/99zzzzd-marici-positive-natural-coprime-euclid.rzk.md` iterates the bounded extended-Euclid constructors, obtains a natural Bézout difference for every coprime pair with positive second coordinate, and eliminates it to prove standard natural Euclid for every positive divisor—the exact denominator domain.

`src/99zzzze-marici-signed-magnitude-euclid-closed.rzk.md` wires positive natural Euclid through the existing magnitude, cross-product, and unit-magnitude split. It supplies closed implementations of signed-magnitude coprime Euclid and one-way reduced cross-product denominator divisibility.

`src/99zzzzf-marici-normalization-canonicality-closed.rzk.md` plugs closed denominator divisibility into the established bidirectional antisymmetry bridge. Equivalent reduced representatives are unconditionally equal, total normalization agrees with every equivalent reduced target, and normalization fixes reduced inputs.

`src/99zzzzg-marici-normalization-respects-equivalence.rzk.md` proves that equivalent raw presentations normalize to identical canonical numerator and denominator components. This closes the presentation-independence gate for normalization itself.

`src/99zzzzh-marici-normalized-multiplication-descent.rzk.md` composes raw multiplication congruence with canonical normalization. Normalize-after-raw multiplication now returns identical canonical components for equivalent inputs in both arguments.

`src/99zzzzi-marici-equivalence-reflected-by-normalization.rzk.md` proves the converse canonicality direction: equality of normalized raw components implies raw-fraction equivalence. Normalized component equality is therefore an exact presentation-independent test.

`src/99zzzzj-marici-decidable-raw-fraction-equivalence.rzk.md` packages normalized component comparison into a total raw-fraction equivalence decision. Positive branches reflect canonical equality to equivalence; negative branches use canonicality to refute equivalence.

`src/99zzzzk-marici-int-add-assoc-zero-faces.rzk.md` proves integer addition associativity whenever any one of the three inputs is zero, removing all zero faces from the remaining constructor census.

`src/99zzzzl-marici-int-negate-add.rzk.md` checks negation/addition compatibility on both nonzero same-sign faces. The attempted global extension identifies the remaining mixed-sign residual as comparison duality between the two ordering-indexed normalizers.

`src/99zzzzm-marici-int-mixed-normalizer-duality.rzk.md` proves by simultaneous predecessor recursion that exchanging mixed-sign magnitudes negates the normalized result. Consequently integer negation preserves addition on every constructor face.

`src/99zzzzn-marici-int-assoc-sign-reversal.rzk.md` transports any integer addition associativity path through simultaneous negation. The eight nonzero sign faces therefore reduce to four sign-reversal representatives.

`src/99zzzzo-marici-int-assoc-unit-cancellation-family.rzk.md` proves an unbounded genuinely mixed associativity family: positive one followed by a positive term and its negative, together with the simultaneous sign reversal. It composes adjacent-gap normalization with equal-magnitude cancellation.

`src/99zzzzp-marici-int-assoc-positive-pair-cancellation.rzk.md` removes the unit restriction from the mixed cancellation family. Associativity holds for arbitrary positive first and second terms when the third is the additive inverse of the second, and for the sign-reversed family.

`src/99zzzzq-marici-int-assoc-positive-dominant-middle.rzk.md` proves the strict three-magnitude associativity region in which the positive middle term dominates the following negative term. Explicit-gap normalization identifies both parenthesizations, and sign reversal supplies the opposite-sign region.

`src/99zzzzr-marici-int-assoc-unit-negative-dominant.rzk.md` proves a strict negative-dominant mixed associativity slice with unit first magnitude, plus its sign reversal. Both parenthesizations reduce by explicit negative gaps to the same residual.

`src/99zzzzs-marici-int-assoc-general-negative-dominant.rzk.md` removes the unit restriction in the region where the third negative magnitude dominates the sum of both positive magnitudes. Natural reassociation aligns the two explicit-gap reductions; sign reversal supplies the opposite region.

`src/99zzzzt-marici-int-assoc-total-magnitude-cancellation.rzk.md` proves the equality boundary where the third negative magnitude equals the combined magnitude of both positive terms. The left sum cancels directly; the right reduces by an explicit gap and residual cancellation. Sign reversal supplies the opposite boundary.

`src/99zzzzu-marici-intermediate-gap-reassociation.rzk.md` proves the natural-number coherence path needed when the negative term dominates the positive middle term but the positive first term dominates the residual.

`src/99zzzzv-marici-int-assoc-intermediate-positive-residual.rzk.md` assembles the intermediate coherence path into mixed integer associativity when the negative term dominates the middle positive term but the first positive term dominates the residual. Sign reversal supplies the opposite region.

`src/99zzzzw-marici-mixed-middle-third-classification.rzk.md` reorients natural gap trichotomy into the exact explicit predecessor forms used by the dominant-middle, equal-cancellation, and nested-residual mixed associativity branches.

`src/99zzzzx-marici-three-magnitude-region-classification.rzk.md` checks the nested residual-classification interface used after the third term dominates the middle term. Its three outputs select the positive-residual, exact-cancellation, and negative-dominant families without discarding explicit gaps.

`src/99zzzzy-marici-mixed-assoc-outer-factorization.rzk.md` discharges the middle-dominant and equal branches of arbitrary `(+,+,-)` associativity. The full face now reduces to one typed handler for the third-dominant residual classification.

`src/99zzzzz-marici-third-handler-first-dominant-branch.rzk.md` implements the first-dominant residual branch of the remaining third-dominant handler for arbitrary inputs by transporting its two explicit gap equations into the checked intermediate-region theorem.

`src/99zzzzza-marici-third-handler-equal-residual-branch.rzk.md` implements the equal leading/residual branch of the remaining third-dominant handler by transporting arbitrary inputs to the checked total-magnitude cancellation theorem.

`src/99zzzzzb-marici-third-handler-residual-dominant-branch.rzk.md` implements the final residual-dominant branch by transporting its two explicit equations into the checked general negative-dominant theorem. Every branch required by the third-dominant handler is now implemented.

`src/99zzzzzc-marici-positive-positive-negative-assoc.rzk.md` assembles the residual classifier and all transported branches into arbitrary `(+,+,-)` integer addition associativity. Simultaneous sign reversal also closes `(-,-,+)`.

`src/99zzzzzd-marici-int-assoc-middle-sign-permutation.rzk.md` uses additive commutativity and two checked adjacent-order associativity paths to close arbitrary `(+,-,+)` associativity. Sign reversal also closes `(-,+,-)`.

`src/99zzzzze-marici-int-assoc-leading-sign-permutation.rzk.md` uses commutativity plus the checked middle- and trailing-sign faces to close arbitrary `(-,+,+)` associativity. Sign reversal closes `(+,-,-)`. Every nonzero mixed-sign constructor face is now proved.

`src/99zzzzzf-marici-int-add-assoc.rzk.md` assembles zero, same-sign, and all six mixed-sign constructor faces into global canonical-integer addition associativity. The principal additive-normalization blocker is closed.

`src/99zzzzzg-marici-normalized-additive-inverses.rzk.md` combines the existing raw-fraction inverse equivalences with normalization canonicality. Normalize-after-raw addition of any presentation and its negation now equals normalized zero in both orders at the component level.

`src/99zzzzzh-marici-normalized-add-basic-laws.rzk.md` transports strict raw addition commutativity and zero laws through total normalization. Normalize-after-raw addition is now componentwise commutative and unital without a distributivity premise.

`src/99zzzzzi-marici-int-distrib-zero-faces.rzk.md` introduces a typed global integer left-distributivity interface and checks its zero multiplier and double-zero summand faces.

`src/99zzzzzj-marici-int-global-distrib.rzk.md` records the corrected readback: module 70 already assembled unrestricted left and right integer distributivity. With global addition associativity now checked, the actual remaining additive frontier is raw-fraction addition congruence and associativity.

`src/99zzzzzk-marici-normalized-multiplication-laws.rzk.md` transports strict raw multiplication commutativity and associativity through final normalization. Finite raw Euler-factor products normalized once at the end are independent of order and parenthesization at the canonical-component level.

All two hundred fifteen files passed Rzk 0.11.3 against `rzk-lang/sHoTT` commit
`52a441cc4aaa03f3fe94ee94f70bb2874e26a6a2`:

```text
[8 out of 8] Checking #define marici-triangle-witness-is-rezk
[3 out of 3] Checking #define marici-map-preserves-composite
[12 out of 12] Checking #define marici-two-times-two
[6 out of 6] Checking #define marici-mul-add-left-distrib
[5 out of 5] Checking #define marici-mul-add-right-distrib
[12 out of 12] Checking #define marici-two-minus-four
[15 out of 15] Checking #define marici-int-minus-one-plus-minus-one
[10 out of 10] Checking #define marici-int-two-times-two
[8 out of 8] Checking #define marici-int-add-zero-right
[1 out of 1] Checking #define marici-int-add-comm
[5 out of 5] Checking #define marici-int-embed-mul
[4 out of 4] Checking #define marici-nat-int-map-laws
[5 out of 5] Checking #define marici-int-mul-minus-one-right
[5 out of 5] Checking #define marici-nat-int-map-laws-compose-id
[4 out of 4] Checking #define marici-map-triangle-compose
[7 out of 7] Checking #define marici-nat-int-preserves-composite-if-discrete
[4 out of 4] Checking #define marici-int-mul-assoc
[12 out of 12] Checking #define marici-raw-four-fourths-equivalent-one
[4 out of 4] Checking #define marici-raw-fraction-equivalent-negate
[2 out of 2] Checking #define marici-raw-fraction-mul-assoc
[4 out of 4] Checking #define marici-raw-zero-at-equivalent
[3 out of 3] Checking #define marici-raw-fraction-mul-zero-right-equivalent
[2 out of 2] Checking #define marici-raw-fraction-mul-congruent
[3 out of 3] Checking #define marici-raw-fraction-equivalent-trans-if-positive-cancellative
[2 out of 2] Checking #define marici-raw-fraction-multiplicative-descent-if-positive-cancellative
[3 out of 3] Checking #define marici-raw-fraction-add-zero-left
[2 out of 2] Checking #define marici-raw-fraction-add-negate-left-equivalent
[3 out of 3] Checking #define marici-raw-fraction-mul-negate-both
[3 out of 3] Checking #define marici-raw-fraction-scale-positive-equivalent
[2 out of 2] Checking #define marici-raw-fraction-scale-positive-compose
[2 out of 2] Checking #define marici-int-mul-add-left-distrib-embedded-nat
[1 out of 1] Checking #define marici-int-mul-add-right-distrib-embedded-nat
[2 out of 2] Checking #define marici-int-add-assoc-negated-embedded-nat
[2 out of 2] Checking #define marici-int-mul-add-left-distrib-negated-by-embedded
[2 out of 2] Checking #define marici-int-embedded-single-sign-placement
[1 out of 1] Checking #define marici-int-mul-add-left-distrib-embedded-by-negated
[1 out of 1] Checking #define marici-int-mul-add-left-distrib-negated-by-negated
[4 out of 4] Checking #define marici-int-mul-add-right-distrib-negated-by-negated
[2 out of 2] Checking #define marici-int-mul-add-inverse-pair-right-distrib
[2 out of 2] Checking #define marici-int-mul-add-reversed-inverse-pair-right-distrib
[4 out of 4] Checking #define marici-int-mul-add-right-distrib-negated-by-arbitrary
[4 out of 4] Checking #define marici-int-mul-add-right-distrib-from-mixed-branches
[3 out of 3] Checking #define marici-int-mul-add-right-distrib-from-single-mixed-branch
[4 out of 4] Checking #define marici-int-add-adjacent-negative-positive
[5 out of 5] Checking #define marici-int-add-reversed-opposite-common-prefix
[4 out of 4] Checking #define marici-int-add-neg-pos-residual-positive
[3 out of 3] Checking #define marici-sub-mul-successor-right
[2 out of 2] Checking #define marici-mul-sub-right-distrib
[1 out of 1] Checking #define marici-mul-sub-left-distrib
[1 out of 1] Checking #define marici-compare-positive-scale
[1 out of 1] Checking #define marici-compare-positive-product-predecessor
[2 out of 2] Checking #define marici-positive-product-successor-left
[1 out of 1] Checking #define marici-positive-product-residual-base
[1 out of 1] Checking #define marici-positive-product-residual
[2 out of 2] Checking #define marici-compare-explicit-gap-less
[1 out of 1] Checking #define marici-int-add-scaled-pos-neg-gap
[1 out of 1] Checking #define marici-int-add-scaled-pos-neg-negative-gap
[1 out of 1] Checking #define marici-positive-factor-equal-mixed-left-distrib
[1 out of 1] Checking #define marici-int-add-pos-neg-gap
[3 out of 3] Checking #define marici-positive-factor-negative-gap-left-distrib
[1 out of 1] Checking #define marici-positive-factor-mixed-successor-step
[1 out of 1] Checking #define marici-positive-factor-mixed-left-distrib
[1 out of 1] Checking #define marici-zero-factor-mixed-left-distrib
[1 out of 1] Checking #define marici-negative-factor-positive-gap-left-distrib
[2 out of 2] Checking #define marici-negative-factor-equal-mixed-left-distrib
[1 out of 1] Checking #define marici-negative-products-common-successor
[1 out of 1] Checking #define marici-negative-factor-mixed-successor-step
[1 out of 1] Checking #define marici-negative-factor-mixed-left-distrib
[1 out of 1] Checking #define marici-all-factor-positive-negative-left-distrib
[2 out of 2] Checking #define marici-int-mul-add-right-distrib
[2 out of 2] Checking #define marici-add-prefix-injective
[6 out of 6] Checking #define marici-succ-not-zero
[1 out of 1] Checking #define marici-mul-positive-left-injective
[1 out of 1] Checking #define marici-mul-positive-right-injective
[12 out of 12] Checking #define marici-int-neg-not-pos
[1 out of 1] Checking #define marici-positive-product-predecessor-injective
[1 out of 1] Checking #define marici-int-positive-left-injective
[1 out of 1] Checking #define marici-int-positive-right-injective
[1 out of 1] Checking #define marici-int-mul-swap-right-factors
[1 out of 1] Checking #define marici-raw-fraction-equivalent-trans
[2 out of 2] Checking #define marici-raw-fraction-scale-positive-reflects-equivalent
[4 out of 4] Checking #define marici-nat-identity-decode
[1 out of 1] Checking #define marici-nat-identity-decode-refl
[2 out of 2] Checking #define marici-nat-identity-code-unique
[1 out of 1] Checking #define marici-nat-path-equal-from-composites
[2 out of 2] Checking #define marici-nat-identity-path-unique
[3 out of 3] Checking #define marici-int-identity-encode
[1 out of 1] Checking #define marici-int-identity-decode
[1 out of 1] Checking #define marici-int-identity-code-unique
[2 out of 2] Checking #define marici-int-identity-decode-encode-all
[1 out of 1] Checking #define marici-int-identity-path-unique
[4 out of 4] Checking #define marici-positive-nat-unit-right-divides
[2 out of 2] Checking #define marici-raw-components-unit-common-positive-factor
[2 out of 2] Checking #define marici-unit-common-factor-reduces-trivially
[3 out of 3] Checking #define marici-common-factor-reconstruction
[2 out of 2] Checking #define marici-common-factor-removal-preserves-equivalent
[3 out of 3] Checking #define marici-nonunit-common-factor-removal-preserves-equivalent
[4 out of 4] Checking #define marici-reduced-raw-fraction-no-nonunit-common-factor
[3 out of 3] Checking #define marici-normalization-forget-representative
[1 out of 1] Checking #define marici-certified-factor-normalization
[4 out of 4] Checking #define marici-reduction-decision-next-fraction
[3 out of 3] Checking #data MariciRawComponentsDecreasingReduction
[2 out of 2] Checking #define marici-nonunit-common-factor-with-decrease
[2 out of 2] Checking #define marici-normalization-from-reduction-decision
[2 out of 2] Checking #define marici-nat-decide-equality
[2 out of 2] Checking #define marici-int-decide-equality
[3 out of 3] Checking #define marici-int-zero-right-positive-divides
[2 out of 2] Checking #define marici-magnitude-factorization-lifts-to-int
[3 out of 3] Checking #define marici-search-two-times-two
[3 out of 3] Checking #define marici-search-positive-cofactor-traced
[2 out of 2] Checking #define marici-positive-cofactor-at-most-target
[3 out of 3] Checking #define marici-at-most-successor-split
[4 out of 4] Checking #define marici-decide-positive-cofactor-bounded
[3 out of 3] Checking #define marici-two-right-divides-four-decision
[3 out of 3] Checking #define marici-decide-int-right-positive-divisibility
[2 out of 2] Checking #define marici-decide-common-positive-factor
[2 out of 2] Checking #define marici-nonunit-common-factor-at-most-denominator
[4 out of 4] Checking #define marici-unit-denominator-normalization
[3 out of 3] Checking #define marici-decide-nonunit-common-factor-bounded
[1 out of 1] Checking #define marici-decide-raw-components-reduction
[3 out of 3] Checking #define MariciBoundedNormalizationFamily
[1 out of 1] Checking #define marici-normalize-bounded
[3 out of 3] Checking #define marici-normalized-raw-representative
[2 out of 2] Checking #define marici-unit-denominator-equivalent-raw-fractions-equal
Everything is ok!
```

The upstream run emitted existing meta-prefix warnings. No warning was specific
to the Marici declarations.

## Reproducible check

Run:

```powershell
pwsh -NoProfile -File research/grothendieck/rzk/check.ps1
```

The checker downloads the pinned sHoTT commit into a fresh temporary directory,
verifies the archive digest, stages the Marici sources there, requires Rzk
0.11.3, and typechecks the combined project. Success ends with
`MARICI_RZK_CHECK_OK` carrying the Rzk version, sHoTT commit, and archive
digest. It does not vendor upstream sources into Marici.

## Dependency boundary

The tested sHoTT archive SHA-256 is
`b396523107ce51d24fb8e248c6f8409f2e1efd402854843791356d29a07566a8`.
The upstream repository declares no license in GitHub metadata and contains no
root license file at the tested commit. Its sources therefore are not vendored
here. Testing used a temporary checkout. Redistribution or vendoring requires
an explicit license or permission.

## Comparison gate

The Cubical Agda `GenericPastingComplex` proves additive exactness in an
abelian group. This Rzk increment proves directed simplicial composition and
coherence. A comparison requires a typed interpretation functor from the Rzk
Segal/Rezk object into an additive target and proofs that its images agree with
the Cubical boundary maps. Similar triangle notation does not provide that
functor.
