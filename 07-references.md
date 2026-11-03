---
title: References ทั้งหมด
updated: 2026-10-31
---

# References ทั้งหมด

กลับไป [[00-README]]

หมายเหตุ: ลิงก์ `https://cordis.europa.eu/project/id/814761` ที่เคยระบุว่าเป็น "paper" จริงๆ คือ **หน้าโปรเจกต์ CORDIS** ไม่ใช่เปเปอร์ (เปเปอร์แยกอยู่ด้านล่าง)

## A. เปิดตรวจแล้วในแชต [ตรวจแล้ว]

### โปรเจกต์/ข้อมูล
| รายการ | ลิงก์ |
|---|---|
| Zenodo sample dataset v1.0 (DOI 10.5281/zenodo.7684848) | <https://zenodo.org/records/7684848> |
| CORDIS project 814761 | <https://cordis.europa.eu/project/id/814761> |
| CORDIS Results (รายการ deliverable/publication) | <https://cordis.europa.eu/project/id/814761/results> |
| เว็บโปรเจกต์ | <https://idreamsproject.eu/> · <https://idreamsproject.eu/wp/> |
| Technical reports (D4.1–D8.3) | <https://idreamsproject.eu/wp/deliverables/> |
| Scientific publications | <https://idreamsproject.eu/wp/scientific-publications/> |
| Non-scientific publications | <https://idreamsproject.eu/wp/popular-publications/> |
| Publications (ภาพรวม) | <https://idreamsproject.eu/wp/publications/> |

### Deliverable (ดู [[06-deliverables-catalog]] สำหรับ D อื่น)
| รายการ | ลิงก์ |
|---|---|
| D3.6 PDF | <https://idreamsproject.eu/wp/wp-content/uploads/2022/09/iDREAMS_814761_D3.6_31082021_final.pdf> |
| D2.1 (UHasselt repository) | <https://documentserver.uhasselt.be/handle/1942/32592> |
| D2.1 PDF | <https://documentserver.uhasselt.be/bitstream/1942/32592/1/iDREAMS_814761_D2.1_28022020_Final%20%281%29.pdf> |
| D2.1 (Loughborough) | <https://repository.lboro.ac.uk/articles/report/D2_1_State_of_the_art_on_monitoring_driver_state_and_task_demand/13181807/1> |
| D3.1 | <https://documentserver.uhasselt.be/handle/1942/32594> |
| D3.4 | <https://documentserver.uhasselt.be/handle/1942/35514> |
| D9.3 / D9.4 (UHasselt) | <https://documentserver.uhasselt.be/bitstream/1942/32702/1/iDREAMS_814761_D9.3_31102019_Final.pdf> · <https://documentserver.uhasselt.be/bitstream/1942/41684/1/iDREAMS_814761_D9.4_31102020_final.pdf> |

### เปเปอร์
| รายการ | ลิงก์ |
|---|---|
| Garefalakis, Katrakazas, Yannis (2022) *Data-Driven Estimation of a Driving Safety Tolerance Zone Using Imbalanced Machine Learning*, Sensors 22(14):5309 | <https://doi.org/10.3390/s22145309> · <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9319394/> |
| Garefalakis et al. (2024) *Predicting risky driving behavior with classification algorithms...*, Eur. Transp. Res. Rev. 16:65 | <https://doi.org/10.1186/s12544-024-00691-9> |
| Roussou et al. (2024) *Machine Learning Insights on Driving Behaviour Dynamics among Germany, Belgium, and UK Drivers*, Sustainability 16(2):518 | <https://www.mdpi.com/2071-1050/16/2/518> |
| Theodoraki, Garefalakis, Michelaraki, Yannis — *Evaluating Risky Driving Behavior Using a Naturalistic Driving Dataset: A Hybrid Modelling Approach*, Infrastructures 11(8):266 | <https://www.mdpi.com/2412-3811/11/8/266> |
| Kaiser et al. (2020) *State of the art on measuring driver state and technology-based risk prevention and mitigation*, TRA 2020 | <https://www.nrso.ntua.gr/geyannis/wp-content/uploads/geyannis-pc364.pdf> |
| Pilkington-Cheney et al. (2021) *i-DREAMS intervention strategies to reduce driver fatigue and sleepiness...* | <https://doi.org/10.1109/mt-its49943.2021.9529340> |
| *A big data-as-a-service architecture for naturalistic driving studies* (2021) | <https://doi.org/10.1109/mt-its49943.2021.9529322> |
| สไลด์ Garefalakis (STZ levels จาก time headway; "Normal" ที่ headway > 2 วินาที) | <https://www.nrso.ntua.gr/geyannis/wp-content/uploads/geyannis-pc537c.pdf> |

ข้อมูลโดยสรุปจากเปเปอร์ที่ใช้อ้าง: RF 84% / MLP 82% (Garefalakis 2022); ชุดข้อมูลปี 2026 = 69 drivers, 15,389 trips, 265,512 นาที (BE + UK)

### เอกสารรุ่นพี่ (ไฟล์ในเครื่อง `Capstone/จากรุ่นพี่/`) [ตรวจแล้ว: ค้นข้อความ ไม่รวมข้อความในรูป]
- `SCGJWD-CP-Report.pdf` §5.1.1, §5.1.7–5.1.8, §5.3, §5.6.1, §5.10.1 (ตาราง 5.10.1.2), §5.12.1
- `Capstone Final Presentation SCGJWD2025.pptx` สไลด์ 11, 24–29, 39, 58
- `Progress presentation.pdf`, `SCGJWD-CP-Presentation.pdf`, `Capstone Proposal SCGJWD2026 Presentation.pdf`, `Final_Report_Capstone_2025__DRIVER_BEHAVIOR_AND_LOGISTICS_ANALYTICS_PLATFORM-...pdf`

### เปเปอร์ที่ใช้เรื่อง STZ label ([[10-stz-labelling]])
- Theodoraki et al., *Infrastructures* 11(8):266 — กติกา label จาก headway level (Normal = -1/0/1, Dangerous = 2, Avoidable = 3): <https://www.mdpi.com/2412-3811/11/8/266>
- Garefalakis, Katrakazas, Yannis (2022), *Sensors* 22(14):5309 — label จาก `Headway_min` ต่อ 30 วินาที (2 s / 1.4 s), ข้อมูล simulator: <https://pmc.ncbi.nlm.nih.gov/articles/PMC9319394/>
- Roussou et al. (2024), *Sustainability* 16(2):518 — ไม่ระบุกติกา label: <https://www.mdpi.com/2071-1050/16/2/518>

## B. มาจาก note เดิม ยังไม่ได้เปิดตรวจ [จาก note เดิม]

| รายการ | ลิงก์ |
|---|---|
| MDPI Sensors 23(24):9663 | <https://www.mdpi.com/1424-8220/23/24/9663> |
| TUM — i-DREAMS project page (IEEE Xplore ค้นต่อ) | <https://www.mos.ed.tum.de/en/vvs/forschung/projekte/past-projects/idreams/> |
| ResearchGate 362098908 (ชื่อตรงกับ Sensors 2022 ข้างบน) | <https://www.researchgate.net/publication/362098908_Data-Driven_Estimation_of_a_Driving_Safety_Tolerance_Zone_Using_Imbalanced_Machine_Learning> |

## C. ไฟล์ในเครื่อง

ดูรายการใน [[00-README]] หัวข้อ "ไฟล์ต้นทางในเครื่อง"
