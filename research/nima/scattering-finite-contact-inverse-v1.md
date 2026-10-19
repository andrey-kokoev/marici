# Finite coherent inverse for the coupled positive-contact class

## Scoped result

The fixed actual source core supplies rational bare parity functions r_s(E). At a known equal lead threshold, a complex on-shell parity amplitude t_s(E) at a regular open energy gives the coordinate-invariant response

    y_s(E) = 2 sqrt(E-theta) (1-t_s(E))/(i t_s(E))
           = A+C r_s(E)/(1-b r_s(E)),
    A=a/sqrt(beta)>0, C=g^2/sqrt(beta)>0, b>0, C<=A b.

The sign of the real g and the separate lead-coordinate scale remain gauge/observation-invisible, as in the positive-contact classification. The inverse requires exact **phase**, known theta, three distinct bare response values, a finite dressed response, and the coupled case C>0. No claim about raw intensities or unknown threshold follows.

## Three-point inverse and two-point failure

For three observations let r_i and y_i be their exact source/response values and put D_ij=(y_i-y_j)/(r_i-r_j). Finite-rank elimination gives

    D_ij = C/[(1-b r_i)(1-b r_j)],
    R = D_12/D_13 = (1-b r_3)/(1-b r_2),
    b=(1-R)/(r_3-R r_2),
    C=D_12(1-b r_1)(1-b r_2),
    A=y_1-C r_1/(1-b r_1).

For three distinct finite source values and nonzero C, r_3-R r_2=(r_3-r_2)/(1-b r_2) is nonzero. Thus the formulas are uniquely defined on the stated domain. Reconstructed parameters must satisfy A,b,C>0, C<=A b; otherwise the triple is outside this positive contact class. One energy with both parity amplitudes provides at most two r_i values. In the coupled interior, any nearby admissible b' produces corresponding positive A',C' fitting those two values exactly: two observations do not generally identify all three invariants. When g=0, y=A is constant and b is unobservable even with arbitrarily many on-shell energies.

The exact checker uses actual (even,E=4), (odd,E=4), (even,E=8) source values. It recovers the balanced invariants (A,C,b)=(2,4,2), the strict-positive completion (2,1,2), and constructs a distinct **positive** b'=21/10 alias matching both E=4 parity amplitudes but differing at the third actual source sample. Exact phase-to-y recovery is checked at all three energies. It refuses duplicate/missing source values, decoupled data, and negative squared coupling. These are source-matrix exact controls, not simulated experimental measurements or a stationary field solve.

## Limit and net disposition

This closes finite-energy identifiability only in the explicitly coupled, phase-resolved, known-threshold observation class. It does not repair inverse conditioning near the blind point, prove stability for the expanded class, infer a native extension from fitted data, or discharge the physical bridge. Work net v7 leaves native operation selection deferred and names a source-internal obstruction synthesis as the next executable task—check whether actual source files contain any additional contact/kinetic principle before declaring an irreducible missing axiom.

Checker: `research/nima/checkers/check_scattering_finite_contact_inverse.py`; receipt: `research/nima/results/scattering-finite-contact-inverse-v1.json`. Exact rational checks and a written uniqueness argument, not formal-kernel admission.
