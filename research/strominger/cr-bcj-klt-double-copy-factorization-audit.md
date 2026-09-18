# CR-compatible BCJ/KLT double-copy audit

## Result

**Partial factorization only; the first missing arrow remains**

\[
CR^{\rm SYM}\not\longrightarrow CR^{\rm BCJ}.
\]

Current sources construct amplitude-level BCJ/worldsheet quotient identities, full-color DDM dressing, exact soft kinematics, and an abstract graviton helicity projector. They do not construct Jacobi numerators on Coherent Resolution generators or a chain map commuting with the CR differential.

## Arrow audit

### 1. CR to BCJ/Jacobi-enriched CR — obstructed

At six points all 24 fundamental BCJ component forms vanish after evaluation. However, all 24 corresponding raw CR chains remain nonzero, and all Parke–Taylor-dressed chains remain nonzero. Thus BCJ descent occurs in the worldsheet/scattering-equation quotient, not in the current CR carrier.

No local source assigns cubic-graph numerators `n_i` to CR generators with

\[
n_i+n_j+n_k=0
\]

for every color-Jacobi triple while also providing chain maps `F_k` satisfying

\[
d_{\rm BCJ}F_k=F_{k-1}d_{\rm CR}.
\]

This is the first missing arrow.

### 2. Two gauge copies to gravity — not constructed on CR

The six-point CHY/DDM work constructs full nonabelian color dressing and basis independence. Color dressing is not a second kinematic numerator copy. Existing KLT references, inverse matrices, and pairing analogies do not provide a KLT bilinear on CR chains or prove compatibility with the CR differential.

Squaring evaluated canonical weights would bypass the failed chain-level step and import the desired comparison rather than derive it.

### 3. Graviton-sector projection — abstractly constructed

On the two-copy helicity basis

\[
(++,+-,-+,--),
\]

the exact projector

\[
\Pi_{\rm grav}=\frac{(h_1+h_2)^2}{4}
=\operatorname{diag}(1,0,0,1)
\]

is idempotent, rank two, and parity-natural. This correctly removes the mixed zero-total-helicity sector. But no sourced CR state pairing feeds this projector, so it is a valid downstream component rather than a completed arrow.

### 4. Gravity to Bondi radiative complex — not constructed

The exact `epsilon`-soft family supplies real momentum-conserving kinematics and a nonzero hard limit. It does not normalize a projected gravitational state to `C_AB`, `N_AB`, the radiative symplectic form, or the Bondi differential. Therefore no leading/subleading soft mode has yet been intertwined with BMS charge or memory data.

## Exact independence checks

The audit verifies simultaneously:

- arbitrary finite `CR_m` is exact;
- the exact soft family exists;
- amplitude-level BCJ identities pass;
- raw and Parke–Taylor-dressed CR chain BCJ identities fail;
- full-color DDM dressing exists;
- the abstract graviton projector exists;
- CR-compatible Jacobi numerators, second copy, typed state pairing, and Bondi chain map are absent.

## Minimum executable repair

At six points:

1. assign a cubic-graph Jacobi numerator vector to every relevant CR generator;
2. publish matrices `F_k` and verify `d_BCJ F_k = F_(k-1) d_CR` exactly;
3. require all 24 fundamental BCJ combinations to vanish as enriched chains, not only as evaluated forms;
4. only then add the second copy, state pairing, `Pi_grav`, and Bondi normalization.

This does not deny the standard amplitude-level double copy. It identifies what the current source corpus has not constructed at chain level.

## Evidence

- `research/strominger/checkers/cr_bcj_klt_double_copy_factorization_audit.py`
- `research/strominger/results/cr_bcj_klt_double_copy_factorization_audit.json`
- `research/nima/results/six-point-nmhv-bcj-chain-relation.json`
- `research/nima/results/six-point-chy-full-color-dressing.json`
- `research/nima/results/little_group_graviton_projector.json`
- `research/nima/results/arbitrary-n-exact-soft-family.json`
