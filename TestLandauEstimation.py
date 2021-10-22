from ROOT import TRandom,TH1F
import matplotlib.pyplot as plt
import statistics as stat
r = TRandom()
m=10
s=10

print("### Check mean/std-dev estimation of Landau distributed data as function of statistics")
print("# mpv = ",m)
print("# sigma = ",s)

nstat = [100*pow(2,i) for i in range(1,8)]
ntimes = 100
print("n-toys/point:",ntimes)
print("it can take a bit of time (>20s)...")
means=[]
meansErr=[]
stddevs=[]
stddevsErr=[]
pull=[]
for np in nstat:
    pull.clear()
    imean=[]
    imeanErr=[]
    istddev=[]
    istddevErr=[]
    for n in range(ntimes):
        h = TH1F("h","",100,0,100)
        for i in range(int(np)):
            h.Fill(r.Landau(m,s))

        imean.append(h.GetMean())
        imeanErr.append(h.GetMeanError())
        istddev.append(h.GetStdDev())
        istddevErr.append(h.GetStdDevError())
        del h
    means.append(stat.mean(imean))
    meansErr.append(stat.pstdev(imean))
    stddevs.append(stat.mean(istddev))
    stddevsErr.append(stat.pstdev(istddev))
    pull=[(istddev[i]-stat.mean(istddev))/istddevErr[i] for i in range(len(imean)-1)]

fig = plt.figure()
ax = fig.add_subplot(3, 1, 1)
ax.errorbar(nstat,means,yerr=meansErr)
ax.set_xscale('log')
ax.set_xlabel('#entries/plot')
ax.set_ylabel('mean estimation')
ax = fig.add_subplot(3, 1, 2)
ax.errorbar(nstat,stddevs,yerr=stddevsErr)
ax.set_xscale('log')
ax.set_xlabel('#entries/plot')
ax.set_ylabel('std-dev estimation')
ax = fig.add_subplot(3, 1, 3)
ax.hist(pull)
ax.set_xlabel('pull')
print("Pull results:")
print("mean: ",stat.mean(pull), "stdev: ",stat.stdev(pull))
plt.show()
