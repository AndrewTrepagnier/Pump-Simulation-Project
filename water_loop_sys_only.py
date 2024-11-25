import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pumphead_fitting as phf

#Knowns that must first be defined
abs_rough = 0.02 #ft
viscosity = 8.80e-4  #lbm/ft/s
rho = 62.3 #lbm/ft^3

gc = 32.2 #lbm*ft/lbf*s^2
g = 32.2 #ft/s^2


L = 100 #ft
Di = 0.1722 #ft for 2" sch 40 pipe

rel_rough = abs_rough/Di
A = np.pi*(Di/2)**2 #ft^2

#functions 

def hx_losses(Q):
    return 0.0049*Q**1.852 # given

def overall_ht_coeff(Q): #Big U
    return ( 1/(13*Q**0.8) +0.047)**-1

def reynolds_number(Q):
    return (4*(1/60)*(0.134/1)*Q*rho)/(np.pi*Di*viscosity) # viscoisty is kinematic viscosity, 0.134 gal = 1ft^3

#function with embedded conditional for determining what the fricton factor will be
def friction_factor(Q):
    if reynolds_number(Q) >= 2300:
        f_f = (0.3086)/(np.log10(6.9/(reynolds_number(Q)) + ((abs_rough)/(3.7*Di))**1.11))**2
    elif reynolds_number(Q) < 2300:
        f_f = 64/reynolds_number(Q)
    else:
        print("Reynolds number is out of range")
    return f_f

#function for calculating the friction factor for turbulent flow
def f_t(Q):
    return 0.3086/((np.log10((abs_rough/(3.7*Di))**1.11))**2)

def K_total(Q):
    return 6*8*f_t(Q) + 10*30*f_t(Q) # 6 gate valves, 10 elbows for minor loss K value

def hf_minor(Q):
    return K_total(Q)*((Q*(1/60)*(0.134/1))**2)/(2*gc*A**2)

def hf_major(Q):
    return friction_factor(Q)*(L/Di)*((Q*(1/60)*(0.134/1))**2)/(2*gc*A**2) # 

def total_head_loss(Q): # total head loss is dependent on Q alone
    return hf_minor(Q) + hf_major(Q) + 2*hx_losses(Q) #2*hx_losses because there are two heat exchangers

# Create lists to store Q and head loss values
print(hf_major(4))

Q_values = []
head_values = []
# Calculate head loss for each Q value
for Q in range(1, 300, 1):  # Goes from 1 to 300 in steps of 1
    Q_values.append(Q)
    head_values.append(total_head_loss(Q))

# Set up the plot first
plt.figure(figsize=(12, 8))
sns.set_theme(style="darkgrid", context="notebook")

# Calculate all y_pump values first
x_pump = np.array(Q_values)  # Convert to numpy array
y_pump_7 = phf.quadratic(x_pump, *phf.plot_impeller_7_fit())
y_pump_65 = phf.quadratic(x_pump, *phf.plot_65_fitcurve())
y_pump_6 = phf.quadratic(x_pump, *phf.plot_6_fitcurve())

# Plot all lines
sns.lineplot(x=Q_values, y=head_values, 
            linewidth=3.0, 
            color='#800000',
            linestyle='-',
            label='System Head Loss')  

sns.lineplot(x=x_pump, y=y_pump_7,
            linewidth=2.5,
            color='#2E86C1',
            linestyle='--',
            label='7\" Impeller')

sns.lineplot(x=x_pump, y=y_pump_65,
            linewidth=2.5,
            color='#228B22',
            linestyle=':',
            label='6.5\" Impeller')

sns.lineplot(x=x_pump, y=y_pump_6,
            linewidth=2.5,
            color='#FFD700',
            linestyle='-.',
            label='6\" Impeller')

# Customize the plot
plt.xlabel("Flow Rate (gpm)", fontsize=12, fontweight='bold')
plt.ylabel("Head (ft)", fontsize=12, fontweight='bold')
plt.title("System Head Loss and Pump Performance", 
          fontsize=14, pad=15, fontweight='bold')

# Customize legend
plt.legend(fontsize=10, frameon=True, loc='lower right')

# Set axis limits
plt.xlim(0, 200)
plt.ylim(0, 500)  # Adjust this range as needed

plt.tight_layout()
plt.show()

