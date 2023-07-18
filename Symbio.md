# Tableau SQL report: Symbio  
16 queries have been analyzed.  

21 tables used: ['wau None', 'notifications_allowed as na', 'mailing_allowed as ma', 'first None', 'symbio.user_records as ur', 'lifetime as l', 'avg_lifetime as al', 'ages as a', 'dau None', 'symbio.users u', 'w1_rt as wr', 'symbio.users as u', 'average_ages as aa', 'public.calendar None', 'calendar None', 'total_users as tu', 'w1_retention as w', 'm1_retention as m', 'mau None', 'symbio.program_realizations pr', 'symbio.members as m']  


Query number 1:
| index | input | type |
|---:|:---|:---|
| 34 | ur.created_at | column |
| 57 | pr.program | column |
| 72 | ur.content | column |
| 92 | u.gender | column |
| 130 | symbio.program_realizations pr | table |
| 157 | symbio.user_records as ur | table |
| 179 | ur.id | column |
| 194 | pr.dialogs_realizations_id | column |
| 216 | symbio.users u | table |
| 236 | pr.user_id | column |
| 251 | u.id | column |

Query number 2:
| index | input | type |
|---:|:---|:---|
| 35 | u.created_at | column |
| 58 | u.gender | column |
| 73 | u.organization_name | column |
| 117 | symbio.users as u | table |
| 140 | u.gender | column |
| 178 | u.organization_name | column |

Query number 3:
| index | input | type |
|---:|:---|:---|
| 59 | ur.created_at | column |
| 103 | ur.created_at | column |
| 147 | ur.created_at | column |
| 170 | ur.organization_name | column |
| 198 | user_id | column |
| 220 | symbio.user_records as ur | table |
| 245 | ur.organization_name | column |
| 373 | ur.created_at | column |
| 396 | ur.organization_name | column |
| 424 | user_id | column |
| 446 | symbio.user_records as ur | table |
| 471 | ur.organization_name | column |
| 591 | ur.created_at | column |
| 614 | ur.organization_name | column |
| 642 | user_id | column |
| 664 | symbio.user_records as ur | table |
| 689 | ur.organization_name | column |
| 767 | dau.freq_date | column |
| 782 | dau.organization | column |
| 797 | wau.week | column |
| 812 | mau.month | column |
| 827 | dau.dau | column |
| 842 | wau.wau | column |
| 857 | mau.mau | column |
| 887 | dau.dau | column |
| 901 | mau.mau | column |
| 954 | wau.wau | column |
| 968 | mau.mau | column |
| 1009 | dau None | table |
| 1032 | wau None | table |
| 1046 | dau.week | column |
| 1061 | wau.week | column |
| 1075 | dau.organization | column |
| 1090 | wau.organization | column |
| 1119 | mau None | table |
| 1133 | dau.month | column |
| 1148 | mau.month | column |
| 1162 | dau.organization | column |
| 1177 | mau.organization | column |
| 1199 | dau.freq_date | column |

Query number 4:
| index | input | type |
|---:|:---|:---|
| 35 | ur.created_at | column |
| 58 | ur.organization_name | column |
| 86 | user_id | column |
| 106 | symbio.user_records as ur | table |
| 129 | ur.organization_name | column |

Query number 5:
| index | input | type |
|---:|:---|:---|
| 60 | date | column |
| 77 | public.calendar None | table |
| 106 | calendar.freq_date | column |
| 126 | u.organization_name | column |
| 152 | u.id | column |
| 174 | calendar None | table |
| 190 | symbio.users as u | table |
| 212 | calendar.freq_date | column |
| 248 | u.created_at | column |
| 271 | freq_date | column |
| 299 | u.organization_name | column |

Query number 6:
| index | input | type |
|---:|:---|:---|
| 35 | ur.created_at | column |
| 58 | ur.organization_name | column |
| 86 | user_id | column |
| 106 | symbio.user_records as ur | table |
| 129 | ur.organization_name | column |

Query number 7:
| index | input | type |
|---:|:---|:---|
| 35 | ur.created_at | column |
| 58 | ur.origin | column |
| 73 | ur.organization_name | column |
| 112 | symbio.user_records as ur | table |
| 135 | ur.state | column |
| 160 | ur.content | column |
| 302 | ur.origin | column |
| 330 | ur.organization_name | column |

Query number 8:
| index | input | type |
|---:|:---|:---|
| 59 | ur.created_at | column |
| 82 | ur.content | column |
| 102 | ur.category_id | column |
| 122 | ur.organization_name | column |
| 186 | freq_date | column |
| 200 | freq_date | column |
| 211 | nb_dialogs | column |
| 237 | symbio.user_records as ur | table |
| 262 | ur.state | column |
| 287 | ur.content | column |
| 429 | ur.organization_name | column |
| 495 | freq_date | column |
| 506 | nb_dialogs | column |
| 531 | freq_date | column |
| 541 | organization | column |
| 551 | dialog | column |
| 561 | category | column |
| 571 | nb_dialogs | column |
| 579 | first None | table |

Query number 9:
| index | input | type |
|---:|:---|:---|
| 35 | ur.created_at | column |
| 58 | ur.category_id | column |
| 78 | ur.content | column |
| 98 | u.gender | column |
| 113 | ur.organization_name | column |
| 157 | symbio.user_records as ur | table |
| 183 | symbio.users as u | table |
| 205 | u.id | column |
| 216 | ur.user_id | column |
| 232 | ur.state | column |
| 257 | ur.category_id | column |
| 285 | ur.content | column |
| 427 | u.organization_name | column |

Query number 10:
| index | input | type |
|---:|:---|:---|
| 59 | u.created_at | column |
| 82 | u.organization_name | column |
| 128 | symbio.users as u | table |
| 153 | u.organization_name | column |
| 255 | u.created_at | column |
| 278 | u.organization_name | column |
| 324 | symbio.users as u | table |
| 349 | u.is_notification | column |
| 374 | u.organization_name | column |
| 476 | u.created_at | column |
| 499 | u.organization_name | column |
| 545 | symbio.users u | table |
| 568 | u.has_mailling_subscription | column |
| 593 | u.organization_name | column |
| 653 | tu.freq_date | column |
| 668 | tu.organization | column |
| 698 | tu.nb_users | column |
| 724 | tu.organization | column |
| 743 | tu.freq_date | column |
| 803 | na.nb_users_notifications_allowed | column |
| 829 | tu.organization | column |
| 848 | tu.freq_date | column |
| 908 | ma.nb_users_mailing_allowed | column |
| 934 | tu.organization | column |
| 953 | tu.freq_date | column |
| 1008 | nb_users_notifications_allowed_cumulative_sum | column |
| 1017 | nb_users_cumulative_sum | column |
| 1055 | nb_users_mailing_allowed_cumulative_sum | column |
| 1064 | nb_users_cumulative_sum | column |
| 1091 | total_users as tu | table |
| 1119 | notifications_allowed as na | table |
| 1140 | tu.freq_date | column |
| 1155 | na.freq_date | column |
| 1171 | tu.organization | column |
| 1186 | na.organization | column |
| 1213 | mailing_allowed as ma | table |
| 1234 | tu.freq_date | column |
| 1249 | ma.freq_date | column |
| 1265 | tu.organization | column |
| 1280 | ma.organization | column |

Query number 11:
| index | input | type |
|---:|:---|:---|
| 38 | ur.user_id | column |
| 53 | ur.organization_name | column |
| 94 | u.created_at | column |
| 166 | ur.created_at | column |
| 180 | u.created_at | column |
| 246 | ur.created_at | column |
| 260 | u.created_at | column |
| 319 | timedelta | column |
| 374 | symbio.user_records as ur | table |
| 400 | symbio.users as u | table |
| 422 | ur.user_id | column |
| 433 | u.id | column |
| 528 | ur.user_id | column |
| 543 | ur.organization_name | column |
| 584 | u.created_at | column |
| 656 | ur.created_at | column |
| 670 | u.created_at | column |
| 736 | ur.created_at | column |
| 750 | u.created_at | column |
| 809 | timedelta | column |
| 864 | symbio.user_records as ur | table |
| 890 | symbio.users as u | table |
| 912 | ur.user_id | column |
| 923 | u.id | column |
| 1000 | w.created_at_week | column |
| 1020 | w.organization | column |
| 1050 | w.w1_retention | column |
| 1098 | m.m1_retention | column |
| 1135 | w1_retention as w | table |
| 1156 | m1_retention as m | table |
| 1181 | w.created_at_week | column |
| 1196 | m.created_at_week | column |
| 1212 | w.organization | column |
| 1227 | m.organization | column |
| 1249 | week | column |

Query number 12:
| index | input | type |
|---:|:---|:---|
| 38 | ur.user_id | column |
| 53 | ur.organization_name | column |
| 122 | ur.created_at | column |
| 136 | u.created_at | column |
| 202 | ur.created_at | column |
| 216 | u.created_at | column |
| 275 | timedelta | column |
| 330 | symbio.user_records as ur | table |
| 356 | symbio.users as u | table |
| 378 | ur.user_id | column |
| 389 | u.id | column |
| 407 | ur.organization_name | column |
| 465 | timedelta | column |
| 510 | l.organization | column |
| 532 | l.timedelta | column |
| 559 | lifetime as l | table |
| 624 | l.organization | column |
| 654 | l.w1_retention | column |
| 690 | lifetime as l | table |
| 736 | l.timedelta | column |
| 756 | l.organization | column |
| 777 | l.user_id | column |
| 804 | al.average_lifetime | column |
| 831 | wr.w1_retention | column |
| 857 | lifetime as l | table |
| 881 | avg_lifetime as al | table |
| 898 | l.organization | column |
| 913 | al.organization | column |
| 935 | w1_rt as wr | table |
| 952 | l.organization | column |
| 967 | wr.organization | column |

Query number 13:
| index | input | type |
|---:|:---|:---|
| 35 | ur.created_at | column |
| 58 | ur.organization_name | column |
| 86 | user_id | column |
| 106 | symbio.user_records as ur | table |
| 129 | ur.organization_name | column |

Query number 14:
| index | input | type |
|---:|:---|:---|
| 35 | u.created_at | column |
| 58 | u.os_name | column |
| 73 | u.app_version | column |
| 88 | u.organization_name | column |
| 127 | symbio.users as u | table |
| 150 | u.os_name | column |
| 178 | u.app_version | column |
| 206 | u.organization_name | column |

Query number 15:
| index | input | type |
|---:|:---|:---|
| 14 | m.organization_name | column |
| 40 | m.user_id | column |
| 97 | total_signups | column |
| 110 | total_invitations | column |
| 143 | symbio.members as m | table |
| 166 | m.organization_id | column |

Query number 16:
| index | input | type |
|---:|:---|:---|
| 31 | u.id | column |
| 46 | u.organization_name | column |
| 66 | u.age | column |
| 81 | u.gender | column |
| 112 | gender | column |
| 139 | gender | column |
| 167 | gender | column |
| 209 | u.created_at | column |
| 240 | age | column |
| 254 | age | column |
| 284 | age | column |
| 303 | age | column |
| 341 | age | column |
| 357 | age | column |
| 395 | age | column |
| 411 | age | column |
| 449 | age | column |
| 465 | age | column |
| 503 | age | column |
| 519 | age | column |
| 557 | age | column |
| 573 | age | column |
| 611 | age | column |
| 627 | age | column |
| 665 | age | column |
| 681 | age | column |
| 719 | age | column |
| 735 | age | column |
| 773 | age | column |
| 789 | age | column |
| 827 | age | column |
| 843 | age | column |
| 881 | age | column |
| 897 | age | column |
| 935 | age | column |
| 951 | age | column |
| 989 | age | column |
| 1005 | age | column |
| 1043 | age | column |
| 1059 | age | column |
| 1097 | age | column |
| 1113 | age | column |
| 1151 | age | column |
| 1167 | age | column |
| 1205 | age | column |
| 1221 | age | column |
| 1259 | age | column |
| 1275 | age | column |
| 1313 | age | column |
| 1329 | age | column |
| 1367 | age | column |
| 1383 | age | column |
| 1421 | age | column |
| 1437 | age | column |
| 1471 | age | column |
| 1495 | age | column |
| 1515 | symbio.users as u | table |
| 1568 | u.organization_name | column |
| 1594 | age | column |
| 1613 | symbio.users as u | table |
| 1664 | a.freq_date | column |
| 1679 | a.gender_mapped | column |
| 1694 | a.age_bins | column |
| 1709 | a.organization | column |
| 1730 | aa.average_age | column |
| 1763 | a.id | column |
| 1783 | ages as a | table |
| 1804 | average_ages as aa | table |
| 1821 | a.organization | column |
| 1836 | aa.organization | column |
| 1852 | a.age_bins | column |
| 1880 | a.organization | column |
| 1942 | a.freq_date | column |
| 1954 | a.age_bins | column |
