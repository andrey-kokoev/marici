# Four coherence roles on the forgotten residual cube

## Result

All four proposed coherence roles have an exact working instance on the forgotten-diamond packets. They are **four roles, not four independent higher cells**. In this model their witnesses are strict equalities; the compatibility between reconstruction and composed actions follows from the underlying associative source product.

This extends the experiment in `../voevodsky/residual-only-replay-exposes-the-hidden-interaction-hierarchy.md`. It does not identify these roles with the four faces of the outstanding actual observer-tower tetrahedron.

## The retained carrier

A packet contains up to three consecutive forgotten diamonds. Its source coefficients are rational and signed, not probabilities. The interaction coordinates are

`m_T = sum_(b contains T) a_b`.

The checker independently verifies them against actual ordered Fox coefficients, including translated packets. The envelope stores typed visible coordinates and all omitted interaction orders as residual bundles. It contains no original path-coefficient capsule. JSON round trips are part of the checks.

The public metadata records block offsets and event primes. Concatenation rejects incompatible endpoints. A change in visible order moves coordinates between visible and residual fields; it does not erase them.

## 1. Reconstruction coherence

Möbius inversion decodes the received interaction coordinates. At every visible order,

`decode(reduce_with_residuals(encode(s))) = s`.

Successive reductions agree with direct reduction as serialized envelopes. Missing residual orders are rejected, not interpreted as zero.

## 2. Source-action compatibility

For compatible disjoint consecutive packets, the interaction-coordinate product is

`m_(T union U)(xy) = m_T(x) m_U(y)`.

The transported action is implemented directly on the interaction coordinates, not by decoding and calling source multiplication. It is then checked against the independent marked-path multiplication:

`decode(propagate(e,d)) = decode(e) * decode(d)`.

Reducing either incoming view, while retaining its residuals, leaves the propagated result unchanged. Reducing the output commutes with producing it at the lower visible order.

Basis and interaction-mode checks establish the bilinear identities on the indicated rational packet spaces. These are compatible block concatenations, not all actions of the marked source algebra.

## 3. Compatibility of the first two squares

For three packets, both parenthesizations and every tested intermediate visible order yield the same final serialized envelope:

`propagate(propagate(e,d),h) = propagate(e,propagate(d,h))`.

Decoding either route agrees with actual associative source multiplication. This is the cube tying reconstruction, reduction and composed actions together.

Here it requires no additional nonzero homotopy: reconstruction is invertible as a linear encoding and the coordinate product is associative. It does not furnish an equivariant splitting of the lossy terminal recorder or of any of our nonsplit observer restrictions.

## 4. Forward prediction and backward evidence refinement

Now the observer does NOT know an exact source envelope. It retains an affine set C of rational histories compatible with the evidence. These two situations must not be conflated: an unmeasured residual is unknown, not available to the decoder.

For a declared deterministic linear source action T and an exact later-evidence set B,

`T(C intersect T^-1(B)) = T(C) intersect B`.

The left route refines earlier histories using pulled-back evidence and then predicts. The right route predicts from the retained histories and intersects with the new evidence.

This equality follows directly from set membership. The checker implements the routes separately using exact rational affine-system solving and canonical affine-space comparison, including empty fibers and the zero action. It is not an enumeration of finitely many candidate histories: each tested fiber represents its entire rational affine space.

Evidence pullback also respects composition:

`(T2 T1)^* = T1^* T2^*`.

Thus the fourth role connects to the composed-action cube rather than remaining an unrelated square. This is not Bayesian updating: no prior, probabilities, or noisy likelihoods are supplied. Nondeterministic source dynamics would require a separately typed relational version.

### Concrete example

For the first diamond, retain only the terminal evidence

`a_P + a_Q = 1`.

Append the last two forgotten relations. The future vacuum observation is `a_P`. Therefore P and Q, which have the same historical terminal reading, predict respectively one and zero.

If the later vacuum reading is one, the refined historical fiber is

`a_P=1, a_Q=0`.

The old reading remains one. What changes is the compatible-history set, not the recorded past fact.

## Negative controls

The checker establishes three failures of lossy shortcuts:

- deleting a required residual bundle is rejected;
- terminal-only data cannot determine the later vacuum prediction;
- separately compatible marginal claims need not be jointly compatible.

For the last control, the same future coordinate is constrained once to zero and once to one. Each claim separately has a compatible history, but their joint fiber is empty. Retaining only the two marginal feasibility answers would lose the decisive correlation.

## Verification and boundary

Run:

`python research/nima/checkers/check_four_residual_coherence_roles.py`

The checks include 152 reconstruction cases, 1,728 action cases, 12,000 higher-composition cases and 532 affine prediction/evidence cases, plus the actual Fox-coordinate audit and composition of evidence pullback.

Artifact:

`research/nima/results/four-residual-coherence-roles.json`

This is a successful finite prototype of the four roles. It does not supply the actual selected O_2 with missing forgotten coordinates, classify the assembled retained observer's full filtration, implement noisy physical reconstruction, or solve its tetrahedral coherence gate.
