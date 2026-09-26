"""SM RG: run from M_Z DOWN to low energy, check vev -> 246 GeV (Gram value)."""
import math

r_S12, l_U1, l_SU2, C_U1 = 11, 12, 4, 10

# Gram exact values at q^2 = 0:
v_gram = 2 * r_S12**2 + 4  # 246 GeV
mH_gram = r_S12**2 + l_SU2  # 125 GeV
lam_gram = mH_gram**2 / (2 * v_gram**2)  # 0.129098...

# sin^2theta_W = 3/13 (zero momentum Gram exact)
sin2_0 = 3/13
cos2_0 = 10/13
alpha_inv_0 = r_S12**2 + l_SU2**2  # 137

# Couplings at q^2 = 0:
g1_sq_0 = 4*math.pi / (alpha_inv_0 * cos2_0)
g2_sq_0 = 4*math.pi / (alpha_inv_0 * sin2_0)
# g3 at q^2 = 0 is not well-defined (confinement) — we use alpha_s(M_Z) and run

# === Running from mu_min to M_Z ===
# We start at a low scale mu_min (e.g., 1 GeV) with initial guesses,
# and use shooting to match Gram values at mu_min.

# SM one-loop RG (from M_Z downward, t = ln(mu))
def beta_fns(g1, g2, g3, yt, la, m2sq):
    "All SM one-loop beta functions with Higgs anomalous dimension."
    pi16 = 16 * math.pi**2
    # Higgs anomalous dimension (numerator only)
    gamma_H = 6*yt**2 - 2.25*g2 - 0.75*g1
    
    dg1 = (41.0/6.0) * g1**2 / pi16
    dg2 = (-19.0/6.0) * g2**2 / pi16
    dg3 = (-7.0) * g3**2 / pi16
    
    dyt_num = yt * (4.5*yt**2 - 17/12*g1 - 2.25*g2 - 8*g3)
    dyt = dyt_num / pi16
    
    dlam_num = (12*la**2 + 6*yt**2*la - 3*yt**4 - 3*la*(g1+3*g2) 
                + 0.375*(g1**2 + 2*g1*g2 + 3*g2**2))
    dlam = (dlam_num + 4*gamma_H*la) / pi16
    
    # dm2/dt includes 2*gamma_H effect
    dm2_num = m2sq * (6*la + 6*yt**2 - 4.5*g2 - 1.5*g1)
    dm2 = (dm2_num + 2*gamma_H*m2sq) / pi16
    
    return dg1, dg2, dg3, dyt, dlam, dm2

# We run from M_Z DOWN to mu_min
M_Z = 91.1876
mu_min = 1.0  # GeV

N_steps = 20000
dt = (math.log(mu_min) - math.log(M_Z)) / N_steps  # negative (running down)

# Initial values at M_Z (from Gram at M_Z, with alpha_em^-1 run to M_Z)
alpha_em_inv_MZ = 127.95
g1_sq = 4*math.pi / (alpha_em_inv_MZ * cos2_0)  # Gram sin^2theta_W gives coupling ratio
g2_sq = 4*math.pi / (alpha_em_inv_MZ * sin2_0)
g3_sq = 4*math.pi * 0.1179  # alpha_s at M_Z
y_t = 0.935  # top Yukawa at M_Z
lam = 0.12907  # from Gram (m_H=125, v=246)
# At M_Z: v = 246.22, so m_H^2 = 2*lam*v^2
v_MZ = 246.22
m2 = -lam * v_MZ**2  # m^2 = -lam * v^2, gives v_MZ at M_Z
m2_init = m2  # save

# Store full history
history = []
mu = M_Z
for step in range(N_steps + 1):
    if step % (N_steps // 60) == 0 or step == N_steps:
        v_val = math.sqrt(-m2 / lam) if lam > 0 and m2 < 0 else 0.0
        mH_val = math.sqrt(max(0, -2*m2))
        alpha_inv = 4*math.pi / g1_sq if g1_sq > 0 else 0
        history.append((math.log10(mu), alpha_inv, 4*math.pi/g2_sq, 4*math.pi/g3_sq,
                        y_t, lam, v_val, mH_val))
    if step == N_steps:
        break
    # RK4 using beta_fns
    vars = (g1_sq, g2_sq, g3_sq, y_t, lam, m2)
    k1 = beta_fns(*vars)
    k2_vars = (g1_sq+dt*k1[0]/2, g2_sq+dt*k1[1]/2, g3_sq+dt*k1[2]/2, y_t+dt*k1[3]/2, lam+dt*k1[4]/2, m2+dt*k1[5]/2)
    k2 = beta_fns(*k2_vars)
    k3_vars = (g1_sq+dt*k2[0]/2, g2_sq+dt*k2[1]/2, g3_sq+dt*k2[2]/2, y_t+dt*k2[3]/2, lam+dt*k2[4]/2, m2+dt*k2[5]/2)
    k3 = beta_fns(*k3_vars)
    k4_vars = (g1_sq+dt*k3[0], g2_sq+dt*k3[1], g3_sq+dt*k3[2], y_t+dt*k3[3], lam+dt*k3[4], m2+dt*k3[5])
    k4 = beta_fns(*k4_vars)
    for var, kk in [(g1_sq, [k[0] for k in [k1,k2,k3,k4]]),
                    (g2_sq, [k[1] for k in [k1,k2,k3,k4]]),
                    (g3_sq, [k[2] for k in [k1,k2,k3,k4]]),
                    (y_t, [k[3] for k in [k1,k2,k3,k4]]),
                    (lam, [k[4] for k in [k1,k2,k3,k4]]),
                    (m2, [k[5] for k in [k1,k2,k3,k4]])]:
        pass  # using direct update below
    g1_sq += (dt/6)*(k1[0]+2*k2[0]+2*k3[0]+k4[0])
    g2_sq += (dt/6)*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
    g3_sq += (dt/6)*(k1[2]+2*k2[2]+2*k3[2]+k4[2])
    y_t   += (dt/6)*(k1[3]+2*k2[3]+2*k3[3]+k4[3])
    lam   += (dt/6)*(k1[4]+2*k2[4]+2*k3[4]+k4[4])
    m2    += (dt/6)*(k1[5]+2*k2[5]+2*k3[5]+k4[5])
    mu = M_Z * math.exp(step * dt)

# Results at low energy
final = history[-1]
f = final
print("=== GRAM VALUES AT q^2 = 0 ===")
print(f"v     = {v_gram} GeV  (from 2*{r_S12}^2 + 4)")
print(f"m_H   = {mH_gram} GeV  (from {r_S12}^2 + {l_SU2})")
print(f"lam   = {lam_gram:.6f}")
print(f"sin^2W = {sin2_0} = 3/13")
print(f"alpha^-1 = {alpha_inv_0}")
print()
print("=== RUN DOWNWARD: M_Z -> low energy ===")
print(f"At mu = 10^{f[0]:.1f} GeV:")
print(f"  v     = {f[6]:.2f} GeV  (Gram: {v_gram})")
print(f"  m_H   = {f[7]:.2f} GeV  (Gram: {mH_gram})")
print(f"  lam   = {f[5]:.6f}  (Gram: {lam_gram:.6f})")
print(f"  alpha^-1 = {f[1]:.2f}  (Gram: {alpha_inv_0})")
print()
v_err = (f[6] - v_gram) / v_gram * 100
mH_err = (f[7] - mH_gram) / mH_gram * 100
print(f"vev error vs Gram: {v_err:.4f}%")
print(f"m_H error vs Gram: {mH_err:.4f}%")
print()

# Show full evolution
print("=== RG DOWNWARD HISTORY ===")
print(f"{'log10(mu)':>9} {'a^-1':>8} {'a2^-1':>8} {'a3^-1':>8} {'y_t':>6} {'v':>8} {'m_H':>8}")
for h in history:
    print(f"{h[0]:9.2f} {h[1]:8.1f} {h[2]:8.1f} {h[3]:8.1f} {h[4]:6.3f} {h[6]:8.2f} {h[7]:8.2f}")