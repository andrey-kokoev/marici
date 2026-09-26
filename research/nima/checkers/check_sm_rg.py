"""SM RG flow from Gram boundary conditions at M_Planck -> M_Z."""
import math

# === GRAM NUMBERS ===
r_S12, l_U1, l_SU2, C_U1 = 11, 12, 4, 10

# === BOUNDARY CONDITIONS AT M_PL ===
M_Pl = 1.22089e19  # GeV
M_Z = 91.1876  # GeV

# From Gram:
alpha1_inv_0 = r_S12**2 + l_SU2**2  # 137
alpha1_0 = 1.0 / alpha1_inv_0
g1_sq_0 = 4.0 * math.pi * alpha1_0

# Coupling ratio from Gram eigenvalues:
g2_sq_0 = g1_sq_0 * (l_SU2**2) / (l_U1**2)  # g1^2 * 16/144 = g1^2/9
alpha2_0 = g2_sq_0 / (4.0 * math.pi)

g3_sq_0 = g1_sq_0 * (l_SU2**2) / (l_U1**2)  # same as SU(2): l_SU3 = 4
alpha3_0 = g3_sq_0 / (4.0 * math.pi)

# Top Yukawa
y_t_0 = 1.0

# Higgs parameters
v_0 = 2 * r_S12**2 + 4  # 246 GeV
m_H_0 = r_S12**2 + l_SU2  # 125 GeV
lambda_0 = (m_H_0**2) / (2.0 * v_0**2)
m2_0 = -m_H_0**2  # Higgs mass parameter at Planck scale

print("=== GRAM BOUNDARY CONDITIONS AT M_PL ===")
print(f"M_Pl = {M_Pl:.4e} GeV, M_Z = {M_Z:.4f} GeV")
print(f"alpha1^-1 = {alpha1_inv_0}  (g1^2 = {g1_sq_0:.6f})")
print(f"alpha2^-1 = {1/alpha2_0:.1f}  (g2^2 = {g2_sq_0:.6f})")
print(f"alpha3^-1 = {1/alpha3_0:.1f}  (g3^2 = {g3_sq_0:.6f})")
print(f"g2^2/g1^2 = {g2_sq_0/g1_sq_0:.4f} = {l_SU2}^2/{l_U1}^2 = {l_SU2**2}/{l_U1**2}")
print(f"y_t = {y_t_0}, v = {v_0} GeV, m_H = {m_H_0} GeV, lambda = {lambda_0:.6f}")
print()

# === ONE-LOOP SM RG ===
N_steps = 50000
dt = (math.log(M_Z) - math.log(M_Pl)) / N_steps  # negative (running down)

# Initialize
g1_sq, g2_sq, g3_sq = g1_sq_0, g2_sq_0, g3_sq_0
y_t, lam, m2 = y_t_0, lambda_0, m2_0
mu = M_Pl

def step_all(g1, g2, g3, yt, la, m2sq):
    """Compute all derivatives at current point"""
    pi2 = 16 * math.pi**2
    dg1 = (41.0/6.0) * g1**2 / pi2
    dg2 = (-19.0/6.0) * g2**2 / pi2
    dg3 = (-7.0) * g3**2 / pi2
    dyt = yt * (4.5*yt**2 - 17.0/12.0*g1 - 2.25*g2 - 8*g3) / pi2
    dla = (12*la**2 + 6*yt**2*la - 3*yt**4 - 3*la*(g1+3*g2) 
           + 0.375*(g1**2 + 2*g1*g2 + 3*g2**2)) / pi2
    dm2 = m2sq * (6*la + 6*yt**2 - 4.5*g2 - 1.5*g1) / pi2
    return dg1, dg2, dg3, dyt, dla, dm2

# Storage
history = []
header = ("mu", "a1inv", "a2inv", "a3inv", "yt", "lam", "v", "mH", "g2g1r")

for step in range(N_steps + 1):
    if step % (N_steps // 50) == 0 or step == N_steps:
        v = math.sqrt(-m2 / lam) if lam > 0 and m2 < 0 else 0.0
        mH = math.sqrt(max(0, -2*m2))
        history.append((math.log10(mu), 4*math.pi/g1_sq if g1_sq>0 else 0,
                        4*math.pi/g2_sq if g2_sq>0 else 0,
                        4*math.pi/g3_sq if g3_sq>0 else 0,
                        y_t, lam, v, mH, g2_sq/g1_sq))
    if step == N_steps:
        break
    
    # RK4
    k1 = step_all(g1_sq, g2_sq, g3_sq, y_t, lam, m2)
    k2 = step_all(g1_sq+0.5*dt*k1[0], g2_sq+0.5*dt*k1[1], g3_sq+0.5*dt*k1[2],
                  y_t+0.5*dt*k1[3], lam+0.5*dt*k1[4], m2+0.5*dt*k1[5])
    k3 = step_all(g1_sq+0.5*dt*k2[0], g2_sq+0.5*dt*k2[1], g3_sq+0.5*dt*k2[2],
                  y_t+0.5*dt*k2[3], lam+0.5*dt*k2[4], m2+0.5*dt*k2[5])
    k4 = step_all(g1_sq+dt*k3[0], g2_sq+dt*k3[1], g3_sq+dt*k3[2],
                  y_t+dt*k3[3], lam+dt*k3[4], m2+dt*k3[5])
    
    for var, ks in [(g1_sq, [k[0] for k in [k1,k2,k3,k4]]),
                    (g2_sq, [k[1] for k in [k1,k2,k3,k4]]),
                    (g3_sq, [k[2] for k in [k1,k2,k3,k4]]),
                    (y_t, [k[3] for k in [k1,k2,k3,k4]]),
                    (lam, [k[4] for k in [k1,k2,k3,k4]]),
                    (m2, [k[5] for k in [k1,k2,k3,k4]])]:
        pass  # I'll just do direct RK4 below
    
    g1_sq += (dt/6)*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
    g2_sq += (dt/6)*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
    g3_sq += (dt/6)*(k1[2] + 2*k2[2] + 2*k3[2] + k4[2])
    y_t    += (dt/6)*(k1[3] + 2*k2[3] + 2*k3[3] + k4[3])
    lam    += (dt/6)*(k1[4] + 2*k2[4] + 2*k3[4] + k4[4])
    m2     += (dt/6)*(k1[5] + 2*k2[5] + 2*k3[5] + k4[5])
    
    mu = mu * math.exp(dt)

# Results at M_Z
final = history[-1]
print("=== PREDICTIONS AT M_Z (from Gram boundary at M_Pl) ===")
f = final
print(f"alpha1^-1 = {f[1]:.2f}  (obs: ~127.9)")
print(f"alpha2^-1 = {f[2]:.2f}  (obs: ~30)")
print(f"alpha3^-1 = {f[3]:.2f}  (obs: ~8.5)")
print(f"y_t       = {f[4]:.4f}  (obs: ~0.93)")
print(f"lambda    = {f[5]:.6f}")
print(f"v         = {f[6]:.2f} GeV  (obs: 246.22)")
print(f"m_H       = {f[7]:.2f} GeV  (obs: ~125)")
print(f"g2^2/g1^2 = {f[8]:.4f}  (Gram fixed: 0.1111)")
print()

# Check the 0.09% Higgs vev running
v_pred = final[6]
v_obs = 246.22
v_error = (v_pred - v_obs) / v_obs * 100
print(f"vev running check: v_pred = {v_pred:.2f}, v_obs = {v_obs:.2f}")
print(f"Error = {v_error:.4f}%")
print()

# Show full history
print("=== RG FLOW HISTORY ===")
print(f"{'log10(mu)':>9} {'a1^-1':>8} {'a2^-1':>8} {'a3^-1':>8} {'y_t':>6} {'v':>8} {'m_H':>8}")
for h in history:
    print(f"{h[0]:9.2f} {h[1]:8.1f} {h[2]:8.1f} {h[3]:8.1f} {h[4]:6.3f} {h[6]:8.2f} {h[7]:8.2f}")