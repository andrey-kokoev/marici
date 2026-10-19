# VF1 cycle 1 — verified inertia/separation of binary D blocks

The durable witness stores all 49 Hermitian D blocks, all subdiagonal L multipliers and all numerical D eigenframes/eigenvalues. Inputs enter Arb at 128 bits as exact binary dyadics. Replay reconstructs and compares the witness exactly; differing factors are refused rather than overwritten.

For each block define B=U diag(lambda) U*. Arb encloses g=||U*U-I||_F and s=||D-B||_F. If g<1, U is invertible and Sylvester's law gives inertia(B)=inertia(diag(lambda)). The singular value bound for U gives separation(B)>=(1-g)min|lambda|. If s is strictly below that separation, the Hermitian homotopy from B to D stays nonsingular, so D has the same inertia and separation(D)>=(1-g)min|lambda|-s.

The checker verifies exact binary Hermiticity, both strict inequalities and complete coverage. Numerical eigenvalues are only entries of an exact comparison witness: their signs alone are not used as source eigenvalue certificates. Ball products, norms and outward presentation endpoints provide verified subcalculations for the binary D blocks.

## Scope

This certifies the binary D-block inertia, not inertia of the original source Hamiltonian. To transfer it one still needs a verified L inverse bound, an H-LDL* residual bound linked to **these** factor bytes, and source assembly/energy-reference enclosures. A previous factor-product receipt generated its own factors; equality/linkage to the new durable witness must be checked, not silently assumed. The retained spectral-frame and full-band coupled inverse gates remain further obligations.

H7 remains open. One VF1 execution cycle is spent; two remain. Next: residual-controlled verified inverse-factor bound using the saved witness, subject to the protocol's 300-second pilot and precision limits. No stationary solve or threshold search is repeated.

Replay in the pinned source environment with python-flint installed:

    python research/scattering/high-energy/check_verified_d_blocks.py --check
