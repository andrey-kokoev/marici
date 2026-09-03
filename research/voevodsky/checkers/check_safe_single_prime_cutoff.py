from __future__ import annotations
import cmath,json,math
B=[1/6,-1/30,1/42,-1/30,5/66,-691/2730]
def psi(z):
 v=cmath.log(z)-1/(2*z)
 for k,b in enumerate(B,1): v-=b/(2*k*z**(2*k))
 return v
def main():
 L=.35; delta=.05; R=10000.; p=2*math.pi/math.log(2)
 c=math.log(2)/math.sqrt(2)
 mg=(psi(complex(.25,R/2)).real-math.log(math.pi))/(4*math.pi)
 cminus=(0.5772156649015329+math.pi/2+3*math.log(2)+math.log(math.pi))/(4*math.pi)+c
 eta=delta/(delta+cminus)
 N=math.ceil(2*R/p)+1; W=2*R
 K=max(1,math.floor(N/(2*math.pi)+.5))
 H=sum(1/(k-.5) for k in range(1,K+1))
 D=1+2*math.log(N)+8*L*p*N/math.pi**2*H+4*L*p*N/math.pi**2
 trace=L*W/math.pi; M=math.ceil(trace+D/eta)
 assert mg>c+delta
 result={"schema":"marici.voevodsky.safe-single-prime-cutoff-check.v1",
 "status":"safe_cutoff_finite_bound_diagnostic","L":"7/20","delta":delta,"R":R,
 "m_gamma_R":mg,"required_level":c+delta,"component_upper":N,"measure_upper":W,
 "transition_bound":D,"trace_upper":trace,"eta":eta,"sufficient_M":M,
 "digamma_remainder_theorem_instantiated":False,"directed_interval_certified":False,
 "root_isolation_required":False,"rh_implication":False,"passed":True}
 print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
