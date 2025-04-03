from dataclasses import dataclass
from typing import Optional
import numpy as np

@dataclass
class ThermoFluidProperties: 
    """Metaparameters of Water"""

    cmin: Optional[float] = None
    cr: Optional[float] = None
    
    water_flow_rate_L_min: float = 2.10  # L/min
    water_vol_flow_rate: Optional[float] = None
    water_density: float = 1000.0 
    water_mass_flow_rate: Optional[float] = None
    water_specific_heat: float = 4.18*1000# J/kgK
    
    # Let's use simpler temperature differences for now
    water_temp_change: float = 1.0  # K (start with a simple value)
    
    """Metaparamters of Air"""
    air_specific_heat: float = 1.005*1000  # J/kgK (converted from kN·m/kg·K)
    air_temp_change: float = 17.5  # K
    air_mass_flow_rate: Optional[float] = None
    
    T_hot_in: float = 47.4  
    T_cold_in: float = 43.0 
    
    def calculate_duty(self) -> float:
        """Calculate heat duty (Q) in Watts"""
        Q = (self.water_mass_flow_rate * 
              self.water_specific_heat * 
             self.water_temp_change)
        return Q  # Energy, in units of Watts
    
    def calculate_water_mass_flow(self) -> float:
        """Calculate water mass flow rate in kg/s"""
        self.water_vol_flow_rate = self.water_flow_rate_L_min*(1/1000)*(1/60) # convert to cubic meter/s
        self.water_mass_flow_rate = self.water_vol_flow_rate * self.water_density # Produces mass flow rate in kg/s
        return  self.water_mass_flow_rate 
    
    def calculate_air_mass_flow(self) -> float:
        """Calculate air mass flow rate in kg/s"""
        Q = self.calculate_duty()
        self.air_mass_flow_rate = Q / (self.air_specific_heat * self.air_temp_change)
        return self.air_mass_flow_rate
    
    #Run this first to access cmin and cr values 
    def calculate_heat_capacity_rates(self) -> (float, float):
        """Calculate hot and cold heat capacity rates (Ch, Cc)"""
        C_h = self.water_mass_flow_rate * self.water_specific_heat  # Hot fluid (water)
        C_c = self.air_mass_flow_rate * self.air_specific_heat     # Cold fluid (air)
        self.cr = C_c/C_h
        if C_h <= C_c: # condition only happens when Ch is less than Cc
            self.cmin = C_h
        else:
            self.cmin = C_c
        return C_h, C_c  #This makes a tuple of two floats
    
    # def calculate_capacity_ratio(self) -> float:
    #     """Calculate heat capacity ratio (Cr)"""
    #     C_h, C_c = self.calculate_heat_capacity_rates()
    #     return C_c / C_h  # Returns 0.098
    
    def calculate_actual_heat_transfer(self) -> float:
        """Calculate actual heat transfer rate (q_actual) in Watts"""
        C_h, _ =self.calculate_heat_capacity_rates()
        return C_h*self.water_temp_change  
    
    def calculate_max_heat_transfer(self) -> float:
        """Calculate maximum possible heat transfer rate (q_max) in Watts"""
        _, C_c = self.calculate_heat_capacity_rates()
        return self.cmin * (self.T_hot_in - self.T_cold_in)  # Using Cmin instead of C_c
    
    def calculate_effectiveness(self) -> float:
        """Calculate heat exchanger effectiveness (ε)"""
        q_actual = self.calculate_actual_heat_transfer()
        q_max = self.calculate_max_heat_transfer()
        return q_actual / q_max  
    

if __name__=="__main__":
    instance1 = ThermoFluidProperties()

    
    water_mass = instance1.calculate_water_mass_flow()
    print(f"\nWater mass flow rate: {water_mass} kg/s")
    
    
    duty = instance1.calculate_duty()
    print(f"Heat duty: {duty} W")
    
   
    air_mass = instance1.calculate_air_mass_flow()
    print(f"Air mass flow rate: {air_mass} kg/s")
    
    
    C_h, C_c = instance1.calculate_heat_capacity_rates()
    print(f"\nHeat capacity rates:")
    print(f"C_h (hot fluid): {C_h} W/K")
    print(f"C_c (cold fluid): {C_c} W/K")
    
    
    q_actual = instance1.calculate_actual_heat_transfer()
    print(f"\nActual heat transfer rate: {q_actual} W")
    
    
    q_max = instance1.calculate_max_heat_transfer()
    print(f"Maximum heat transfer rate: {q_max} W")
    
    
    effectiveness = instance1.calculate_effectiveness()
    print(f"\nHeat exchanger effectiveness: {effectiveness}")
    

