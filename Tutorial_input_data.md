# Tutorial Input Data

Author: [Souleymane Daniel](mailto:souleymane.daniel@insa-lyon.fr)

[INSA Lyon](https://www.insa-lyon.fr), Lyon, France, 17/03/2022

The Python code presented here requires some specific input data to work. This input data can be entry manually in accordance with the requirements of the ELECTRE Tri-B python code or can be stored as comma-separated values files, known as CSV. This is a text file, as opposed to the so-called "binary" formats. Each line of text corresponds to a line in a table and commas are used to separate the columns. The portions of text separated by a comma thus correspond to the contents of the table cells. A line is an ordered sequence of characters terminated by an end-of-line character.

## Manual entry of input data

In the case where the input data are manually entered, it is necessary to respect a certain shaping. The respect of this shaping determines the correct execution of the code and the exploitation of the results. The following sub-sections detail and illustrate with clear examples in which form these input data must be provided.

### 1. Names of the categories

The first step is to define the names of the different ranking categories, which should be given in ascending order from worst to best in the form of a python list. Be careful that this list of classification categories **Categories = [C(1),...,C(k),...,C(q)]** is consistent with the boundary reference actions that delimit them **Boundary_reference_actions = [b(0),...,b(k),...,b(q)]**.

*Exemple*

    Categories = ['C1', 'C2', 'C3']

### 2. Names of the criteria

Then you have to indicate the names of the criteria also given in the form of a python list. These names must be of string type and written in an order that will be kept afterwards. 

*Exemple*

    Criteria = ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7']

### 3. Weights of the criteria

After indicating the name of the criteria it is necessary to indicate their respective weight. The weight of the criteria must be provided in the form of a python dictionary where the keys are the names of the criteria and the values are their weight. *

*Exemple*

    Weights = {'g1': 0.20, 'g2': 0.15, 'g3': 0.10, 'g4': 0.10, 'g5': 0.10, 'g6': 0.15, 'g7': 0.20}

### 4. Names of the actions

Then it is necessary to indicate in the form of a python list the names of the actions that will be analyzed and compared. These names must be of type string.

*Exemple*

    Actions = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10']

### 5. Names of the boundary reference actions

In the same way as for the actions, it is then necessary to indicate in the form of a python list the names of the boundary reference actions that will be used to build the categories and to evaluate the actions. These names must be of type string.

*Exemple* 
    
    Boundary_reference_actions = ['b0', 'b1', 'b2', 'b3']

### 6. Performances of the actions

Must then be indicated the performances of the actions that will be analyzed. These performances must be provided in the form of a python dictionary whose keys are the names of the actions and whose values are dictionaries containing the names of the criteria associated with the evaluations of the action.

*Exemple*
    
    Actions_performances =
    {'a1': {'g1': 16, 'g2': 15, 'g3': 40, 'g4': 12, 'g5': 15, 'g6': 5, 'g7': 3},
     'a2': {'g1': 45, 'g2': 92, 'g3': 85, 'g4': 16, 'g5': 16, 'g6': 5, 'g7': 5},
     'a3': {'g1': 21, 'g2': 62, 'g3': 24, 'g4': 16, 'g5': 12, 'g6': 5, 'g7': 3},
     'a4': {'g1': 21, 'g2': 25, 'g3': 50, 'g4': 10, 'g5': 12, 'g6': 3, 'g7': 5}
     ...}

### 7. Performances of the boundary reference actions

In the same way as for the actions performances, it is necessary to indicate the performances of the boundary reference actions. These performances must also be provided in the form of a dictionary whose keys are the names of the boundary reference actions and whose values are dictionaries containing the names of the criteria associated with the evaluations of the boundary reference action.

*Exemple*
    
    Boundary_actions_performances =
    {'b0': {'g1': 0, 'g2': 0, 'g3': 0, 'g4': 0, 'g5': 0, 'g6': 0, 'g7': 0},
     'b1': {'g1': 5, 'g2': 10, 'g3': 20, 'g4': 5, 'g5': 5, 'g6': 1, 'g7': 1},
     'b2': {'g1': 15, 'g2': 30, 'g3': 40, 'g4': 10, 'g5': 10, 'g6': 2, 'g7': 2},
     'b3': {'g1': 25, 'g2': 50, 'g3': 60, 'g4': 10, 'g5': 10, 'g6': 3, 'g7': 3}}

### 8. Indifference, preference and veto Thresholds

Finally, the indifference, preference and veto thresholds must be indicated in order to allow for a one-by-one comparison of the scenarios. These thresholds are three, and they allow determining if a scenario is preferable, equivalent, worse or cannot be compared to another one. They must be provided in the form of a python dictionary whose keys are the name of the criteria and whose values are python lists containing the thresholds in the right order *[indifference, preference, veto]*.

*Exemple*

    Thresholds =
    {'g1': [4, 8, 100],
     'g2': [10, 15, 100],
     'g3': [10, 15, 100],
     'g4': [2, 4, 100],
     'g5': [2, 4, 100],
     'g6': [0, 1, 100],
     'g7': [0, 1, 100]}

## CSV files structure

In case the input data is provided as comma-separated values files, it is also necessary to respect a certain shaping of the csv files. Within the source code, the function "***input_data***" is assigned to import and reshape the input data from the csv files. This csv file should contain the names of the criteria and their weights, the names of the actions and their performances, the names of the boundary reference actions and their performances and the different thresholds for each criterion.

*Note: There must be exactly four csv files that are described below.*

### 1. csv file related to criteria and their weight

The first csv file concerns the criteria. 

It should contain on the first line the names of the criteria as strings separated by commas. To facilitate the use of the simulation results, the names of the criteria should be represented by numbering. For example the explicit criteria of a problem can be represented by the set {*g1*, *g2*, *g3*, *g4*, *g5*, *g6*}.

The second line should contain the weights of the criteria, also separated by commas. 

*Note: There should therefore be as many comma-separated text sections for the names of the criteria as for the weights.*

*Example: [01_Weights.csv](01_Weights.csv)*

### 2. csv file related to the actions and their performances

The second csv file concerns the actions.

It must contain on the first line the names of the actions as strings separated by commas. As for the criteria, the names of the actions must be represented by numbering. For example {*S1*, *S2*, *S3*, *S4*, *S5*, *S6*, *S8*, *S9*, *S10*}.

The following lines should represent, in the correct order, the performance of the actions against each criterion. For example, the second line represents the performance of the action *S1* with regard to each criterion {*g1*, *g2*, *g3*, *g4*, *g5*, *g6*}. Then the next line the performance of the action *S2* and so on.

*Note: The performances of the actions must be numerical values.*

*Example: [02_Actions_performances.csv](02_Actions_performances.csv)*

### 3. csv file related to boundary reference actions and their performances

The third csv file concerns the boundary reference actions and their performances.

It must contain on the first line the names of the boundary reference actions separated by commas as in the criteria csv file.

In the same way as the csv file related to the actions and their performances, the following lines should contain in the correct order the performance of the boundary reference actions against each criterion.

*Note: The performances of the boundary reference actions must also be numerical values.*

*Example: [03_Boundaries_actions_performances.csv](03_Boundaries_actions_performances.csv)*

### 4. csv file related to the thresholds

The last csv file provides the data concerning the thresholds.

It must contain on the first line the name of the indifference, preference and veto thresholds separated by commas and usually called {*q*, *p*, *v*}.

The following lines should contain, in the correct order, the values of the indifference, preference and veto thresholds.

*Note: The values of the thresholds must also be numerical values.*

*Example: [04_Thresholds.csv](04_Thresholds.csv)*
