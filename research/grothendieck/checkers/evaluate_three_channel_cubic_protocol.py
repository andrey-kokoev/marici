"""Rank-three coordinate enclosures and calibration-robust prediction separation.

CLI JSON: raw {positive,crossed,vacuum:[real,imag]}, errors {name:decimal},
optional total_l1_error, precision_bits; optional predictions=[state,state],
where each state maps the three names to [real,imag] source coefficients.
There is NO physical w_seam^2 multiplier and NO automatic conjugation.
"""
from pathlib import Path
import importlib.util,json,hashlib,sys
from flint import arb,acb,ctx

spec=importlib.util.spec_from_file_location('bin_receiver',Path(__file__).with_name('evaluate_time_bin_cubic_observer.py'))
bin_receiver=importlib.util.module_from_spec(spec);spec.loader.exec_module(bin_receiver)
base=bin_receiver.base

def nonnegative(value):
    value=arb(value)
    if not value.is_finite() or not value>=0:raise ValueError('Finite nonnegative error required')
    return value

def upper(value):return arb(value.upper())
def box(radius):return arb(0).union(upper(radius)).union(-upper(radius))

class ThreeChannelObserver:
    def __init__(self,manifest_path=base.RESULTS/'three-channel-cubic-protocol.json',precision_bits=2048,mode='private'):
        path=Path(manifest_path);raw=path.read_bytes()
        cert=json.loads(path.with_name('three-channel-cubic-certificate.json').read_text(encoding='utf-8'))
        if hashlib.sha256(raw).hexdigest()!=cert['manifest_sha256']:raise ValueError('Protocol checksum mismatch')
        self.manifest=json.loads(raw)
        filter_path=path.parent/self.manifest['filter_manifest']
        if hashlib.sha256(filter_path.read_bytes()).hexdigest()!=self.manifest['filter_manifest_sha256']:
            raise ValueError('Stale bin-filter calibration')
        self.bin_receiver=bin_receiver.TimeBinObserver(filter_path,precision_bits)
        self.precision_bits=precision_bits;self.names=self.manifest['channel_order']
        if mode not in self.manifest['modes']:raise ValueError('Unknown acquisition mode')
        self.mode=mode
        self.channels=dict(self.manifest['channels'])
        if mode=='reuse':self.channels['crossed']=self.manifest['modes']['reuse']['crossed_channel']
        self.gain={n:base.rational(self.channels[n]['rational_inverse']) for n in self.names}
        self.lower={n:base.rational(self.channels[n]['forward_gain_lower']) for n in self.names}
        self.upper={n:base.rational(self.channels[n]['forward_gain_upper']) for n in self.names}
        self.defect={n:base.rational(self.channels[n]['relative_calibration_defect_upper']) for n in self.names}
        assert all(self.lower[n]>0 and self.gain[n]>0 for n in self.names)

    def _keys(self,data):
        if set(data)!=set(self.names):raise ValueError('All three separately labelled channels are required')

    def _budgets(self,errors,total_l1_error):
        self._keys(errors)
        budgets={n:nonnegative(errors[n]) for n in self.names}
        total=None if total_l1_error is None else nonnegative(total_l1_error)
        if total is not None:
            for n in self.names:
                if total<budgets[n]:budgets[n]=total
        return budgets,total

    def aggregate_reuse(self,feature_values,feature_errors,vacuum_value,vacuum_error):
        """Retain coordinate information from raw labelled data, not the scalar Lambda."""
        ctx.prec=self.precision_bits
        if self.mode!='reuse':raise ValueError('Aggregation requires reuse mode')
        rows=self.bin_receiver.manifest['rows']
        if len(feature_values)!=len(rows) or len(feature_errors)!=len(rows):
            raise ValueError('All 449 raw feature readings and error budgets required')
        raw={'positive':acb(0),'crossed':acb(0),'vacuum':base.complex_value(vacuum_value)}
        errors={'positive':arb(0),'crossed':arb(0),'vacuum':nonnegative(vacuum_error)}
        for row,z,e in zip(rows,feature_values,feature_errors):
            name=row['coefficient']
            raw[name]+=row['sign']*base.complex_value(z)
            errors[name]+=nonnegative(e)
        return raw,{n:upper(e) for n,e in errors.items()}

    def normalize(self,raw,errors,total_l1_error=None):
        ctx.prec=self.precision_bits;self._keys(raw)
        budgets,total=self._budgets(errors,total_l1_error)
        coordinates={}
        for n in self.names:
            z=base.complex_value(raw[n]);e=budgets[n];g=self.gain[n]
            value=g*z
            # Data-dependent bound, no unspoken prior on the source coefficient.
            source_size=(upper(abs(z))+e)/self.lower[n]
            radius=upper(g*e+self.defect[n]*source_size+value.real.rad()+value.imag.rad())
            center=acb(value.real.mid(),value.imag.mid())
            coordinates[n]={'center':str(center),'radius_upper':str(radius),
                            'rectangular_outer_enclosure':str(center+acb(box(radius),box(radius))),
                            'assumed_raw_error':str(e)}
        return {'mode':self.mode,'coordinates':coordinates,
                'joint_region':'For some E0,Ex in the certified positive calibration intervals: |E_i*c_i-z_i|<=eps_i in each channel (E_vacuum=1). If declared, also sum_i |E_i*c_i-z_i|<=total_l1_error. The displayed polydisc is a conservative outer bound.',
                'total_l1_error':None if total is None else str(total),
                'scope':'Linear visible source coordinates in the declared J3 corner, conditional on the acquisition budgets. Calibration intervals may be correlated; no statistical independence or full source reconstruction is inferred.'}

    def separate(self,first,second,errors,total_l1_error=None):
        ctx.prec=self.precision_bits;self._keys(first);self._keys(second)
        budgets,total=self._budgets(errors,total_l1_error)
        gaps={};separators=[]
        for n in self.names:
            a=base.complex_value(first[n]);b=base.complex_value(second[n]);g=self.gain[n]
            # Distance between OUTER calibration disks, not just predictions
            # computed using the same unknown ideal gain.
            gap=(abs(a-b)-self.defect[n]*(abs(a)+abs(b)))/g
            gaps[n]=arb(gap.lower()) if gap>0 else arb(0)
            if gaps[n]>2*budgets[n]:separators.append(n)
        global_separation=total is not None and sum(gaps.values(),arb(0))>2*total
        return {'mode':self.mode,'certified_distinct':bool(separators or global_separation),
                'separating_channels':separators,'using_total_l1_budget':bool(global_separation),
                'raw_calibration_robust_distance_lower_by_channel':{n:str(v) for n,v in gaps.items()},
                'meaning':'False means not certified by these conservative bounds, not that the predictions are equal. True includes calibration uncertainty and both acquisitions error budgets.'}

if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit(__doc__)
    data=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    observer=ThreeChannelObserver(precision_bits=data.get('precision_bits',2048),mode=data.get('mode','private'))
    result=observer.normalize(data['raw'],data['errors'],data.get('total_l1_error'))
    if 'predictions' in data:
        if len(data['predictions'])!=2:raise ValueError('Two predictions required')
        result['prediction_comparison']=observer.separate(*data['predictions'],data['errors'],data.get('total_l1_error'))
    print(json.dumps(result,indent=2))
