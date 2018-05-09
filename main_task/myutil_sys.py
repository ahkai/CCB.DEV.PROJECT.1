import os, time

last_worktime=0
last_idletime=0

def get_cpu():
        global last_worktime, last_idletime
        f=open("/proc/stat","r")
        line=""
        while not "cpu " in line: line=f.readline()
        f.close()
        spl=line.split(" ")
        worktime=int(spl[2])+int(spl[3])+int(spl[4])
        idletime=int(spl[5])
        dworktime=(worktime-last_worktime)
        didletime=(idletime-last_idletime)
        rate=float(dworktime)/(didletime+dworktime)
        last_worktime=worktime
        last_idletime=idletime
        if(last_worktime==0): return 0
        return rate

def get_mem_usage_percent():
    try:
        f = open('/proc/meminfo', 'r')
        for line in f:
            if line.startswith('MemTotal:'):
                mem_total = int(line.split()[1])
            elif line.startswith('MemFree:'):
                mem_free = int(line.split()[1])
            elif line.startswith('Buffers:'):
                mem_buffer = int(line.split()[1])
            elif line.startswith('Cached:'):
                mem_cache = int(line.split()[1])
            elif line.startswith('SwapTotal:'):
                vmem_total = int(line.split()[1])
            elif line.startswith('SwapFree:'):
                vmem_free = int(line.split()[1])
            else:
                continue
        f.close()
    except:
        return None
    physical_percent = usage_percent(mem_total - (mem_free + mem_buffer + mem_cache), mem_total)
    virtual_percent = 0
    if vmem_total > 0:
        virtual_percent = usage_percent((vmem_total - vmem_free), vmem_total)
    return physical_percent, virtual_percent

def usage_percent(use, total):
    try:
        ret = (float(use) / total) * 100
    except ZeroDivisionError:
        raise Exception("ERROR - zero division error")
    return ret

def get_net_data():
    nc = '/proc/net/dev'
    fd = open(nc, "r")
    netcardstatus = False
    Totalrecv1 = 0
    Totalsend1 = 0

    for line in fd.readlines():
        if line.find("ens") > 0:
            field = line.split()
            recv = field[1]
            Totalrecv1 = Totalrecv1 + long(recv)
            Totalsend1 = Totalsend1 + long(field[9])

    fd.close()

    time.sleep(1)
    Totalrecv2 = 0
    Totalsend2 = 0

    fd = open(nc, "r")
    for line in fd.readlines():
        if line.find("ens") > 0:
            field = line.split()
            recv = field[1]
            Totalrecv2 = Totalrecv2 + long(recv)
            Totalsend2 = Totalsend2 + long(field[9])

    fd.close()

    return ( float( (Totalrecv2 - Totalrecv1) ), float( (Totalsend2 - Totalsend1) ) )

def gettotalusage():

    disk_tip = ''
    mem_tip = ''
    cpu_tip = ''

    statvfs = os.statvfs('/')

    total_disk_space = statvfs.f_frsize * statvfs.f_blocks
    free_disk_space = statvfs.f_frsize * statvfs.f_bfree
    disk_usage = (total_disk_space - free_disk_space) * 100.0 / total_disk_space
    disk_usage = int(disk_usage)
    disk_tip = str(disk_usage)

    mem_usage = get_mem_usage_percent()
    mem_usage = int(mem_usage[0])
    mem_tip =str(mem_usage)

    (new_recv, new_send) = get_net_data()
    # networkout = new_send/1024/1024
    # networkin = new_recv / 1024 / 1024
    networkout = new_send
    networkin = new_recv

    cpu_usage = int(get_cpu()*100)
    cpu_tip = str(cpu_usage)

    obj={}
    obj['disk'] = disk_tip
    obj['mem'] = mem_tip
    obj['cpu'] = cpu_tip
    obj['networkout'] = networkout
    obj['networkin'] = networkin


    return obj


