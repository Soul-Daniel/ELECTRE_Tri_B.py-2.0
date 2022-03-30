# Tutorial "ELECTRE_Tri_B.py"

Author: [Souleymane Daniel](mailto:souleymane.daniel@insa-lyon.fr)

[INSA Lyon](https://www.insa-lyon.fr), Lyon, France, 17/03/2022

## 1. ELECTRE Tri-B procedure

The [**ELECTRE_Tri_B.py**](ELECTRE_Tri_B.py) code is based on the ELECTRE Tri-B ranking method and follows exactly the same procedure. This method is part of the sorting problem or assignment procedure. One of the particularities of this method is that boundary reference actions are used to segment the categories in which the actions will be classified. So each category is bounded below and above by two boundary reference actions. Finally, the **ELECTRE_Tri_B.py** code has been designed according to an object-oriented architecture, however there is no need to define classes and instances and only methods (or functions) are used.

## 2. Import of data

The first step of the **ELECTRE_Tri_B.py** code is to retrieve the analysis data from the csv files. The function "**input_data**" is used for this. The input data can also be given manually in the form of lists and dictionaries according to the code requirement.
___
***input_data(name_W, name_AP, name_BP, name_T)***

Generates the different input data in the correct format from .csv files.

    :param name_W: Name of the .csv file which must contain on the first line the name of the criteria and on the 
        second line the weightings.
    :param name_AP: Name of the .csv file which must contain on the first line the names of the possibles actions 
        and on the following lines the performance of each action against each criterion.
    :param name_BP: Name of the .csv file which must contain on the first line the names of the boundaries actions 
        and on the following lines, the performances of each boundary action against each criterion.
    :param name_T: Name of the .csv file which must contain on the first line the names of the thresholds and on the 
        following lines, for each criterion, the values of the indifference threshold, preference threshold and veto 
        threshold.

    :return C: List containing the names of the criteria as strings.
    :return W: Dictionary containing the weightings of each criterion.
    :return A: List containing the names of the actions as strings.
    :return AP: Actions performances dictionary.
    :return B: List containing the names of the boundary reference actions as strings.
    :return BP: Boundary reference actions performances dictionary.
    :return T: Dictionary of thresholds.
___

## 2. Concordance indices

The following function calculates the concordance indices by criteria. This is an indicator of how well an action ***a(i)*** is at least as good as the boundary reference action ***b(k)*** for a given criterion ***g(j)***.
___
***concordance(C, A, AP, b, BP, T)*** 

Calculates the concordance matrix for a given boundary reference action.

    :param C: List containing the names of the criteria as strings.
    :param A: List containing the names of the actions as strings.
    :param AP: Actions performances dictionary.
    :param b: Name of the boundary reference actions for which the concordance matrix is calculated.
    :param BP: Performances dictionary of the boundary reference actions.
    :param T: Dictionary of thresholds.

    :return Concordance: Dictionary containing the matrix of concordance of actions with regard to the boundary 
        reference action chosen as input. The keys are '(ai,bk)' and '(bk,ai)'.

## 3. Discordance indices

The following function calculates the discordance indices by criteria. This indicator is expressed using the veto threshold. They mark the limit beyond which the hypothesis that a given action ***a(i)*** outperforms a boundary reference action ***b(k)*** for a given criterion ***g(j)*** can be rejected without affecting the credibility of the opposite hypothesis.
___
***discordance(C, A, AP, b, BP, T)***

Calculates the discordance matrix for a given boundary reference action.

    :param C: List containing the names of the criteria as strings.
    :param A: List containing the names of the actions as strings.
    :param AP: Actions performances dictionary.
    :param b: Name of the boundary reference actions for which the discordance matrix is calculated.
    :param BP: Performances dictionary of the boundary reference actions.
    :param T: Dictionary of thresholds.

    :return discordance: Dictionary containing the matrix of discordance of actions with regard to the boundary
        reference action chosen as input. The keys are '(ai,bk)' and '(bk,ai)'.

## 4. Global concordance indices

The global concordance indices allow stating to what extent the hypothesis "the action ***a(i)*** globally outperforms the boundary reference action ***b(k)***" is met.
___
***global_concordance(CONC, b, C, W, A)***

Calculates the global concordances vectors for a given boundary reference action using a given concordance matrix.

    :param CONC: Matrix of concordance of actions with regard to a given boundary reference action.
    :param b: Name of the boundary reference actions for which you want to calculate the global concordance indices.
    :param C: List containing the names of the criteria as strings.
    :param W: Dictionary containing the weightings of each criterion.
    :param A: List containing the names of the actions as strings.
    
    :return Global_concordance: Dictionary containing two vectors corresponding to the global concordance of the 
        actions Si with the boundary actions defined in input bk, and of bk with the actions Si. The keys are '(ai,bk)' 
        and '(bk,ai)'.

## 5. Credibility

In the ELECTRE-Tri method, the credibility of the outranking relationships between the action and the boundary reference action varies from pair to pair and is represented by the degree of credibility of the outranking.
___
***credibility(GLOB_CONC, b, DISC, C, A)***

Calculates the credibility vectors for a given boundary reference action using the global concordance vector and  the 
    discordance matrix for the same boundary reference action.

    :param GLOB_CONC: Dictionary containing the global concordances vectors for a given boundary reference action.
    :param b: Name of the boundary reference actions for which you want to calculate the credibility indices.
    :param DISC: Matrix of discordance of actions with regard to the same given boundary reference action.
    :param C: List containing the names of the criteria as strings.
    :param A: List containing the names of the actions as strings.
    
    :return Credibility: Dictionary containing two vectors corresponding to the credibility of the over ranking of the
        actions Si by the boundary reference action defined as input bk, and to the over ranking of de bk by the
        actions Si. The keys are '(ai,bk)' and '(bk,ai)'.

## 6. Over-ranking relation

This function dedicated to over ranking relationships uses the lambda cutting threshold value and the credibilities values to decide on four over ranking relationships.
___
***over_ranking_relations(CRED, b, λ)***

Built the over ranking relations matrix using the credibility vectors and the cutting threshold. The result is a matrix containing the following four outranking relations:
- preference of *a(i)* over *b(k)*: "**>**"
- preference of *b(k)* over *a(i)*: "**<**"
- indifference: "**I**"
- incomparability: "**R**"


    :param CRED: List of credibility values for the boundary reference actions considered.
    :param b: Name of the boundary reference actions for which you want to calculate the over ranking relations.
    :param λ: Cutting threshold value.
    
    :return over_ranking: Dictionary containing the over ranking relation and where the keys are name of the boundaries
        reference actions, représenting the limits and boundaries of the different categories.

## 7. Pessimistic and Optimistic sorting

Two sorting procedures specific to the ELECTRE Tri-B method are performed based on the previous over-ranking relationships. Each of these sorting procedures assigns actions to a specific performance category. The difference between the two procedures is the ranking of incomparabilities (***R***).
For pessimistic sorting an incomparability relationship between an action ***a(i)*** and a boundary reference action ***b(k)*** moves the action into the lower performance category.
For optimistic sorting an incomparability relationship between an action ***a(i)*** and a boundary reference action ***b(k)*** moves the action into the upper performance category.
___
***pessimistic_sorting(OVER_RANK, CAT, A, B)***

***optimistic_sorting(OVER_RANK, CAT, A, B)***

Rank actions in the different performance category according to a pessimistic or optimistic procedure.

    :param OVER_RANK: Dictionary containing the over sorting relations for each boundary reference actions.
    :param CAT: List of the names of the different categories in which the actions will be classified.
    :param A: List containing the names of the actions as strings.
    :param B: Name of the boundary reference actions for which you want to calculate the concordance matrix.
    
    :return: sorting: Dictionary containing the different categories and the actions they contain. The keys are the
        categories 'Bad', 'Moderate', and 'Good'. The values are lists containing the actions.
    :return: category: Dictionary containing the rank of each actions according to a optimistic procedure.
        The keys are the actions and the values are the median ranks.

## 8. Median rank

When the two sorting procedures do not lead to the same results, a median rank is calculated. So an action classified as "**_C2_**" by the optimistic sorting and "**_C1_**" by the pessimistic sorting, will therefore belong to the "**_C21_**" category with a median rank of **1.5** (it will be less preferable than an action belonging to the "**_C22_**" category with a median rank of **2.0**).
___
***median_rank(PESSI_SORT, OPTI_SORT, A)***

Calculates the median rank of each action.

    :param PESSI_SORT: Dictionary containing the actions classified according to the pessimistic procedure.
    :param OPTI_SORT: Dictionary containing the actions classified according to the optimistic procedure.
    :param A: List containing the names of the actions as strings.
    
    :return med_rank: Dictionary containing the median rank of each action. The keys are the names of the actions
        and the values are the median ranks.

## 9. Display

When all the steps are completed, it is then possible to display results with the "***display_results***" function for a better visualisation of the ranking of the actions and of the median ranks.
___
***display_results(PESSI_SORT, OPTI_SORT, MED_RANK, A)***

Display of the median ranks and of the categories in which each action is classified.

    :param PESSI_SORT: Dictionary containing the actions classified according to the pessimistic procedure.
    :param OPTI_SORT: Dictionary containing the actions classified according to the optimistic procedure.
    :param MED_RANK: Dictionary containing the median rank of each action.
    :param A: List containing the names of the actions as strings.

## 10. Separability conditions

The degree of separability represents the level of difference that can exist between two actions. It is equal to the credibility of the statement **_a(i)_** outperforms **_b(k)_** so to the value of "**_σ(ai,bk)_**". It is interesting to calculate this degree of separability between two consecutive boudary reference actions "**_σ(bk,bk+1)_**" in order to determine with what level of difference the performance categories are constructed. The maximum value of the credibilities calculated in this way corresponds to the minimum required cutting threshold **_λ_**.
___
***separability_test(C, W, B, BP, T, display='NO')***

Calculates the minimum required credibility threshold.

    :param C: List containing the names of the criteria as strings.
    :param W: Dictionary containing the weightings of each criterion.
    :param B: Name of the boundary reference actions for which you want to calculate the concordance matrix.
    :param BP: Performances dictionary of the boundary reference actions.
    :param T: Dictionary of thresholds.
    :param display: Parameter allowing to choose if the display of the comments is desired or not.
    
    :return Sigma_bk: Dictionary containing the credibility index values for the pairs of boundary reference actions
        like (bk,bk+1). The keys are 'S(b0,b1)', 'S(b1,b2)', 'S(b2,b3)', etc.
    :return Separability: Variable stating whether the separability is "Weak", "Strict" or "Hyper-strict".

## 11. Execution of the ELECTRE Tri-B method
___
***ELECTRE_Tri_B(C, W, A, AP, B, BP, T, CAT, λ, display='NO')***

Upper function to execute the ELECTRE Tri-B method by calling each of the elementary functions in the order they should be called. The input data are described below.

    :param C: List containing the names of the criteria as strings.
    :param W: Dictionary containing the weightings of each criterion.
    :param A: List containing the names of the actions as strings.
    :param AP: Actions performances dictionary.
    :param B: List containing the names of the boundary reference actions.
    :param BP: Dictionary of the Boundaries reference actions performances.
    :param T: Dictionary of thresholds.
    :param CAT: List of the names of the different categories in which the actions will be classified.
    :param λ: Cutting threshold value.
    :param display: Parameter allowing to choose if the display of the results and comments is desired or not.
    
    :return: Conc, Disc, Glob_conc, Cred, Over_rank, Pessi_sort, Opti_sort, Med_rank, Sigma_bk, Separability
