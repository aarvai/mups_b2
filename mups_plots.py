import numpy as np
from Ska.engarchive import fetch_eng as fetch
from Chandra.Time import DateTime
import matplotlib.pyplot as plt

from utilities import find_first_after, find_last_before, append_to_array

def mups_ELBI(t1, t2):
    close('all')
    msids = ['AOVBM1FS', 'AOVBM2FS', 'AOVBM3FS', 'AOVBM4FS', 'ELBI']    
    
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
    ax2.plot(data['ELBI'].times, data['ELBI'].vals, color="#56B4E9", alpha=0.5)
    ax2.yaxis.set_label_position('right')
    ax2.yaxis.tick_right()
    ax2.set_ylabel('ELBI')
    ax2.set_xticks(xticks)
    ax2.set_xticklabels('')
    ax2.set_xlim(xticks[0], xticks[-1])
 
    title('MUPS B-Side Activations and Bus Current - ' + t1[:8] + ' Firing')

    fig.savefig(t1[:4] + '_' + t1[5:8] + '_elbi.png')

def mups_delta_ELBI(t1, t2):
    close('all')
    msids = ['AOVBM1FS', 'AOVBM2FS', 'AOVBM3FS', 'AOVBM4FS', 'ELBI']    
    
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
    ax2.plot(data['ELBI'].times[1:], diff(data['ELBI'].vals), color="#56B4E9", alpha=0.5)
    ax2.yaxis.set_label_position('right')
    ax2.yaxis.tick_right()
    ax2.set_ylabel('Change in ELBI')
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

def mups_2_delta_temps(t1, t2):
    
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

    data.interpolate(dt=.25625)
    dt = data['PM2THV2T'].vals - data['PM2THV1T'].vals 
    
    ax2 = fig.add_axes(rect, frameon=False)
    ax2.plot(data[msids[-2]].times, dt, color="#0072B2", alpha=0.5, label=msids[-2])
    ax2.yaxis.set_label_position('right')
    ax2.yaxis.tick_right()
    ax2.set_ylabel('MUPS-2B minus MUPS-2A Temps [deg F]')
    ax2.set_xticks(xticks)
    ax2.set_xticklabels('')
    ax2.set_xlim(xticks[0], xticks[-1])
    
    title('MUPS B-Side Activations and MUPS-2 B-side vs A-side Temps - ' + t1[:8] + ' Firing')

    fig.savefig(t1[:4] + '_' + t1[5:8] + '_mups2_delta_temps.png')

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


def mups_ELBI(t1, t2):
    close('all')
    msids = ['AOVBM1FS', 'AOVBM2FS', 'AOVBM3FS', 'AOVBM4FS', 'ELBI']    
    
    data = fetch.Msidset(msids, t1, t2, stat=None)
   
    xticks = np.linspace(DateTime(t1).secs, DateTime(t2).secs, 11)
    xticklabels = [DateTime(t).date[5:17] for t in xticks]

    fig = plt.figure(figsize=[18,9], facecolor='w')
    rect = [0.06, 0.15, 0.88, 0.75]
    ax1 = fig.add_axes(rect)

    for n, names in enumerate(msids[:4]):
        ax1.plot(data[msids[n]].times, data[msids[n]].raw_vals + n * 2.0, 
                 color=[0.4, 0.4, 0.4])
        fire = data[msids[n]].raw_vals == 1
        ax1.plot(data[msids[n]].times[fire], data[msids[n]].raw_vals[fire] + n * 2.0, 
                 '*', color=[0.4, 0.4, 0.4])       
    ax1.set_ylim(-1, 20)
    ax1.set_yticks([0,2,4,6])
    ax1.set_yticklabels(msids[:4], rotation=45)
    for t in ax1.yaxis.get_ticklines():
        t.set_visible(False) 
        ax1.set_xticks(xticks)
    ax1.set_xticklabels(xticklabels, rotation=45, ha='right')
    ax1.set_xlim(xticks[0], xticks[-1])
    
    ax2 = fig.add_axes(rect, frameon=False)
    ax2.plot(data['ELBI'].times, data['ELBI'].vals, color="#56B4E9", alpha=0.5)
    for thr in range(1,5):
        msid = 'AOVBM' + str(thr) + 'FS'
        fire = data[msid].raw_vals == 1 
        first_fire = append_to_array(~fire[:-1] & fire[1:], pos=0, val=bool(0))
        t_fire = data[msid].times[fire]
        for t in t_fire:
            i1 = find_first_after(t-.6, data['ELBI'].times)
            i2 = find_last_before(t, data['ELBI'].times)
            ax2.plot(data['ELBI'].times[i1:i2+1], data['ELBI'].vals[i1:i2+1], color='r', alpha=0.5)
            ax2.plot(data['ELBI'].times[i1:i2+1], data['ELBI'].vals[i1:i2+1], 'r*', mew=0, alpha=0.5)
    if np.min(data['ELBI'].vals) < 55:
        ax2.set_ylim(45,60)
    else:
        ax2.set_ylim(50,65)
    ax2.set_ylim(45,65)    
    ax2.yaxis.set_label_position('right')
    ax2.yaxis.tick_right()
    ax2.set_ylabel('ELBI')
    ax2.set_xticks(xticks)
    ax2.set_xticklabels('')
    ax2.set_xlim(xticks[0], xticks[-1])
 
    title('MUPS B-Side Activations and Bus Current - ' + t1[:8] + ' Firing')

    fig.savefig(t1[:4] + '_' + t1[5:8] + '_elbi.png')
    
    
    
    

    