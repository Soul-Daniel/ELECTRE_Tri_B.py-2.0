# Description of a case study

Author: [Souleymane Daniel](mailto:souleymane.daniel@insa-lyon.fr)

[INSA Lyon](https://www.insa-lyon.fr), Lyon, France, 17/03/2022

## Introduction

The [**ELECTRE_Tri_B.py**](ELECTRE_Tri_B.py) code was developed within the scope of a research project aiming the establishment of a multiple-criteria decision analysis methodology to help and support the actors of energy renovation for social housing in their choices during renovation/rehabilitation projects. More particularly, this work is based on the renovation project of a collective residence located in France.

In order to use the **ELECTRE Tri-B** method for the selection of a retrofit programme for collective residential buildings, we have carried out the different preliminary steps required for the realisation of a multi-criteria analysis, which have been presented in the *"2. Quick explanations"* part of the [README](README.md) document.

These preliminary steps consist in particular of:
1. Definition of possible global retrofit scenarios: the method used here consists in identifying a certain number of elementary retrofit actions allowing to act on a family of key components. These can be the envelope of the building, the heating system, the DHW production system, the external joinery or the installation of photovoltaic solar panels on roofs. The objective is then to construct possible global retrofit scenarios which are combinations of these different elementary actions.
2. Definition of evaluation criteria: to define the evaluation criteria, it is necessary to bring together the decision-makers as well as all partners and collaborators. The objective is to identify and describe precisely the important criteria that will allow an objective evaluation of the different scenarios in relation to the project objectives.
3. Weighting of criteria: to put the chosen MCA into practice, it is necessary to assign weights to the different criteria. For this purpose, we have chosen to use a specific weighting method called SRF (Simos, Roy and Figueira) which is very well adapted to our problem.
4. Evaluation of the different alternatives: the last step consists of evaluating the performance of each scenario regarding the criteria defined by relying on the skills and expertise of the stakeholders, partners, and collaborators.
5. Definition of thresholds and baseline scenarios: given the experimental nature of the development of this decision support methodology and the large number of scenarios to be compared, we have chosen to define the baseline scenarios and the different thresholds in a statistical way.

These different steps allowed the construction of the performance matrix of the multicriteria analysis problem and the definition of the additional essential parameters.

## 1. Definition of possible global retrofit scenarios

In order to construct the possible energy renovation scenarios, we first defined several basic renovation actions which we divided into six categories:
- Existing electric underfloor heating (kept or disconnected).
- Supplementary individual heating.
- Domestic hot water production.
- Ventilation system.
- Local renewable energy production.
- Replacement of external joinery.
- External wall insulation.

Each of these basic renovation actions comprises several individual energy improvement measures defined in accordance with the methodology of the EU Energy Performance Directive 244 ([European Commission, 2012]).

From these elementary actions, different scenarios of global renovation were then built, which can be classified in seven categories:
- *S1* : existing individual electric heating and DHW.
- *S2* : modern electric individual heating and DHW V1.
- *S3* : modern electric individual heating and DHW V2.
- *S4* : individual electric heating and individual thermodynamic DHW.
- *S5* : individual gas heating and DHW.
- *S6* : individual electric heating and collective thermodynamic DHW.
- *S7* : individual electric heating and collective solar DHW.

Each of these seven categories of global retrofit scenarios was then divided into 4 variants (*Si.1*, *Si.2*, *Si.3* and *Si.4*) in which the installation of photovoltaic electricity production and the replacement of joinery with more or less high-end components appear or not. In total, twenty-eight scenarios were evaluated. In addition, some scenarios only consider the replacement of balcony joinery, while others consider the replacement of all external joinery.

The global retrofit scenarios are thus built from these individual elementary actions and presented in the table below.

|**N°**|**Basic renovation actions**                    |S1.1|S1.2|S1.3|S1.4|S2.1|S2.2|S2.3|S2.4|S3.1|S3.2|S3.3|S3.4|S4.1|S4.2|S4.3|S4.4|S5.1|S5.2|S5.3|S5.4|S6.1|S6.2|S6.3|S6.4|S7.1|S7.2|S7.3|S7.4|
|------|------------------------------------------------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|**s1**|**Existing electric underfloor heating**        |----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|s1.1  |Electrical underfloor heating kept              | X  | X  | X  | X  | X  | X  | X  | X  |    |    |    |    |    |    |    |    |    |    |    |    | X  | X  | X  | X  | X  | X  | X  | X  |
|s1.2  |Electric floor heating disconnected             |    |    |    |    |    |    |    |    | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  |    |    |    |    |    |    |    |    |
|**s2**|**Supplementary heating**                       |----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|s2.1  |Existing radiant electric heater                | X  | X  | X  | X  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
|s2.2  |Modern radiant electric heater                  |    |    |    |    | X  | X  | X  | X  |    |    |    |    |    |    |    |    |    |    |    |    | X  | X  | X  | X  | X  | X  | X  | X  |
|s2.3  |Electric storage heater                         |    |    |    |    |    |    |    |    | X  | X  | X  | X  | X  | X  | X  | X  |    |    |    |    |    |    |    |    |    |    |    |    |
|s2.4  |Low temperature hot water radiators             |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | X  | X  | X  | X  |    |    |    |    |    |    |    |    |
|s2.5  |Automated towel water                           |    |    |    |    | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  |
|**s3**|**Domestic hot water**                          |----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|s3.1  |Existing individual electric hot water tank     | X  | X  | X  | X  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
|s3.2  |Modern individual electric hot water tank       |    |    |    |    | X  | X  | X  | X  | X  | X  | X  | X  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
|s3.3  |Modern individual thermodynamic hot water tank  |    |    |    |    |    |    |    |    |    |    |    |    | X  | X  | X  | X  |    |    |    |    |    |    |    |    |    |    |    |    |
|s3.4  |Individual gas condensing boiler                |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | X  | X  | X  | X  |    |    |    |    |    |    |    |    |
|s3.5  |Collective thermodynamic hot water              |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | X  | X  | X  | X  |    |    |    |    |
|s3.6  |Bivalent solar hot water tank                   |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | X  | X  | X  | X  |
|**s4**|**Ventilation system**                          |----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|s4.1  |Existing controlled mechanical ventilation      | X  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
|s4.2  |Single flow controlled mechanical ventilation   |    | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  |
|**s5**|**Local renewable energy production**           |----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|s5.1  |No                                              | X  | X  | X  | X  | X  |    |    |    | X  |    |    |    | X  |    |    |    | X  |    |    |    | X  |    |    |    |    |    |    |    |
|s5.2  |Photovoltaic solar panels on the roof           |    |    |    |    |    | X  | X  | X  |    | X  | X  | X  |    | X  | X  | X  |    | X  | X  | X  |    | X  | X  | X  |    | X  | X  | X  |
|s5.3  |Thermal solar panels on the roof                |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    | X  | X  | X  | X  |
|**s6**|**Replacement of external joinery**             |----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|s6.1  |No replacement of external joinery              | X  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
|s6.2  |Double-glazing PVC                              |    | X  |    |    | X  | X  |    |    | X  | X  |    |    | X  | X  |    |    | X  | X  |    |    | X  | X  |    |    | X  | X  |    |    |
|s6.3  |Triple-glazing parietodynamic wood              |    |    | X  |    |    |    | X  |    |    |    | X  |    |    |    | X  |    |    |    | X  |    |    |    | X  |    |    |    | X  |    |
|s6.4  |Replacement of balcony windows only             |    |    |    | X  |    |    |    | X  |    |    |    | X  |    |    |    | X  |    |    |    | X  |    |    |    | X  |    |    |    | X  |
|**s7**|**External wall insulation**                    |----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|s7.1  |Keeping the existing insulation                 | X  |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
|s7.2  |External thermal insulation                     |    | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  | X  |

*Note: Particular attention was given to the scenario "*S1.1*" which represents the initial state of the building without any modification of the envelope or systems. This scenario was also modelled to have a reference to compare the other scenarios and determine their impact on the energy performance of the building. Particular attention was also paid to the homogeneity and consistency of the combinations. Furthermore, in each category the actions need to be mutually exclusive and complementary exhaustive.*

## 2. Definition of evaluation criteria

The next step is to decide how to compare the contribution of different options to the achievement of the project objectives. This requires the selection of criteria to reflect the performance in achieving the objectives. It appeared important to group the criteria by family, especially because of their large number. So we first decided to group them into four main families which we named "**Economic**", "**Technical**", "**Social**" and "**Environmental**".

We then defined sub-criteria within each family in order to achieve a coherent structuring of the criteria and drawing on the UK manual on how to undertake and make best use of multi-criteria analysis ([UK Government, 2009]). The criteria used are presented in the following tables.

|**N°**|1. Economic                                          |
|------|-----------------------------------------------------|
|g1.1  |Owner investment cost                                |
|g1.2  |Reinvestment cost over 30 years                      |
|g1.3  |Possibility of financial aid and special subventions |
|g1.4  |Operating costs                                      |
|g1.5  |Energy cost-effectiveness of the solution            |

|**N°**|2. Technical                                         |
|------|-----------------------------------------------------|
|g2.1  |Easy to integrate into existing buildings            |
|g2.2  |Can be installed on occupied sites                   |
|g2.3  |Serviceability / Maintenance                         |
|g2.4  |Easy Metering / Monitoring / Energy Management       |

|**N°**|3. Social                                            |
|------|-----------------------------------------------------|
|g3.1  |Impact on the cost to the tenant                     |
|g3.2  |Thermal comfort level                                |
|g3.3  |Sound comfort level                                  |
|g3.4  |Aesthetics and space requirements                    |

|**N°**|4. Environmental                                     |
|------|-----------------------------------------------------|
|g4.1  |Energy efficiency                                    |
|g4.2  |CO2 emissions avoided                                |
|g4.3  |Place of production                                  |


## 3. Weighting of criteria

For the allocation of weights we used the revisited SRF procedure, or card method, which is particularly suited in the context of over-ranking methods ([Figueira & Roy, 2002]). 

The procedure consists of presenting a set of cards corresponding to each criterion to decision-makers or groups of experts. The instruction is then to rank these criteria (cards) in increasing order of importance on a grid. It is possible to group together several criteria of equal importance and to leave gaps between two consecutive cards to mark the difference in importance ([Wang, et al., 2009]). Following this ranking, the criteria are given a normalised weighting via a relative percentage. The data relating to the criteria and their weights are stored in the **Building_retrofit_scenarios_CRIT** file.

|**N°**|1. Economic      |
|------|-----------------|
|g1.1  |11.56            |
|g1.2  |10.11            |
|g1.3  | 4.33            |
|g1.4  |11.56            |
|g1.5  | 5.78            |

|**N°**|2. Technical     |
|------|-----------------|
|g2.1  | 6.48            |
|g2.2  | 9.07            |
|g2.3  | 3.89            |
|g2.4  | 3.89            |

|**N°**|3. Social        |
|------|-----------------|
|g3.1  | 6.37            |
|g3.2  | 5.39            |
|g3.3  | 2.45            |
|g3.4  | 2.45            |

|**N°**|4. Environmental |
|------|-----------------|
|g4.1  | 7.78            |
|g4.2  | 5.56            |
|g4.3  | 3.33            |

*[01_Weights.csv](01_Weights.csv)*

## 4. Evaluation of the different alternatives

In order to evaluate the economic performance of these different renovation alternatives, we have estimated the investment (purchase and installation) and maintenance costs from suppliers and maintenance companies in order to calculate the overall cost of each renovation scenario. We also determined, according to the average life span of each elementary system that makes up the scenarios, what the reinvestment cost would be for the company over a period of fifteen and thirty years.

In order to evaluate the performance in terms of technical and social criteria, we submitted these different scenarios to a specialised consultancy and to internal rental management for their expertise. The objective was to evaluate certain criteria by a score from 0 to 5.

In order to compare the systems from the point of view of their energy performance, we called on an engineering office specialising in building thermal simulation capable of modelling all the scenarios envisaged. Numerous simulations were carried out by varying the input parameters (heating system, DHW production, type of joinery, local energy production, etc.) to determine the primary and final energy consumption of each scenario.

This evaluation work, in close collaboration with suppliers, consultancies and staff specialising in rental management, enabled us to construct the performance matrix represented by the data stored in the **2.Actions_performances** file.

*[02_Actions_performances.csv](02_Actions_performances.csv)*

## 5. Definition of thresholds and boundary reference actions

In order to compare the different scenarios one by one according to each criterion, it is necessary to define thresholds. These thresholds will determine whether a solution is preferred, equivalent, worse, or simply cannot be compared to another. Thus, three thresholds have been defined for each criterion:

- indifference threshold "*qj*": it indicates for a given criterion the maximum difference below which two solutions cannot be compared;
- preference threshold "*pj*": it indicates for a given criterion the minimum difference from which a solution will be largely preferred to another;
- veto threshold "*vj*": it is characteristic of the **ELECTRE-Tri** method and avoids the phenomenon of compensation of criteria.

Each of these thresholds corresponds, not to an absolute value, but to a relative value characterising the difference in performance between two compared scenarios.

The thresholds for familiar criteria were constructed in consultation with the decision-makers to reflect their decision-making habits as closely as possible. For the thresholds used for original new criteria, for which we have no experience, a statistical method was applied.

For this application we chose to create six boundary reference actions called "*b0*", "*b1*", "*b2*", "*b3*", "*b4*" and "*b5*". These six boundary reference actions will make it possible to delimit five categories "*C1*", "*C2*", "*C3*", "*C4*" and "*C5*" which we can also call "*Very poor*", "*Poor*", "*Acceptable*", "*Satisfactory*" and "*Very satisfactory*".

Given the experimental nature of the development of this decision support methodology and the large number of criteria and scenarios to be compared, we have chosen to define these boundary reference actions in a statistical method in order to maintain a certain objectivity.

*[03_Boundaries_actions_performances.csv](03_Boundaries_actions_performances.csv)*

*[04_Thresholds.csv](04_Thresholds.csv)*


[European Commission, 2012]:https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A52012XC0419%2802%29

[UK Government, 2009]:https://www.gov.uk/government/publications/multi-criteria-analysis-manual-for-making-government-policy

[Figueira & Roy, 2002]:https://www.sciencedirect.com/science/article/pii/S0377221701003708

[Wang, et al., 2009]:https://doi.org/10.1016/j.rser.2009.06.021
