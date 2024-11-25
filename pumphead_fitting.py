import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# all functions use these 5 flowrates
arbitrary_flowrates = [0 , 50 , 75 , 175 , 200] # flowrates used for fitting

def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

"""FOR 7' IMPELLER"""
def plot_impeller_7_fit():
    """Display and save the fitted curve plot for the 7" impeller"""
    tested_heads = [209, 204, 200, 165, 155]
    
    # Fit quadratic curve to the data
    popt, pcov = curve_fit(quadratic, arbitrary_flowrates, tested_heads)
    a, b, c = popt
    
    # Generate points for smooth curve
    x_fit = np.linspace(0, 200, 100)
    y_fit = quadratic(x_fit, a, b, c)
    
    # Plot both the original points and the fitted curve
    # plt.scatter(arbitrary_flowrates, tested_heads, color='red', label='Data points')
    # plt.plot(x_fit, y_fit, 'b-', label=f'Fit: {a:.5f}x² + {b:.5f}x + {c:.5f}')
    # plt.xlabel("Flow Rate (gpm)")
    # plt.ylabel("Head Increase (ft)")
    # plt.title("7\" Impeller: Head Increase vs Flow Rate")
    # plt.legend()
    # plt.grid(True)
    # plt.savefig('impeller_7_quadratic_fit.png')
    # plt.show()
    
    print(f"Fitted equation: h = {a:.5f}x² + {b:.5f}x + {c:.5f}")
    return popt

def impeller_7_fitcurve(flow_rate):
    """Calculate head increase for any flow rate using the fitted curve"""
    # Coefficients from curve fitting
    a, b, c = curve_fit(quadratic, arbitrary_flowrates, [209, 204, 200, 165, 155])[0]
    
    # Return the head increase for the given flow rate
    return quadratic(flow_rate, a, b, c)

"""FOR 6.5' IMPELLER"""

def plot_65_fitcurve():
    """Display and save the fitted curve plot for the 6.5" impeller"""
    tested_heads = [180, 179, 175, 140, 122]
    
    # Fit quadratic curve to the data
    popt, pcov = curve_fit(quadratic, arbitrary_flowrates, tested_heads)
    a, b, c = popt
    
    # Generate points for smooth curve
    x_fit = np.linspace(0, 200, 100)
    y_fit = quadratic(x_fit, a, b, c)
    
    # Plot both the original points and the fitted curve
    plt.scatter(arbitrary_flowrates, tested_heads, color='red', label='Data points')
    plt.plot(x_fit, y_fit, 'b-', label=f'Fit: {a:.5f}x² + {b:.5f}x + {c:.5f}')
    plt.xlabel("Flow Rate (gpm)")
    plt.ylabel("Head Increase (ft)")
    plt.title("6.5\" Impeller: Head Increase vs Flow Rate")
    plt.legend()
    plt.grid(True)
    plt.savefig('impeller_65_quadratic_fit.png')
    plt.show()
    
    print(f"Fitted equation: h = {a:.5f}x² + {b:.5f}x + {c:.5f}")
    return popt

def impeller_65_fitcurve(flow_rates):
    # Coefficients from curve fitting
    a, b, c = curve_fit(quadratic, arbitrary_flowrates, [180, 179, 175, 140, 122])[0]
    
    # Return the head increase for the given flow rate
    return quadratic(flow_rate, a, b, c)
    

"""FOR 6' IMPELLER"""

def plot_6_fitcurve():
    tested_heads = [150, 145, 142, 101, 85]
    
    # Fit quadratic curve to the data
    popt, pcov = curve_fit(quadratic, arbitrary_flowrates, tested_heads)
    a, b, c = popt
    
    # Generate points for smooth curve
    x_fit = np.linspace(0, 200, 100)
    y_fit = quadratic(x_fit, a, b, c)
    
    # Plot both the original points and the fitted curve
    plt.scatter(arbitrary_flowrates, tested_heads, color='red', label='Data points')
    plt.plot(x_fit, y_fit, 'b-', label=f'Fit: {a:.5f}x² + {b:.5f}x + {c:.5f}')
    plt.xlabel("Flow Rate (gpm)")
    plt.ylabel("Head Increase (ft)")
    plt.title("6\" Impeller: Head Increase vs Flow Rate")
    plt.legend()
    plt.grid(True)
    plt.savefig('impeller_6_quadratic_fit.png')
    plt.show()
    
    print(f"Fitted equation: h = {a:.5f}x² + {b:.5f}x + {c:.5f}")
    return popt

def impeller_6_fitcurve(flow_rate):
    a, b, c = curve_fit(quadratic, arbitrary_flowrates, [150, 145, 142, 101, 85])[0]
    return quadratic(flow_rate, a, b, c)

def validation(popt, test_data_x, test_data_y):
    a, b, c = popt
    array_diffs = []
    validation_y = quadratic(test_data_x, a, b, c)
    print(validation_y)
    return (validation_y - test_data_y)


# for i in range(1, 400, 1):
#     flow.append(i)
#     head_increase.append(i)

plot_impeller_7_fit()
plot_6_fitcurve()
plot_65_fitcurve()

"""Equations"""
"""
Fitted equation for 7" : h = -0.00116x² + -0.04360x + 209.16544
Fitted equation for 6": h = -0.00168x² + 0.01350x + 149.65944
Fitted equation for 6.5": h = -0.00183x² + 0.08316x + 179.65074

"""

# validation(impeller_6_fitcurve(), [0, 50, 75, 175, 200], [209, 204, 200, 165, 155])