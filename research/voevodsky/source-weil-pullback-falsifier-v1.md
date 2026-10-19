# Test verdict: the current bridge does not pull back the positive source form

## Fix the claim before testing

The conversational conjecture asked for a source-derived analytic realization
J and a positive source form Q with Q(v)=W(Jv*(Jv)^*) on a sufficiently rich
domain. It did not specify a unique future realization or form. The executable
candidate tested here is the one already constructed, not an arbitrary new
map selected after observing the outcome:

- Strominger's independently constructed twelve-arrow source;
- its declared positive coefficient metric G12=10I+J;
- its declared Hamiltonian H(x)=x^T K12 x/2 at alpha=1/2;
- the actual four-port analytic attachment R_a=B_a Jport P;
- its unshifted Riemann specialization R_0.

SCC obligation: form/readout descent. We test both available source quadratic
forms. Failure of either is not a theorem about every unspecified alternative
form or every future infinite realization.

## Necessary condition

For ANY quadratic form b on an analytic target and ANY linear map R, its
pullback vanishes on ker R. Therefore

  Q=b pulled back through R  implies  Q(h)=0 for every h in ker R.

In particular the Weil functional applied to the zero test is zero. This test
requires no zero list, prime cutoff, quadrature or unproved positivity.
The comb image need not itself be an admissible Weil test: any linear
preparation from that image to admissible tests still sends zero to zero.

## First exact witness: positive hidden energy

Use source order AD,CA,DB,BC,AB,AC,BA,BD,CB,CD,DA,DC and choose

  h=14 e_AB-e_AD-e_CA-e_DB-e_BC.

The actual projection is P=[I4 | J_(4,8)/14], so Ph=0 and R_a h=0 for every
generic shifted-comb seed a. Direct calculation gives

  h^T G12 h=2100,
  H(h)=h^T K12 h/2=980.

Both source forms are positive on a state whose analytic image is zero.
Consequently neither can equal the Weil pullback through this map on the full
source. No nonzero scalar normalization can repair 2100=0 or 980=0.

The earlier retained split remains correct:

  G12=P^T G4 P+N^T G12 N,
  K12=P^T K4 P+N^T K12 N, N=I-EP.

The hidden metric has rank eight and hidden energy has rank four. Keeping Nx
in an archive recovers the source, but does not make the analytic Weil readout
see that energy. Replacing Q by its visible part changes the conjectured form.

## Second exact witness: restriction to the visible four-plane is not enough

At the unshifted Riemann specialization the four comb ports all become Delta_Z.
The coefficient map is the sum of cyclic ports. Thus

  v=e_AD-e_BC

lies in the visible four-plane but R_0 v=0, while

  v^T G12 v=20, H(v)=20.

So merely discarding the original eight hidden directions does not repair the
Riemann specialization. Its analytic image loses three more visible directions,
including this active rotor vector.

## Verdict and implications

**Falsified:** the current analytic attachment transfers either the complete
positive coefficient metric or the complete declared Hamiltonian to the Weil
form on all source states.

The operation intertwiners, six-step descent, retained-history connections and
Fourier/Mellin identities are unaffected. They did not assert this positive-form
identity. The finite atom-to-character bridge on the separate channel lattice
is not tested as though it were an identified twelve-arrow constructor.

A form on a genuine quotient must annihilate its discarded directions. Here
they carry positive source norm and sometimes positive source energy. A repair
therefore must change something substantive: construct an analytic map that
retains those directions, change the domain, or specify a different form and
justify it independently. Matching a quotient metric by definition does not
establish that it is the Weil form.

This test settles the concrete existing candidate, not the unquantified claim
that some source-derived realization might exist. Before testing that stronger
claim, the actual map, form, admissible domain and completion must be fixed.

## Verification

`uv run research/voevodsky/checkers/check_source_weil_pullback_falsifier.py`
reconstructs the source and checks its pinned receipt hashes, both witnesses,
the metric/energy split, hidden ranks and the distinction between the old form
and its visible replacement. Result:
`results/source-weil-pullback-falsifier-v1.json`.

The checker exits zero when these counterexamples are verified; the result
explicitly records `conjecture_for_existing_realization: falsified`. A passing
checker is not a passing conjecture.
