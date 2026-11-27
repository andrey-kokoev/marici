"""Synthetic graph6 controls for the compiled inverse scanner (not Ramsey graphs)."""
import subprocess,sys
from ramsey38_trap_markability import prev
p=prev.out/'ramsey38_inverse_trap_templates.tsv';s,j,e,a=map(int,p.open().readline().split());
def scan(extra):
    g={(0,v) for v in range(1,8)}|{(v+1,x) for x,m in [(8,s),(9,e),(10,extra)] for v in range(7) if m>>v&1};bits=''.join(str(int((i,k) in g)) for k in range(1,27) for i in range(k));bits+='0'*(-len(bits)%6);w='Z'+''.join(chr(63+int(bits[k:k+6],2)) for k in range(0,len(bits),6));z=subprocess.run([sys.argv[1],str(p)],input=w+'\n',capture_output=True,text=True,check=True);return f'1 1 9 {j+2} {e} {a}' in z.stdout.splitlines()
assert scan(0) and not scan(e) and not scan(s);print('Known fit accepted; duplicate hidden edge and duplicate buried triangle rejected.')
