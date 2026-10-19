# Iteration 10: typed spin channels and the multi-object closure gate

## Orbital follow-up

`multiobject-orbital-selfenergy.md` now constructs independent two-/three-object
orbital Hamiltonians and typed infinite-volume endpoint self-energies, with 41
checks and certified below-band values. It does not turn the representation
choices below into physical positron/photon channels.

## Verified result

`checkers/check_typed_spin_channels.py` passes **52 exact checks**. It binds to
the freshly regenerated native pentachoron cycle-transport receipt, including
both chiral spin lifts. The previously unfinished iterations 8–9 audit is now
completed, rather than credited as an earlier verified result.

The finite merge/split identities in the supplied note remain valid on their
specified copy algebra. They do **not** automatically act as covariant maps on
the retained electron spinor doublet. Likewise, the three stationary port leads
are not already two-/three-object asymptotic configuration spaces.

There are constructive alternatives under explicit representation choices, but
these do not derive positron or photon channels or the working ratio 372.

## 1. The spinor type obstruction

The note's algebra has basis e_0,e_1 with

    m(e_i tensor e_j)=delta_ij e_i,
    Delta(e_i)=e_i tensor e_i.

Suppose every leg of that algebra were identified with a spinor doublet V.
The central spin rotation acts as -I on V but as +I on V tensor V. Thus
covariance of a merge requires

    (-I) m = m ((-I) tensor (-I)) = m,

so m must vanish. The nonzero copy merge fails; its adjoint split fails too.
The checker also exhibits failure under the actual source-cycle lift for each
chirality, not only under an abstract central operation. This is a type failure,
not a contradiction in the original Frobenius algebra.

Two edge-seed orbits, two copy-algebra basis vectors and a spinor doublet all have
cardinality/dimension two. That is not an intertwiner identifying their actions.

## 2. A declared, type-compatible input space

For a constructive control use

    H_in = V tensor conjugate(V), dimension 4.

The conjugate partner is a **declared representation**, not a constructed physical
positron. With vec(I)=(1,0,0,1), define

    P_scalar = |vec(I)><vec(I)|/2,
    P_vector = I-P_scalar.

These orthogonal projectors have ranks one and three. The source spin action is
S tensor conjugate(S); its fifth power is I even though S^5=-I. The input thus
contains scalar and vector sectors, not a single undifferentiated encounter state.

Choose a test output representation W of dimension three, the adjoint vector
representation of the same SU(2) factor:

    R_ij = tr(sigma_i S sigma_j S^dagger)/2.

The checker verifies R's orthogonality, fifth-power identity and covariance for
both retained source lifts. It also checks all three Lie generators. This is a
representation-theoretic witness, not a transverse massless photon model or a
replacement for the retained full native mismatch records.

## 3. Explicit two-/three-output maps

For outputs in one common orbital, the symmetric internal spaces are

    H_2 = Sym^2 W, dimension 6,
    H_3 = Sym^3 W, dimension 10.

For x in H_in, define

    (M_2 x)_ij = delta_ij <vec(I),x>/sqrt(6).

For the three-output map, use the vector embedding F with columns vec(sigma_a),
and the symmetric tensor Q:

    Q_(ijk),a = delta_ij delta_ka + delta_ik delta_ja
                + delta_jk delta_ia,
    M_3 = Q F^dagger/sqrt(30).

Exact identities are

    F^dagger F=2I,  Q^dagger Q=15I,
    M_2^dagger M_2=P_scalar,
    M_3^dagger M_3=P_vector.

Both maps are exchange symmetric and covariant under the native cycles and all
three Lie generators. Their ranks are one and three. Their images sit in the
larger tensor spaces; no output is identified with a scalar channel label alone.

The scalar intermediate suffices for M_2. M_3 requires a vector intermediate in
this common-orbital construction. A scalar-to-scalar chain cannot silently supply
that missing representation.

## 4. What a scalar three-output state would need

On the complete symmetric bases the checker verifies the Casimir polynomials

    C(C-6)=0 on Sym^2 W,
    (C-2)(C-12)=0 on Sym^3 W.

Their rotation types are disjoint. The inverse of C(C-6) on Sym^3 W is
(C-11)/72. Hence any rotation intertwiner from Sym^2 W to Sym^3 W is zero.
A nonzero direct split between these common-orbital sectors requires additional
representation records or a symmetry-breaking operation.

The scalar three-vector tensor epsilon_ijk does exist in W tensor W tensor W,
but it is antisymmetric. Its Bose projection with a single common orbital is
zero. This is not a blanket prohibition of three-object outputs.

Retain three distinct orbital modes O instead. The explicitly normalized state

    Psi = (1/6) sum epsilon_ijk epsilon_abc
                 |i,a> tensor |j,b> tensor |k,c>

in (W tensor O)^tensor3 is a rotation scalar and symmetric under whole-object
exchange. Its internal and orbital antisymmetries cancel. The checker verifies
norm one, exchange symmetry and infinitesimal rotation invariance. Collapsing
all orbitals to one mode erases the state. This is a concrete witness of why the
intermediate/mismatch/orbital records must not be discarded.

No kinetic energies, photon polarizations or physical preparation operation for
this witness are supplied here.

## 5. Normalized probabilities do not fix the ratio

For independent declared conversion strengths 0<=q_s,q_v<=1, a typed isometry is

    J x = (sqrt(1-q_s) P_scalar + sqrt(1-q_v) P_vector)x
          direct_sum sqrt(q_s) M_2 x
          direct_sum sqrt(q_v) M_3 x.

Its Gram is I. For a normalized incoming density matrix rho,

    P_2 = q_s tr(P_scalar rho),
    P_3 = q_v tr(P_vector rho),
    P_survival = 1-P_2-P_3.

Two exact isometry fixtures and their probability effects are checked, including
scalar, vector-mixture and unpolarized inputs. For rho=I/4 and q_s=q_v=3/4:

    (P_survival,P_2,P_3)=(1/4,3/16,9/16),
    P_2/P_3=1/3.

Changing q_s to 1/4 while retaining q_v=3/4 gives ratio 1/9 with the same
covariance. Thus normalization and symmetry leave coupling freedom. Generally
for the unpolarized input the ratio is q_s/(3q_v). Making it 372 would require
q_s/q_v=1116: a further supplied constraint, not a derived prediction.

These are finite typed-isometry probabilities. J is not the energy-dependent
scattering operator of a constructed multi-object Hamiltonian, and these numbers
must not replace the original port flux probabilities.

## 6. Independent motion defeats the diagonal lead shortcut

The old single-coordinate collective leads have one position per port. A genuine
k-object free space has k independently moving position coordinates. Even on a
two-site test, with positive one-body edge operator

    h = [[1,-1],[-1,1]],
    H_free = sum_(a=1..k) h_a,

starting with the two-dimensional diagonal-copy span |0>^tensor k, |1>^tensor k
requires a symmetric cyclic closure of dimension k+1:

| Objects | Diagonal-copy dimension | Free closure dimension |
|---|---:|---:|
| 2 | 2 | 3 |
| 3 | 2 | 4 |

The exact rank calculation retains the mixed-position states. A single lead may
be declared as a constrained collective-motion model, but cannot stand for free
multi-object motion without this loss being acknowledged.

## 7. Status of the five requested steps

Fresh headless checks reconfirmed the earlier fixtures in this turn:

| Step | Verified conditional result | Remaining gate |
|---|---|---|
| 1. Finite identities | 44 exact finite-operator checks | Physical channel identification is not an algebra identity |
| 2. Native adapter/moving port | Source-bound discrete phase transport and labelled electron five-cycle | Continuous movement, physical clock and control costs |
| 3. Retain mismatch space | Residual records and reachable hidden coordinates are retained | Orbital and full-spinor interaction records must also be supplied |
| 4. Collective closure | Eleven-dimensional scalar port closure, not only three visible coordinates; 22 adapter/closure checks | It does not close the full spin/multi-object problem |
| 5. Asymptotic probabilities | 54 port-scattering checks, normalized flux; full-tail internal bound weights | Genuine pair/2-object/3-object kinetic channels and native vertices |

The spin-type audit adds 52 checks, rather than asserting that these open gates
are now solved. It neither calibrates nor derives the working ratio 372.

## 8. Nonredundant continuation

Construct a two-/three-object orbital Hamiltonian and explicit attachment vertices
for the retained scalar/vector/orbital records. Compute its matrix-valued spectral
measures at those vertices, then insert those self-energies into a channel-typed
central resolvent. Check positivity, flux normalization and bandwidth/threshold
sensitivity before claiming any branching ratio. This is executable continuation,
not completion of the physical objective.

## Reproduction

```sh
python research/voevodsky/checkers/check_pentachoron_cycle_transport.py
python research/voevodsky/checkers/check_typed_spin_channels.py
```

Receipt: `results/typed_spin_channels.json`. It retains exact source hashes,
projectors, typed maps, native cycle actions, orbital witness amplitudes and
kinetic closure ranks. Arithmetic is Q(sqrt(2),sqrt(3),sqrt(5),i).
