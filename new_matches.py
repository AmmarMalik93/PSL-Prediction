import numpy as np

def get_match(num):
    if num == 1:
        match = np.array([7.16, 7.00, 6.60, 3.00, 7.15, 
                               7.16,10,7.28,10,7.41,10,
                               7.56,9,7.40,9,7.57,9,
                               7.69,9,8.25,8,8.55,8,
                               8.70,8,8.67,8,7.88,8,
                               8.43,7,8.00,7,9.20,6,
                               10.00,6,10.00,6,11.50,6,
                               16.00,5]).reshape(1,-1) #IU vs LQ
        Team1 = 'IU'
        Team2 = 'LQ'

    if num == 2:
        match = np.array([10.00, 8.00, 8.66, 5.00, 8.80,
                              9.26,10,9.67,10,9.82,10,
                              10.19,9,10.13,9,10.43,9,
                              10.46,9,10.83,9,11.00,9,
                              11.50,8,11.44,8,12.50,7,
                              12.86,7,14.17,7,14.80,7,
                              15.50,7,16.67,7,18.00,7,
                              23.00,6]).reshape(1,-1) #MS vs KK
        Team1 = 'MS'
        Team2 = 'KK'

    if num == 3:

        match = np.array([3.00, 7.00, 6.40, 6.00, 8.50,
                               8.89,10,9.22,8,9.59,8,
                               9.75,8,9.93,8,9.86,8,
                               10.38,8,10.00,8,10.55,8,
                               11.40,6,10.89,6,12.25,6,
                               12.43,6,12.17,4,11.80,4,
                               14.00,3,14.33,3,20.50,3,
                               24.00,2]).reshape(1,-1) #LQ vs PZ
        Team1 = 'LQ'
        Team2 = 'PZ'

    if num == 4:

        match = np.array([6.00, 9.00, 7.33, 5.00 ,6.65,
                           6.05,10,5.94,10,5.59,10,
                           5.00,10,3.93,10,2.64,10,
                           2.31,10,1.74,10,0.64,10,
                           0.00,10,0.00,10,0.00,10,
                           0.00,10,0.00,10,0.00,10,
                           0.00,10,0.00,10,0.00,10,
                           0.00,10]).reshape(1,-1) #QG vs IU
        Team1 = 'QG'
        Team2 = 'IU'

    if num == 5: 
        match = np.array([3.66, 8.00, 9.40, 7.00, 9.85,
                               10.26, 10,10.67, 10,10.76, 10,
                               10.44, 10,10.80, 10,11.07, 10,
                               11.08, 10,11.33, 9,11.73,9,
                               12.80,6,12.56,6, 13.88,4,
                               15.14,4,16.33,4,19.20,4,
                               23.00,4,28.00,4,37.50,3,
                               69.00,1]).reshape(1,-1) #PZ vs QG

        Team1 = 'PZ'
        Team2 = 'QG'

    if num == 6:
        match = np.array([3.33, 6.00, 7.00, 5.00, 7.60,
                              7.47, 10,7.78, 10,7.53, 10,
                              7.44, 10,7.07, 10,7.00, 9,
                              7.00, 8,6.50, 8,6.36, 8,
                              6.70, 8,7.22, 6,7.66, 6,
                              8.14, 5,9.00, 3,10.60, 1,
                              12.25, 1,14.67, 1,15.00, 1,
                              100.00, 0]).reshape(1,-1) #IU vs LQ

        Team1 = 'IU'
        Team2 = 'LQ'

    if num == 7:
        match = np.array([8.66, 10.00, 7.33, 6.00, 8.30,
                              8.00, 10,7.89, 10,7.29, 10,
                              7.63, 9,7.40, 9,7.71, 9,
                              7.00, 9,7.00, 9,7.09, 9,
                              6.70, 9,6.89, 9,6.63, 9,
                              6.00, 9,6.17, 9,6.00, 9,
                              3.00, 9,0.00, 10,0.00, 10,
                              0.00, 10]).reshape(1,-1) #PZ vs MS
        Team1 = 'PZ'
        Team2 = 'MS'

    return(Team1, Team2, match)