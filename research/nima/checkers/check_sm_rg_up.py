"""SM RG: run from M_Z (Gram values) UP to M_Planck."""
import math

r_S12, l_U1, l_SU2, C_U1 = 11, 12, 4, 10

M_Z = 91.1876  # GeV
M_Pl = 1.22089e19

# Gram-predicted values at M_Z:
sin2_W = 3/13  # 0.230769
cos2_W = 10/13 # 0.769231
alpha_em_inv_MZ = 127.95  # fine-structure at M_Z (Gram 137 run to M_Z)

g1_sq_MZ = 4*math.pi / (alpha_em_inv_MZ * cos2_W)  # from e^2 = g1^2 * cos2_W
g2_sq_MZ = 4*math.pi / (alpha_em_inv_MZ * sin2_W)  # from e^2 = g2^2 * sin2_W
g3_sq_MZ = 4*math.pi * 0.1179  # alpha_s at M_Z

y_t_MZ = 0.935  # top Yukawa at M_Z (from m_t = 172.5 GeV, v=246.22)
v_MZ = 246.22  # Higgs vev at M_Z
m_H_MZ = 125.1  # Higgs mass
lam_MZ = (m_H_MZ**2) / (2 * v_MZ**2)
m2_MZ = -m_H_MZ**2

print("=== GRAM VALUES AT M_Z (INPUT) ===")
print(f"sin2_W = {sin2_W:.6f} = 3/13 (Gram)")
print(f"cos2_W = {cos2_W:.6f} = 10/13 (Gram)")
print(f"alpha_em^-1 = {alpha_em_inv_MZ:.2f} (Gram 137 run to M_Z)")
print(f"g1^2(M_Z) = {g1_sq_MZ:.6f}")
print(f"g2^2(M_Z) = {g2_sq_MZ:.6f}")
print(f"g3^2(M_Z) = {g3_sq_MZ:.6f}")
print(f"g2^2/g1^2 = {g2_sq_MZ/g1_sq_MZ:.4f}  (Gram ratio: {l_SU2**2}/{l_U1**2} = {l_SU2**2/l_U1**2:.4f})")
print(f"yt = {y_t_MZ:.4f}, v = {v_MZ:.2f}, mH = {m_H_MZ:.2f}, lam = {lam_MZ:.6f}")
print()

# === RG RUNNING UP FROM M_Z TO M_PL ===
N_steps = 50000
dt = (math.log(M_Pl) - math.log(M_Z)) / N_steps  # positive

g1_sq, g2_sq, g3_sq = g1_sq_MZ, g2_sq_MZ, g3_sq_MZ
y_t, lam, m2 = y_t_MZ, lam_MZ, m2_MZ
mu = M_Z

def dg1(g1, g2, g3, yt, la):
    return (41.0/6.0) * g1**2 / (16 * math.pi**2)
def dg2(g1, g2, g3, yt, la):
    return (-19.0/6.0) * g2**2 / (16 * math.pi**2)
def dg3(g1, g2, g3, yt, la):
    return (-7.0) * g3**2 / (16 * math.pi**2)
def dyt(g1, g2, g3, yt, la):
    return yt * (4.5*yt**2 - 17/12*g1 - 2.25*g2 - 8*g3) / (16*math.pi**2)
def dlam(g1, g2, g3, yt, la):
    return (12*la**2 + 6*yt**2*la - 3*yt**4 - 3*la*(g1+3*g2) 
            + 0.375*(g1**2 + 2*g1*g2 + 3*g2**2)) / (16*math.pi**2)
def dm2(g1, g2, g3, yt, la, m2sq):
    return m2sq * (6*la + 6*yt**2 - 4.5*g2 - 1.5*g1) / (16*math.pi**2)

def rk4_step(vars):
    g1, g2, g3, yt, la, m2sq = vars
    k1 = (dg1(g1,g2,g3,yt,la), dg2(g1,g2,g3,yt,la), dg3(g1,g2,g3,yt,la),
          dyt(g1,g2,g3,yt,la), dlam(g1,g2,g3,yt,la), dm2(g1,g2,g3,yt,la,m2sq))
    k2 = (dg1(g1+dt*k1[0]/2,g2+dt*k1[1]/2,g3+dt*k1[2]/2,yt+dt*k1[3]/2,la+dt*k1[4]/2),
          dg2(g1+dt*k1[0]/2,g2+dt*k1[1]/2,g3+dt*k1[2]/2,yt+dt*k1[3]/2,la+dt*k1[4]/2),
          dg3(g1+dt*k1[0]/2,g2+dt*k1[1]/2,g3+dt*k1[2]/2,yt+dt*k1[3]/2,la+dt*k1[4]/2),
          dyt(g1+dt*k1[0]/2,g2+dt*k1[1]/2,g3+dt*k1[2]/2,yt+dt*k1[3]/2,la+dt*k1[4]/2),
          dlam(g1+dt*k1[0]/2,g2+dt*k1[1]/2,g3+dt*k1[2]/2,yt+dt*k1[3]/2,la+dt*k1[4]/2),
          dm2(g1+dt*k1[0]/2,g2+dt*k1[1]/2,g3+dt*k1[2]/2,yt+dt*k1[3]/2,la+dt*k1[4]/2,
              m2sq+dt*k1[5]/2))
    k3 = (dg1(g1+dt*k2[0]/2,g2+dt*k2[1]/2,g3+dt*k2[2]/2,yt+dt*k2[3]/2,la+dt*k2[4]/2),
          dg2(g1+dt*k2[0]/2,g2+dt*k2[1]/2,g3+dt*k2[2]/2,yt+dt*k2[3]/2,la+dt*k2[4]/2),
          dg3(g1+dt*k2[0]/2,g2+dt*k2[1]/2,g3+dt*k2[2]/2,yt+dt*k2[3]/2,la+dt*k2[4]/2),
          dyt(g1+dt*k2[0]/2,g2+dt*k2[1]/2,g3+dt*k2[2]/2,yt+dt*k2[3]/2,la+dt*k2[4]/2),
          dlam(g1+dt*k2[0]/2,g2+dt*k2[1]/2,g3+dt*k2[2]/2,yt+dt*k2[3]/2,la+dt*k2[4]/2),
          dm2(g1+dt*k2[0]/2,g2+dt*k2[1]/2,g3+dt*k2[2]/2,yt+dt*k2[3]/2,la+dt*k2[4]/2,
              m2sq+dt*k2[5]/2))
    k4 = (dg1(g1+dt*k3[0],g2+dt*k3[1],g3+dt*k3[2],yt+dt*k3[3],la+dt*k3[4]),
          dg2(g1+dt*k3[0],g2+dt*k3[1],g3+dt*k3[2],yt+dt*k3[3],la+dt*k3[4]),
          dg3(g1+dt*k3[0],g2+dt*k3[1],g3+dt*k3[2],yt+dt*k3[3],la+dt*k3[4]),
          dyt(g1+dt*k3[0],g2+dt*k3[1],g3+dt*k3[2],yt+dt*k3[3],la+dt*k3[4]),
          dlam(g1+dt*k3[0],g2+dt*k3[1],g3+dt*k3[2],yt+dt*k3[3],la+dt*k3[4]),
          dm2(g1+dt*k3[0],g2+dt*k3[1],g3+dt*k3[2],yt+dt*k3[3],la+dt*k3[4],
              m2sq+dt*k3[5]))
    return (dt/6)*(k1[0]+2*k2[0]+2*k3[0]+k4[0]), (dt/6)*(k1[1]+2*k2[1]+2*k3[1]+k4[1]), \
           (dt/6)*(k1[2]+2*k2[2]+2*k3[2]+k4[2]), (dt/6)*(k1[3]+2*k2[3]+2*k3[3]+k4[3]), \
           (dt/6)*(k1[4]+2*k2[4]+2*k3[4]+k4[4]), (dt/6)*(k1[5]+2*k2[5]+2*k3[5]+k4[5])

history = []
for step in range(N_steps + 1):
    if step % (N_steps // 50) == 0 or step == N_steps:
        v = math.sqrt(-m2 / lam) if lam > 0 and m2 < 0 else 0.0
        mH = math.sqrt(max(0, -2*m2))
        history.append((math.log10(mu), 4*math.pi/g1_sq, 4*math.pi/g2_sq, 4*math.pi/g3_sq,
                        y_t, lam, v, mH, g2_sq/g1_sq))
    if step == N_steps:
        break
    dg1v, dg2v, dg3v, dytv, dlamv, dm2v = rk4_step((g1_sq, g2_sq, g3_sq, y_t, lam, m2))
    g1_sq += dg1v; g2_sq += dg2v; g3_sq += dg3v
    y_t += dytv; lam += dlamv; m2 += dm2v
    mu = M_Z * math.exp(step * dt / N_steps * N_steps)  # simple
    mu = M_Z * math.exp(step * dt)  # correct

# At M_Pl
final = history[-1]
f = final
print("=== AT M_PL (Gram-predicted values run upward) ===")
print(f"alpha1^-1(M_Pl) = {f[1]:.1f}")
print(f"alpha2^-1(M_Pl) = {f[2]:.1f}")
print(f"alpha3^-1(M_Pl) = {f[3]:.1f}")
print(f"y_t(M_Pl) = {f[4]:.4f}")
print(f"lam(M_Pl) = {f[5]:.6f}")
print(f"v(M_Pl) = {f[6]:.2f} GeV  (Gram: 246.00)")
print(f"m_H(M_Pl) = {f[7]:.1f} GeV  (Gram: 125.0)")
print(f"g2^2/g1^2 = {f[8]:.6f}  (Gram: {l_SU2**2/l_U1**2:.4f})")
print()

# Check: does v at M_Pl match Gram prediction?
v_error = (f[6] - 246.0) / 246.0 * 100
mH_error = (f[7] - 125.0) / 125.0 * 100
rat_error = (f[8] - l_SU2**2/l_U1**2) / (l_SU2**2/l_U1**2) * 100
print(f"vev at M_Pl: {f[6]:.2f} GeV, Gram: 246.0 GeV, error = {v_error:.4f}%")
print(f"m_H at M_Pl: {f[7]:.1f} GeV, Gram: 125.0 GeV, error = {mH_error:.4f}%")
print(f"g2^2/g1^2 at M_Pl: {f[8]:.6f}, Gram: {l_SU2**2/l_U1**2:.4f}, error = {rat_error:.2f}%")
print()

# Show history
print("=== RG FLOW UPWARD ===")
print(f"{'log10(mu)':>9} {'a1^-1':>8} {'a2^-1':>8} {'a3^-1':>8} {'y_t':>6} {'v':>8} {'m_H':>8} {'g2^2/g1^2':>10}")
for h in history:
    print(f"{h[0]:9.2f} {h[1]:8.1f} {h[2]:8.1f} {h[3]:8.1f} {h[4]:6.3f} {h[6]:8.2f} {h[7]:8.2f} {h[8]:10.6f}")