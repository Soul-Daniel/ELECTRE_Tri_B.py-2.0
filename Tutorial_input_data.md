# Tutorial "CSV_files_structure"

Author: [Souleymane Daniel](mailto:souleymane.daniel@insa-lyon.fr)

[INSA Lyon](https://www.insa-lyon.fr), Lyon, France, 17/03/2022

The Python code presented here requires some specific input data to work. This data must be stored as comma-separated values, known as CSV. This is a text file, as opposed to the so-called "binary" formats. Each line of text corresponds to a line in a table and commas are used to separate the columns. The portions of text separated by a comma thus correspond to the contents of the table cells. A line is an ordered sequence of characters terminated by an end-of-line character.

## CSV files structure

Within the source code, the function "***input_data***" is assigned to import the input data and shape it for further processing. This input data should be provided in the form of csv files containing the names of the criteria and their weights, the names of the actions and their performances, the names of the boundary reference actions and their performances and the different thresholds for each criterion.

*Note: There must be exactly four csv files that are described below.*

### 1. csv file related to criteria and their weight

The first csv file concerns the criteria. 

It should contain on the first line the names of the criteria as strings separated by commas. To facilitate the use of the simulation results, the names of the criteria should be represented by numbering. For example the explicit criteria of a problem can be represented by the set {*g1*, *g2*, *g3*, *g4*, *g5*, *g6*}.

The second line should contain the weights of the criteria, also separated by commas. 

*Note: There should therefore be as many comma-separated text sections for the names of the criteria as for the weights.*

*Example: [1.Weights.csv](1.Weights.csv)*

### 2. csv file related to the actions and their performances

The second csv file concerns the actions.

It must contain on the first line the names of the actions as strings separated by commas. As for the criteria, the names of the actions must be represented by numbering. For example {*S1*, *S2*, *S3*, *S4*, *S5*, *S6*, *S8*, *S9*, *S10*}.

The following lines should represent, in the correct order, the performance of the actions against each criterion. For example, the second line represents the performance of the action *S1* with regard to each criteria {*g1*, *g2*, *g3*, *g4*, *g5*, *g6*}. Then the next line the performance of the action *S2* and so on.

*Note: The performances of the actions must be numerical values.*

*Example: [2.Actions_performances.csv](2.Actions_performances.csv)*

### 3. csv file related to boundary reference actions and their performances

The third csv file concerns the boundary reference actions and their performances.

It must contain on the first line the names of the boundary reference actions separated by commas as in the criteria csv file.

In the same way as the csv file related to the actions and their performances, the following lines should contain in the correct order the performance of the boundary reference actions against each criterion.

*Note: The performances of the boundary reference actions must also be numerical values.*

*Example: [3.Boundaries_actions_performances.csv](3.Boundaries_actions_performances.csv)*

### 4. csv file related to the thresholds

The last csv file provides the data concerning the thresholds.

It must contain on the first line the name of the indifference, preference and veto thresholds separated by commas and usually called {*q*, *p*, *v*}.

The following lines should contain, in the correct order, the values of the indifference, preference and veto thresholds.

*Note: The values of the thresholds must also be numerical values.*

*Example: [4.Thresholds.csv](4.Thresholds.csv)*









