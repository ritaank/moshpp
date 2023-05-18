# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Max-Planck-Gesellschaft zur Förderung der Wissenschaften e.V. (MPG),
# acting on behalf of its Max Planck Institute for Intelligent Systems and the
# Max Planck Institute for Biological Cybernetics. All rights reserved.
#
# Max-Planck-Gesellschaft zur Förderung der Wissenschaften e.V. (MPG) is holder of all proprietary rights
# on this computer program. You can only use this computer program if you have closed a license agreement
# with MPG or you get the right to use the computer program from someone who is authorized to grant you that right.
# Any use of the computer program without a valid license is prohibited and liable to prosecution.
# Contact: ps-license@tuebingen.mpg.de
#
# If you use this code in a research publication please cite the following:
#
# @conference{AMASS:ICCV:2019,
#   title = {{AMASS}: Archive of Motion Capture as Surface Shapes},
#   author = {Mahmood, Naureen and Ghorbani, Nima and Troje, Nikolaus F. and Pons-Moll, Gerard and Black, Michael J.},
#   booktitle = {International Conference on Computer Vision},
#   pages = {5442--5451},
#   month = oct,
#   year = {2019},
#   month_numeric = {10}
# }
#
# You can find complementary content at the project website: https://amass.is.tue.mpg.de/
#
# Code Developed by:
# Nima Ghorbani <https://nghorbani.github.io/>
# Naureen Mahmood <https://ps.is.tuebingen.mpg.de/person/nmahmood>
# Matthew Loper <https://ps.is.mpg.de/~mloper>
# While at Max-Planck Institute for Intelligent Systems, Tübingen, Germany
#
# 2021.06.18
general_labels_map = {
        'HEAD_TOP': 'ARIEL',
        'TOPBACK': 'C7',
        'NECK_BASE': 'C7',
        'CHEST': 'CLAV',
        'UPTHRX': 'CLAV',
        'L_ANKLE': 'LANK',
        'L_ANK': 'LANK',
        'L_UPBACK': 'LBAK',
        'LBAC': 'LBAK',
        'LBAC-1': 'LBAK',
        'L_BICEP': 'LBCEP',
        'L_EAR': 'LBHD',
        'NEWLSHO': 'LBCEP',
        'NEWRSHO': 'RBCEP',
        'NEWLBAC': 'LNWST',
        'NEWRBAC': 'RNWST',
        'LBSHO': 'LBSH',
        'L_B_SHOULDER': 'LBSH',
        'L_B_WAIST': 'LBWT',
        'L_BWT': 'LBWT',
        'LPSI': 'LBWT',
        'L_CALF': 'LCLF',
        'LIBH': 'LEBHI',
        'LMBH': 'LEBHM',
        'LPBH': 'LEBHP',
        'LRBH': 'LEBHR',
        'LIDIP': 'LEIDIP',
        'L_ELBOW': 'LELB',
        'L_INELBOW': 'LELBIN',
        'LILB': 'LELBIN',
        'LIEL': 'LELBIN',
        'LMDIP': 'LEMDIP',
        'LPDIP': 'LEPDIP',
        'LPPIP': 'LEPPIP',
        'LPTIP': 'LEPTIP',
        'LRDIP': 'LERDIP',
        'LRPIP': 'LERPIP',
        'LRTIP': 'LERTIP',
        'LTMP': 'LETMP',
        'LTPIPI': 'LETPIPIN',
        'LTPIPO': 'LTHM4',
        'HEAD_OFFSET': 'LFHD',
        'L_PINKY': 'LFIN',
        'LOHAND': 'LFIN',
        'L_FIN': 'LFIN',
        'LPHLX5': 'LFIN',
        'L_FOREARM': 'LFRM',
        'LARM': 'LFRM',
        'LFRA': 'LFRM',
        'LWRE': 'LFRM',
        'LWRI': 'LFRMIN',
        'L_F_SHOULDER': 'LFSH',
        'LASI': 'LFWT',
        'L_F_WAIST': 'LFWT',
        'L_FWT': 'LFWT',
        'L_HEEL': 'LHEE',
        'LHEL': 'LHEE',
        'LANKIN': 'LHEEI',
        'LANKI': 'LHEEI',
        'LIPIP': 'LIDX1',
        'LEIPIP': 'LIDX1',
        'LITIP': 'LIDX3',
        'LEITIP': 'LIDX3',
        'L_INWRIST': 'LIWR',
        'LWRA': 'LIWR',
        'LWRST': 'LIWR',
        'L_OUTKNEE': 'LKNE',
        'L_KNEE': 'LKNE',
        'L_INKNEE': 'LKNI',
        'LKNEIN': 'LKNI',
        'LMPIP': 'LMID1',
        'LEMPIP': 'LMID1',
        'LMTIP': 'LMID3',
        'LEMTIP': 'LMID3',
        'L_BIGTOE': 'LMT1',
        'L_PINKYTOE': 'LMT5',
        'L_OUTWRIST': 'LOWR',
        'LWRB': 'LOWR',
        'L_WRIST': 'LOWR',
        # 'LEPTIP': 'LPNK3',
        'LMWT': 'LPRFWT',
        'LTOE5': 'LRSTBEEF',
        'L_MIDBACK': 'LSCAP',
        'L_SHIN': 'LSHN',
        'LSHIN': 'LSHN',
        'L_SHOULDER': 'LSHOUP',
        'LHIP': 'LTHI',
        'L_HIP': 'LTHI',
        'L_HAM': 'LTHI',
        'L_THIGH': 'LTHILO',
        'LTHIGH': 'LTHILO',
        'LTTIP': 'LTHM3',
        # 'LETTIP': 'LTHM3',
        'L_THUMB': 'LTHMB',
        'LIHAND': 'LTHMB',
        'LPHLX1': 'LTHMB',
        'LLEG': 'LTIB',
        'L_TOETIP': 'LTOE',
        'LTOE1': 'LTOE',
        'L_TRICEP': 'LUPA',
        'R_ANKLE': 'RANK',
        'R_ANK': 'RANK',
        'R_UPBACK': 'RBAK',
        'RBAC': 'RBAK',
        'RBAC-1': 'RBAK',
        'R10': 'RBAK',
        'OFFSET': 'RBAK',
        'R_BICEP': 'RBCEP',
        'R_EAR': 'RBHD',
        'RBSHO': 'RBSH',
        'R_B_SHOULDER': 'RBSH',
        'RPSI': 'RBWT',
        'R_B_WAIST': 'RBWT',
        'R_BWT': 'RBWT',
        'R_CALF': 'RCLF',
        'R_ELBOW': 'RELB',
        'R_INELBOW': 'RELBIN',
        'RILB': 'RELBIN',
        'RIEL': 'RELBIN',
        'R_PINKY': 'RFIN',
        'ROHAND': 'RFIN',
        'R_FIN': 'RFIN',
        'RPHLX5': 'RFIN',
        'R_FOREARM': 'RFRM',
        'RARM': 'RFRM',
        'RFRA': 'RFRM',
        'RWRE': 'RFRM',
        'RWRI': 'RFRMIN',
        'R_F_SHOULDER': 'RFSH',
        'RASI': 'RFWT',
        'R_F_WAIST': 'RFWT',
        'R_FWT': 'RFWT',
        'R_HEEL': 'RHEE',
        'RHEL': 'RHEE',
        'RANKIN': 'RHEEI',
        'RANKI': 'RHEEI',
        'RIBH': 'RIBHI',
        'RMBH': 'RIBHM',
        'RPBH': 'RIBHP',
        'RRBH': 'RIBHR',
        'RITIP': 'RIDX3',
        'RIITIP': 'RIDX3',
        'RIDIP': 'RIIDIP',
        'RIPIP': 'RIIPIP',
        'RMDIP': 'RIMDIP',
        'RMPIP': 'RIMPIP',
        'RPDIP': 'RIPDIP',
        'RPPIP': 'RIPPIP',
        'RRDIP': 'RIRDIP',
        'RRPIP': 'RIRPIP',
        'RTMP': 'RITMP',
        'RTPIPI': 'RITPIPIN',
        'RTPIPO': 'RITPIPOUT',
        'RTTIP': 'RITTIP',
        'R_INWRIST': 'RIWR',
        'RWRA': 'RIWR',
        'R_OUTKNEE': 'RKNE',
        'R_KNEE': 'RKNE',
        'R_INKNEE': 'RKNI',
        'RKNEIN': 'RKNI',
        'RMTIP': 'RMID3',
        'RIMTIP': 'RMID3',
        'R_BIGTOE': 'RMT1',
        'R_PINKYTOE': 'RMT5',
        'R_OUTWRIST': 'ROWR',
        'RWRB': 'ROWR',
        'R_WRIST': 'ROWR',
        'RPTIP': 'RPNK3',
        'RIPTIP': 'RPNK3',
        'RMWT': 'RPRFWT',
        'RRTIP': 'RRNG3',
        'RIRTIP': 'RRNG3',
        'RTOE5': 'RRSTBEEF',
        'R_MIDBACK': 'RSCAP',
        'R_SHIN': 'RSHN',
        'RSHIN': 'RSHN',
        'R_SHOULDER': 'RSHOUP',
        'RHIP': 'RTHI',
        'R_HIP': 'RTHI',
        'R_HAM': 'RTHI',
        'R_THIGH': 'RTHILO',
        'RTHIGH': 'RTHILO',
        'R_THUMB': 'RTHMB',
        'RIHAND': 'RTHMB',
        'RPHLX1': 'RTHMB',
        'RLEG': 'RTIB',
        'R_TOETIP': 'RTOE',
        'RTOE1': 'RTOE',
        'R_TRICEP': 'RUPA',
        'STERNUM': 'STRN',
        'SETRNUM': 'STRN',
        'LOTHRX': 'STRN',
        'LOBACK': 'T10',
        'MIDBACK': 'T8',
        'MID_BACK': 'T8',
        'ghost': 'nan',
        'NaN': 'nan',
}

immersion_map = {
        'CLAV': 'CLAV',
        'T10': 'T10',
        'LPSI': 'LBWT',
        'RPSI': 'RBWT',
        'C7': 'C7',
        'LFHD': 'LFHD',
        'STRN': 'STRN',
        'RBAK': 'RBAK',
        'LASI': 'LFWT',
        'RASI': 'RFWT',
        'RSHO': 'RSHOUP',
        'RELB': 'RELB',
        'LWRB': 'LOWR',
        'LWRA': 'LIWR',
        'RFIN': 'RFIN',
        'RWRB': 'ROWR',
        'RUPA': 'RUPA',
        'RFRM': 'RFRM',
        'RBHD': 'RBHD',
        'LSHO': 'LSHOUP',
        'RFHD': 'RFHD', # What is this?
        'LBHD': 'LBHD',
        'LFRM': 'LFRM',
        'LFIN': 'LFIN',
        'LELB': 'LELB',
        'LUPA': 'LUPA',
        'RTIB': 'RTIB',
        'RTOE': 'RTOE',
        'RTHI': 'RTHI',
        'RANK': 'RHEEI',
        'RHEE': 'RHEE',
        'LTHI': 'LTHI',
        'LANK': 'LHEEI',
        'RWRA': 'RIWR',
        'LKNE': 'LKNE',
        'LHEE': 'LHEE',
        'RKNE': 'RKNE',
        'LTIB': 'LTIB',
        'LTOE': 'LTOE',
}

general_labels_map.update(immersion_map)
