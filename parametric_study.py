import numpy as np
import matplotlib.pyplot as plt

m_air= m_core = 17  # kg/s
stio_ratio = 0.028
t_air = 288  # K
phi_value = []
temp_value = []

def equiv_ratio(m_core, m_dot_fuel):
    return (m_dot_fuel / m_core) / stio_ratio

def combustion_temperature(t_air, m_dot_fuel, m_air, q_fuel=120e6, eta_c=0.98, c_p=1005):
    delta_t = eta_c * (q_fuel * m_dot_fuel) / (m_air * c_p)
    return t_air + delta_t

m_dot_fuel = fuel_flow = np.linspace(0.1,0.5,20)



for fuel in m_dot_fuel:
    phi = equiv_ratio(m_core, fuel)
    temp = combustion_temperature(t_air, fuel, m_air)

    phi_value.append(phi)
    temp_value.append(temp)
print("phi value:",phi_value)
print("temp value:",temp_value)

plt.plot(phi_value, temp_value)

plt.xlabel("Equivalence Ratio (phi)")
plt.ylabel("Combustion Temperature (K)")
plt.title("Effect of Equivalence Ratio on Combustion Temperature")
plt.grid(True)
plt.show()

"""import numpy as np
import matplotlib.pyplot as plt

# Constants
m_core = m_air = 17
stio_ratio = 0.028
t_air = 288  # K

phi_value = []
temp_value = []

def equiv_ratio(m_core, m_dot_fuel):
    return (m_dot_fuel / m_core) / stio_ratio

def combustion_temperature(t_air, m_dot_fuel, m_air, q_fuel=120e6, eta_c=0.98, c_p=1005):
    delta_t = eta_c * (q_fuel * m_dot_fuel) / (m_air * c_p)
    return t_air + delta_t

# Fuel flow array
m_dot_fuel = np.linspace(0.1, 0.5, 20)

# Loop over each fuel value (scalar)
for fuel in m_dot_fuel:
    phi = equiv_ratio(m_core, fuel)
    temp = combustion_temperature(t_air, fuel, m_air)

    phi_value.append(phi)
    temp_value.append(temp)

# Check lists
print("phi_value:", phi_value[:5], "...")  # first 5 values
print("temp_value:", temp_value[:5], "...")

# Plot
plt.plot(phi_value, temp_value, marker='o')
plt.xlabel("Equivalence Ratio (phi)")
plt.ylabel("Combustion Temperature (K)")
plt.title("Effect of Equivalence Ratio on Combustion Temperature")
plt.grid(True)
plt.show()"""
