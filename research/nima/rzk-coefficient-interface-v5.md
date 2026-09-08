# Rzk coefficient interface v5: base change and retained Tor data

## Question and scope

Operator instruction: add the base-change certificate, ordinary crossing and normalization-specialization regressions, and record the Rees bundle reproduction gap. This extends v1-v4 without changing Fact_n or generic Rzk composition. It is a specification and exact mathematical fixture suite, not a compiled Rzk certificate implementation.

Source: research/chatgpt/rees-physical-extension/rees_physical_extension.md. Its proper coefficient trace, branch-selected support comparison, and corrected endpoint marking are distinct claims. A successful first claim does not certify the second.

## BaseChangeCertificate

Record the actual source square, all schemes/rings or coefficient categories, variance and functors, coefficient object, and exact comparison arrow between the two composite operations. State which base-change theorem is invoked and its hypotheses, including properness/perfectness or Tor-independence where required. Do not replace those hypotheses by names of similar operations.

Choose and record either a proved Tor-independent underived square or the actual derived fibre model. Preserve Tor degree, support, conormal twists and filtration as required by the consumer. In simultaneous-intersection problems a single-divisor test is not a certificate for the derived centre.

Record the comparison cone/fibre with its grading and structured category. Distinguish:
- comparison is an equivalence with proved vanishing defect;
- comparison exists but has a nonzero computed defect;
- comparison or needed source data remain unconstructed.

A proof that an unrelated trace or objectwise equivalence is natural does not instantiate this record. A derived-equivalence certificate from v3 applies to its named map only. An acyclic total-family object stays acyclic under derived coefficient change; it cannot be identified with a nonzero newly formed special-fibre object without an additional operation and its comparison.

## RequiredClassPreservationCertificate

Independently of coherence, record the required source class, its degree and normalization, the target class, and the induced comparison on the relevant derived fibre/homology. A homotopy between two maps does not prove either preserves the specified nonzero class.

For B=k[X,t], compare K(Xt) to K(X,t). With degree-zero map identity, every B-linear chain map has degree-one column

f_h(e_u)=t(1-h)e_X+Xh e_t, h in B.

This exhaustiveness uses the regular-sequence syzygy: Xa+tb=Xt implies (a-t,b)=h(-t,X). At X=t=0 every such column vanishes. Therefore no member preserves the nonzero first Tor generator. This is an ordinary-support comparison no-go under the fixed degree-zero map and source modules, not a no-go for every logarithmic/excess construction.

The endpoint choices f_X=(t,0), f_t=(0,X) differ by d(e_X wedge e_t)=(-t,X). Their homotopy already exists. Adding more homotopies between these choices cannot change their common zero map on Tor_1. The fibre cone has free homology k^2 in homological degrees one and two. Do not rename these free classes as ordinary integer-prime torsion.

## Normalization base change

Over k=Z, the total polynomial chart B=Z[X,t] is normal, so its normalization cofiber is zero. Its derived specialization remains zero. The fibre at u=Xt=0 is A0=Z[X,t]/(Xt), whose normalization is N0=Z[X] plus Z[t]. The exact row

0 -> A0 -> N0 -> Z_or -> 0

has conductor difference as its last map. Thus the normalization cofiber formed on the fibre is Z_or in homological degree zero, not zero. A candidate identification with specialization of the total normalization cofiber fails. The nonzero conductor line is the explicit defect, not the old common-conductor unit.

The regression keeps the target line and its operation distinct; it does not fabricate a generic-Q map from a vanishing total cofiber. The Z case suffices to refute a universal base-change assertion. Extension to other bases requires the stated geometric hypotheses.

## Proper trace and locality boundary

The source packet's two-chart blowup trace R p_* kappa ~= S is a separate positive model. The dualizing-line overlap monomial X^a t^b e_X, a>=0, extends to the X chart when b>=0 and to the u chart when b<=a-1. Every monomial is covered; common sections have 0<=b<=a-1 and identify with X^(a-b-1)u^b. This all-degree partition explains the coefficient repair; a bounded grid test is not its proof.

Keep both charts and the line transition. The notation e_X=1/X denotes a line frame, not permission to invert X in the base. A single raw chart can lose the Cartier fibre through localization. The trace roof must be specified before asserting compatibility with derived Cartier restrictions. No scalar trace alone identifies the product divisor with a selected branch intersection.

The corrected endpoint marking remains omega tensor z with matching sheet-difference and road-sum readout. The earlier common-conductor pair is a different marking problem. Neither the local regressions here nor the reported contractible coefficient extension establish the full geometric endpoint/support-PC/generic-Q natural transformation.

## Regression and reproduction status

The standard-library checker verifies the universal symbolic f_h chain equation with an independent formal parameter h; its reduction at the crossing; the explicit homotopy between endpoint choices; integral fibre-cone ranks with unit pivots; special-node normalization on untruncated sample polynomials and its constant conductor quotient; and a bounded two-chart monomial partition control. Universal statements rely on the syzygy, exact row and partition proofs above, not on sampling coefficients or exponents.

Governing conjecture: requiring the actual base-change arrow, defect and preserved class prevents promotion of coefficient-trace success into endpoint-support equivalence. Rivals: coherent branch choices preserve first Tor; normalization cofiber automatically commutes with degeneration. The all-choice zero map and nonzero special conductor quotient refute those rivals at the stated scope. Full physical comparison remains missing; no waiting leaf is created.

Reproduction defect: the inspected rees-physical-extension directory contains only rees_physical_extension.md and rees_physical_extension_certificate.json. Its reproduction section claims three checkers are included, but none is present there, including check_rees_physical_extension.py. This suite does not reproduce or validate its reported 27310 assertions. Remedy: supply the exact scripts and dependency paths/digests matching that certificate; do not reconstruct a replacement and call it the original run.

Checker: research/nima/checkers/check_rzk_coefficient_interface_v5.py. Results: research/nima/results/rzk_coefficient_interface_v5.json. Command: python research/nima/checkers/check_rzk_coefficient_interface_v5.py through structured-command. No formal Rzk code, other-owner file, or full spatial comparison is changed. Git remains prohibited.
