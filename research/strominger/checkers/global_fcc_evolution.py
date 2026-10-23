"""Candidate whole-field evolution plus lossless, flag-controlled presentations.

New assumptions: scalar complex vertex field; counting inner product; Cayley
step of the prior FCC quadratic kernel; one field step per flag-zipper action.
This is not an implementation of native particle dynamics or channel Fourier.
"""
from collections import defaultdict
from itertools import combinations
import copy


def lu_factor(matrix):
    a=[list(map(complex,row)) for row in matrix];n=len(a);swaps=[]
    for k in range(n):
        pivot=max(range(k,n),key=lambda i:abs(a[i][k]))
        if abs(a[pivot][k])<1e-14:raise ValueError('singular candidate step')
        a[k],a[pivot]=a[pivot],a[k];swaps.append(pivot)
        for i in range(k+1,n):
            a[i][k]/=a[k][k];factor=a[i][k]
            for j in range(k+1,n):a[i][j]-=factor*a[k][j]
    return a,swaps


def lu_solve(factor,rhs):
    a,swaps=factor;x=list(rhs);n=len(x)
    for k,p in enumerate(swaps):x[k],x[p]=x[p],x[k]
    for i in range(n):x[i]-=sum(a[i][j]*x[j] for j in range(i))
    for i in reversed(range(n)):x[i]=(x[i]-sum(a[i][j]*x[j] for j in range(i+1,n)))/a[i][i]
    return x


class GlobalFCCEvolution:
    def __init__(self,census,coarse,flag,tau=1):
        self.payload=copy.deepcopy(census)  # Includes original forms and incidence annotations.
        self.vertex_ids=[r['id'] for r in census['vertices']]
        self.index={v:i for i,v in enumerate(self.vertex_ids)}
        self.bary={r['id']:tuple(r['barycentric']) for r in census['vertices']}
        self.cumulative={r['id']:tuple(r['cumulative']) for r in census['vertices']}
        self.by_point={p:v for v,p in self.bary.items()}
        self.cells={r['id']:(r['id'],) for r in census['vertices']}
        for kind in ['edges','triangles','tetrahedra']:
            self.cells.update({r['id']:tuple(sorted(r['vertices'],key=self.cumulative.get)) for r in census[kind]})
        lookup={frozenset(vs):id for id,vs in self.cells.items()}
        self.boundary={id:[] if len(vs)==1 else [(lookup[frozenset(vs[:i]+vs[i+1:])],(-1)**i) for i in range(len(vs))] for id,vs in self.cells.items()}
        vertex_rotation={v:self.by_point[(p[3],p[0],p[1],p[2])] for v,p in self.bary.items()}
        self.rho={};self.rho_sign={}
        for id,vs in self.cells.items():
            images=[vertex_rotation[v] for v in vs]
            self.rho[id]=lookup[frozenset(images)]
            self.rho_sign[id]=(-1)**sum(self.cumulative[images[i]]>self.cumulative[images[j]] for i in range(len(images)) for j in range(i+1,len(images)))
        self.flag=tuple(flag)
        assert all(len(self.cells[id])==i+1 for i,id in enumerate(flag))
        assert all(a in dict(self.boundary[b]) for a,b in zip(flag,flag[1:]))
        assert self.rho[flag[-1]]==flag[-1]
        n=len(self.vertex_ids);self.A=[[0]*n for _ in range(n)]  # Exactly 28K.
        for cell in coarse['coarse_cells']:
            vs=[self.index[self.by_point[tuple(p)]] for p in cell['vertices']]
            for i in vs:self.A[i][i]+=2
            for i,j in combinations(vs,2):
                a=self.bary[self.vertex_ids[i]];b=self.bary[self.vertex_ids[j]]
                if sum((x-y)**2 for x,y in zip(a,b))==2:
                    self.A[i][i]+=7;self.A[j][j]+=7
                    self.A[i][j]-=7;self.A[j][i]-=7
        self.tau=tau
        self.plus=lu_factor([[int(i==j)+1j*tau*self.A[i][j]/56 for j in range(n)] for i in range(n)])
        self.minus=lu_factor([[int(i==j)-1j*tau*self.A[i][j]/56 for j in range(n)] for i in range(n)])

    def linear_step(self,field,inverse=False):
        sign=-1 if inverse else 1
        rhs=[z-sign*1j*self.tau*sum(a*w for a,w in zip(row,field))/56 for z,row in zip(field,self.A)]
        return lu_solve(self.minus if inverse else self.plus,rhs)

    def rotate(self,id,power):
        for _ in range(power%4):id=self.rho[id]
        return id

    def initial(self,field):
        if len(field)!=len(self.vertex_ids):raise ValueError('full field required')
        return {'field':list(field),'cursor':self.flag[0],'remaining':self.flag[1:],
                'parents':(),'leg':'up','frame':0,'formal_grade':0,'history':[]}

    def step(self,state):
        # No stage-number predicate, 7-entry schedule or endpoint-triggered relabel.
        s={**state,'field':self.linear_step(state['field']),'history':list(state['history'])}
        event={k:copy.deepcopy(state[k]) for k in ['cursor','remaining','parents','leg','frame','formal_grade']}
        if state['leg']=='up' and state['remaining']:
            s['parents']=(*state['parents'],state['cursor'])
            s['cursor']=state['remaining'][0];s['remaining']=state['remaining'][1:]
            action='ascend'
        elif state['parents']:
            s['leg']='down';s['cursor']=self.rho[state['parents'][-1]]
            s['parents']=state['parents'][:-1];action='descend-in-successor-view'
        else:
            assert state['leg']=='down'
            s['frame']=(state['frame']+1)%4
            s['formal_grade']=state['formal_grade']+int(s['frame']==0)
            s['cursor']=self.flag[0];s['remaining']=self.flag[1:];s['parents']=();s['leg']='up'
            action='handoff'
        s['history'].append({'action':action,'before':event})
        return s

    def presentation(self,state,branch=0):
        frame=(state['frame']+branch)%4
        window=self.rotate(state['cursor'],frame);window_vertices=set(self.cells[window])
        groups=defaultdict(list)
        for id in self.cells:
            displayed=self.rotate(id,frame)
            key=tuple(sorted(window_vertices.intersection(self.cells[displayed])))
            groups[key].append(id)
        return {'frame':frame,'window':window,'groups':dict(groups)}

    def restore(self,view):
        rows=[id for group in view['groups'].values() for id in group]
        if len(rows)!=len(self.cells) or set(rows)!=set(self.cells):raise ValueError('lost or duplicated retained cell')
        w=set(self.cells[view['window']])
        for key,group in view['groups'].items():
            for id in group:
                if tuple(sorted(w.intersection(self.cells[self.rotate(id,view['frame'])])))!=key:
                    raise ValueError('wrong marked fiber membership')
        return tuple(sorted(rows))

    def cell_readouts(self,state,frame=0):
        # One field value per shared vertex, transported with the chart.
        field={self.rotate(v,frame):state['field'][self.index[v]] for v in self.vertex_ids}
        return {self.rotate(id,frame):{self.rotate(v,frame):field[self.rotate(v,frame)] for v in vs} for id,vs in self.cells.items()}

    def restrictions_agree(self,readouts):
        for id,faces in self.boundary.items():
            for face,_ in faces:
                if {v:readouts[id][v] for v in self.cells[face]}!=readouts[face]:return False
        return True
