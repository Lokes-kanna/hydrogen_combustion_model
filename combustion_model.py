"""def compute_thrust(m_dot, v_exit):
    return(m_dot * v_exit)

m_dot = 711
v_exit = 280    
print(compute_thrust(m_dot,v_exit)

def fuel_flow(far,m_dot_air):
    m_dot_fuel=far*m_dot_air
    return(m_dot_fuel)
far=0.014
m_dot_air=17
print(fuel_flow(far,m_dot_air))

def tsfc(m_dot_fuel, thrust):
    
    ratio=m_dot_fuel/thrust
    return(ratio)
m_dot_fuel=0.24
thrust=17850


print(tsfc(m_dot_fuel,thrust))"""


# ----------------------------------------------
# Mass flow calculation
# ----------------------------------------------

def m_split(m_tot, bpr):

    m_core = m_tot / (bpr + 1)
    m_fan = bpr * m_core

    return m_fan, m_core

far = 0.014
m_tot = 187
bpr = 10

m_fan, m_core = m_split(m_tot, bpr)

print("Mass flow fan:", m_fan)
print("Mass flow core:", m_core)


# ----------------------------------------------
# Thrust Calculation
# ----------------------------------------------

def thrust(m_fan, m_core, v_fan, v_core, v_af):

    fan_thrust = m_fan * (v_fan - v_af)
    core_thrust = m_core * (v_core - v_af)

    return fan_thrust + core_thrust


# ----------------------------------------------
# Fuel Flow Calculation
# ----------------------------------------------

def fuel_flow(far, m_core):

    m_dot_fuel = far * m_core
    return m_dot_fuel

m_dot_fuel = fuel_flow(far, m_core)
# ----------------------------------------------
# TSFC Calculation
# ----------------------------------------------

def tsfc(m_dot_fuel, thrust_value):

    return m_dot_fuel / thrust_value


# ----------------------------------------------
# INPUT VALUES
# ----------------------------------------------

v_fan = 320
v_core = 600
v_af = 250




# ----------------------------------------------
# Calculations
# ----------------------------------------------

engine_thrust = thrust(m_fan, m_core, v_fan, v_core, v_af)

fuel = fuel_flow(far, m_core)

tsfc_value = tsfc(fuel, engine_thrust)


# ----------------------------------------------
# Output
# ----------------------------------------------

print("Thrust:", engine_thrust)
print("Fuel:", fuel)
print("TSFC value:", tsfc_value)

#-----------------------------------------------
#              Mission Fuel
#-----------------------------------------------

def mission_fuel(m_dot_fuel, time):
    fuel_tot = m_dot_fuel * time
    return(fuel_tot)

time = 7200

print(mission_fuel(m_dot_fuel, time))


#-----------------------------------
#    Equivilance ratio
#-----------------------------------

stio_ratio = 0.028 

def equiv_ratio(m_core,m_dot_fuel):
    phi = (m_dot_fuel/m_core) /stio_ratio
    return phi
phi = equiv_ratio(m_core,m_dot_fuel)

print("phi =",phi)

#--------------------------------------
#        Combustion temperature
#--------------------------------------


"""" Estimate combustion temperature (K) for hydrogen-air mixture
    T_air: inlet air temperature (K)
    m_dot_fuel: fuel flow (kg/s)
    m_air: air mass flow (kg/s)
    Q_fuel: heating value (J/kg)
    eta_c: combustion efficiency
    c_p: specific heat of air (J/kg.K)"""

q_fuel=120e6
eta_c=0.98
c_p=1005
t_air = 288

def comb_eff (t_air, q_fuel, eta_c, m_dot_fuel, m_core, c_p):
    delta_value = eta_c *((q_fuel * m_dot_fuel)/ (m_core * c_p))
    t_comb= t_air + delta_value
    return t_comb

t_comb = comb_eff(t_air, q_fuel, eta_c, m_dot_fuel, m_core, c_p)
print("combustion temprature:", t_comb)



