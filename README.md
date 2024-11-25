### Full Report is located in main.tx file!

The purpose of this repository is to provide the methodology and analysis for optimizing the flow rate of a piping water loop consisting of approximately 100 feet of 2" SCH. 40 pipe with 10 elbows, 6 gate valves, and two heat exchangers(finned tube cross flow with air mixed, water unmixed) in series.

Optimizing energy systems with computation simulations is critical to ensuring a system makes the most effective use of equipment life and energy. This water loop simulation was modeled in python.
The water loop system modelled is illustrated below.

![image](https://github.com/user-attachments/assets/12e2280c-e179-4484-8eb4-d3854768e338)

### Results:

In this analysis, five data points were extracted from the manufacturer data sheet. By utilizing a python library, Scipy. Fitting procedures can be easily called and modeled to any nth-order polynomial users would like. For this simulation, a quadratic fit the data perfectly. The 6" impeller's fitted equation intersected with the system head loss relation at [84, 138]. This tells us that for a Gould's 0.5x3-7 pump with a 6" impeller, the system is optimal at a flow rate of ~84 GPM and can supply the system with 138 feet of head.

we can analyze the effect this will have on each heat exchanger within our system, including the outlet temperatures of each and the temperature of the water entering and exiting the exchangers. 

Fluid and gas properties such as density(T=50$^{\circ}$F), kinematic viscosity, and specific heat capacities were collected from thermodynamic tables. Temperature calculations were derived as functions of flow rate, Q [GPM]. The Number of Transfer Units(NTU) methods was utilized to model the tandem exchangers as a function of three equations and three unknowns. 

With these mathematical models defined as functions of flow rate, Q. An input of 84 GPM yields a total heat transfer of 303.32 BTU/Hr with the hot water outlet temperature and cold water outlet temperatures as 53.99$^{\circ}$F and 28.01$^{\circ}$F, respectively. 

![image](https://github.com/user-attachments/assets/51eb7268-f0ef-428b-a443-a031a4819322)

![image](https://github.com/user-attachments/assets/2e5d787a-457a-4c8a-8760-287f5e127a25)





