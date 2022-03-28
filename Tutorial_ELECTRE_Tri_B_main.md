# Tutorial "ELECTRE_Tri_B_main.py"

Author: [Souleymane Daniel](mailto:souleymane.daniel@insa-lyon.fr)

[INSA Lyon](https://www.insa-lyon.fr), Lyon, France, 17/03/2022

## Introduction

In order to dissociate the representative functions of the ELECTRE Tri-B method and their execution in the case of examples or concrete applications, a "main" executable code has been created. The [**ELECTRE_Tri_B_main.py**](ELECTRE_Tri_B_main.py) code is the executable. It contains the different instructions that will lead to the construction of the objects used throughout the method. The different stages of this executable code are presented here.

## 1. First step : Ranking categories

The first step is to define the names of the different ranking categories, which should be given in ascending order from worst to best in the form of a Python list. Be careful that this list of classification categories **{C(1);...;C(k);...;C(q)}** is consistent with the boundary reference actions that delimit them **{b(0);...;b(k);...;b(q)}**. 

## 2. Second step : Importing the input data

The second step consist of importing the input data of the problem. These data should be stored in csv files according to the data structure presented in the document [Tutorial_CSV_files_format.md](Tutorial_input_data.md). There should be four such files:

- a csv file containing the different data related to the criteria and their weight.

    *Example: [1.Weights.csv](1.Weights.csv)*
    
- a csv file containing the different data related to the actions and their performances.

    *Example: [2.Actions_performances.csv](2.Actions_performances.csv)*
    
- a csv file containing the different data related to the boundary reference actions and their performances. 

    *Example: [3.Boundaries_actions_performances.csv](3.Boundaries_actions_performances.csv)*
    
- a csv file containing the different data related to the thresholds. 

    *Example: [4.Thresholds.csv](4.Thresholds.csv)*

To import the data, the following function is used, where the input parameters are of the csv files names:

- ***input_data(name_W, name_AP, name_BP, name_T)***

This functions will then return the different objects needed for the rest of the method.

## 3. Third step : Cutting threshold

The third step is to define the "**cutting threshold λ**". The cutting threshold is the basis of the comparison. It allows deciding on the existing over-ranking relationships between an actions "**_a(i)_**" and a boundary reference action "**_b(k)_**". The closer it is to 1, the more demanding the classification will be and may lead to situations of incomparability. The most common values for this cutting threshold are generally between **0.50** and **0.75**.

## 4. Fourth step : Automatic execution of the ELECTRE Tri-B

In the fourth step the objective is to use the input data to calculate the indicators of the ELECTRE Tri-B method. This calculation can be done automatically using the **ELECTRE_Tri_B(C, W, A, AP, B, BP, T, CAT, λ, display='YES')** function. This function automatically executes the different calculation steps of the ELECTRE Tri-B method in order to obtain the final rankings of the alternatives within the different categories.

## 5. Fifth step : Manual execution of the ELECTRE Tri-B

The ELECTRE Tri-B indicators can also be calculated manually using the following functions in the correct order.

#### 5.1 Calculation of the indicators

To calculate the indicators of the ELECTRE Tri-B method the following functions must be used in the correct order:
- Calculation of concordance indices by criteria: ***concordance(C, A, AP, b, BP, T)***
- Calculation of discordance indices by criteria: ***discordance(C, A, AP, b, BP, T)***
- Calculation of global concordance indices: ***global_concordance(CONC, b, C, W, A)***
- Calculation of credibility degrees: ***credibility(GLOB_CONC, b, DISC, C, A)***
- Construction of the outranking relationships: ***over_ranking_relations(CRED, b, λ)***

Particular attention should be paid to the calculation of these indicators. Each of them must be calculated as many times as there are boundary reference actions. This means that the functions used to perform these calculations must be called several times.

#### 5.2 Ranking of actions

The next step consists in classifying the actions in the categories, based on the outranking relations obtained previously, and following two ranking procedures: "**optimistic**" and "**pessimistic**".

To achieve this sorting we call the two functions ***pessimistic_sorting(OVER_RANK, CAT, A, B)*** and ***optimistic_sorting(OVER_RANK, CAT, A, B)*** and display the result of the ranking in the form of lists representing the categories and containing the actions.

#### 5.3 Calculation of median rank

Then the median rank of each action is also calculated with the function "***median_rank(PESSI_SORT, OPTI_SORT, A)***". It allows assigning to each action a score representing their median ranking with respect to the optimistic and pessimistic sorting procedures.

#### 5.4 Display the results

When all the steps are completed, it is then possible to display the results with the "***display_results(PESSI_SORT, OPTI_SORT, MED_RANK, A)***" function for a better visualisation of the ranking of the actions and of their median ranks.
