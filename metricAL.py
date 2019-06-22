import sys
import os
import numpy as np



trantab = str.maketrans('RrWw', '0011')


# s is RW sequence, in format of '0 0 0 1 1 0 1 0 1', or 'R R R W W R W R W', flexible on blank/comma
def RW2AP(s, add_eos=False):
    if isinstance(s, str):  
        s = s.translate(trantab).replace(' ','').replace(',','')
        if add_eos: # to add eos token for both src and tgt if you did not do it during RW generating
            idx = s.rfind('0')
            s = s[:idx+1]+'0'+s[idx+1:]+'1'  # remove last 0/1(<eos>) to keep actuall setence length
            # s = (s[:idx]+s[idx+1:])[:-1]  # remove last 0/1(<eos>) to keep actuall setence length
    else: return None
    x, y = s.count('0'), s.count('1')
    if x == 0 or y == 0: return 0

    count = 0
    curr = []
    for i in s:
        if i == '0': count += 1
        else: curr.append(count)
    return sum(curr) / x / y


# s is RW sequence, in format of '0 0 0 1 1 0 1 0 1', or 'R R R W W R W R W', flexible on blank/comma
def RW2AL(s, add_eos=False):
    if isinstance(s, str):  
        s = s.translate(trantab).replace(' ','').replace(',','')
        if add_eos: # to add eos token for both src and tgt if you did not do it during RW generating
            idx = s.rfind('0')
            s = s[:idx+1]+'0'+s[idx+1:]+'1'  # remove last 0/1(<eos>) to keep actuall setence length
            # s = (s[:idx]+s[idx+1:])[:-1]  # remove last 0/1(<eos>) to keep actuall setence length
    else: return None
    x, y = s.count('0'), s.count('1')
    if x == 0 or y == 0: return 0

    count = 0
    rate = y/x
    curr = []
    for i in s:
        if i == '0': count += 1
        else: curr.append(count)
        if i == '1' and count == x: break
    y1 = len(curr)
    diag = [(t-1)/rate for t in range(1, y1+1)]
    return sum(l1-l2 for l1,l2 in zip(curr,diag)) / y1



def RW2AL_file(file_rw, is_weight_ave=False):
    ALs, Lsrc = [], []
    for line in open(file_rw, 'r').readlines():
        line = line.strip()
        rw = RW2AL(line)
        if rw is not None:
            ALs.append(rw)
            Lsrc.append(line.count('0'))
    
    AL = np.average(ALs) if is_weight_ave else np.average(ALs, weights=Lsrc)
    return AL


if __name__=="__main__":
    file_rw = 'sample_rw.txt'
    print("corpus mean:", RW2AL_file(file_rw))
    print("weighted average:", RW2AL_file(file_rw, is_weight_ave=True))
