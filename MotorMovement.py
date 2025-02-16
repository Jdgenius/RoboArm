import math

def MotorMovement(targ_x,targ_y,targ_z):
    L1 = 15
    L2 = 10

    targ_r = math.sqrt(pow(targ_x,2) + pow(targ_y,2) + pow(targ_z,2))
    targ_phi = math.atan(targ_y/targ_x)
    targ_theta = math.atan(math.sqrt(pow(targ_x, 2) + pow(targ_y, 2))/targ_z)

    fin_ang0 = targ_phi

    fin_ang1 = targ_theta - math.acos((pow(L2,2) + pow(targ_r,2) - pow(L1,2))/(2*L2*targ_r))
    fin_ang2 = -math.acos((pow(L1,2) + pow(targ_r,2) - pow(L2,2))/(2*L1*targ_r)) + fin_ang1 + math.pi

    if(fin_ang1 > math.pi):
        fin_ang1-=math.pi
    if(fin_ang2 > math.pi):
        fin_ang2-=math.pi

    print(fin_ang0 * (180/math.pi), fin_ang1 * (180/math.pi), fin_ang2 * (180/math.pi))
