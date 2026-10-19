# Pivot/normal covariance and physical contour — iteration 2

Freshly read pins v41, the covariance receipt, the signed directional residue table, and the owning source kernel, contour and homological-identity passages. This turn constructs the local integral contour lattice and verifies its marked-pole periods under the previously tested normal/direction changes. It does not select a physical cycle.

## Exact lattice and split obstruction

After dividing periods by 2*pi*i times the shared external fermionic constraint current, the retained one-forms are

    K0=-drho/[rho(1+rho)], B22=-drho/(1+rho).

On P1 minus {0,-1,infinity}, positively oriented local loops C0,Cminus1,Cinfinity obey C0+Cminus1+Cinfinity=0. The integral homology is Z3/<(1,1,1)>. The split period matrix is

    [-1, 1, 0]
    [ 0,-1, 1].

In quotient coordinates (w0-winfinity,wminus1-winfinity), its matrix is [[-1,1],[0,-1]], with determinant1. Thus the two split periods detect every integral homology class: for generic nonzero shared amplitude, **no nonzero contour class annihilates both splits**. This is not a demand that a physical contour kill both periods; it rejects that proposed shortcut to split cancellation.

The full three-loop zero is the null homology relation, not a discovered nontrivial physical cycle. C0+Cinfinity has periods(-1,+1), total0, and is homologous to -Cminus1. The total form alone cannot detect the central-loop class. Consequently total cancellation cannot certify split cancellation or positive-cycle admission. Small complex loops around the positive endpoints are not the positive real integration interval.

The checker verifies the integer quotient identity symbolically and 125 winding controls, including invariance under adding the relation. It also recomputes residues at the three mapped marked poles in all three prior normal/direction frames, restoring the external delta determinant before comparison. All period matrices agree, including orientation-reversing frames.

## Positive relative interval and source scope

For 0<epsilon<L the positive relative interval has coefficients

    int K0 = log(1+L)-log(L)-log(1+epsilon)+log(epsilon),
    int B22= -log(1+L)+log(1+epsilon),
    total  = log(epsilon/L).

The unregularized K0 coefficient diverges at0 and B22 at infinity. An endpoint/branch/regularization prescription is additional data; no finite integral or closed contour is selected by positivity alone.

The owning source `1212.5605/positive_grassmannian_update.tex` specifies Gamma_hat_sigma in `general_on_shell_function_momentum_twistors` (line1266), discusses excess constraints as singular external support (line157), and uses oriented Cauchy identities for generic dimension4k+1 cells in `homological_identities_subsection`. Those statements are compatible with the scoped construction but do not identify its exceptional rho contour. Here the source has dimension7 with8 bosonic constraints and a retained fiber over external codim2 support, rather than a generic9-dimensional k=2 cell localized to an ordinary one-form. Real loop-momentum contours are likewise not automatically these exceptional cycles. Exact source anchors are retained in the receipt.

## Next executable continuation

Lift the candidate direction cycles from ordered small normal-link tori in (b2,b3). Track rho=b2/b3, the b2+b3 pole, radius hierarchy and source orientation; identify induced homology classes and wall crossing. Then compare the needed selection data with the owning Gamma prescription. No arbitrary winding, added nonpositive pole, or endpoint subtraction is admitted merely to fit a desired cancellation.

Evidence: `checkers/check_history6_current_contour_lattice.py`, `results/history6_current_contour_lattice.json`. Initial direct SymPy import failed in the project interpreter; using the existing checker import bootstrap yielded a passing fresh run without changing formulas. Scientific verdicts unchanged; pins v42 and structural checks are separate. Physical admission and global gluing remain open.
