# The frozen endpoint coefficients are linear in the mixed Adams block but quadratic in self-energy

## Scope

The quarter-density correction applies when a prescribed half-density is being lifted from a quadratic energy coefficient to a linear operator amplitude. The already frozen primitive and square coefficients occur in a different constructor: they label two endpoint lifts before a mixed pairing. This note separates those uses.

For one prime (p), the frozen endpoint coefficients are

[
a_p=p^{-1/2-sigma-it},
qquad
b_p=rac12p^{-1-2it}.
]

The raw adjacent-window mixed operator has the typed form

[
B_p=L_{Q,p},D_p,L_{P,p}^*.
]

## Endpoint-amplitude typing

If the endpoint lifts factor as

[
L_{P,p}=a_p,widetilde L_{P,p},
qquad
L_{Q,p}=b_p,widetilde L_{Q,p},
]

then

[
B_p
=
b_poverline{a_p},
widetilde L_{Q,p}D_pwidetilde L_{P,p}^*,
]

up to the frozen convention for which argument is conjugate-linear.

At the seam, its magnitude carries

[
|a_p b_p|
=
rac12p^{-3/2}.
]

This is exactly the previously obtained prime-diagonal mixed summability coefficient. No quarter-density replacement is called for: (a_p) and (b_p) are already linear endpoint amplitudes.

## Self-energy typing

The same endpoint lifts contribute diagonal Gram blocks

[
A_{P,p}=L_{P,p}L_{P,p}^*,
qquad
A_{Q,p}=L_{Q,p}L_{Q,p}^*.
]

Their scalar magnitudes are therefore

[
|a_p|^2=p^{-1-2sigma},
]

[
|b_p|^2=rac14p^{-2}.
]

Thus polarization automatically squares the endpoint coefficients on the diagonal while multiplying them in the mixed block.

If instead a source theorem begins by prescribing (p^{-k/2}) directly as a diagonal Green-energy coefficient, then its linear lift is (p^{-k/4}). That is the quarter-density situation. It is not the same input typing as the frozen endpoint-current formula.

## Polarized block

The complete local block must retain the factorization

[
mathcal G_p
=
egin{pmatrix}
L_{P,p}L_{P,p}^* & L_{P,p}D_p^*L_{Q,p}^*\
L_{Q,p}D_pL_{P,p}^* & L_{Q,p}L_{Q,p}^*
end{pmatrix},
]

or the source-authorized variant with its actual diagonal energies.

This single block records all coefficient levels:

- primitive linear amplitude (a_p);
- square linear amplitude (b_p);
- primitive energy (|a_p|^2);
- square energy (|b_p|^2);
- mixed amplitude (b_poverline{a_p}).

A scalar Euler readout sees only selected products and cannot reconstruct where the square roots entered.

## Reconciliation of the two margins

For a normalized primitive incidence carrying the already frozen linear coefficient (p^{-k/2}), the bound

[
|K_{p^k}|le p^{-k/2}
]

is the correct amplitude-level estimate.

For a different constructor whose source datum is the energy coefficient (p^{-k/2}), the amplitude bound is

[
|K_{p^k}|le p^{-k/4}.
]

Both statements are correct under different typings. The defect was treating either one as universal without displaying the polarization square.

## Remaining authority gate

The raw adjacent-window source establishes the scalar coefficient product and the contraction (|D_p|le1). It does not yet prove that the analytic endpoint lifts factor exactly as (a_pwidetilde L_{P,p}) and (b_pwidetilde L_{Q,p}) on their reduced graph domains.

The next theorem must prove this endpoint factorization before closure and show that polarization commutes with cutoff assembly. Only then is the stronger norm margin (1-2^{-1/2}) authorized for the primitive linear endpoint channel.

## Result

The coefficient hierarchy is now explicit:

[
	ext{endpoint amplitudes}
longrightarrow
	ext{polarized self and mixed blocks}
longrightarrow
	ext{scalar Euler shadow}.
]

Quarter-density is required when lifting an energy coefficient. It is not required when the source already supplies a linear endpoint current. The first Adams edge therefore needs a typed polarization diagram, not a single coefficient copied across all three lenses.
