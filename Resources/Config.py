from Core.InfoPdfData import InfoPdfData

SAVE_DATA_PATH = '../Resources/SavedPath.txt'

PDF_CONFIG_PATH_AVANGARD_4 = '../Resources/Avangard_4.csv'
PRICE_AVANGARD_4 = 209400
ARTICUL_AVANGARD_4 = '480F160=0_AA02_C'

PDF_CONFIG_PATH_AVANGARD_TEEN = 'Avangard_TEEN.csv'
PRICE_AVANGARD_TEEN = 205200
ARTICUL_AVANGARD_TEEN = '480F45=30000_K'

PDF_CONFIG_PATH_MOTION_2_CS = '../Resources/Motus_2_CS.csv'
PRICE_MOTION_2_CS = 131500
ARTICUL_MOTION_2_CS = '480F61=2_AA03_C'

PDF_CONFIG_PATH_MOTION_2_CV = '../Resources/Motus_2_CV.csv'
PRICE_MOTION_2_CV = 131500
ARTICUL_MOTION_2_CV = '480F61=2_AA02_C'


def get_configs():

    config_avangard_4 = InfoPdfData(PDF_CONFIG_PATH_AVANGARD_4, PRICE_AVANGARD_4, ARTICUL_AVANGARD_4)
    config_avangard_teen = InfoPdfData(PDF_CONFIG_PATH_AVANGARD_TEEN, PRICE_AVANGARD_TEEN, ARTICUL_AVANGARD_TEEN)
    config_motion_cs = InfoPdfData(PDF_CONFIG_PATH_MOTION_2_CS, PRICE_MOTION_2_CS, ARTICUL_MOTION_2_CS)
    config_motion_cv = InfoPdfData(PDF_CONFIG_PATH_MOTION_2_CV, PRICE_MOTION_2_CV, ARTICUL_MOTION_2_CV)

    configs = []
    configs.append(config_avangard_4)
    configs.append(config_avangard_teen)
    configs.append(config_motion_cv)
    configs.append(config_motion_cs)

    return configs

