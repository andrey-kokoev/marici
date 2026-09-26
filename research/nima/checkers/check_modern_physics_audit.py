"""Systematic audit: what modern physics is connected vs missing."""
print("=" * 72)
print("GRAM UNIFICATION: CONNECTIVITY AUDIT")
print("=" * 72)

audit = {
    "CONNECTED (verified or sketched)": {
        "QM Born rule": "rank-1 Gram factorization G_ij = psi_i* psi_j",
        "QM N-path interference": "I = sum G_ij exp(i(theta_j - theta_i))",
        "GR spatial metric": "g_ab(p) = G_ab (stabilizer Gram)",
        "GR ADM constraints": "close on finite carrier, (+++-) signature",
        "GR continuum limit": "delta(x,y) constructed from N -> inf carrier",
        "LQG holonomy-flux": "structural match, SU(2) promotion from cocycle",
        "SM gauge group": "SU(3)xSU(2)xU(1) from S4 irrep (1+1+2)",
        "SM 3 generations": "S12 -> S4xS4xS4 branching",
        "SM CKM quark mixing": "Gram misalignment between up/down bases",
        "SM sterile neutrinos (DM)": "3 nu_R states, Y=0, 25% Gram trace",
        "SM cosmological constant": "uniform diagonal Gram entries from transitivity",
    },
    "PARTIALLY CONNECTED": {
        "SM Higgs mechanism": "mass scale from Gram eigenvalues, Higgs vev not placed",
        "SM fermion masses": "hierarchies from Gram eigenvalues, Yukawa not placed",
        "QCD confinement": "SU(3) as S3 subgroup stabilizer, dynamics not checked",
        "Neutrino masses": "seesaw via nu_R, mixing angles not computed",
        "Dark energy dynamics": "uniform Lambda from Gram trace, w=-1 exact",
        "Inflation": "early phase dynamics via carrier expansion? Not formalized",
    },
    "MISSING (not connected)": {
        "SM PMNS lepton mixing": "Should exist from Gram misalignment in lepton sector, not computed",
        "SM anomaly cancellation": "Fermion content must be anomaly-free, not checked",
        "SM Higgs particle": "Scalar SU(2) doublet, not placed in carrier",
        "Strong CP problem": "Neutron EDM bound theta < 1e-10, no axion mechanism",
        "Baryogenesis": "Matter-antimatter asymmetry, not addressed",
        "Entanglement": "QM predicts Bell violation, not shown in Gram picture",
        "Hawking radiation": "Black hole evaporation, not addressed",
        "String theory": "10D, Calabi-Yau, branes - no connection",
        "Twistor theory": "Penrose's program - no connection",
        "Non-commutative geometry": "Connes' program - no connection",
        "Causal sets": "Discrete spacetime - structurally related but not explicit",
        "Fine-tuning": "Hierarchy problem, cosmological constant problem - not resolved",
    }
}

for category, items in audit.items():
    print(f"\n{category}")
    print("-" * 72)
    for item, desc in items.items():
        status = "[" + ("O" if category == "CONNECTED (verified or sketched)" else 
                      ("~" if category == "PARTIALLY CONNECTED" else " ")) + "]"
        print(f"  {status} {item}: {desc}")

print("\n" + "=" * 72)
print("MOST CRITICAL MISSING:")
print("  1. PMNS mixing (leptons) - Gram should give it, not computed")
print("  2. Anomaly cancellation - powerful constraint, not checked")
print("  3. Higgs mechanism - mass generator not placed in carrier")
print("  4. Strong CP / axion - Theta < 1e-10 not explained")
print("  5. Full fermion content - S4 (1+1+2) gives only 3 gauge rep types")
print("     SM needs 5 types (Q_L, u_R, d_R, L_L, e_R) + nu_R")
print("=" * 72)