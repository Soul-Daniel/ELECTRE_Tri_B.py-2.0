import ELECTRE_Tri_B
import math

########################################################################################################################
# ===========================================   Input data import   ================================================== #
########################################################################################################################

CAT = ['C1', 'C2', 'C3', 'C4', 'C5']
C, W, A, AP, B, BP, T = ELECTRE_Tri_B.input_data('01_Weights.csv',
                                                 '02_Actions_performances.csv',
                                                 '03_Boundaries_actions_performances.csv',
                                                 '04_Thresholds.csv')

print('')
Sigma_bk_init, Separability_init = ELECTRE_Tri_B.separability_test(C, W, B, BP, T, display='YES')
λ_min = math.ceil(max(Sigma_bk_init.values()) * 1000) / 1000
print('Minimum required initial credibility threshold λ =', λ_min)
λ = 0.50
print('Chosen initial credibility threshold λ =', λ)

########################################################################################################################
# ================================   Automatic execution of the ELECTRE Tri-B   ====================================== #
########################################################################################################################

Test_init = ELECTRE_Tri_B.ELECTRE_Tri_B(C, W, A, AP, B, BP, T, CAT, λ, display='YES')

########################################################################################################################
# ================================   OR Manual execution of the ELECTRE Tri-B   ====================================== #
########################################################################################################################

# ======================   Test of the minimum requirements to run the ELECTRE Tri method   ====================== #

# The weights of the criteria must be normalized and their sum must be equal to 1 or 100
if sum(W.values()) <= 1.000001 and not 0.999999 <= sum(W.values()) <= 1.000001:
    raise NameError('Condition of normalized weights is not respected')
elif sum(W.values()) > 1.000001 and not 99.999999 <= sum(W.values()) <= 100.000001:
    raise NameError('Condition of normalized weights is not respected')

# The values of the thresholds 'q', 'p' and 'v' must be increasing 'q' < 'p' < 'v'
for gj in T.keys():
    if not T[gj][0] < T[gj][1] < T[gj][2]:
        raise NameError('Condition of increasing order of thresholds is not respected')

# Separability test and verification of the minimum required credibility threshold
Sigma_bk, Separability = ELECTRE_Tri_B.separability_test(C, W, B, BP, T, display='NO')
if λ < max(Sigma_bk.values()):
    raise NameError('The chosen credibility threshold is lower than the minimum required credibility threshold '
                    'λ_min = {}'.format(max(Sigma_bk.values())))

# ==========================   Calculation of the indicators of the ELECTRE Tri method   ========================= #

# Calculation of the concordance matrices for all the boundary scenarios
Conc = {}
for b in B:
    name = '{}'.format(b)
    Conc[name] = ELECTRE_Tri_B.concordance(C, A, AP, b, BP, T)

# Calculation of the discordance matrices for all the boundary scenarios
Disc = {}
for b in B:
    name = '{}'.format(b)
    Disc[name] = ELECTRE_Tri_B.discordance(C, A, AP, b, BP, T)

# Calculation of the global concordances vectors for all the boundary scenarios
Glob_conc = {}
for b in B:
    name = '{}'.format(b)
    Glob_conc[name] = ELECTRE_Tri_B.global_concordance(Conc['{}'.format(b)], b, C, W, A)

# Calculation of the credibility vectors for all the boundary scenarios
Cred = {}
for b in B:
    name = '{}'.format(b)
    Cred[name] = ELECTRE_Tri_B.credibility(Glob_conc['{}'.format(b)], b, Disc['{}'.format(b)], C, A)

# Building the matrix of outranking relations
Over_rank = {}
for b in B:
    name = '{}'.format(b)
    Over_rank[name] = ELECTRE_Tri_B.over_ranking_relations(Cred['{}'.format(b)], b, λ)

# ============================   Ranking of actions and calculation of median ranks   ============================ #

# Ranking of actions in the three categories according to the pessimistic procedure and display of the result
Pessi_sort = ELECTRE_Tri_B.pessimistic_sorting(Over_rank, CAT, A, B)

# Ranking of actions in the three categories according to the optimistic procedure and display of the result
Opti_sort = ELECTRE_Tri_B.optimistic_sorting(Over_rank, CAT, A, B)

# Calculating the median rank of each share
Med_rank = ELECTRE_Tri_B.median_rank(Pessi_sort, Opti_sort, A)

# ==========================================   Display of the results   ========================================== #

# Display of the categories in which each action is classified
print(' ')
print("Results of the pessimistic sorting : ")
for cat in Pessi_sort[0].keys():
    print('{} :'.format(cat), Pessi_sort[0][cat])
print('Pessimistic category :', Pessi_sort[1])
print(' ')
print('Results of the optimistic sorting : ')
for cat in Opti_sort[0].keys():
    print('{} :'.format(cat), Opti_sort[0][cat])
print('Optimistic category : ', Opti_sort[1])

# Display of the median rank of each action
print(' ')
ELECTRE_Tri_B.display_results(Pessi_sort, Opti_sort, Med_rank, A)
