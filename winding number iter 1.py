import math
from matplotlib import pyplot as plt
import numpy as np
import random

def quad_no(dx,dy):
    if dx > 0 and dy > 0:
        #quadrant 1
        q = 1
    elif dx > 0 and dy < 0:
        #quadrant 2
        q = -1
    elif dx < 0 and dy < 0:
        #quadrant 3
        q = 1
    else:
        #quadrant 4
        q = -1
    return q

def quad_val(dx,dy):
    if dx > 0 and dy > 0:
        #quadrant 1
        qv = 0
    elif dx > 0 and dy < 0:
        #quadrant 2
        qv = 360
    elif dx < 0 and dy < 0:
        #quadrant 3
        qv = 180
    else:
        #quadrant 4
        qv = 180
    return qv

def angle(pnta,pntb,pntc):
    #distant
    dx_a = pntb[0]-pnta[0]
    dy_a = pntb[1]-pnta[1]
    dx_b = pntc[0]-pnta[0]
    dy_b = pntc[1]-pnta[1]
    
    #quadrant
    qn_a = quad_no(dx_a,dy_a)
    qn_b = quad_no(dx_b,dy_b)
    qv_a = quad_val(dx_a,dy_a)
    qv_b = quad_val(dx_b,dy_b)
    
    #angle
    try:
        a_a = math.floor(math.degrees(math.atan(dy_a/dx_a))*100)/100
    except:
        if dx_a > 0:
            a_a = 180
        else:
            a_a = 0 
            
    try:
        a_b = math.floor(math.degrees(math.atan(dy_b/dx_b))*100)/100
    except:
        if dx_b > 0:
            a_b = 180
        else:
            a_b = 0 
    
    cal_a = abs(a_a)*qn_a + qv_a
    cal_b = abs(a_b)*qn_b + qv_b
    
    ang = cal_a - cal_b
    
    if abs(ang) < 180:
        ang_cal = ang
    else:
        if ang > 1:
            ang_cal =  - 360 + ang
        else:
            ang_cal = 360 + ang
            
        
    return ang_cal
    #return [a_a,qv_a,cal_a,a_b,qv_b,cal_b,ang_cal]

# =============================================================================
# def pts_vector(pta,ptb):
#     v = (pta[0]-ptb[0],pta[1]-ptb[1])
#     return v
# 
# def unit_vector(vector):
#     """ Returns the unit vector of the vector.  """
#     return vector / np.linalg.norm(vector)
# 
# def angle_between(va, vb):
#     va_u = unit_vector(va)
#     vb_u = unit_vector(vb)
#     deg = math.degrees(np.arccos(np.clip(np.dot(va_u, vb_u), -1.0, 1.0)))
#     r_deg = math.floor(deg*10000)/10000
#     #deg = math.degrees(np.arccos(np.dot(va_u, vb_u)))
#     return r_deg
# =============================================================================


pnt_a = [[5,10]]
#polys = [[0,10],[10,10],[10,0],[0,0]]
#polys2 = [[0,10],[10,10],[10,0],[0,0,],[0,10]]
#polys = [[0,0],[10,0],[10,10],[0,10]]
polys = [[0,10],[5.77,0],[17.32,0],[23.09,10],[17.32,20],[5.77,30]]
polys2 = [[0,10],[5.77,0],[17.32,0],[23.09,10],[17.32,20],[5.77,30],[0,10]]
#polys = [[12.37,12.36],[90.83,12.36],[90.83,32.91],[36.44,32.91],[36.44,62.74],[12.39,62.74]]
#polys2 = [[12.37,12.36],[90.83,12.36],[90.83,32.91],[36.44,32.91],[36.44,62.74],[12.39,62.74],[12.37,12.36]]
b_pnts_x = []
b_pnts_y = []

#random points
pnts = [[] for i in range(20000)]
for pnt in pnts:
    pnt.append(random.randint(0, 100))
    pnt.append(random.randint(0, 100))
#print(pnts)

#points to series
for pnt0s in polys2:
    b_pnts_x.append(pnt0s[0])
    b_pnts_y.append(pnt0s[1])
    
inpt = []
outpt = []

#winding function
for pnt in pnt_a:
#for pnt in pnts:
    d = 0
    j = 0
    while j < len(polys):
        if j < len(polys) - 1:
            b = angle(pnt,polys[j],polys[j+1])
            print(b)
            d = d + b
            j = j + 1
            
        elif j == len(polys) - 1:
            b = angle(pnt,polys[j],polys[0])
            print(b)
            d = d + b
            j = j + 1
    e = math.floor(d)
    print(f"result {e}")
    if abs(e) < 10:
        outpt.append(pnt)
    else:
        inpt.append(pnt)
        
# =============================================================================
# for pnt in pnts:
#     d = 0
#     j = 0
#     while j < len(polys):
#         if j < len(polys) - 1:
#             va = pts_vector(pnt,polys[j])
#             vb = pts_vector(pnt,polys[j+1])
#             b = angle_between(va,vb)
#             print(b)
#             
#             d = d + b
#             j = j + 1
#             
#         elif j == len(polys) - 1:
#             va = pts_vector(pnt,polys[j])
#             vb = pts_vector(pnt,polys[0])
#             b = angle_between(va,vb)
#             print(b)
#             
#             d = d + b
#             j = j + 1
#     print(f"result {d}")
#     e = math.floor(d*10000)/10000
#     if d < 359:
#         outpt.append(pnt)
#     else:
#         inpt.append(pnt)
# =============================================================================
        
pp_xa = []
pp_ya = []
for pnt in inpt:
    pp_xa.append(pnt[0])
    pp_ya.append(pnt[1])

pp_xb = []
pp_yb = []
for pnt in outpt:
    pp_xb.append(pnt[0])
    pp_yb.append(pnt[1])
#plot
fig = plt.figure(figsize=(10,10))
ax = fig.add_axes([0,0,1,1])
ax.plot(b_pnts_x,b_pnts_y)
ax.plot(pp_xa,pp_ya,'x', color='black')
ax.plot(pp_xb,pp_yb,'x', color='red')
