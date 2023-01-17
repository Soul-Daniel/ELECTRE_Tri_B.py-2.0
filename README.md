# ELECTRE Tri-B MCDA Python

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6394320.svg)](https://doi.org/10.5281/zenodo.6394320)

[![DOI](https://zenodo.org/badge/DOI/10.3390/en16020902.svg)](https://doi.org/10.3390/en16020902)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Soul-Daniel/ELECTRE_Tri_B.py-2.0/HEAD)

Author: [Souleymane Daniel](mailto:souleymane.daniel@insa-lyon.fr)

[INSA Lyon](https://www.insa-lyon.fr), Lyon, France, 17/03/2022

[**ELECTRE_Tri_B**](ELECTRE_Tri_B.py) is an over-ranking multi criteria decision analysis procedure allowing the ranking of a number of scenarios related to an issue into categories in order to assist in decision-making. The code proposed here is based on the ELECTRE Tri-B multi-criteria analysis procedure and aims to classify potential scenarios into a hierarchical set of categories. The particularity of this code is that it can be used to classify any scenario related to a decision problem as long as the input data is correctly provided.

## 1. Licence
Code is released under [MIT Lincence](https://choosealicense.com/licenses/mit/).

Docs are released under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/). 

[![Creative Commons License](http://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

## 2. Quick explanations
In order to use a ELECTRE Tri-B multi-criteria analysis procedure to select the best scenario among others, several steps must first be carried out:
- Identification of issues and objectives
- Definition of possible alternatives to achieve all or part of the objectives
- Definition of the criteria by which the analysis will be done
- Weighting of the different criteria
- Evaluation of the different alternatives regarding the different criteria
- Definition of thresholds and boundary reference scenarios.

Once these steps have been completed it is then possible to use the ELECTRE Tri-B multi-criteria analysis method to determine the best scenario among those identified.

## 3. Installation

In order to use the ELECTRE Tri-B code, a Python interpreter is required (see [Python_interpreter]).
To execute the code it is also necessary to install several packages :
- numpy ([NumPy module]) 
- csv ([CSV File Reading and Writing])
- math ([Mathematical functions])

## 4. How to use it

Typical workflow:

1. Go through all the steps defined above to define the composition of the multi-criteria analysis and build the performance matrix.
2. Store all the data of the problem in the different .csv files according to the structure defined in [Tutorial_CSV_files_format](Tutorial_input_data.md).
3. Indicate the correct name of the csv files to be imported for the analysis in the code [ELECTRE_Tri_B_main](ELECTRE_Tri_B_main.py).
4. Choose an initial lambda cutting threshold for the simulation.
5. Execute the code.
6. Interpreting the ranking results.

*Note: The correct execution of the code depends on the structuring of the csv data files were the information must be stored in a particular order. Another way to use the code would be to enter directly the input data in the code respecting the input data format.*

## 5. Contents
### 5.1 Tutorials

[Tutorial_ELECTRE_Tri_B](Tutorial_ELECTRE_Tri_B.md): Tutorial explaining how the calculation code ELECTRE_Tri_B.py is built.

[Tutorial_ELECTRE_Tri_B_main](Tutorial_ELECTRE_Tri_B_main.md): Tutorial explaining the structure and functionalities of the executable code ELECTRE_Tri_B_main.py.

[Tutorial_CSV_files_format](Tutorial_input_data.md): Tutorial explaining what format the different csv files must have in order to be interpreted by the executable.

*Note: The tutorials documents are used to explain the logic behind the calculation codes and how to use them.* 

### 5.2 Examples
#### 5.2.1 Description

[Tutorial_building_retrofit_scenarios](Tutorial_building_retrofit_scenarios.md): Document describing the origin and composition of the data for the example of multi-criteria decision support for the energy retrofit scenarios of a collective housing building.

*Note: The description documents are used to explain how the examples are constructed and what they are made of.* 

#### 5.2.2 CSV files

[01_Weights.csv](01_Weights.csv): csv file containing the different data related to the criteria and their weightings for the analysis of the energy renovation scenarios in the case of a collective housing building.

[02_Actions_performances.csv](02_Actions_performances.csv): csv file containing the different data related to the scenarios and their performances.

[03_Boundaries_actions_performances.csv](03_Boundaries_actions_performances.csv): csv file containing the different data related to the boundary reference scenarios and their performances.

[04_Thresholds.csv](04_Thresholds.csv): csv file containing the different data related to the indifference, preference and veto thresholds.

[Python_interpreter]:https://www.python.org/

[NumPy module]:https://numpy.org/doc/stable/reference/

[CSV File Reading and Writing]:https://docs.python.org/3/library/csv.html

[Mathematical functions]:https://docs.python.org/3/library/math.html
