# Witnessed reference substitution with retained parents

## A reference-changing operation already supported by the data

Each retained comparison has an actual map C_i and witness h_i with

    delta(h_i)=C_i-d.

Choose one retained comparison as the new reference. Its existing witness
kappa=h_j supplies the reference-change boundary C_j-d. No new matrix-valued
coupling or edit metric is needed for this construction.

This changes the comparison standard while keeping actual slot maps fixed. It
is distinct from passive relabelling, which transports those maps too. Whether
changing a standard is also a physical intervention requires a measurement
interpretation. The data make this operation available; they do not select when
or which reference to choose.

## One update rule

For any supplied kappa with delta(kappa)=d_new-d, retain the return r and set

    h_i_new=h_i-kappa,
    u_new=u+r*kappa,
    v_new=v+kappa*r,
    W_new=W+kappa*u+v*kappa+kappa*r*kappa.

The new records satisfy

    delta(h_i_new)=C_i-d_new,
    delta(u_new)=r*d_new-1_A,
    delta(v_new)=d_new*r-1_B,
    delta(W_new)=d_new*u_new-v_new*d_new.

Every previous record is retained as an immutable parent. Retaining history
therefore does not require freezing the current witness coefficients while their
reference changes. The earlier protected-active protocol made that additional
choice and remains a separate operation type.

## Composition, return and family promotion

Apply the rule with kappa1 and then kappa2. The current state agrees exactly with
one application using kappa1+kappa2, including the quadratic triangle term.
Selecting reference j and then k gives total witness h_k. Returning to the old
reference uses the retained witness -h_j and restores all current fields. A
repeat selection of the current reference is a no-op. Different operation
histories remain separately recorded.

An incoming retained family F already has a weighted actual map and witness:

    C_F=sum_i w_i*C_i, h_F=sum_i w_i*h_i, sum_i w_i=1.

Thus delta(h_F)=C_F-d, making the newly labelled family an available reference
candidate. The checker constructs all32 incoming-family records from the137
slots, retains their members, and applies the same reference rule twice using
two of those families. Transported member masses also produce a total-family
anchor; direct and staged weighted aggregation agree.

This supplies a reference operation on promoted records. It does not select
next-level from/to fields for the complete family tower.

## Observable consequences

The actual paths and their slot count remain unchanged. Residuals transform as

    R_i_new=R_i-R_j

when selecting slot j, or by the corresponding family residual when selecting a
family. Every alternating four-slot rectangle is unchanged, including its
factored mixed response. The mean residual shifts by the chosen reference change.

In particular, the retained total-family mean C_bar can be chosen as reference.
It gives zero mean residual while preserving every mixed defect. For the fixed
matrix inner product used by the existing prototype,

    mean_i ||C_i-d||^2
      = mean_i ||C_i-C_bar||^2 + ||C_bar-d||^2.

The exact checker verifies this split. The variance term is independent of the
comparison standard; the second term records its offset from the mean.

The operator has since specified rung4 as the physical-reference locus; see
[rung transport diagram](rung-transport-diagram-and-fixed-reference.md).
Reanchoring changes local comparison coordinates while retaining the offset to
that fixed reference: C-d4=(C-d_local)+(d_local-d4). Setting the local mean
residual to zero therefore preserves the rung4-relative offset. The physical
reference is not replaced by the local mean. Its numerical realization and
readout, together with those of the mixed defects, remain to be constructed.

## Domain and authority boundary

The comparison domain is explicitly fixed during these updates. The original
137 slots and their retained primitive exclusion policy remain unchanged; new
reference candidates are auxiliary records, not newly counted slots. If physical
reference changes must also change which primitive arrow is excluded, an
additional carrier/reference-to-mask adapter is required. Selecting a composite
or family mean as a comparison standard does not itself provide that adapter.

The construction uses the free DG shared-leg model with explicitly adjoined
weak-return unit and triangle witnesses. It verifies formal boundaries and the
existing matrix response, without claiming that witness adjunction or reference
selection is a derived physical dynamics law.

## Verification

    python research/nima/checkers/check_witnessed_reference_reanchoring.py

Exact formal path arithmetic and rational matrix readouts: all137 slots and32
family candidates, two reference changes, direct/staged equality, round-trip
restoration, idempotence, immutable parents, family mass transport, preservation
of all109 rectangles, total-mean reference and the mean/variance norm identity.
