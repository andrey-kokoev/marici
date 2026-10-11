# Shape-interaction continuation — iteration 1: finite-operator audit

## Disposition

The central finite-operator identities in the supplied
`braid-composition-effective-shape-interaction-operators.md` now have an
independent exact checker. All 44 checks pass. The original note remains
unchanged. This is not verification of its whole braid/geometric/empirical chain,
nor a construction of a native particle interaction.

Freshly read starting state: the supplied note's finite-operator sections and
`braid-shape-interaction-implications.md`. No additional numerical/symbolic
package was installed. The checker uses the Python standard library with exact
Q(sqrt(2),i) arithmetic and sparse multivariate rational polynomials.

## Verified identities

### Braid and crossing-phase matrices

- A=(I+iZ)/sqrt(2) and B=(I+iX)/sqrt(2) are unitary.
- ABA=BAB, while AB is not BA.
- The two explicitly stated same-coset histories give the stated orthogonal
  internal states.
- The crossing-phase Hamiltonian formula is checked at three exact phases;
  its I/X spectral projectors are checked for arbitrary scalar coefficients.
  They give the stated two-channel sinusoidal transition law, with the identity
  term contributing only a common phase.

This does not audit the infinite history-space walk or prove a physical exchange
interpretation for the supplied matrices.

### Frobenius composition and channel isometry

The explicit two-state multiplication/comultiplication satisfy associativity,
coassociativity, commutativity, cocommutativity, unit/counit and Frobenius
compatibility. Both conversion maps have Gram operator P, the same rank-two
orthogonal matching-label projector.

The scalar polynomial identity

    (1-q) + qp + q(1-p) = 1

and those matrix identities prove S* S=I for every p,q in [0,1]. In addition,
an exact fixture with p=1/2, q=8/9 constructs the actual 16-by-4 isometry and a
20-by-20 unitary completion. For an isometry S, the completion used is

    U = [[S, I-SS*],
         [0,   -S*]].

Both U*U and UU* are checked, not merely its action on one input.

Negative controls:

- multiplication destroys unequal-label inputs unless the survival channel is
  retained;
- the split copies its distinguished basis but does not clone an arbitrary
  superposition;
- split-after-merge is P, not the identity on all four input coordinates.

### Three-state model and symmetric square

Exact spectral projectors for the equal-coupling chain reproduce the stated
propagator and probabilities. Their normalization and

    P(2)^2 = 4 P(E) P(3)

are verified as polynomial identities modulo cos(x)^2+sin(x)^2=1.
The stated symmetric-square embedding is isometric and its image invariant
under X tensor I + I tensor X. This is a genuine closure result for the
**declared binary toy model**, not yet for the geometric port records.

The ratio 34596:372:1 and P(E)/P(2)=93 follow exactly when the working ratio
372 is imposed. They are conditional arithmetic, not independent predictions.

### Four-state model

For arbitrary symbolic real a,b,c, the Hamiltonian is Hermitian, hence generates
unitary finite-dimensional evolution. An independent Taylor expansion through
order eight verifies probability conservation and the stated leading terms:

    P(2) = a^2 b^2 t^4/4 + O(t^6),
    P(3) = a^2 b^2 c^2 t^6/36 + O(t^8).

The leading-ratio cancellation of a,b is exact for fixed nonzero couplings in
the short-time limit. Choosing ct from the working ratio alone does not prove
that |a|t and |b|t are small enough for that approximation.

The three-state binomial relation does not carry over. Its defect in this model
has leading term

    P(2)^2 - 4 P(E) P(3) = -a^2 b^2 c^2 t^6/9 + O(t^8).

## Full resolvent and Schur-complement verification

The characteristic polynomial is

    D(z) = z^4 - (a^2+b^2+c^2)z^2 + a^2 c^2.

The checker constructs the entire adjugate and verifies both matrix inverse
identities polynomially. In particular,

    G_2E(z) = abz / D(z),
    G_3E(z) = abc / D(z).

Thus z G_3E=c G_2E holds identically wherever the resolvent exists. Dividing
requires the relevant nonzero denominators; a=b=0 or a disconnected conversion
path does not furnish a meaningful branching ratio.

The projected resolvent is checked against the full Schur complement, in both
multiplication orders. This is stronger than checking only the last-row ratio.
The note's H_eff(z) is recovered for z!=0 outside the spectrum.

A useful qualification: the 1/z self-energy pole need not be a pole of the full
resolvent. D(0)=a^2 c^2, so the full resolvent is regular at zero when a,c are
nonzero even though this particular eliminated representation is singular there.

## Hidden-state loss controls

For an initial E state,

    P(C) = a^2 t^2 + O(t^4).

Consequently, simply keeping the E,2,3 coordinates gives visible norm
1-a^2 t^2+O(t^4), not a closed unitary evolution.

If C is deleted without retaining its self-energy, the E-to-2 resolvent entry
vanishes. In the full model its numerator is abz. This gives an explicit
counterexample to replacing elimination by erasure.

The result supports the requirement to retain native mismatch/intermediate
information. It does not identify our actual mismatch space with the scalar C
state; that is a later closure question.

## Current five-step frontier

1. **Finite-operator audit:** completed for the central finite identities listed
   above. The complete 35-section supplied investigation is not certified.
2. **Native phase adapter and moving electron port:** next executable step.
3. **Retained native intermediate/mismatch space:** must be built with that
   adapter; the toy C-state audit is not a substitute.
4. **Collective closure of the actual geometric interaction:** not established.
5. **Asymptotic channels and normalized scattering probabilities:** not yet built.

For step 2, freshly read `neutron-rim-port-transport.md`, its checker and receipt,
and the native triangle-mode constructors. Keep the documented 4198/675 versus
20/3 norm mismatch explicit. Construct a reversible metric-compatible adapter
with retained auxiliary information rather than identifying unequal vectors.
Specify transport of the electron's ABC port through its supplied five-cycle;
do not silently replace that action by a port-preserving three-cycle.

## Reproduction

```sh
python research/voevodsky/checkers/check_shape_interaction_finite_operators.py
```

Receipt: `results/shape_interaction_finite_operators.json`, including every check,
exact series coefficients, characteristic polynomial, transfer numerators and
hashes of the supplied note and checker. No physical identification, coupling
calibration, prediction of 372 or scattering theorem is claimed by this audit.
