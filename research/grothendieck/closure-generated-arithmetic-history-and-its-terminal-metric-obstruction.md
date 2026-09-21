# Closure-generated arithmetic history and its terminal metric obstruction

## Outcome

The tensor-history adapter has a precise universal construction: it is the free four-step nilpotent associative history algebra on the admitted interval generators, with linear single-event increments. This derives its memory and its attachment update within that specified algebraic realization of ordered closure.

The first nontrivial same-terminal comparison has an invariant three-dimensional Jordan subspace. This forces a concrete metric choice: a positive metric must remain indexed by history presentations, or a terminal-state invariant form must lose the comparison-sensitive directions. A nondegenerate invariant form on that three-dimensional subspace is necessarily indefinite.

These results connect the new arithmetic adapter to the metric question without introducing a detector model.

## 1. Universal construction from the source windows

Let V=C^15 be the span of the consecutive divisor chambers for the squarefree (2,3,5,7) packet rooted at 2. An event (n,p) supplies v(n,p) in V by the already defined window restriction.

Consider unital associative complex algebras A with a specified two-sided ideal I satisfying I^5=0 and a linear assignment ell:V->I. Define

T_<=4(V)=direct_sum_(r=0)^4 V^(tensor r),

with concatenation truncated above degree four and augmentation ideal of positive degree.

There is a unique unital algebra homomorphism Eval_ell:T_<=4(V)->A extending ell, given on each tensor by

Eval_ell(v_1 tensor ... tensor v_r)=ell(v_1)...ell(v_r).

Terms discarded by truncation map to zero because I^5=0. Uniqueness follows because the degree-one generators generate the algebra. This proves the universal property, including the actual map into every admitted realization.

If a single event acts by a linear increment 1+ell(v(n,p)), repeated ordered composition is forced to be the evaluation of

S_w=product_(events in w)(1+v(n,p)).

The source update z->z(1+v(n,p)) is therefore the universal history realization for this class of receivers. Its degree-r terms are the event-segmented signatures by expansion. No parity labels or final-route lookup are required.

The assumptions are important: the current general homotopy closure operator does not by itself select complex linearization, associative tensor multiplication, the linear one-event increment, or nilpotent truncation. Here these specify its arithmetic record realization. Four is the maximum event count of this packet, not a claim that homotopy-coherence depth terminates at four. The full tensor algebra is universal in this class; it need not be the smallest observer for a restricted family of routes.

## 2. Comparison attachments

The augmentation ideal is nilpotent, so every S_w is invertible. For routes w,w' the comparison is right multiplication by

r_(w,w')=S_w^-1 S_w'.

This derives the comparison map from the same generator operations. Associativity and cancellation supply composition and identity laws on the history-indexed system. Closed routes in that comparison system have identity holonomy.

The functor forgetting history retains only the terminal integer. Different route objects can have the same image under that functor. Their comparison can act nontrivially on memory even though their terminal integers agree.

## 3. Actual arithmetic comparison at terminal label 12

Take w=(2,3), w'=(3,2), both starting at 2. Their degree-one totals agree. Set

r=S_w^-1 S_w'=1+d.

The exact arithmetic calculation gives d with first nonzero degree two, d^2 nonzero in degree four, and d^3=0. Thus 1,d,d^2 are independent, distinguished by their lowest degrees. Right multiplication by r preserves their span and acts as

U=[[1,0,0],[1,1,0],[0,1,1]].

This is an actual subrepresentation of the prime-window comparison, not a chosen surrogate matrix.

## 4. The invariant metric equation

A metric depending only on the terminal integer assigns one positive Hermitian form to this same memory space at label 12. If the comparison is isometric, that form must satisfy U* G U=G on the invariant subspace.

For a real symmetric matrix, solving this equation gives

G=[[a,-e/2,-e],[-e/2,e,0],[-e,0,0]].

Its final diagonal entry vanishes. A positive definite G is impossible. The same conclusion holds for complex Hermitian forms: their restriction to real coefficient vectors yields a positive real symmetric invariant form.

If G is positive semidefinite, the zero final diagonal forces the last row and column to vanish, hence e=0. The remaining matrix is diag(a,0,0), a>=0. Such a form annihilates both d and d^2. Therefore a positive invariant terminal metric loses the actual arithmetic comparison directions.

For e nonzero the displayed form is nondegenerate, with determinant -e^3. At e>0 it has inertia (2,1); at e<0 the inertia is reversed. The null vector d^2 is then isotropic but is not in the radical: it pairs with 1 through -e. Removing that vector would change the form and the attachment.

This explains a concrete route to an indefinite Green structure on the retained history. It does not identify this finite form with the already prescribed analytic Green form, or select the free parameters a,e.

## 5. History-indexed positive metrics

A positive family on the separate word presentations remains possible. Let R_w be right multiplication by S_w and choose a positive form G_ref on the reference memory. Put

G_w=(R_w^-1)* G_ref R_w^-1.

Then the generated comparison C_(w,w')=R_w' R_w^-1 is an isometry from G_w to G_w'. This is the familiar frame-transport construction, now evaluated on actual arithmetic histories.

The family generally fails to descend to a metric indexed by terminal n alone. The explicit Jordan calculation proves that failure already for n=12. The remaining choice G_ref is part of the metric construction and requires its own source justification.

## 6. Implication for the single-operator programme

The adapter can be constructed by ordered closure with its universal linear/nilpotent specification. The first metric obstruction appears precisely when history is compressed to the commutative arithmetic base while demanding isometric comparison.

The next Green comparison must therefore state which object it preserves:

- a full history-indexed positive system with compatible forms;
- an indefinite form retaining the comparison directions;
- or a quotient in which those directions become null.

The third loses faithfulness in the explicit fixture. The first two retain the information but carry different descent obligations. This is now a constraint derived from the actual prime-window attachment, rather than a generic warning about positivity.

The unresolved necessity question is whether the main closure construction itself selects the linear history receiver and its bilinear structure. The universal theorem above settles the receiver once those local algebraic requirements are specified; it does not assert that the presently polymorphic Agda operator already supplies them.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_closure_history_universal_and_metric_gate.py`

Exact checks passed:
- evaluation into a five-by-five strictly upper-triangular nilpotent algebra;
- equality with independently assembled prime-window event products;
- inverse and two-order comparison identities;
- d^2 nonzero and d^3=0 in the actual chamber tensor algebra;
- the three-dimensional Jordan action;
- the full real symmetric invariant-metric solution.

Source: `research/voevodsky/prime-window-history-constructs-the-theta-signature-adapter.md`. The checker uses the already tested source-window implementation and exact tensor coefficients. Universal-property and metric conclusions are proved above; finite fixtures exercise their source-specific instances.
