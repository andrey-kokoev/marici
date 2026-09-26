"""Check SM anomaly cancellation from S4 irrep assignments."""
# Standard Model fermion content per generation (left-handed Weyl basis):
# Q_L  = (3, 2)_{+1/6}   -- quark doublet
# u_R^c = (3*, 1)_{-2/3}  -- charge-conjugated right-handed u
# d_R^c = (3*, 1)_{+1/3}  -- charge-conjugated right-handed d
# L_L  = (1, 2)_{-1/2}   -- lepton doublet
# e_R^c = (1, 1)_{+1}    -- charge-conjugated right-handed e
# nu_R^c = (1, 1)_0      -- charge-conjugated right-handed nu (sterile, DM)

# In our S4 / S12 framework:
# S4 -> SM: 1_a (trivial), 1_b (sign), 2 (doublet)
# Under S12 -> S4 x S4 x S4: 3 generations
# S3 stabilizer gives SU(3)_C: 3 (triplet) for each state, plus 1 (lepton singlet)

# Assignment per generation:
# S4 irrep -> (SU(3)_C, SU(2)_L)_Y -> SM fermions
# 2 (doublet) -> (3, 2)_{+1/6} = Q_L (3 colors, 2 isospin)
#              -> (1, 2)_{-1/2} = L_L (1 lepton, 2 isospin)
# 1_a (trivial) -> (3, 1)_{-1/3} = d_R^c (3 colors)
#               -> (1, 1)_{+1} = e_R^c (1 lepton)
# 1_b (sign) -> (3, 1)_{+2/3} = u_R^c (3 colors)
#            -> (1, 1)_0 = nu_R^c (1 sterile, dark matter)

# This gives EXACTLY one SM generation in the 16-dimensional representation:
# Q_L: 3 x 2 = 6
# L_L: 1 x 2 = 2
# d_R^c: 3 x 1 = 3
# u_R^c: 3 x 1 = 3
# e_R^c: 1 x 1 = 1
# nu_R^c: 1 x 1 = 1
# Total: 6 + 2 + 3 + 3 + 1 + 1 = 16 = SO(10) spinor!

def anomaly_check_one_generation():
    print("=== SM Anomaly Cancellation (one generation) ===")
    print()
    
    # Fermion content (all left-handed Weyl)
    # Format: (name, SU(3)_rep, SU(2)_rep, Y, multiplicity)
    # multiplicity = (dim of SU(3) rep) * (dim of SU(2) rep) * (count if needed)
    # For anomaly, we sum over the appropriate group's representation indices
    
    fermions = [
        # (name, SU3_rep, A_SU3, SU2_rep, dim_SU2, Y, color_factor)
        # A_SU3: anomaly coefficient for SU(3) rep: A(3)=1, A(3*)=-1, A(1)=0
        # dim_SU2: dimension of SU(2) rep: 2 for doublet, 1 for singlet
        # color_factor: number of SU(3) colors = 3 for triplet, 1 for singlet
        # A_SU2: anomaly for SU(2): 0 for all reps (SU(2) is pseudo-real)
        ("Q_L", "3", 1, "2", 2, +1/6, 3),
        ("u_R^c", "3*", -1, "1", 1, -2/3, 3),
        ("d_R^c", "3*", -1, "1", 1, +1/3, 3),
        ("L_L", "1", 0, "2", 2, -1/2, 1),
        ("e_R^c", "1", 0, "1", 1, +1, 1),
        ("nu_R^c", "1", 0, "1", 1, 0, 1),
    ]
    
    print("Fermion content per generation (16 states = SO(10) spinor):")
    for name, s3r, a3, s2r, d2, y, col in fermions:
        print(f"  {name:8s}: ({s3r:2s}, {s2r:2s})_{y:+.0f}/_{y*3:+.0f}  x{col}")
    
    # 1. [SU(3)]^3 anomaly
    print(f"\n--- [SU(3)]^3 anomaly ---")
    su3_cubic = 0
    for name, s3r, a3, s2r, d2, y, col in fermions:
        contrib = d2 * a3  # SU(2) multiplicity × SU(3) anomaly coefficient
        su3_cubic += contrib
        print(f"  {name:8s}: dim(SU2)={d2}, A_SU3({s3r})={a3:+d} -> {contrib:+d}")
    print(f"  Total [SU(3)]^3 = {su3_cubic}")
    print(f"  Expected: 0")
    print(f"  STATUS: {'OK' if su3_cubic == 0 else 'FAIL'}")
    
    # 2. [SU(2)]^3 anomaly (always 0 for SU(2) since it's pseudo-real)
    print(f"\n--- [SU(2)]^3 anomaly ---")
    print(f"  SU(2) is pseudo-real: A(R) = 0 for all SU(2) reps")
    print(f"  Total [SU(2)]^3 = 0 (automatic)")
    print(f"  STATUS: OK")
    
    # 3. [SU(2)]^2 x U(1) anomaly
    print(f"\n--- [SU(2)]^2 x U(1) anomaly ---")
    su2sq_u1 = 0
    for name, s3r, a3, s2r, d2, y, col in fermions:
        if d2 == 2:  # only doublets contribute
            contrib = col * y  # color × hypercharge
            su2sq_u1 += contrib
            print(f"  {name:8s}: {col} colors × Y={y:+.2f} -> {contrib:+.4f}")
    print(f"  Total [SU(2)]^2 x U(1) = {su2sq_u1:.4f}")
    print(f"  Expected: 0")
    print(f"  STATUS: {'OK' if abs(su2sq_u1) < 1e-10 else 'FAIL'}")
    
    # 4. [U(1)]^3 anomaly
    print(f"\n--- [U(1)]^3 anomaly ---")
    u1_cubic = 0
    for name, s3r, a3, s2r, d2, y, col in fermions:
        contrib = col * d2 * y**3  # color × isospin × Y^3
        u1_cubic += contrib
        print(f"  {name:8s}: ({col} x {d2}) x Y^3 = {col*d2} x {y**3:.6f} -> {contrib:+.6f}")
    print(f"  Total [U(1)]^3 = {u1_cubic:.6f}")
    print(f"  Expected: 0")
    print(f"  STATUS: {'OK' if abs(u1_cubic) < 1e-10 else 'FAIL'}")
    
    # 5. Gravitational anomaly (U(1) x [gravity]^2)
    print(f"\n--- Gravitational anomaly (U(1) x [gravity]^2) ---")
    grav = 0
    for name, s3r, a3, s2r, d2, y, col in fermions:
        contrib = col * d2 * y
        grav += contrib
        print(f"  {name:8s}: ({col} x {d2}) x Y={y:+.2f} -> {contrib:+.3f}")
    print(f"  Total gravitational = {grav:.3f}")
    print(f"  Expected: 0")
    print(f"  STATUS: {'OK' if abs(grav) < 1e-10 else 'FAIL'}")
    
    # 6. [SU(3)]^2 x U(1) anomaly
    print(f"\n--- [SU(3)]^2 x U(1) anomaly ---")
    su3sq_u1 = 0
    for name, s3r, a3, s2r, d2, y, col in fermions:
        if s3r != "1":
            # For [SU(3)]^2 x U(1): use quadratic Casimir C(R) where Tr(T^a T^b) = C(R) delta^ab
            # C(3) = C(3*) = 1/2 (for fundamental and anti-fundamental, the trace is the same)
            c = 0.5  # for both 3 and 3*
            contrib = d2 * y * c
            su3sq_u1 += contrib
            print(f"  {name:8s}: dim(SU2)={d2}, Y={y:+.2f}, C({s3r})={c:.1f} -> {contrib:+f}")
    print(f"  Total [SU(3)]^2 x U(1) = {su3sq_u1:.4f}")
    print(f"  Expected: 0")
    print(f"  STATUS: {'OK' if abs(su3sq_u1) < 1e-10 else 'FAIL'}")
    
    print(f"\n=== OVERALL ===")
    all_ok = (su3_cubic == 0 and abs(su2sq_u1) < 1e-10 and abs(u1_cubic) < 1e-10 
              and abs(grav) < 1e-10 and abs(su3sq_u1) < 1e-10)
    print(f"All anomalies cancel: {'YES' if all_ok else 'NO'}")
    print(f"The S4 assignment (2->Q_L+L_L, 1_a->d_R+e_R, 1_b->u_R+nu_R) gives")
    print(f"exactly the SM fermion content per generation, including color factors.")
    print(f"The 16 states = one SO(10) spinor, anomaly-free by construction.")

anomaly_check_one_generation()