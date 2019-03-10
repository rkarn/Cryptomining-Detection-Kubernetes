import itertools
syscalldict = dict()
syshistogram = dict()
for syscalltype in Syscalls_frame.keys():
    print '----------------------------{0}---------------------------'.format(syscalltype)
    syscalldict[syscalltype] = list(itertools.chain(*Syscalls_frame[syscalltype].values.tolist()))
    syscalllist = syscalldict[syscalltype]
    current_syshist = dict()
    for usys in set(syscalllist):
        print usys,'\t ------->',syscalllist.count(usys)
        current_syshist[usys] = syscalllist.count(usys)
    syshistogram[syscalltype] = current_syshist

unique_syscall = dict()
for syslist in syshistogram.keys():
    unique_syscall[syslist] = syshistogram[syslist].keys()
    
Allminers_uniquesyscalls = []
for i,key in enumerate(unique_syscall.keys()):
    if i == 0:
        currlist = unique_syscall[key]
    else:
        common_syscall = list(set(currlist) & set(unique_syscall[key]))
        currlist = common_syscall
    Allminers_uniquesyscalls = list(set(Allminers_uniquesyscalls).union(unique_syscall[key]))
    
print 'Common syscalls among all 5 cryptominers:',common_syscall,'.\n','Descriptions are:'
for sys in common_syscall:
    try:
        print sys,'\t', LinuxKernelSyscalls[sys]
    except:
        print sys,' is not available in the Linux syscall list given at https://filippo.io/linux-syscall-table/.'

print '\n'
syscounter = 0
common_sys_4miners = []
for syscall in Allminers_uniquesyscalls:
    for key in unique_syscall.keys():
        if syscall in unique_syscall[key]:
            syscounter = syscounter+1
    if syscounter >= 4:
        syscounter = 0
        common_sys_4miners.append(syscall)
print 'Common syscalls among 4 cryptominers:',common_sys_4miners,'.\n','Descriptions are:'
for sys in common_sys_4miners:
    try:
        print sys,'\t', LinuxKernelSyscalls[sys]
    except:
        print sys,' is not available in the Linux syscall list given at https://filippo.io/linux-syscall-table/.'

print '\n'
syscounter = 0
common_sys_3iners = []
for syscall in Allminers_uniquesyscalls:
    for key in unique_syscall.keys():
        if syscall in unique_syscall[key]:
            syscounter = syscounter+1
    if syscounter >= 3:
        syscounter = 0
        common_sys_3iners.append(syscall)
print 'Common syscalls among 3 cryptominers:',common_sys_3iners,'.\n','Descriptions are:'
for sys in common_sys_3iners:
    try:
        print sys,'\t', LinuxKernelSyscalls[sys]  
    except:
        print sys,' is not available in the Linux syscall list given at https://filippo.io/linux-syscall-table/.'
