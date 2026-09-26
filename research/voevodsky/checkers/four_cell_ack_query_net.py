"""Acknowledged attributed queries. Cleanup is an explicit model obligation,
not a claim that geometric source obligations have been identified or discharged.
"""
from copy import deepcopy
from four_cell_query_net import QueryNet
from four_cell_port_net import ARITY
ARITY.update({'READC':('p','o','c'), 'CLEAN':('p','c'),
              'TICKET':('p',), 'ACK':('p',), 'DONE':('p',)})

class AckNet(QueryNet):
    def enabled(self):
        self.validate()
        result=[]
        for n,(kind,_) in self.nodes.items():
            peer,port=self.wires[n,'p']
            if port=='p' and (kind,self.nodes[peer][0]) in (
                    ('EB','FB'),('VALUE','READC'),('CLEAN','TICKET')):
                result.append((n,peer))
        return result

    def step(self,pair):
        if pair not in self.enabled():raise ValueError('inactive pair')
        a,b=pair
        kind,x=self.nodes[a]
        if kind=='EB':
            return super().step(pair)
        if kind=='VALUE':
            if x['family']!=self.nodes[b][1][0]:raise ValueError('wrong family')
            out=self.wires[b,'o']; ack=self.wires[b,'c']
        else:
            ack=self.wires[a,'c']
        for n in pair:
            for port in ARITY[self.nodes[n][0]]:
                endpoint=(n,port)
                if endpoint in self.wires:
                    peer=self.wires.pop(endpoint);del self.wires[peer]
            del self.nodes[n]
        if kind=='VALUE':
            answer=self.add('ANSWER',x)
            clean=self.add('CLEAN');ticket=self.add('TICKET')
            self.link((answer,'p'),out)
            self.link((clean,'p'),(ticket,'p'))
            self.link((clean,'c'),ack)
        else:
            done=self.add('DONE');self.link((done,'p'),ack)
        self.validate()

    def observe_public(self):
        """Immutable snapshot; None denotes pending, never numeric zero."""
        answers={};acks={}
        for n,(kind,label) in self.nodes.items():
            if kind not in ('OUT','ACK'):continue
            peer,_=self.wires[n,'p']
            agent,payload=self.nodes[peer]
            if kind=='OUT':
                answers[label]=payload['value'] if agent=='ANSWER' else None
            else:acks[label]=agent=='DONE'
        complete=all(acks.values())
        entries=tuple((label,answers[label],acks[label]) for label in sorted(answers))
        return entries,complete

    def live_meanings(self):
        result={}
        for n,(kind,label) in self.nodes.items():
            if kind!='OUT':continue
            peer,_=self.wires[n,'p'];agent,payload=self.nodes[peer]
            if agent=='READC':
                peer,_=self.wires[peer,'p'];agent,payload=self.nodes[peer]
            assert agent in ('EB','FB','VALUE','ANSWER')
            result[label]=payload['value']
        return result

def construct(records):
    net=AckNet()
    for family in sorted({v['family'] for v in records.values()}):
        pair=[]
        for kind,suffix in (('EB','E_B'),('FB','F_B')):
            label=(family,kind)
            node=net.add(kind,records[family+'_'+suffix])
            read=net.add('READC',label);out=net.add('OUT',label);ack=net.add('ACK',label)
            net.link((node,'o'),(read,'p'));net.link((read,'o'),(out,'p'))
            net.link((read,'c'),(ack,'p'));pair.append(node)
        net.link((pair[0],'p'),(pair[1],'p'))
    net.validate();return net
