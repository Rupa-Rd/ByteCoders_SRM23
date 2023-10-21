from diabetic_retinopathy_predict import retinopathy_prediction
from diabetic_readmission_predict import re_admission_prediction

def output():
    dr_res = retinopathy_prediction()
    re_res = re_admission_prediction()

    labels = ['Healthy','Mild DR','Moderate DR','Proliferate DR','Severe DR']

    if dr_res[1] >= 3 and re_res == 1 :
        print('{}% is confirmed that, it is {}'.format(dr_res[0],labels[dr_res[1]]))
        print('There will be a need of Re-admission')
    elif dr_res[1] >= 3 and re_res == 0:
        print('{}% is confirmed that, it is {}'.format(dr_res[0],labels[dr_res[1]]))
        print('There will be 60 % getting Re-admission')
    else:
        print('{}% is confirmed that, it is {}'.format(dr_res[0],labels[dr_res[1]]))
        print('There will be no need of Re-admission')


output()