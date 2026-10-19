# Three-vertex seed candidate: retained incidence and additive-mode obstruction

**Strength:** exact finite linear-algebra identities and a scoped observer obstruction. Not a source-realization theorem, quantum-state factorization, physical annihilation result, or formal outcome admission.

[Candidate](three-vertex-candidate.v1.json) · [Exact checker](check_incidence_audit.py) · [Receipt](results/incidence-audit.v1.json) · [Original frontier](CONJECTURE-NET.md)

## 1. Operation and types first

Start with the supplied identification A'=A, B'=B, C'=C of the electron and reversed-positron cycles. It is not derived by this audit. Expand each displayed composite into its **ordered, owner-labelled primitive path**. Nothing in this operation fills a triangle or turns a path into one elementary photon occurrence.

Use the free rational primitive **cochain** carrier X=Q^10, in order

    x=(a,b,c,d,e,f,g,h,i,j)
      =(AB,BC,CD,DE,EA,AEp,EpDp,DpC,CB,BA).

The letters in this tuple denote independently variable formal coordinates, not measured particle amplitudes. Opposite arrows AB and BA are distinct occurrences, not negatives of one coordinate. Actual source states might occupy a constrained subspace; no such state-space identification is assumed here. Scalar extension of these rational identities is possible, but does not supply a physical Hilbert space.

There are two different maps:

1. **R:X→Q^18:** retain every primitive usage, path position and owner. This is a labelled coordinate-copying map into a direct sum, not a tensor-product cloning operation.
2. **B=S R:X→Q^12:** sum primitive coordinates along each displayed edge. S is an explicitly declared **additive observer**, not a source-authorized quantum composition law. Its transpose B^T expands displayed directed edge chains into primitive chains.

All spaces here are finite. There is no completion or convergence claim, and no scientific interpretation of a final scalar readout.

## 2. Full retention is reversible on a constrained image

For the two triangle pairs, the retained-use lists are

    R1 x = (a,b,i,j,c,d,e,a,b),
    R2 x = (f,g,h,i,j,i,j,a,b).

Consequently:

- rank R = **10**, with **8 compatibility constraints** in its 18-dimensional codomain;
- rank R1 = rank R2 = **7**;
- the two readouts share exactly **four input directions**, a,b,i,j;
- the multiplicity matrix is

      D = R^T R = diag(3,3,1,1,1,1,1,1,3,3).

The exact decoder is L=D^-1 R^T, satisfying LR=I. The projector P=RL is symmetric and idempotent, of rank 10. A retained output is consistent precisely when Py=y. The checker changes one duplicated occurrence independently and verifies that this hostile output is rejected by the image condition.

Thus information retention itself is possible at the bookkeeping level. **Arbitrary independent choices of the two output lists are not:** their 7+7 coordinate freedoms have four shared coordinates, leaving ten joint freedoms rather than fourteen. This is a statement about these linear readouts, not a universal no-go for physical state preparation or tensor-factor independence.

### Metric check

R is not an isometry for unweighted counting metrics: an a-only unit input has output squared norm 3, while a c-only input has norm 1. If every usage of primitive r is weighted by 1/m_r, the resulting diagonal W obeys R^T W R=I.

This gives a conditional bookkeeping isometry, not a source-derived physical metric. Selecting W does not establish independently prepared sectors, geometric gluing, or dynamical intertwining. Keeping the eight output consistency conditions remains necessary.

## 3. Additive path compression loses exactly two directions

In the original displayed-edge order,

    q1 = (AB,BC,CA,CE,EA,AC)
       = (a,b,i+j,c+d,e,a+b),

    q2 = (ADp,DpC,CA,CB,BA,AC)
       = (f+g,h,i+j,i,j,a+b).

The combined B has rank **8**, with kernel

    span{e_CD - e_DE, e_AEp - e_EpDp}.

Each separate six-coordinate output has rank five. The complete four compatibility equations for the joint twelve-coordinate output are

    q1[5] = q1[0] + q1[1],
    q1[2] = q2[3] + q2[4],
    q2[2] = q1[2],
    q2[5] = q1[5].

Indices are zero-based. The receipt contains the full matrices and checks both necessity and sufficiency by exact rank.

A minimal linear residual repair is to retain r1=c-d and r2=f-g. Then (B,r1,r2) has rank ten: recover c,d from their sum and difference, and likewise f,g. Two scalar residuals are necessary for this unrestricted free-coordinate model because ker B has dimension two. The repair restores **information**, not photon dynamics.

### Endpoints commute; faces remain absent

The chain expansion B^T commutes with directed vertex boundary maps, checked exactly on all twelve displayed edges. All four expanded triangle boundaries are closed primitive chains, but their span has rank **three**, not four: the first and fourth displayed triangles expand to the same chain

    AB + BC + CB + BA.

A closed chain is not a filled face. The computation neither provides the required two-cells nor establishes the source photon stage's topology or metric.

## 4. The additive observer does not transport the reference photon planes

Use the existing [photon mode source](../../nima/photon-two-packet-construction.md), whose ordered occurrences are (AB,BC,CA,BA,AD,DB). The checker reads its recorded rational real-plane frame and independently verifies it against endpoint incidence K:

    U = ((1,0),(-1,0),(1/2,1/2),(-1,0),(1,0),(-1/2,-1/2)),
    T = ((-1/2,1/2),(-3/2,-1/2)),
    K U = U T,     T^3 = I.

The source-owner's full historical checker suite is not replayed. These finite identities are recomputed here; the source receipt is not taken as proof of physical photon identification.

Relabel the reference vertices (A,B,C,D) as follows:

- first proposed output: (C,A,B,E), giving order (CA,AB,BC,AC,CE,EA);
- second proposed output: (C,A,Dp,B), giving order (CA,ADp,DpC,AC,CB,BA).

These are the actual shared-edge relabellings, not independent coefficient fits. Let V:Q^4→Q^12 be the resulting direct sum of two frames. If their plane coordinates are (s,t,u,v), requiring V(s,t,u,v) to lie in im B forces

    (s,t,u,v) = (s,-s,s,-s).

So the intersection of im B with the four-dimensional pair of mode planes has dimension **one**. It is nonempty: the primitive input

    (-1,0,1,0,0,-1,0,0,1,0)

maps to the intersection vector with s=1. But one reference continuation step sends its plane parameters

    (1,-1,1,-1) -> (-1,-1,-1,-1),

which violates the additive compatibility equations, with defect (1,-1,0,0). The stacked compatibility matrix before and after one step has rank four. Therefore the intersection has **no nonzero continuation-stable subspace**.

**Scoped conclusion:** with this additive B, these shared-edge relabellings and the stated reference continuation, there is no nonzero invariant photon-plane output. Merely preserving B and appending a residual cannot fix this output-continuation obstruction. A different source-authorized operation or output readout must be constructed and checked.

This is not a rejection of every encoder, retained-path dynamics, nonlinear construction, additional physical input, or interpretation of the seed. In particular, the original ordered paths do not automatically compose by summing arbitrary amplitudes: B is precisely the proposed linear shortcut being tested.

## 5. Updated local next step

The broad work-net frontier remains open; no existing contract, source pin or formal outcome is changed by this audit.

The next construction must specify an actual operation on the **retained histories**, an output map and explicit residuals, rather than identifying additive edge totals with the six photon occurrences. Test:

1. source permission for the operation and its input state carrier;
2. lossless recovery or a justified quotient, without discarding reused histories;
3. a commuting continuation square on the proposed output modes;
4. transport of the source metric and the two filled faces;
5. only then, independently meaningful output sectors and physical channel binding.

The finite B-obstruction is an early falsifier for future proposals, not a replacement for those constructions. No physical annihilation or ratio 372 is derived.

## Reproduce

```sh
python research/scattering/seed-composition/check_incidence_audit.py
python research/scattering/seed-composition/check_incidence_audit.py --check
python research/scattering/seed-composition/check_seed_composition_net.py
python research/scattering/low-energy/check_low_energy_net_v3.py
```

The new checker uses Python's exact `Fraction` arithmetic, writes only its own receipt (or compares it read-only with `--check`), and records input/checker hashes. Existing pinned net documents are intentionally left unchanged so their upstream source identities remain valid.
