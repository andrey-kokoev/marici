# Finite contraction quotient class is canonical

## Construction

For a source map d and target r, let the contraction fiber be the nonempty affine set of source words w satisfying d(w)=r. Quotient this fiber by the translation action of ker(d).

If w and w' contract the same target, then d(w-w')=0. Therefore every nonempty fiber modulo ker(d) is a singleton. This removes representative dependence without choosing a pivot word or additional normalization.

## Verified finite diagram

- Nonempty exact contraction fibers: 264 across A12, A14, A16, and A18.
- Vertical difference cells verified in kernels: 288.
- Two-cover overlap cells verified in kernels: 144.
- Strict direct/composite coefficient matches: 108.
- Ambient source maps preserve kernels because they commute rowwise with d.

Thus the singleton quotient classes transport independently of representative throughout the verified finite diagram.

## Disposition

P5d3a is completed. The finite mechanism has a canonical ambient-compatible contraction class, although no canonical source word exists.

P5d3b becomes active: prove the constructor identities and two-monomial boundary cover uniformly for arbitrary ambient degree. Only then can the quotient classes be organized into an unbounded directed system.

The quotient class records absorption. It is not a surviving p-normal quotient line and supplies no horn/Bockstein class.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_finite_quotient_class_gate.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_finite_quotient_class_gate.json`
