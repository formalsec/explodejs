import latextable

import pandas as pd
import numpy as np

from texttable import Texttable

def load_data(filename):
    return pd.read_csv(filename)

def recall(tp, fn):
    return tp / (tp + fn)

def er(e, tp, fp):
    return e / (tp + fp)

total_cwe_22 = 166
total_cwe_78 = 169
total_cwe_94 = 54
total_cwe_1321 = 214
total = total_cwe_22 + total_cwe_78 + total_cwe_94 + total_cwe_1321
assert(total == 603)

explode_tp_cwe_22 = 2
explode_fn_cwe_22 = total_cwe_22 - explode_tp_cwe_22
explode_e_cwe_22 = 1
explode_r_cwe_22 = recall(explode_tp_cwe_22, explode_fn_cwe_22)
explode_er_cwe_22 = er(explode_e_cwe_22, explode_tp_cwe_22, 0)
explode_cwe_22 = [ explode_tp_cwe_22, explode_fn_cwe_22, explode_e_cwe_22, explode_r_cwe_22, explode_er_cwe_22 ]

explode_tp_cwe_78 = 114
explode_fn_cwe_78 = total_cwe_78 - explode_tp_cwe_78
explode_e_cwe_78 = 75
explode_r_cwe_78 = recall(explode_tp_cwe_78, explode_fn_cwe_78)
explode_er_cwe_78 = er(explode_e_cwe_78, explode_tp_cwe_78, 0)
explode_cwe_78 = [ explode_tp_cwe_78, explode_fn_cwe_78, explode_e_cwe_78, explode_r_cwe_78, explode_er_cwe_78 ]

explode_tp_cwe_94 = 34
explode_fn_cwe_94 = total_cwe_94 - explode_tp_cwe_94
explode_e_cwe_94 = 6
explode_r_cwe_94 = recall(explode_tp_cwe_94, explode_fn_cwe_94)
explode_er_cwe_94 = er(explode_e_cwe_94, explode_tp_cwe_94, 0)
explode_cwe_94 = [ explode_tp_cwe_94, explode_fn_cwe_94, explode_e_cwe_94, explode_r_cwe_94, explode_er_cwe_94 ]

explode_tp_cwe_1321 = 146
explode_fn_cwe_1321 = total_cwe_1321 - explode_tp_cwe_1321
explode_e_cwe_1321 = 90
explode_r_cwe_1321 = recall(explode_tp_cwe_1321, explode_fn_cwe_1321)
explode_er_cwe_1321 = er(explode_e_cwe_1321, explode_tp_cwe_1321, 0)
explode_cwe_1321 = [ explode_tp_cwe_1321, explode_fn_cwe_1321, explode_e_cwe_1321, explode_r_cwe_1321, explode_er_cwe_1321 ]

explode_tp_total = explode_tp_cwe_22 + explode_tp_cwe_78 + explode_tp_cwe_94 + explode_tp_cwe_1321
explode_fn_total = explode_fn_cwe_22 + explode_fn_cwe_78 + explode_fn_cwe_94 + explode_fn_cwe_1321
explode_e_total = explode_e_cwe_22 + explode_e_cwe_78 + explode_e_cwe_94 + explode_e_cwe_1321
explode_r_total = recall(explode_tp_total, explode_fn_total)
explode_er_total = er(explode_e_total, explode_tp_total, 0)
explode_total = [ explode_tp_total, explode_fn_total, explode_e_total, explode_r_total, explode_er_total ]

explode_nolo_df = load_data("explode-vulcan-results.csv")

explode_nolo_tp_cwe_22 = explode_nolo_df[(explode_nolo_df['cwe'] == 'CWE-22') & (explode_nolo_df['exploit'] == True)]['exploit'].count()
explode_nolo_fn_cwe_22 = total_cwe_22 - explode_nolo_tp_cwe_22
explode_nolo_e_cwe_22 = 0
explode_nolo_r_cwe_22 = recall(explode_nolo_tp_cwe_22, explode_nolo_fn_cwe_22)
explode_nolo_er_cwe_22 = er(explode_nolo_e_cwe_22, explode_nolo_tp_cwe_22, 0)
explode_nolo_cwe_22 = [ explode_nolo_tp_cwe_22, explode_nolo_fn_cwe_22, explode_nolo_e_cwe_22, explode_nolo_r_cwe_22, explode_nolo_er_cwe_22 ]

explode_nolo_tp_cwe_78 = explode_nolo_df[(explode_nolo_df['cwe'] == 'CWE-78') & (explode_nolo_df['exploit'] == True)]['exploit'].count()
explode_nolo_fn_cwe_78 = total_cwe_78 - explode_nolo_tp_cwe_78
explode_nolo_e_cwe_78 = 0
explode_nolo_r_cwe_78 = recall(explode_nolo_tp_cwe_78, explode_nolo_fn_cwe_78)
explode_nolo_er_cwe_78 = er(explode_nolo_e_cwe_78, explode_nolo_tp_cwe_78, 0)
explode_nolo_cwe_78 = [ explode_nolo_tp_cwe_78, explode_nolo_fn_cwe_78, explode_nolo_e_cwe_78, explode_nolo_r_cwe_78, explode_nolo_er_cwe_78 ]

explode_nolo_tp_cwe_94 = explode_nolo_df[(explode_nolo_df['cwe'] == 'CWE-94') & (explode_nolo_df['exploit'] == True)]['exploit'].count()
explode_nolo_fn_cwe_94 = total_cwe_94 - explode_nolo_tp_cwe_94
explode_nolo_e_cwe_94 = 0
explode_nolo_r_cwe_94 = recall(explode_nolo_tp_cwe_94, explode_nolo_fn_cwe_94)
explode_nolo_er_cwe_94 = er(explode_nolo_e_cwe_94, explode_nolo_tp_cwe_94, 0)
explode_nolo_cwe_94 = [ explode_nolo_tp_cwe_94, explode_nolo_fn_cwe_94, explode_nolo_e_cwe_94, explode_nolo_r_cwe_94, explode_nolo_er_cwe_94 ]

explode_nolo_tp_cwe_1321 = explode_nolo_df[(explode_nolo_df['cwe'] == 'CWE-471') & (explode_nolo_df['exploit'] == True)]['exploit'].count()
explode_nolo_fn_cwe_1321 = total_cwe_1321 - explode_nolo_tp_cwe_1321
explode_nolo_e_cwe_1321 = 0
explode_nolo_r_cwe_1321 = recall(explode_nolo_tp_cwe_1321, explode_nolo_fn_cwe_1321)
explode_nolo_er_cwe_1321 = er(explode_nolo_e_cwe_1321, explode_nolo_tp_cwe_1321, 0)
explode_nolo_cwe_1321 = [ explode_nolo_tp_cwe_1321, explode_nolo_fn_cwe_1321, explode_nolo_e_cwe_1321, explode_nolo_r_cwe_1321, explode_nolo_er_cwe_1321 ]

explode_nolo_tp_total = explode_nolo_tp_cwe_22 + explode_nolo_tp_cwe_78 + explode_nolo_tp_cwe_94 + explode_nolo_tp_cwe_1321
explode_nolo_fn_total = explode_nolo_fn_cwe_22 + explode_nolo_fn_cwe_78 + explode_nolo_fn_cwe_94 + explode_nolo_fn_cwe_1321
explode_nolo_e_total = explode_nolo_e_cwe_22 + explode_nolo_e_cwe_78 + explode_nolo_e_cwe_94 + explode_nolo_e_cwe_1321
explode_nolo_r_total = recall(explode_nolo_tp_total, explode_nolo_fn_total)
explode_nolo_er_total = er(explode_nolo_e_total, explode_nolo_tp_total, 0)
explode_nolo_total = [ explode_nolo_tp_total, explode_nolo_fn_total, explode_nolo_e_total, explode_nolo_r_total, explode_nolo_er_total ]

tbl = Texttable()
tbl.set_cols_align(["c"] * 2 + ["r"] * 15)
tbl.add_rows([
    ["CWE", "Total"] + ["TP", "FN", "E", "R", "Er"] * 3,
    ["CWE-22", total_cwe_22] + explode_cwe_22 + explode_nolo_cwe_22 + [0] * 5,
    ["CWE-78", total_cwe_78] + explode_cwe_78 + explode_nolo_cwe_78 + [0] * 5,
    ["CWE-94", total_cwe_94] + explode_cwe_94 + explode_nolo_cwe_94 + [0] * 5,
    ["CWE-1321", total_cwe_1321] + explode_cwe_1321 + explode_nolo_cwe_1321 + [0] * 5,
    ["Total", total] + explode_total + explode_nolo_total + [0] * 5,
])
print(latextable.draw_latex(tbl))
