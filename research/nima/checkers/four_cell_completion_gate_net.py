"""Per-channel successor release gated by actual DONE, not answer publication.
READY is a release witness, not execution of a geometric successor operation.
"""
from four_cell_ack_query_net import AckNet, construct as base_construct
from four_cell_port_net import ARITY
ARITY.update({'GATE':('p','o'), 'READY':('p',), 'NEXT':('p',)})

class GatedNet(AckNet):
    def enabled(self):
        result=super().enabled()
        for n,(kind,_) in self.nodes.items():
            if kind!='DONE':continue
            peer,port=self.wires[n,'p']
            if port=='p' and self.nodes[peer][0]=='GATE':result.append((n,peer))
        return result

    def step(self,pair):
        if pair not in self.enabled():raise ValueError('inactive pair')
        a,b=pair
        if self.nodes[a][0]!='DONE':return super().step(pair)
        boundary=self.wires[b,'o']
        label=self.nodes[b][1]
        for n in pair:
            for port in ARITY[self.nodes[n][0]]:
                endpoint=(n,port)
                if endpoint in self.wires:
                    peer=self.wires.pop(endpoint);del self.wires[peer]
            del self.nodes[n]
        ready=self.add('READY',label)
        self.link((ready,'p'),boundary)
        self.validate()

    def observe_public(self):
        answers={};complete={};released={}
        for n,(kind,label) in self.nodes.items():
            if kind=='OUT':
                peer,_=self.wires[n,'p'];agent,payload=self.nodes[peer]
                answers[label]=payload['value'] if agent=='ANSWER' else None
            elif kind=='NEXT':
                peer,_=self.wires[n,'p'];agent,_=self.nodes[peer]
                released[label]=agent=='READY'
                if agent=='READY':complete[label]=True
                elif agent=='GATE':
                    upstream,_=self.wires[peer,'p']
                    complete[label]=self.nodes[upstream][0]=='DONE'
                else:raise ValueError('invalid successor boundary')
        rows=tuple((label,answers[label],complete[label],released[label]) for label in sorted(answers))
        return rows,all(complete.values()),all(released.values())

def construct(records):
    net=base_construct(records)
    # Same constructed graph and monotone allocator; replace terminal ACK leaves
    # by gates, preserving their existing p connections.
    result=GatedNet();result.__dict__=net.__dict__
    for n,(kind,label) in list(result.nodes.items()):
        if kind=='ACK':
            result.nodes[n]=('GATE',label)
            end=result.add('NEXT',label)
            result.link((n,'o'),(end,'p'))
    result.validate();return result
