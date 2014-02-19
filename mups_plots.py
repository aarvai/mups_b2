import numpy as np
from Ska.engarchive import fetch_eng as fetch
from Chandra.Time import DateTime
import matplotlib
import matplotlib.pyplot as plt

from utilities import find_first_after, find_last_before, append_to_array

def mups_ELBI(t1, t2, **kwargs):
    close('all')
    msids = ['AOVBM1FS', 'AOVBM2FS', 'AOVBM3FS', 'AOVBM4FS', 'ELBI_LOW']    
    
    data = fetch.Msidset(msids, t1, t2, stat=None)
   
    xticks = np.linspace(DateTime(t1).secs, DateTime(t2).secs, 11)
    xticklabels = [DateTime(t).date[5:17] for t in xticks]

    fig = plt.figure(figsize=[18,9], facecolor='w')
    rect = [0.06, 0.15, 0.88, 0.75]
    ax1 = fig.add_axes(rect)

    for n, names in enumerate(msids[:4]):
        ax1.plot(data[msids[n]].times, data[msids[n]].raw_vals + n * 2.0, 
                 color=[0.4, 0.4, 0.4], linewidth=3.0)
        fire = data[msids[n]].raw_vals == 1
        ax1.plot(data[msids[n]].times[fire], data[msids[n]].raw_vals[fire] + n * 2.0, 
                 '*', color=[0.4, 0.4, 0.4], markersize=10)       
    ax1.set_ylim(-1, 20)
    ax1.set_yticks([0,2,4,6])
    ax1.set_yticklabels(msids[:4], rotation=45)
    for t in ax1.yaxis.get_ticklines():
        t.set_visible(False) 
        ax1.set_xticks(xticks)
    ax1.set_xticklabels(xticklabels, rotation=45, ha='right')
    ax1.set_xlim(xticks[0], xticks[-1])
    
    ax2 = fig.add_axes(rect, frameon=False)
    ax2.plot(data['ELBI_LOW'].times, data['ELBI_LOW'].vals, color="#56B4E9", linewidth=3.0)
    for thr in range(1,5):
        msid = 'AOVBM' + str(thr) + 'FS'
        fire = data[msid].raw_vals == 1 
        first_fire = append_to_array(~fire[:-1] & fire[1:], pos=0, val=bool(0))
        t_fire = data[msid].times[fire]
        for t in t_fire:
            i1 = find_first_after(t-.6, data['ELBI_LOW'].times)
            i2 = find_last_before(t, data['ELBI_LOW'].times)
            ax2.plot(data['ELBI_LOW'].times[i1:i2+1], data['ELBI_LOW'].vals[i1:i2+1], '*-', color='#D55E00', linewidth=3.0, mew=0, markersize=10)
    ax2.set_ylim(16,31)    
    ax2.yaxis.set_label_position('right')
    ax2.yaxis.tick_right()
    ax2.set_ylabel('ELBI_LOW')
    ax2.set_xticks(xticks)
    ax2.set_xticklabels('')
    ax2.set_xlim(xticks[0], xticks[-1])
 
    title('MUPS B-Side Activations and Bus Current - ' + t1[:8] + ' Firing')
    if kwargs.has_key('savefig'):
        fig.savefig(kwargs.pop('savefig'))
    else:
        fig.savefig(t1[:4] + '_' + t1[5:8] + '_elbi.png')
    
def mups_delta_ELBI(t1, t2):
    close('all')
    msids = ['AOVBM1FS', 'AOVBM2FS', 'AOVBM3FS', 'AOVBM4FS', 'ELBI_LOW']    
    
    data = fetch.Msidset(msids, t1, t2, stat=None)
    
    xticks = np.linspace(DateTime(t1).secs, DateTime(t2).secs, 11)
    xticklabels = [DateTime(t).date[5:17] for t in xticks]

    fig = plt.figure(figsize=[18,9], facecolor='w')
    rect = [0.06, 0.15, 0.88, 0.75]
    ax1 = fig.add_axes(rect)

    for n, names in enumerate(msids[:4]):
        ax1.plot(data[msids[n]].times, data[msids[n]].raw_vals + n * 2.0, 
                 color=[0.4, 0.4, 0.4])
    ax1.set_ylim(-1, 8)
    ax1.set_yticks([0,2,4,6])
    ax1.set_yticklabels(msids[:4], rotation=45)
    for t in ax1.yaxis.get_ticklines():
        t.set_visible(False) 
        ax1.set_xticks(xticks)
    ax1.set_xticklabels(xticklabels, rotation=45, ha='right')
    ax1.set_xlim(xticks[0], xticks[-1])
    
    ax2 = fig.add_axes(rect, frameon=False)
    ax2.plot(data['ELBI_LOW'].times[1:], diff(data['ELBI_LOW'].vals), color="#56B4E9", alpha=0.5)
    ax2.yaxis.set_label_position('right')
    ax2.yaxis.tick_right()
    ax2.set_ylabel('Change in ELBI_LOW')
    ax2.set_xticks(xticks)
    ax2.set_xticklabels('')
    ax2.set_xlim(xticks[0], xticks[-1])
 
    title('MUPS B-Side Activations and Bus Current - ' + t1[:8] + ' Firing')

    fig.savefig(t1[:4] + '_' + t1[5:8] + '_delta_elbi.png')

def mups_2_temps(t1, t2):
    
    close('all')
    
    msids = ['AOVBM1FS', 'AOVBM2FS', 'AOVBM3FS', 'AOVBM4FS', 'PM2THV1T', 'PM2THV2T']

    data = fetch.Msidset(msids, t1, t2, stat=None)

    xticks = np.linspace(DateTime(t1).secs, DateTime(t2).secs, 11)
    xticklabels = [DateTime(t).date[5:17] for t in xticks]
    
    fig = plt.figure(figsize=[18,9], facecolor='w')
    rect = [0.06, 0.15, 0.88, 0.75]
    ax1 = fig.add_axes(rect)
    
    for n, names in enumerate(msids[:4]):
        ax1.plot(data[msids[n]].times, data[msids[n]].raw_vals + n * 2.0, 
                 color=[0.4, 0.4, 0.4])
    ax1.set_ylim(-1, 8)
    ax1.set_yticks([0,2,4,6])
    ax1.set_yticklabels(msids[:4], rotation=45)
    for t in ax1.yaxis.get_ticklines():
        t.set_visible(False) 
    ax1.set_xticks(xticks)
    ax1.set_xticklabels(xticklabels, rotation=45, ha='right')
    ax1.set_xlim(xticks[0], xticks[-1])
    
    ax2 = fig.add_axes(rect, frameon=False)
    ax2.plot(data[msids[-2]].times, data[msids[-2]].vals, color="#56B4E9", alpha=0.5, label=msids[-2])
    ax2.plot(data[msids[-1]].times, data[msids[-1]].vals, color="#009E73", alpha=0.5, label=msids[-1])   
    ax2.legend()
    ax2.yaxis.set_label_position('right')
    ax2.yaxis.tick_right()
    ax2.set_ylabel('MUPS-2 Temperatures [deg F]')
    ax2.set_xticks(xticks)
    ax2.set_xticklabels('')
    ax2.set_xlim(xticks[0], xticks[-1])
    
    title('MUPS B-Side Activations and MUPS 2B Temperature - ' + t1[:8] + ' Firing')

    fig.savefig(t1[:4] + '_' + t1[5:8] + '_mups2_temps.png')

def mups_2_temps_xout_2():
    
    close('all')
    
    t1 = '2013:231:11:00:00'
    t2 = '2013:231:12:45:00'
    
    msids = ['AOVBM2FS', 'PM2THV1T', 'PM2THV2T']

    data = fetch.Msidset(msids, t1, t2, stat=None)
    b2_exp = data['PM2THV1T'].vals + 3

    xticks = np.linspace(DateTime(t1).secs, DateTime(t2).secs, 11)
    xticklabels = [DateTime(t).date[5:17] for t in xticks]
    
    fig = plt.figure(figsize=[18,9], facecolor='w')
    rect = [0.06, 0.15, 0.88, 0.75]
    ax1 = fig.add_axes(rect)
    
    ax1.plot(data['AOVBM2FS'].times, data['AOVBM2FS'].raw_vals, 
             color=[0.4, 0.4, 0.4])
    ax1.set_ylim(-1, 12)
    ax1.set_yticks([0])
    ax1.set_yticklabels(['AOVBM2FS'], rotation=45)
    for t in ax1.yaxis.get_ticklines():
        t.set_visible(False) 
    ax1.set_xticks(xticks)
    ax1.set_xticklabels(xticklabels, rotation=45, ha='right')
    ax1.set_xlim(xticks[0], xticks[-1])

    ax2 = fig.add_axes(rect, frameon=False)
    ax2.plot(data['PM2THV1T'].times, data['PM2THV1T'].vals, color="#56B4E9", linewidth=4.0, label='2A Actual')
    ax2.plot(data['PM2THV2T'].times, data['PM2THV2T'].vals, 'm', linewidth=4.0, label='2B Actual')   
    ax2.plot(data['PM2THV1T'].times, b2_exp, 'm:', linewidth=4.0, label='2B Predicted w/o Firings')
    ax2.legend(loc='upper left')
    ax2.set_ylim(100, 150)
    ax2.yaxis.set_label_position('right')
    ax2.yaxis.tick_right()
    ax2.set_ylabel('MUPS-2 Temperatures [deg F]')
    ax2.set_xticks(xticks)
    ax2.set_xticklabels('')
    ax2.set_xlim(xticks[0], xticks[-1])
    
    title('MUPS B-Side Activations and MUPS 2B Temperature - 2013:231 Firing')

    fig.savefig('2013_231_mups2_temps_expected.png')

def mups_2_delta_temps(t1, t2):
    
    close('all')
    
    msids = ['AOVBM1FS', 'AOVBM2FS', 'AOVBM3FS', 'AOVBM4FS', 'PM2THV1T', 'PM2THV2T']

    data = fetch.Msidset(msids, t1, t2, stat=None)

    xticks = np.linspace(DateTime(t1).secs, DateTime(t2).secs, 11)
    xticklabels = [DateTime(t).date[5:17] for t in xticks]
    
    fig = plt.figure(figsize=[18,9], facecolor='w')
    rect = [0.06, 0.15, 0.88, 0.75]
    ax1 = fig.add_axes(rect)
    
    ax1.plot(data['AOVBM2FS'].times, data['AOVBM2FS'].raw_vals, 
             color=[0.4, 0.4, 0.4])
    ax1.set_ylim(-1, 12)
    ax1.set_yticks([0])
    ax1.set_yticklabels(['AOVBM2FS'], rotation=45)
    for t in ax1.yaxis.get_ticklines():
        t.set_visible(False) 
    ax1.set_xticks(xticks)
    ax1.set_xticklabels(xticklabels, rotation=45, ha='right')
    ax1.set_xlim(xticks[0], xticks[-1])

    data.interpolate(dt=.25625)
    dt = data['PM2THV2T'].vals - data['PM2THV1T'].vals 
    
    ax2 = fig.add_axes(rect, frameon=False)
    ax2.plot(data[msids[-2]].times, dt, 'g', linewidth=3.0, label=msids[-2])
    ax2.set_ylim(-1, 6)
    ax2.yaxis.set_label_position('right')
    ax2.yaxis.tick_right()
    ax2.set_ylabel('MUPS-2B minus MUPS-2A Temps [deg F]')
    ax2.set_xticks(xticks)
    ax2.set_xticklabels('')
    ax2.set_xlim(xticks[0], xticks[-1])
    
    title('MUPS B-Side Activations and MUPS-2 B-side vs A-side Temps - ' + t1[:8] + ' Firing')

    fig.savefig(t1[:4] + '_' + t1[5:8] + '_mups2_delta_temps.png')

def att_errs(t1, t2, ylim=[-1000,1000]):
    
    close('all')
    
    msids = ['AOVBM1FS', 'AOVBM2FS', 'AOVBM3FS', 'AOVBM4FS', 'AOATTER1', 'AOATTER2', 'AOATTER3']

    data = fetch.Msidset(msids, t1, t2, stat=None)

    xticks = np.linspace(DateTime(t1).secs, DateTime(t2).secs, 11)
    xticklabels = [DateTime(t).date[5:17] for t in xticks]
    
    fig = plt.figure(figsize=[19,9], facecolor='w')
    rect = [0.06, 0.15, 0.88, 0.75]
    ax1 = fig.add_axes(rect)
    
    for n, names in enumerate(msids[:4]):
        ax1.plot(data[msids[n]].times, data[msids[n]].raw_vals + n * 2.0, 
                 color=[0.4, 0.4, 0.4])
    ax1.set_ylim(-1, 20)
    ax1.set_yticks([0,2,4,6])
    ax1.set_yticklabels(['B1 Fire','B2 Fire', 'B3 Fire', 'B4 Fire'], rotation=45)
    for t in ax1.yaxis.get_ticklines():
        t.set_visible(False) 
    ax1.set_xticks(xticks)
    ax1.set_xticklabels(xticklabels, rotation=45, ha='right')
    ax1.set_xlim(xticks[0], xticks[-1])
    
    ax2 = fig.add_axes(rect, frameon=False)
    ax2.plot(data[msids[-3]].times, data[msids[-3]].vals*180/pi*3600, color="#56B4E9", alpha=0.5, label='Roll Attitude Error', linewidth=5)
    ax2.plot(data[msids[-2]].times, data[msids[-2]].vals*180/pi*3600, color="#009E73", alpha=0.5, label='Pitch Attitude Error', linewidth=5)   
    ax2.plot(data[msids[-1]].times, data[msids[-1]].vals*180/pi*3600, color="#E69F00", alpha=0.5, label='Yaw Attitude Error', linewidth=5)   
    ax2.set_ylim(ylim)
    ax2.legend()
    ax2.yaxis.set_label_position('right')
    ax2.yaxis.tick_right()
    ax2.set_ylabel('Attitude Errors [arcsec]')
    ax2.set_xticks(xticks)
    ax2.set_xticklabels('')
    ax2.set_xlim(xticks[0], xticks[-1])

    matplotlib.rcParams.update({'font.size': 16})
    
    title('MUPS B-Side Activations and Attitude Errors - ' + t1[:8] + ' Firing')

    fig.savefig(t1[:4] + '_' + t1[5:8] + '_mups2_att_errs.png')

def timeline(t1, t2):
    
    close('all')
    
    msids = ['PM1THV1T', 'PM1THV2T','PM2THV1T', 'PM2THV2T', 
             'AOVBM1FS', 'AOVBM2FS', 'AOVBM3FS', 'AOVBM4FS', 
             'PITCH', 'ROLL', 'AOPCADMD', 'EECLIPSE']
    
    x = fetch.Msidset(msids,t1, t2)
    
    figure(1, figsize=(15,18))
    subplot(611)
    x['PM1THV1T'].plot('g-', label='PM1THV1T')
    x['PM1THV2T'].plot('g:', label='PM1THV2T')
    x['PM2THV1T'].plot('r-', label='PM2THV1T')
    x['PM2THV2T'].plot('r:', label='PM2THV2T')
    legend()
    title('MUPS-1B and MUPS-2B Valve Temps')
    
    subplot(612)
    x['AOVBM1FS'].plot('g-', label='AOVBM1FS')
    x['AOVBM2FS'].plot('r-', label='AOVBM2FS')
    x['AOVBM3FS'].plot('b-', label='AOVBM3FS')
    x['AOVBM4FS'].plot('c-', label='AOVBM4FS')    
    legend()
    title('MUPS-B Firing Status')
    
    subplot(613)
    x['PITCH'].plot('b-', label='PITCH')
    ylim([45,180])
    title('Pitch')
    ylabel('deg')
    
    subplot(614)
    x['ROLL'].plot('b-', label='ROLL')
    ylim([-10,10])
    title('Roll')
    ylabel('deg')
    
    subplot(615)
    x['AOPCADMD'].plot('b-', label='AOPCADMD')
    title('PCAD Mode')
    
    subplot(616)
    x['EECLIPSE'].plot('b-', label='EECLIPSE')
    title('Eclipse')
    
    savefig(t1[:4] + '_' + t1[5:8] + '_timeline.png')

def plot_dropouts(msid, thresh=-20):
    close('all')
    x = fetch.Msid(msid,'2012:300',stat='5min')
    d_temp = diff(x.vals)
    drop = d_temp < thresh
    figure()
    subplot(2,1,1)
    title(msid + ' Dropouts w.r.t. Time \n Dropout defined as:  T2 - T1 < ' + str(thresh) +' deg F')
    plot_cxctime(x.times, x.vals, 'b', label='All Temps')
    plot_cxctime(x.times[:-1][drop],x.vals[:-1][drop],'r.', alpha=.5, label='Temp Prior to a Dropout')
    ylabel('deg F')
    legend(loc=3)
    subplot(2,1,2)
    hist(x.vals, bins=20, range=[min(x.vals), max(x.vals)], normed=True, color='b', label='All Temps')
    hist(x.vals[:-1][drop], bins=20, range=[min(x.vals), max(x.vals)], normed=True, color='r', alpha=.5, label='Temp Prior to a Dropout')
    legend(loc=3)
    ylabel('Fraction of 5-min Data Points')
    xlabel('deg F')
    tight_layout()
    savefig(msid+'_dropouts.png')

    
    
    
    

    