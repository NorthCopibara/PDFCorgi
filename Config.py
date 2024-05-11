import os

from Core.InfoPdfData import InfoPdfData

IS_RELEASE = False #TODO

UI_PATH = '../Resources/CalcUI.ui' if IS_RELEASE else './View/CalcUI.ui'

SAVE_DATA_PATH = 'Resources/SavedPath.txt'

NAME_AVANGARD_4 = 'Авангард 4'
PDF_CONFIG_PATH_AVANGARD_4 = './Resources/Avangard_4.csv'
PDF_CONFIG_PATH_AVANGARD_4_release = '../Resources/Avangard_4.csv'
PRICE_AVANGARD_4 = 209400
ARTICUL_AVANGARD_4 = '480F160=0_AA02_C'

NAME_AVANGARD_TEEN = 'Авангард TEEN'
PDF_CONFIG_PATH_AVANGARD_TEEN = './Resources/Avangard_TEEN.csv'
PDF_CONFIG_PATH_AVANGARD_TEEN_release = '../Resources/Avangard_TEEN.csv'
PRICE_AVANGARD_TEEN = 205200
ARTICUL_AVANGARD_TEEN = '480F45=30000_K'

NAME_MOTION_2_CS = 'Мотус 2.0 CS'
PDF_CONFIG_PATH_MOTION_2_CS = './Resources/Motus_2_CS.csv'
PDF_CONFIG_PATH_MOTION_2_CS_release = '../Resources/Motus_2_CS.csv'
PRICE_MOTION_2_CS = 131500
ARTICUL_MOTION_2_CS = '480F61=2_AA03_C'

NAME_MOTION_2_CV = 'Мотус 2.0 CV'
PDF_CONFIG_PATH_MOTION_2_CV = './Resources/Motus_2_CV.csv'
PDF_CONFIG_PATH_MOTION_2_CV_release = '../Resources/Motus_2_CV.csv'
PRICE_MOTION_2_CV = 131500
ARTICUL_MOTION_2_CV = '480F61=2_AA02_C'


def get_configs():

    path_1 = PDF_CONFIG_PATH_AVANGARD_4_release if IS_RELEASE else PDF_CONFIG_PATH_AVANGARD_4
    config_avangard_4 = InfoPdfData(NAME_AVANGARD_4, path_1, PRICE_AVANGARD_4, ARTICUL_AVANGARD_4)

    path_2 = PDF_CONFIG_PATH_AVANGARD_TEEN_release if IS_RELEASE else PDF_CONFIG_PATH_AVANGARD_TEEN
    config_avangard_teen = InfoPdfData(NAME_AVANGARD_TEEN, path_2, PRICE_AVANGARD_TEEN,
                                       ARTICUL_AVANGARD_TEEN)

    path_3 = PDF_CONFIG_PATH_MOTION_2_CS_release if IS_RELEASE else PDF_CONFIG_PATH_MOTION_2_CS
    config_motion_cs = InfoPdfData(NAME_MOTION_2_CS, path_3, PRICE_MOTION_2_CS,
                                   ARTICUL_MOTION_2_CS)

    path_4 = PDF_CONFIG_PATH_MOTION_2_CV_release if IS_RELEASE else PDF_CONFIG_PATH_MOTION_2_CV
    config_motion_cv = InfoPdfData(NAME_MOTION_2_CV, path_4, PRICE_MOTION_2_CV,
                                   ARTICUL_MOTION_2_CV)

    configs = []
    configs.append(config_avangard_4)
    configs.append(config_avangard_teen)
    configs.append(config_motion_cv)
    configs.append(config_motion_cs)

    return configs
