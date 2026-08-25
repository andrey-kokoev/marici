# Twenty-six-contact exRec fault table

Owner: `marici.Kitaev`

Status: exhaustive macro-location single/pair audit; microscopic factory pairs
remain unavailable where the source itself is absent.

## Frozen contact order

The recovered controlled-power extractor has 26 two-block contacts:

1. four holonomy compute contacts;
2. three forward relative-shuttle contacts;
3. transporter alignment;
4. four forward class/Fourier contacts;
5. flux-label and charge-label contacts;
6. four inverse class/Fourier contacts;
7. transporter unalignment;
8. three reverse relative-shuttle contacts;
9. four holonomy uncompute contacts.

Both incident blocks undergo the explicit distance-three recovery after every
contact.  The schedule therefore has 26 contact-fault classes and 52
block-recovery fault classes.

## Exhaustive support automaton

The checker enumerates all 78 single macro faults and all

\[
\binom{78+1}{2}=3081
\]

fault pairs, including two distinct microscopic faults represented inside the
same macro class.

A contact fault conservatively adds one rail error to each incident block.  A
faulty recovery fails to clear its input and adds one error to that block.  An
ideal recovery clears zero or one error and declares two errors malignant.

Results:

- single faults: 78/78 contained, zero malignant;
- pairs: 2,861 benign and 220 malignant;
- first malignant accumulation: 71 at a contact and 149 at recovery.

The complete row table, including first failed block and schedule location, is
stored in the result JSON rather than expanded into this packet.

## Meaning of the count

This proves the declared schedule-level distance-three claim: one macro fault
never exceeds one residual rail error in an encoded block.  It also identifies
every macro pair that can exceed the code distance under the conservative
model.

It is not a physical threshold coefficient.  A microscopic count requires
the internal contact, Choi verification, cat preparation, and magic-state
factory circuits.  The first three now have bounded interfaces; the
controlled-inversion and controlled-phase factories do not exist in the
frozen source, so their internal malignant pairs cannot honestly be counted.

## Verification

Run:

```text
python research/kitaev/checkers/check_s3_26_contact_exrec_fault_pairs.py
```

Saved output:
`research/kitaev/results/s3-26-contact-exrec-fault-pairs.json`.
