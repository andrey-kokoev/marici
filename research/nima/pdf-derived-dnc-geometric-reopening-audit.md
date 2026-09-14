# PDF audit: derived DNC clarifies but does not remove the support obstruction

The closest applicable reference is *Condensed Math and Complex Geometry*, Lecture XIII, Proposition 13.3 and Construction 13.4 (extracted text lines 7240--7340).

For a map of animated commutative rings `A -> B` surjective on `H0`, it constructs a canonical filtered algebra `(I^n)` where `I=fib(A->B)`. Its associated graded is

`Sym_B^n(I/I^2) = Sym_B^n(L_{B/A}[-1])`,

and formation of this filtration commutes with arbitrary base change in `A`. The resulting derived deformation to the normal cone has special fiber

`Spec Sym_B(L_{B/A}[-1])`.

This gives a rigorous architecture for the missing ringed specialization correspondence: specify an actual closed derived support `Spec B -> Spec A`, use its cotangent complex rather than a fitted normal line, form the animated Rees/DNC family, and apply the correspondence-level six functors.

It does **not** repair the present connector automatically. Voevodsky's central-flip audit proves that the literal endpoint supports are disjoint and their derived fiber product is empty. Since Construction 13.3 commutes with base change, applying animated DNC to that empty pullback cannot manufacture the required common special fiber. Derived structure retains nontransverse Tor directions only over an existing derived support; it does not turn a comaximal pair into a nonempty intersection.

Therefore a valid reopening must first provide a different source-derived map `A -> B`: most naturally, the coordinate ring of the full two-edge marked path together with a closed conductor-incidence locus whose `H0` is nonempty. Acceptance then requires:

1. `H0(A) -> H0(B)` is surjective and the locus is independently defined;
2. `L_{B/A}[-1]` contains the required long-normal and transverse-road directions;
3. the three cyclic restrictions recover the established local Cartier classes;
4. proper/base-change hypotheses for the chosen IndCoh or analytic six-functor correspondence hold;
5. ordinary forgetting kills the resulting supported class;
6. the construction does not identify Rees parameters or invert a normal.

The DAG volumes reinforce the categorical target: IndCoh is a functor from a category of correspondences, formal completions encode support, and proper base change is part of the construction. These references offer a legitimate implementation framework, but no source-derived `B` for this connector is present in the PDFs or repository.
