# Interaction continuation — iteration 3: full embedding and collective closure

## Actual-energy follow-up

Iteration 4, `native-joint-generator-resolvent.md`, adds the retained native
phase/alignment/seam energy to this operator audit. That enlarged library
requires an eleven-dimensional closure. The nine-dimensional result below
remains scoped to U,L,G,N and must not be used as an invariant truncation of
the full stored energy.

## Result

The local rim adapter is now embedded in a **48-complex-coordinate model**:
36 actual intrinsic belt coordinates plus 12 carrier-port coordinates. All
untouched belt coordinates remain present. The original 1836 coefficient arrows
are read and conjugated exactly, not replaced by an assumed small Hamiltonian.

The minimal invariant closures under the embedded adapter U and native L,G,N are:

| Initial space | Initial dimension | Smallest invariant closure |
|---|---:|---:|
| Native belt return, proton port character, electron current port character | 3 | **9** |
| Arbitrary independent inputs on all six two-sided local ports | 24 | **27** |

For the three named collective inputs there are **six additional hidden
coordinates**, not one. Already one application of the adapter has leakage rank
three outside the proposed visible space. Thus no four-dimensional invariant
space containing those three inputs can implement all the retained operators.

All **22 exact checks** pass. This is an exact conditional finite construction,
not a physical identification of these three inputs with E,2,3 scattering channels.

## 1. Fresh sources and unchanged records

Starting state was freshly read from `native-rim-phase-adapter.md` and the actual
intrinsic L/G/N constructor. Inputs are:

- `results/belt_three_by_twelve_store.json`;
- `results/coupled_six_piece_belt_store.json`;
- `results/native_rim_phase_adapter.json`.

The predecessor source hashes, the ambient packet root and the shared native
source root are checked before constructing the extension. No source arrows or
native selected-vector entries are fitted to obtain the closure dimensions.

## 2. Exact phase-retaining coordinates

Let d_i be the intrinsic plane-axis norm and z_i the stored selected numerator.
The physical orthonormal coefficient is z_i/sqrt(d_i). In unnormalized geometric
plane coordinates the selected coefficient is

    w_i = z_i/d_i.

All w_i are nonzero in this source. Write arbitrary coefficients as

    x_i = w_i y_i.

This is an invertible coordinate change, not deletion of phase. The full complex
w_i are retained in the receipt. The selected native vector becomes y_i=1 and
the diagonal metric becomes

    h_i = |z_i|^2/d_i.

For a stored operator numerator q_ij, the exact transformed entry is

    A'_ij = q_ij z_j/(z_i d_j).

Every one of the 1836 supplied arrows is checked in this formula. In these
coordinates the matrices become real: L is the weighted sector projector, G is
the three-sector average and N is the weighted collective projector. This is a
consequence of the stored coefficients, not a replacement interaction rule.

The calculation uses Q(sqrt(151)) with complex-linear extension. No floating
rank threshold, singular-value cutoff or external algebra package is used.

## 3. The full extension keeps all modes

Append the six carrier edge/transverse pairs. In phase-retaining coordinates
their metrics are (6,2/3), while the belt rim pairs have metrics (6,148/675).
Both edge coordinates carry the same native factor i sqrt(3), so the iteration-2
adapter matrix is unchanged by this coordinate change.

Embed its six disjoint 4-by-4 blocks. It acts as the identity on the other
**24 nonrim belt coordinates**. The full adapter is an involution and is
self-adjoint in the full positive metric, hence metric-unitary.

Extend each native belt projector as its direct sum with the identity on the
12 carrier coordinates. This convention means native belt stages do nothing to
those ports. It is **not** a derivation of the full proton or electron spinor
operator on the appended space.

The full L,G,N remain metric-self-adjoint projectors, with GL=LG=N. Native belt
matrices are covariant under the retained three-cycle. We use the co-moving
charts and explicit registration policy of iteration 2, not a newly fixed
physical electron port.

## 4. What the nine collective coordinates actually are

An orthogonal geometric basis of the minimal nine-dimensional closure is:

1. One collective over all 24 nonrim belt coordinates.
2. Lower belt rim edge collective.
3. Lower belt rim transverse collective.
4. Upper belt rim edge collective.
5. Upper belt rim transverse collective.
6. Proton carrier edge collective.
7. Proton carrier transverse collective.
8. Electron carrier edge collective.
9. Electron carrier transverse collective.

Each collective has coefficient one on its named coordinates, in the retained
phase gauge. Their disjoint-support Gram diagonal is

    (9544/225, 18, 148/225, 18, 148/225, 18, 2, 18, 2).

The initially proposed visible vectors are:

- native belt return: the sum of the first five collectives;
- proton port character: the sum of coordinates six and seven;
- electron current port character: the sum of coordinates eight and nine.

The adapter separates edge and transverse behavior. Native selection then
repopulates nonrim belt modes. These operations generate the larger space; the
three initially aggregated vectors are not closed.

On this nine-dimensional space, G is the identity and L=N. The remaining
operators are still nontrivial. The receipt stores all reduced matrices in both
the simple geometric basis and a metric-orthogonal basis whose first three
vectors span the proposed visible space. The remaining six are an explicit
orthogonal hidden complement.

## 5. How minimality is certified

Start with the stated seeds. Repeatedly apply every retained generator, retaining
an image only if it is linearly independent of the current span. Stop only when
every generator maps every basis vector back into the span.

The checker then verifies:

- seed inclusion;
- invariance under U,L,G,N;
- exact full-space reconstruction of each restricted operator image;
- a replayable construction certificate for every generated basis vector.

Each vector in a construction certificate is obtained from a seed or an earlier
generator image by recorded eliminations and normalization. Thus the final space
is generated by the allowed operations and is invariant. Any other invariant
space containing the seeds must contain it. This proves the claimed minimum
for the named inputs and operator library, not merely one successful truncation.

Because all generators are metric-self-adjoint, the orthogonal complement of
this invariant space is also invariant. We do not discard it from the full
48-coordinate model or erase its provenance.

## 6. General local inputs require 27 dimensions

The smaller nine-dimensional result relies on the specified collective inputs.
Allowing independent edge/transverse amplitudes on both sides of all six ports
starts with 24 coordinates. Its closure is exactly

    24 local port coordinates
    + one nonrim collective in each of three sectors
    = 27.

Both inclusions between this geometric description and the generated closure
are checked. Generic independently excited nonrim belt states are not included:
a concrete nonrim coordinate fails membership in the 27-dimensional space.
Those states remain in the full model. This control prevents a special-input
closure from being reported as a universal reduction of all 48 inputs.

## 7. Implication for the four-state interaction proposal

The abstract E-C-2-3 model remains algebraically valid. But **one scalar hidden
state does not reproduce this particular source-bound interface system while
retaining all three specified collective inputs and all U,L,G,N operations**.
The first-step leakage rank is already three, and the full required hidden
complement has dimension six.

This does not rule out a four-state approximation, a differently prepared input,
a different operator library or another physical identification. Each would need
its own justification and error/control statement. We have not established that
these geometric port collectives are the physical survival/two-output/three-output
channels of the supplied interaction note.

## 8. Next executable continuation

1. Freshly inspect the retained native positive-defect energy construction and
   the rule for realizing metric-unitary involutions as controlled operations.
2. Specify a joint generator using those admitted ingredients, keeping its
   coupling weights and clock assumptions explicit.
3. Restrict it to the now-certified nine-dimensional closure, retain the six
   hidden coordinates, and compute the corresponding effective resolvent.
4. Check whether any smaller dynamically invariant block is justified by that
   particular generator or preparation; do not substitute the four-state chain
   merely because it has familiar channel names.
5. Only then add specified asymptotic channel spaces and test flux normalization.

Full electron spinor coupling and a physical energy/particle correspondence
remain separate gates. No scattering or 372 prediction is claimed here.

## Reproduction

```sh
python research/voevodsky/checkers/check_native_rim_phase_adapter.py
python research/voevodsky/checkers/check_native_adapter_collective_closure.py
```

Receipt: `results/native_adapter_collective_closure.json`, containing source
hashes, phase gauges, port slots, full metric, exact reduced matrices, both
closure dimensions and generation certificates.
