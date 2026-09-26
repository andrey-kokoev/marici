"""Linear binary joins aggregate four channel releases into one global token."""
from four_cell_completion_gate_net import GatedNet, construct as gated_construct
from four_cell_port_net import ARITY
ARITY.update({'JOIN':('p','a','o'), 'HOLD':('p','o'), 'BARRIER':('p',)})

class BarrierNet(GatedNet):
    def enabled(self):
        result=super().enabled()
        for n,(kind,_) in self.nodes.items():
            if kind!='READY':continue
            peer,port=self.wires[n,'p']
            if port=='p' and self.nodes[peer][0] in ('JOIN','HOLD'):
                result.append((n,peer))
        return result

    def step(self,pair):
        if pair not in self.enabled():raise ValueError('inactive pair')
        a,b=pair
        if self.nodes[a][0]!='READY':return super().step(pair)
        kind=self.nodes[b][0]
        out=self.wires[b,'o']
        other=self.wires[b,'a'] if kind=='JOIN' else None
        for n in pair:
            for port in ARITY[self.nodes[n][0]]:
                endpoint=(n,port)
                if endpoint in self.wires:
                    peer=self.wires.pop(endpoint);del self.wires[peer]
            del self.nodes[n]
        if kind=='JOIN':
            hold=self.add('HOLD')
            self.link((hold,'p'),other);self.link((hold,'o'),out)
        else:
            ready=self.add('READY','joined')
            self.link((ready,'p'),out)
        self.validate()

    def observe_barrier(self):
        """Independent answer snapshots and actual final-token readiness."""
        answers=[];released=False
        for n,(kind,label) in self.nodes.items():
            if kind=='OUT':
                peer,_=self.wires[n,'p'];agent,payload=self.nodes[peer]
                answers.append((label,payload['value'] if agent=='ANSWER' else None))
            elif kind=='BARRIER':
                peer,port=self.wires[n,'p']
                released=port=='p' and self.nodes[peer][0]=='READY'
        return tuple(sorted(answers)),released

    def observe_public(self):
        return self.observe_barrier()

def construct(records):
    old=gated_construct(records)
    net=BarrierNet();net.__dict__=old.__dict__
    leaves=sorted((label,n) for n,(kind,label) in net.nodes.items() if kind=='NEXT')
    if len(leaves)!=4:raise ValueError('four-channel constructor required')
    peers=[]
    for _,n in leaves:
        peer=net.wires.pop((n,'p'));del net.wires[peer];del net.nodes[n]
        peers.append(peer)
    lower=[]
    for i in (0,2):
        join=net.add('JOIN')
        net.link((join,'p'),peers[i]);net.link((join,'a'),peers[i+1])
        lower.append((join,'o'))
    top=net.add('JOIN');end=net.add('BARRIER')
    net.link((top,'p'),lower[0]);net.link((top,'a'),lower[1])
    net.link((top,'o'),(end,'p'))
    net.validate();return net
