import numpy as np 
from matplotlib import pyplot as pp

from Chandra import Time

#from bad_times import nsm, ssm

def overlap(table1, table2):
    """This function looks for overlap between two sets of ranges, 
    usually times, formatted in seconds. 
    
    It will output a boolean array equal in length to table1.
    Each input table must be formatted with two columns: 
    range start and range stop.
    The output will be True if the corresponding range in table1
    overlaps with any range in table2.  The output will be
    otherwise False.
    """
    out = np.zeros(np.size(table1, axis=0), dtype='bool')
    for i in range(np.size(table1, axis=0)):
        s1_s2 = table1[i, 0] < table2[:, 0] 
        s1_e2 = table1[i, 0] <= table2[:, 1]
        e1_s2 = table1[i, 1] < table2[:, 0]
        e1_e2 = table1[i, 1] < table2[:, 1]
        # no overlap occurs when all four parameters above either == 0 or 1
        sum_params = np.sum(np.array([s1_s2, s1_e2, e1_s2, e1_e2]), axis=0)
        olap = (sum_params == 1) | (sum_params == 2) | (sum_params == 3)
        out[i] = np.any(olap)
    return out

def str_to_secs(table):
    """This function will take a table of time ranges formatted as strings 
    (compatible with bad_times) and convert it to an nx2 array in DateTime 
    seconds
    """
    out = np.zeros([len(table), 2])
    for i in range(len(table)):
        t1, t2 = table[i].split()
        out[i, 0] = Time.DateTime(t1).secs
        out[i, 1] = Time.DateTime(t2).secs
    return out    

def read_torque_table(table):
    """This function reads a comma-delimited text file of 31x136 solar torque  
    values and outputs the values as an array
    """
    f = open(table)
    lines = f.readlines()
    f.close()
    out = np.zeros((61, 136))
    line_num = 0
    for line in lines:
        fields = line.split()
        out[line_num, :] = [float(field) for field in fields]
        line_num = line_num + 1
    return out

def write_torque_table(A, filename):
    """This function writes an array A to a comma-delimited text file with a 
    user-defined filename.
    """
    f = open(filename, 'w')
    for row in range(np.size(A, axis=0)):
        A[row,:].tofile(f, sep=',')
        f.write('\n')
    f.close()    

def read_MCC_results(table):
    """This function reads a fixed-width text file generated by MCC's momentum
    plot using the telemetry overlay and Plot2Text functions.
    Returns time, predictions, actual values
    """
    f = open(table)
    lines = f.readlines()
    lines = lines[1:] # discard header line
    f.close()
    t = np.zeros(len(lines))
    predicts = np.zeros((len(lines), 3))
    actuals = np.zeros((len(lines), 3))
    line_num = 0
    for line in lines:
        fields = line.split()
        t[line_num] = Time.DateTime(fields[0]).secs
        predicts[line_num, :] = [float(field) for field in fields[1:4]]
        actuals[line_num, :] = [float(field) for field in fields[5:8]]
        line_num = line_num + 1
    return t, predicts, actuals

def find_closest(a, b):
    """This function returns an array of length a with the indices of 
    array b that are closest to the values of array a.
    """
    a = np.atleast_1d(np.array(a))
    b = np.atleast_1d(np.array(b))
    out = [np.argmin(abs(b - a1)) for a1 in a]
    return out
    
def find_last_before(a, b):
    """This function returns an array of length a with the indices of 
    array b that are closest without going over the values of array a.
    (Bob Barker rules.  Assumes b is sorted by magnitude.)
    """
    out = np.array([np.searchsorted(b,a,side='left') - 1])
    out[out==-1] = 0
    return out    
     
def find_first_after(a, b):
    """This function returns an array of length a with the indices of 
    array b that are closest without being less than the values of array a.
    (Opposite of Bob Barker rules.  Assumes b is sorted by magnitude.)
    """
    out = np.array(np.searchsorted(b,a,side='right'))
    return out  
    
def append_rss(A):
    """This function appends the squareroot of the sum of the squares
    of all the other values in each row.  
    """
    rss = np.sqrt(np.diag(A.dot(A.transpose()))) 
    out = np.hstack((A, np.atleast_2d(rss).transpose())) 
    return out

def ceil_to_value(number, round_to):
    """This function rounds a given input up to the nearest even multiple
    of the supplied "roundto" input
    """
    number = float(number)
    round_to = float(round_to)
    return (np.ceil(number / round_to) * round_to)    
    
def heat_map(x, y, bins=(20,20), colorbar=True, **kwargs):
    """Plots a "heat map", i.e. a scatter plot highlighting density

    Based on an exmple from 
    http://www.physics.ucdavis.edu/~dwittman/Matplotlib-examples/

    Inputs: 
    x = x vals (as from a scatter plot)
    y = y vals (as from a scatter plot)
    bins = int or tuple bins to feed into histogram2d
    colorbar = whether or not to display colorbar (default=True)
    x_lim = x limits of plot
    y_lim = y_limits of plot
    """
    if kwargs.has_key('x_lim'):
        x_lim = kwargs.pop('x_lim')
    else:  
        x_lim = [np.min(x), np.max(x)]
    if kwargs.has_key('y_lim'):
        y_lim = kwargs.pop('y_lim')
    else:  
        y_lim = [min(y), max(y)]
    hist,xedges,yedges = np.histogram2d(x,y,bins=bins,range=[x_lim,y_lim])
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    pp.imshow(hist.T,extent=extent,interpolation='nearest',origin='lower', aspect='auto')
    if colorbar==True:
        pp.colorbar()
    pp.show()    

def same_limits(subs):
    """Sets the x-limits and y-limits for a given set of subplots
    equal to the collective mins and maxes
    
    Inputs:  
    subs = subplots (tuple of 3-digit subplot numbers)
    
    e.g.  same_limits((411, 412, 413, 414))
    """    
    all_limits = np.zeros((len(subs), 4))
    for sub, i in zip(subs, range(len(subs))):
        pp.subplot(sub)
        all_limits[i,:] = pp.axis()
    best_limits = (min(all_limits[:,0]), max(all_limits[:,1]), 
                   min(all_limits[:,2]), max(all_limits[:,3]))
    for i in subs:
        pp.subplot(i)
        pp.axis(best_limits)

def append_to_array(a, pos=-1, val=0):
    """Appends a zero (or user-defined value) to a given one-dimensional array, 
    either at the end (pos=-1) or beginning (pos=0).
    
    e.g. append_to_array(arange(5),pos=-1)
    returns array([0, 1, 2, 3, 4, 0])
    """
    val_a = np.array([val])
    if pos==0:
        out = np.concatenate([val_a, a])
    elif pos==-1:
        out = np.concatenate([a, val_a])
    return out
    
def remove_therm_dropouts(tlm):
    """Attempts to remove MUPS-1 and MUPS-2 thermistor dropouts from a 
    telemetry data set acquired by:
        fetch.Msidset(['PM1THV1T','PM1THV2T','PM2THV1T','PM2THV2T'],
                      starttime, endtime)

    The timestamps for each msid must be the same.  This can be accomplished
    by using the '5min' or 'daily' statistics or by using the .interpolate
    function.
    
    Returns the same telemetry set with intervals removed for the following 
    conditions:
        -MUPS-1A & MUPS-1B temps vary by > 10 deg F
        -MUPS-2A & MUPS-2B temps vary by > 10 deg F
        -MUPS-1B & MUPS-2B temps vary by > 30 deg F
        
    As a repurcussion, this algorithm will remove some "valid" telemetry 
    during the rare heater cycles in early mission.
    
    Note that temperatures will also naturally vary around momentum unloads 
    due to heat soakback, so it is recommended to exclude unloads from the 
    data set (or accept that dropout false-positives will occur during these 
    timeframes).   
    
    Note that MUPS-1B is the only thermistor in this set that does not 
    currently experience dropouts.    
    """
    msids = ['PM1THV1T', 'PM1THV2T', 'PM2THV1T', 'PM2THV2T']
    mups1a = tlm['PM1THV1T'].vals
    mups1b = tlm['PM1THV2T'].vals
    mups2a = tlm['PM2THV1T'].vals
    mups2b = tlm['PM2THV2T'].vals
    t = tlm['PM1THV1T'].times
    for msid in msids:
        if np.any(tlm[msid].times != t):
            raise inputError('Time sets do not match')
    dropout_1 = np.abs(mups1a - mups1b) > 10
    dropout_2 = np.abs(mups2a - mups2b) > 10
    dropout_b = np.abs(mups1b - mups2b) > 30   
    dropouts = dropout_1 | dropout_2 | dropout_b 
    for msid in msids:
        tlm[msid].times = tlm[msid].times[~dropouts]
        tlm[msid].vals = tlm[msid].vals[~dropouts]
    return tlm