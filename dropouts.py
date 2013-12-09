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

close('all')

msids = ['PM1THV1T','PM2THV1T','PM2THV2T','PR1TV01T','PLAEV4AT','PLAEV2BT']

for msid in msids:
    plot_dropouts(msid)