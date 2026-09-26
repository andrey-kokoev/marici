"""Finite-input estimates without graph construction or unary budget expansion."""
from dataclasses import dataclass
from program_inputs import word, program

@dataclass(frozen=True)
class PreparedProgram:
 bits: tuple
 instructions: tuple
 initial_agents: int
 rewrite_bound: int
 final_word_length_bound: int
 @property
 def constructor_peak_agents(self):return self.initial_agents
 @property
 def constructor_agent_allocations(self):
  return self.initial_agents+sum(op in ('ifadd','scan') for op,arg in self.instructions)
 @property
 def constructor_fresh_names(self):return self.constructor_agent_allocations-2 # RET and ACK are fixed names
 @property
 def total_fresh_name_bound(self):return self.constructor_fresh_names+self.runtime_fresh_name_bound
 @property
 def peak_agent_bound(self):return self.initial_agents+2*self.rewrite_bound
 @property
 def runtime_fresh_name_bound(self):return 4*self.rewrite_bound

def preflight(bits,instructions):
 bits=word(bits);instructions=tuple(program(instructions,{'member','add','union','ifadd','scan'}))
 n=len(bits);initial=n+4;cost=len(instructions)
 for op,a in instructions:
  if op=='member':initial+=a+3;cost+=2*n+a+3
  elif op=='add':initial+=a+2;cost+=2*a+2;n=max(n,a+1)
  elif op=='union':
   m=len(a);initial+=m+2;cost+=2*min(n,m)+2;n=max(n,m)
  elif op=='ifadd':
   i,t,f=a;initial+=i+t+f+5;cost+=2*n+i+2*max(t,f)+min(t,f)+10;n=max(n,t+1,f+1)
  else:
   c,f=a;initial+=c+f+4;C=c+f;N=max(n,C)
   cost+=f*(2*N+5*C+f+18)+C+4;n=N
 return PreparedProgram(bits,instructions,initial,cost,n)
