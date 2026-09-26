# Universal Ward reduction, rather than sampled rank evidence

Fresh symbolic construction proves why the single-flavor space has dimension3 for generic on-shell7-point kinematics. On the regular frame open <12>[67]!=0, normalize lambda columns1,2 and tilde-lambda columns6,7 to identity independently. Keep the other ten lambda entries and six tilde entries free; momentum conservation determines tilde columns1,2. The checker retains all16 parameters symbolically.

Let L be the2x7 lambda row matrix and R the tilde matrix. Momentum conservation gives L R^T=0. Set U_i=e_(i+2)-R_(1,i+2)e_6-R_(2,i+2)e_7 for i=1,2,3. Then K=(L;U) is a basis for ker R: its first5 columns have determinant1.

A single-flavor4-form annihilated by both anti-supercharges lies in Lambda^4(ker R). Requiring multiplication by each of the two Q rows to vanish forces divisibility by L1 wedge L2. The remaining factor lies in Lambda^2(ker R/span L), a space of dimension binomial(3,2)=3. A basis is L1 wedge L2 wedge U_i wedge U_j, i<j.

Its coefficient matrix on subsets1234,1235,1245 is IDENTICALLY identity3. Therefore those three components determine every allowed single-flavor4-form without amplitude-dependent pivot selection. Products over four flavors reduce to fifteen symmetric quartic identities for sums of identical-flavor fourth tensor powers.

`check_seven_point_universal_ward_basis.py` verifies the symbolic basis, kernel/frame determinants, and336 Q-wedge/anti-Q-contraction identities. `check_seven_point_ward_reduced_parity.py` then applies this kinematics-only basis to all twelve amplitude vectors at the existing two rational inputs, verifying all420 embedding entries and all15 parity quartics at each input.

Important boundary: the universal basis is proved generically, but membership of the implemented amplitudes and their fifteen parity identities have not yet been established over the full generic six-modulus chart. The symbolic two-parameter amplitude proof remains the strongest current continuous amplitude result. This turn removes the need to recompute35 minors and an empirical rank decomposition for a future generic calculation; it does not claim that calculation is done.

Next compute only the1234,1235,1245 minors of each of the twelve amplitude terms on the generic momentum-twistor chart, separately checking the Ward conditions on their row spaces. This is a concrete smaller generic proof obligation. Normalization of the spinor frames changes the common basis but does not justify discarding Parke-Taylor or Fourier prefactors.
