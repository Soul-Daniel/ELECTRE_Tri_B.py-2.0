import numpy as np
import math
import csv


def input_data(name_W, name_AP, name_BP, name_T):
    """
    Generates the different input data in the correct format from .csv files.

    :param name_W: Name of the .csv file which must contain on the first line the name of the criteria and on the
        second line the weightings.
    :param name_AP: Name of the .csv file which must contain on the first line the names of the possibles actions and
        on the following lines the performance of each action against each criterion.
    :param name_BP: Name of the .csv file which must contain on the first line the names of the boundaries actions and
        on the following lines, the performances of each boundary action against each criterion.
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
    """
    C = []
    W = {}
    A = []
    AP = {}
    B = []
    BP = {}
    T = {}
    with open(name_W, 'r', newline='') as W_csv:
        reader = csv.reader(W_csv, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                [C.append(item) for item in row]
            else:
                for j in range(len(row)):
                    W[C[j]] = float(row[j])
            line_count += 1

    with open(name_AP, 'r', newline='') as AP_csv:
        reader = csv.reader(AP_csv, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                [A.append(item) for item in row]
            else:
                perf_A = {}
                for j in range(len(row)):
                    perf_A[C[j]] = float(row[j])
                AP[A[line_count-1]] = perf_A
            line_count += 1

    with open(name_BP, 'r', newline='') as BP_csv:
        reader = csv.reader(BP_csv, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                [B.append(item) for item in row]
            else:
                perf_B = {}
                for j in range(len(row)):
                    perf_B[C[j]] = float(row[j])
                BP[B[line_count-1]] = perf_B
            line_count += 1

    with open(name_T, 'r', newline='') as T_csv:
        reader = csv.reader(T_csv, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                perf_T = []
                [perf_T.append(float(item)) for item in row]
                T[C[line_count-1]] = tuple(perf_T)
            line_count += 1

    return C, W, A, AP, B, BP, T


def concordance(C, A, AP, b, BP, T):
    """
    Calculates the concordance matrix for a given boundary reference action.

    :param C: List containing the names of the criteria as strings.
    :param A: List containing the names of the actions as strings.
    :param AP: Actions performances dictionary.
    :param b: Name of the boundary reference actions for which the concordance matrix is calculated.
    :param BP: Performances dictionary of the boundary reference actions.
    :param T: Dictionary of thresholds.

    :return Concordance: Dictionary containing the matrix of concordance of actions with regard to the boundary
        reference action chosen as input. The keys are '(ai,bk)' and '(bk,ai)'.
    """
    Concordance = {}
    conc_2D_1 = np.empty((0, len(C)))
    conc_2D_2 = np.empty((0, len(C)))
    for a in A:
        conc_1D_1 = [min(1, max(0, (AP[a][c] - BP[b][c] + T[c][1]) / (T[c][1] - T[c][0]))) for c in C]
        conc_1D_2 = [min(1, max(0, (BP[b][c] - AP[a][c] + T[c][1]) / (T[c][1] - T[c][0]))) for c in C]
        conc_2D_1 = np.vstack((conc_2D_1, conc_1D_1))
        conc_2D_2 = np.vstack((conc_2D_2, conc_1D_2))
    Concordance['c(ai,{})'.format(b)] = conc_2D_1
    Concordance['c({},ai)'.format(b)] = conc_2D_2
    return Concordance


def discordance(C, A, AP, b, BP, T):
    """
    Calculates the discordance matrix for a given boundary reference action.

    :param C: List containing the names of the criteria as strings.
    :param A: List containing the names of the actions as strings.
    :param AP: Actions performances dictionary.
    :param b: Name of the boundary reference actions for which the discordance matrix is calculated.
    :param BP: Performances dictionary of the boundary reference actions.
    :param T: Dictionary of thresholds.

    :return discordance: Dictionary containing the matrix of discordance of actions with regard to the boundary
        reference action chosen as input. The keys are '(ai,bk)' and '(bk,ai)'.
    """
    Discordance = {}
    disc_2D_1 = np.empty((0, len(C)))
    disc_2D_2 = np.empty((0, len(C)))
    for a in A:
        disc_1D_1 = [min(1, max(0, (BP[b][c] - AP[a][c] - T[c][1]) / (T[c][2] - T[c][1]))) for c in C]
        disc_1D_2 = [min(1, max(0, (AP[a][c] - BP[b][c] - T[c][1]) / (T[c][2] - T[c][1]))) for c in C]
        disc_2D_1 = np.vstack((disc_2D_1, disc_1D_1))
        disc_2D_2 = np.vstack((disc_2D_2, disc_1D_2))
    Discordance['d(ai,{})'.format(b)] = disc_2D_1
    Discordance['d({},ai)'.format(b)] = disc_2D_2
    return Discordance


def global_concordance(CONC, b, C, W, A):
    """
    Calculates the global concordances vectors for a given boundary reference action using a given concordance matrix.

    :param CONC: Matrix of concordance of actions with regard to a given boundary reference action.
    :param b: Name of the boundary reference actions for which you want to calculate the global concordance indices.
    :param C: List containing the names of the criteria as strings.
    :param W: Dictionary containing the weightings of each criterion.
    :param A: List containing the names of the actions as strings.

    :return Global_concordance: Dictionary containing two vectors corresponding to the global concordance of the
        actions Si with the boundary actions defined in input bk, and of bk with the actions Si.
        The keys are '(ai,bk)' and '(bk,ai)'.
    """
    Global_concordance = {}
    glob_conc_1D_1 = []
    glob_conc_1D_2 = []
    for i in range(len(A)):
        gc1 = [(W[C[j]] * CONC['c(ai,{})'.format(b)][i][j]) / sum(W.values()) for j in range(len(C))]
        gc2 = [(W[C[j]] * CONC['c({},ai)'.format(b)][i][j]) / sum(W.values()) for j in range(len(C))]
        glob_conc_1D_1.append(sum(gc1))
        glob_conc_1D_2.append(sum(gc2))
    Global_concordance['C(ai,{})'.format(b)] = glob_conc_1D_1
    Global_concordance['C({},ai)'.format(b)] = glob_conc_1D_2
    return Global_concordance


def credibility(GLOB_CONC, b, DISC, C, A):
    """
    Calculates the credibility vectors for a given boundary reference action using the global concordance vector and
        the discordance matrix for the same boundary reference action.

    :param GLOB_CONC: Dictionary containing the global concordances vectors for a given boundary reference action.
    :param b: Name of the boundary reference actions for which you want to calculate the credibility indices.
    :param DISC: Matrix of discordance of actions with regard to the same given boundary reference action.
    :param C: List containing the names of the criteria as strings.
    :param A: List containing the names of the actions as strings.

    :return Credibility: Dictionary containing two vectors corresponding to the credibility of the over ranking of the
        actions Si by the boundary reference action defined as input bk, and to the over ranking of de bk by the
        actions Si. The keys are '(ai,bk)' and '(bk,ai)'.
    """
    Credibility = {}
    cred_1 = []
    cred_2 = []
    for i in range(len(A)):
        cr1 = 1
        cr2 = 1
        for j in range(len(C)):
            if DISC['d(ai,{})'.format(b)][i][j] > GLOB_CONC['C(ai,{})'.format(b)][i]:
                cr1 = cr1 * (1 - DISC['d(ai,{})'.format(b)][i][j]) / (1 - GLOB_CONC['C(ai,{})'.format(b)][i])
            else:
                cr1 = cr1 * 1
            if DISC['d({},ai)'.format(b)][i][j] > GLOB_CONC['C({},ai)'.format(b)][i]:
                cr2 = cr2 * (1 - DISC['d({},ai)'.format(b)][i][j]) / (1 - GLOB_CONC['C({},ai)'.format(b)][i])
            else:
                cr2 = cr2 * 1
        cred_1.append(cr1 * GLOB_CONC['C(ai,{})'.format(b)][i])
        cred_2.append(cr2 * GLOB_CONC['C({},ai)'.format(b)][i])
    Credibility['σ(ai,{})'.format(b)] = cred_1
    Credibility['σ({},ai)'.format(b)] = cred_2
    return Credibility


def over_ranking_relations(CRED, b, λ):
    """
    Built the over ranking relations matrix using the credibility vectors and the cutting threshold. The result is a
        matrix containing the following four outranking relations:
            - preference of ai over bk: '>'
            - preference of bk over ai: '<'
            - indifference: 'I'
            - incomparability: 'R'.

    :param CRED: List of credibility values for the boundary reference actions considered.
    :param b: Name of the boundary reference actions for which you want to calculate the over ranking relations.
    :param λ: Cutting threshold value.

    :return over_ranking: Dictionary containing the over ranking relation and where the keys are name of the boundaries
        reference actions, représenting the limits and boundaries of the different categories.
    """
    over_ranking = []

    for i in range(len(CRED['σ(ai,{})'.format(b)])):
        if CRED['σ(ai,{})'.format(b)][i] >= λ:
            if CRED['σ({},ai)'.format(b)][i] >= λ:
                over_ranking.append('I')
            else:
                over_ranking.append('>')
        else:
            if CRED['σ({},ai)'.format(b)][i] >= λ:
                over_ranking.append('<')
            else:
                over_ranking.append('R')

    return over_ranking


def pessimistic_sorting(OVER_RANK, CAT, A, B):
    """
    Rank the actions in the three different categories according to a pessimistic procedure.

    :param OVER_RANK: Dictionary containing the over sorting relations.
    :param CAT: List of the names of the different categories in which the actions will be classified.
    :param A: List containing the names of the actions as strings.
    :param B: Name of the boundary reference actions for which you want to calculate the concordance matrix.

    :return: sorting: Dictionary containing the different categories and the actions they contain. The keys are the name
        of the different categories. The values are lists containing the actions.
    :return: category: Dictionary containing the rank of each actions according to a pessimistic procedure.
        The keys are the name of the actions and the values are the median ranks.
    """
    sorting = {}
    category = {}
    for cat in CAT:
        sorting[cat] = []
    for i in range(len(A)):
        for j in reversed(range(len(CAT))):
            if OVER_RANK[B[j]][i] == '>' or OVER_RANK[B[j + 1]][i] == 'I':
                sorting[CAT[j]].append(A[i])
                category[A[i]] = j + 1
                break
    return sorting, category


def optimistic_sorting(OVER_RANK, CAT, A, B):
    """
    Rank the actions in the three different categories according to a optimistic procedure.

    :param OVER_RANK: Dictionary containing the over sorting relations for each boundary reference actions.
    :param CAT: List of the names of the different categories in which the actions will be classified.
    :param A: List containing the names of the actions as strings.
    :param B: Name of the boundary reference actions for which you want to calculate the concordance matrix.

    :return: sorting: Dictionary containing the different categories and the actions they contain. The keys are the
        categories 'Bad', 'Moderate', and 'Good'. The values are lists containing the actions.
    :return: category: Dictionary containing the rank of each actions according to a optimistic procedure.
        The keys are the actions and the values are the median ranks.
    """
    sorting = {}
    category = {}
    for cat in CAT:
        sorting[cat] = []
    for i in range(len(A)):
        for j in range(len(CAT)):
            if OVER_RANK[B[j + 1]][i] == '<' or OVER_RANK[B[j]][i] == 'R':
                sorting[CAT[j]].append(A[i])
                category[A[i]] = j + 1
                break
    return sorting, category


def median_rank(PESSI_SORT, OPTI_SORT, A):
    """
    Calculates the median rank of each action.

    :param PESSI_SORT: Dictionary containing the actions classified according to the pessimistic procedure.
    :param OPTI_SORT: Dictionary containing the actions classified according to the optimistic procedure.
    :param A: List containing the names of the actions as strings.

    :return med_rank: Dictionary containing the median rank of each action. The keys are the names of the actions
        and the values are the median ranks.
    """
    med_rank = {}
    for a in A:
        med_rank[a] = (OPTI_SORT[1][a] + PESSI_SORT[1][a]) / 2
    return med_rank


def display_results(PESSI_SORT, OPTI_SORT, MED_RANK, A):
    """
    Display of the median ranks and of the categories in which each action is classified.

    :param PESSI_SORT: Dictionary containing the actions classified according to the pessimistic procedure.
    :param OPTI_SORT: Dictionary containing the actions classified according to the optimistic procedure.
    :param MED_RANK: Dictionary containing the median rank of each action.
    :param A: List containing the names of the actions as strings.
    """
    for a in A:
        MED_RANK[a] = (OPTI_SORT[1][a] + PESSI_SORT[1][a]) / 2
        print('Action ' + a + ' is classified in the category C' + str(OPTI_SORT[1][a]) +
              str(PESSI_SORT[1][a]) + ' with a median rank of ' + str(MED_RANK[a]))


def separability_test(C, W, B, BP, T, display='NO'):
    """
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
    """
    Sigma_bk = {}
    Separability = ''
    for b in range(1, len(B), 1):
        conc = concordance(C, B, BP, B[b], BP, T)
        disc = discordance(C, B, BP, B[b], BP, T)
        glob_conc = global_concordance(conc, B[b], C, W, B)
        cred = credibility(glob_conc, B[b], disc, C, B)
        Sigma_bk['σ({},{})'.format(B[b - 1], B[b])] = cred['σ(ai,{})'.format(B[b])][b - 1]
    if max(Sigma_bk.values()) == 0:
        Separability = 'Hyper-strict'
        if display == 'YES':
            print(' ')
            print('The degree of separability is', Separability)
            print('Minimum required credibility threshold : max(σ(bk, bk+1)) =',
                  (math.ceil(max(Sigma_bk.values()) * 100) / 100))
        elif display != 'YES' and display != 'NO':
            raise NameError('The variable "display" must be equal to "YES" or "NO"')
    elif 0 < max(Sigma_bk.values()) <= 1/2:
        Separability = 'Strict'
        if display == 'YES':
            print(' ')
            print('The degree of separability is', Separability)
            print('Minimum required credibility threshold : max(σ(bk, bk+1)) =',
                  (math.ceil(max(Sigma_bk.values()) * 100) / 100))
        elif display != 'YES' and display != 'NO':
            raise NameError('The variable "display" must be equal to "YES" or "NO"')
    elif 1/2 < max(Sigma_bk.values()) <= 1:
        Separability = 'Weak'
        if display == 'YES':
            print(' ')
            print('The degree of separability is', Separability)
            print('Minimum required credibility threshold : max(σ(bk, bk+1)) =',
                  (math.ceil(max(Sigma_bk.values()) * 100) / 100))
        raise NameError('Redefine the input parameters to respect at least a strict separability.')

    return Sigma_bk, Separability


def ELECTRE_Tri_B(C, W, A, AP, B, BP, T, CAT, λ, display='NO'):
    """
    Upper function to execute the ELECTRE method by calling each of the elementary functions in the order
        they should be called. The input data are described below.

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
    """
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
    Sigma_bk, Separability = separability_test(C, W, B, BP, T, display='NO')
    if λ < max(Sigma_bk.values()):
        raise NameError('The chosen credibility threshold is lower than the minimum required credibility threshold '
                        'λ_min = {}'.format(max(Sigma_bk.values())))

    # ==========================   Calculation of the indicators of the ELECTRE Tri method   ========================= #
    # Calculation of the concordance matrices for all the boundary scenarios
    Conc = {}
    for b in B:
        name = '{}'.format(b)
        Conc[name] = concordance(C, A, AP, b, BP, T)
    # Calculation of the discordance matrices for all the boundary scenarios
    Disc = {}
    for b in B:
        name = '{}'.format(b)
        Disc[name] = discordance(C, A, AP, b, BP, T)
    # Calculation of the global concordances vectors for all the boundary scenarios
    Glob_conc = {}
    for b in B:
        name = '{}'.format(b)
        Glob_conc[name] = global_concordance(Conc['{}'.format(b)], b, C, W, A)
    # Calculation of the credibility vectors for all the boundary scenarios
    Cred = {}
    for b in B:
        name = '{}'.format(b)
        Cred[name] = credibility(Glob_conc['{}'.format(b)], b, Disc['{}'.format(b)], C, A)
    # Building the matrix of outranking relations
    Over_rank = {}
    for b in B:
        name = '{}'.format(b)
        Over_rank[name] = over_ranking_relations(Cred['{}'.format(b)], b, λ)

    # ============================   Ranking of actions and calculation of median ranks   ============================ #
    # Ranking of actions in the three categories according to the pessimistic procedure and display of the result
    Pessi_sort = pessimistic_sorting(Over_rank, CAT, A, B)
    # Ranking of actions in the three categories according to the optimistic procedure and display of the result
    Opti_sort = optimistic_sorting(Over_rank, CAT, A, B)
    # Calculating the median rank of each action
    Med_rank = median_rank(Pessi_sort, Opti_sort, A)

    # ==========================================   Display of the results   ========================================== #
    # Display of the categories in which each action is classified
    if display == 'YES':
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
    elif display != 'YES' and display != 'NO':
        raise NameError('The choice of displaying the results must be indicated by "YES" or "NO"')
    # Display of the median rank of each action
    if display == 'YES':
        print(' ')
        display_results(Pessi_sort, Opti_sort, Med_rank, A)
    elif display != 'YES' and display != 'NO':
        raise NameError('The choice of displaying the results must be indicated by "YES" or "NO"')

    return Conc, Disc, Glob_conc, Cred, Over_rank, Pessi_sort, Opti_sort, Med_rank, Sigma_bk, Separability
