# Collective carrier modes instead of independent seam resources

## Result

We analyzed the actual 36-dimensional proton and belt Hamiltonians already constructed in `native-operation-energy-lift.md`. No independent seam qubits, reservoirs or oscillator factors were added.

For the belt, the six amplitudes remaining after native phase selection and threefold alignment form an **exactly invariant sector**. There is no leakage from this sector under the full constructed energy operator. The 21 seams select one coherent ground mode and five collective excitations inside it.

The lowest excitation is a paired-face antisymmetric mode, with energy

    0.172938631059 < E_soft/E* < 0.172938631060,

where E*=pi*hbar/tau is the same declared unit as before. The proton's lowest excitation is E*/2.

These are exact structural reductions of a declared finite-dimensional Hamiltonian, not newly identified physical particles or rest masses.

## 1. The source-selected amplitude metric

Let v_j be the retained mode of triangle j within a paired sector. Its six squared norms are

    (2386,4198,2386,2386,4198,2386)/675.

Write an aligned carrier state using amplitudes a_j multiplying these modes, repeated in the three co-rotating sectors. The induced amplitude metric is proportional to diag(||v_j||^2). The factor of three comes from the three sectors and cancels from the reduced operator.

For a shared edge (i,j), the normalized mismatch projector induces

    (K_e a)_i = n_j/(n_i+n_j) * (a_i-a_j),
    (K_e a)_j = n_i/(n_i+n_j) * (a_j-a_i),

where n_j=||v_j||^2. Thus the seven seams in one paired sector define a weighted six-vertex graph Laplacian. Its weights come from the retained mode metric, not from a mass fit or an unweighted replacement graph.

## 2. Exact closure, not an uncontrolled projection

The checker constructs an embedding V from the six amplitudes into the actual 36-dimensional belt coordinates and its metric left inverse V^sharp. It checks

    V^sharp V=I,
    Q_aligned=V V^sharp,
    H V=V K,
    [H,Q_aligned]=0.

Consequently K is the exact restriction of H to this sector. Its eigenstates are genuine eigenstates of the constructed full operator; eliminating the other thirty directions does not hide a coupling correction.

Native phase and alignment energies vanish here. The remaining energy is precisely the collective seam Laplacian. The full source coefficient matrices and their weighted metric are used in these identities.

## 3. What the five excitations do

The reduced matrix has a symmetry exchanging the two faces of the paired sector. It splits into face-even and face-odd three-dimensional blocks.

The even block has exact eigenvalues

    0, 4485/3292, 5391/3292.

The odd block differs from the even block by diag(1,0,0): the bridge between the two faces penalizes their relative amplitude. Its three eigenvalues are approximately

    0.172938631059,
    1.433959780713,
    2.393101588228.

The softest eigenvector changes sign under face exchange. Removing the bridge would allow independent uniform amplitudes on the two faces; the bridge lifts that relative-amplitude freedom. This is a concrete collective formation excitation, rather than an independent excitation attached to each edge.

The complete reduced spectrum is therefore approximately

    0,
    0.172938631059,
    1.362393681652,
    1.433959780713,
    1.637606318348,
    2.393101588228.

The one-dimensional zero space is the retained coherent return. The checker factors the exact rational characteristic polynomial into the even and odd cubics. A rational Sturm count isolates the soft root in the interval above and proves it is the only odd root between zero and one. Numerical eigenvectors are supplementary, with checked residuals below 1e-11.

## 4. The entire belt spectrum

The calculation also accounts for the other thirty carrier dimensions.

The eighteen selected-phase directions consist of the six collective modes in each of the three sector-rotation characters. The trivial character contributes each eigenvalue lambda once; the two nontrivial characters contribute lambda+3/4 twice.

The other eighteen directions are phase-orthogonal triangle modes. Their six local energies are

    (1423249,4405801,1423249,1423249,4405801,1423249)/799200.

Each occurs once in the trivial rotation character and twice after adding 3/4 in the nontrivial characters. These identities are checked against the actual phase operator, not inferred from a floating-point rank.

Together these branches account for all 36 dimensions. The lowest positive energy is the face-odd collective mode above.

## 5. The proton under the same constructor

The proton operator splits into commuting local phase and tetrahedral alignment operators. Exact annihilating polynomials and joint trace moments certify their joint multiplicities.

The local phase energies are

    0, (29-2sqrt(109))/12, (29+2sqrt(109))/12.

The alignment energies and multiplicities are

| Energy/E* | Multiplicity |
|---|---:|
| 0 | 1 |
| 1/2 | 3 |
| 1 | 3 |
| 3/2 | 5 |

Add each local phase energy to each alignment energy with the listed multiplicity. This gives all 36 proton carrier eigenstates. Its ground space is one-dimensional and its lowest excitation is 1/2, below its first nonzero local phase energy.

Thus this constructor predicts a softer first internal excitation for the belt than for the proton. That comparison is not a comparison of their rest masses.

## 6. What changed after the failed mass candidate

The earlier mass candidate added a tensor factor of dimension 2^21 for independent seam resources. That was a physical implementation hypothesis, not something forced by the seam graph or return projector. Its two direct electron-gap identifications failed the neutron–proton comparison.

The source-native calculation now gives an alternative starting point: collective eigenmodes on the existing carrier, including an exactly closed six-amplitude sector. Seven seams per paired sector constrain six amplitudes and leave five excitation directions. Counting the seams as independent elementary excitations is not justified by this spectrum.

This does not prove that extra physical interface fields cannot exist. It separates the modes actually present in the retained carrier from degrees of freedom added by a proposed implementation.

The eigenvectors here are directions in a finite complex carrier space. They are not automatically independent harmonic oscillators. Summing half their eigenvalues as a vacuum energy, or choosing a sum near the observed mass difference, would require an additional quantization and reference construction.

Both retained coherent states still have zero constraint energy. The result therefore supplies a detailed excitation structure, not a positive neutron rest-energy offset. The next physical bridge must connect these collective states to the common vacuum and elementary reference, rather than reinstalling an independent seam-count energy by assumption.

## Verification

    python research/voevodsky/checkers/check_collective_carrier_spectrum.py

Output: `research/voevodsky/results/collective_carrier_spectrum.json`.

The report retains the exact six-mode matrix, mode norms, characteristic polynomials, exact soft-root interval, numerical eigenvectors and residuals, both complete spectra, and source hashes. Exact rational/quadratic-field operator identities certify closure and the spectrum decomposition. No physical mass calibration or new formal proof-assistant theorem is claimed.
