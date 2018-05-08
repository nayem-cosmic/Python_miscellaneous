# Program for solving linear equation of 2 unknows with iterative method

# Value assignments
F_tR = 1461600
a = 0.124
b_B = 0.096
c = 0.131207693
s = 0.04
t = 0.04
f_yB1 = 304545455
f_yF1 = 259090900

# Define functions
def F_u(M_p13_val, initialize=False):
    """
    :param M_p13_val: Moment value
    :param initialize: Put true at first run
    :return: Force value
    """

    val_1 = (F_tR*a+M_p13_val)/(a+b_B)
    val_2 = 1.18*F_tR*a/(a+b_B)

    if initialize:
        return val_2

    return min(val_1, val_2)

def M_p13(F_u_val):
    """
    :param F_u_val: Force value
    :return: Moment value
    """

    val_1 = (1-(F_u_val/(c*s*f_yB1))**2)*c*(s**2)*f_yB1/4
    val_2 = ((1-(F_u_val/(c*t*f_yF1/(3**0.5))))**0.5)*c*(t**2)*f_yF1/4

    if type(val_2) == complex:
        return val_1

    return min(val_1, val_2)


# Taking 1.18*F_tR*a/(a+b_B) as initial minimum in F_u and initialize
F_u_min = F_u(0, True)
M_p13_min = M_p13(F_u_min)

# Iteration loop
while True:
    if abs(F_u_min-F_u(M_p13_min))<0.0001: # as M_p1,3 converges earlier than F_u
        break
    F_u_min = F_u(M_p13_min)
    M_p13_min = M_p13(F_u_min)

print("F_u = {:.3f}".format(F_u_min))
print("M_p1,3 = {:.3f}".format(M_p13_min))
