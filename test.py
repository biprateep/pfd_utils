"""
test the functions
"""
import prepfold as pf
import sys
    
testpfd = "../CAND2_fine_442.54ms_Cand.pfd"

tp = pf.pfd(testpfd)

if (1):
    print tp.start_secs
    print tp.mid_secs
    print tp.start_topo_MJDs
    print tp.mid_topo_MJDs
    print tp.T

#tp.kill_subbands([6,7,8,9,30,31,32,33])
#tp.kill_intervals([2,3,4,5,6])

#tp.plot_chi2_vs_sub()
#(chis, DMs) = tp.plot_chi2_vs_DM(0.0, 50.0, 501, interp=1)
#best_index = Num.argmax(chis)
#print "Best DM = ", DMs[best_index]

(chis, DMs) = tp.plot_chi2_vs_DM(0.0, 50.0, 501)
best_index = Num.argmax(chis)
print "Best DM = ", DMs[best_index]

#tp.dedisperse(tp.bestdm)
tp.plot_subbands()
tp.plot_sumprof()
print "DM =", tp.bestdm, "gives reduced chi^2 =", tp.calc_redchi2()

tp.plot_intervals()