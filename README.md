code for STACL(**S**imultaneous **T**ranslation with Intergrated **A**niticipation and **C**ontrollable **L**atency) [paper](https://arxiv.org/abs/1810.08398)

 ### metric of Average Lagging (AL)  
details in Sec.4 of STACL paper

#### run sample 
```bash
python metricAL.py
# output:
# corpus mean: 5.96639835314598
# weighted average: 5.486924076400874
```
#### functions
1. `RW2AL(s, add_eos=False)`  
- get `AL` value from a single **RW** sequence  
- `s` is **RW** sequence, a string, in format of `0 0 0 1 1 0 1 0 1`, or `R R R W W R W R W`, flexible on blank/comma  
- `add_eos` is used to add eos token for both src and tgt if you did not do it during RW generating (to add tail `0` and `1` into the RW sequence)  
- output is a single value as `AL`

1. `RW2AL_file(file_rw, is_weight_ave=False)` 
- get `AL` value from a file with **RW** sequences  
- `file_rw` is the path to a **RW** sequence file  
- `is_weight_ave` is used to return weighted average result against READ length or mean result on corpus  
- output is a single value as `AL`  


