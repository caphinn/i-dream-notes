---
title: Deliverables ของ i-DREAMS (D2.1, D3.6 และอื่นๆ)
updated: 2026-10-31
---

# Deliverables ของ i-DREAMS

กลับไป [[00-README]] · เวอร์ชันข้อมูล [[05-zenodo-sample-version]]

## เลข D คืออะไร

**D{WP}.{ลำดับ}** = Deliverable ลำดับที่ n ของ Work Package ที่ WP — ไม่ใช่เวอร์ชันของข้อมูลหรือ dataset

| เอกสาร | WP | เวอร์ชัน/วันที่ | หน้า |
|---|---|---|---|
| **D2.1** State of the art on monitoring the driver state and task demand | 2 (นำโดย KFV) | v3.0 (27.02.2020) ส่ง 28.02.2020, "Revised after review", Public | 143 |
| **D3.6** Enhanced toolbox of recommended data collection tools, monitoring methods and interventions including thresholds for the STZ | 3 (นำโดย Loughborough; ผู้เขียนหลัก Rachel Talbot) | V1.0 (12/08/2021) ส่ง 14/08/2021, Public | 46 |

[ตรวจแล้ว จาก PDF ในเครื่อง และ D3.6 จาก URL ออนไลน์ — เนื้อหาและประวัติเวอร์ชันตรงกัน]

## D3.6 — หัวข้อที่เกี่ยวกับเรา

- §2.2 นิยาม STZ และ 3 phase: normal / danger / avoidable accident
- §2.4 real-time warning strategies: 2.4.1 headway · 2.4.2 illegal overtaking · 2.4.3 speeding · 2.4.4 fatigue
- §2.5 ความเชื่อมระหว่าง threshold กับ 3 phase (Table 7)
- §4.3 **STZ labelling and preparation of training datasets** ← เกี่ยวกับ use case "สร้าง STZ label เอง" เพราะ sample ไม่มีคอลัมน์ label
- ข้อควรระวัง: ค่า threshold ที่แน่นอนถูกตัดออกโดยตั้งใจ (IP) เราอ้างได้เฉพาะช่วงที่เปิดเผย:
  - Table 3 headway: อันตราย 1.0–2.2 วินาที, วิกฤต 1.2–0.6 วินาที; ตัวปรับ: ความเร็ว, อากาศ, เวลาของวัน, distraction, KSS, เวลาขับ
  - Table 5 speed: อันตราย ≈ เกินขีดจำกัด 3.25–10% ถึง 4.75–15%; วิกฤต = เกินกว่านั้น
  - Table 6 fatigue: ดู [[03-fatigue-finding]]
  - Overtaking: ทำงานเฉพาะช่วงห้ามแซงและความเร็ว > 35 km/h; ตรวจจากไฟเลี้ยว การข้ามเลน พวงมาลัย และความเร่ง
- Table 7 อ่านจากข้อความที่ดึงได้ไม่สมบูรณ์ ต้องเปิด PDF ดูเอง

## Deliverable อื่นๆ ที่รวบรวมได้

เลข D4.1–D8.3 มาจากหน้า Technical reports ของโปรเจกต์ (<https://idreamsproject.eu/wp/deliverables/>) ส่วนเลขอื่นมาจากหน้า UHasselt repository/PDF; ลิงก์ PDF มาจากหน้า CORDIS Results (<https://cordis.europa.eu/project/id/814761/results>) — **ยังไม่ได้เปิดอ่านเนื้อหาของแต่ละฉบับ** (ใช้ชื่อเรื่องจับคู่)

ฐานลิงก์ CORDIS: `https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=<ID>&appId=PPGMS`

### ที่มีเลข D

| D    | ชื่อ                                                                              | documentIds                                                       |
| ---- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| D2.1 | State of the art on monitoring the driver state and task demand                   | (UHasselt) <https://documentserver.uhasselt.be/handle/1942/32592> |
| D3.1 | Framework for operational design of experimental work                             | 080166e5cb9d9afd                                                  |
| D3.4 | Experimental protocol                                                             | 080166e5d3086528                                                  |
| D3.6 | Enhanced toolbox ... thresholds for the STZ                                       | 080166e5e0e966b0                                                  |
| D4.1 | Flexible modules for sensor data collection, integration and real-time processing | 080166e5d8b3db06                                                  |
| D4.2 | Algorithm for safety tolerance zone calculation                                   | **ไม่มีลิงก์ download**                                           |
| D4.3 | Back-end database storing raw and processed sensor data                           | **ไม่มีลิงก์ download**                                           |
| D4.4 | Flexible driver-machine interface for real-time warnings                          | 080166e5d7705f6d                                                  |
| D4.5 | Android app for personalised driving behavioural feedback                         | 080166e5d71b5939                                                  |
| D4.6 | Web platform for personalised goal setting, tips & tricks, social gamification    | 080166e5d71b6527                                                  |
| D5.1 | Organization of the driving simulator and on-road trial experiments               | 080166e5cc97c235                                                  |
| D5.2 | Description of the driving simulator experiment                                   | 080166e5d4fa0ce1                                                  |
| D5.3 | Description of the on-road driving trials                                         | 080166e5de9b1ceb                                                  |
| D5.4 | Unified Big Data fusion framework for exploiting driving performance data         | 080166e5e6807015                                                  |
| D6.1 | Analysis of task complexity factors                                               | 080166e5fb2f9dfc                                                  |
| D6.2 | Analysis of coping capacity factors: vehicle and operator state                   | 080166e5fb4d6992                                                  |
| D6.3 | Integrated model of driver-vehicle-environment interaction and risk               | 080166e5fb4d7263                                                  |
| D7.1 | Methodology for the evaluation of interventions                                   | 080166e5d526385f                                                  |
| D7.2 | Effectiveness evaluation of the interventions                                     | 080166e5fb197147                                                  |
| D8.1 | Toolkit for vehicle operator safety                                               | 080166e5facbf5c0                                                  |
| D8.2 | Exploitation plans                                                                | 080166e5fae7fd71                                                  |
| D8.3 | Policy recommendations                                                            | 080166e5fb185c69                                                  |
| D9.2 | Prototype of project's website                                                    | 080166e5c8e12259                                                  |
| D9.3 | Communication / Dissemination plan                                                | 080166e5c8820a56                                                  |
| D9.4 | Update of Communication / Dissemination plan                                      | 080166e5d52a2f49                                                  |

### CORDIS ไม่ระบุเลข D

| ชื่อ | documentIds | หมายเหตุ |
|---|---|---|
| Toolbox of recommended data collection tools and monitoring methods + conceptual definition of the STZ | 080166e5ceb0b2be | น่าจะเป็น D3.2 (D3.6 อ้าง "D3.2 Katrakazas 2020") [ยังไม่ยืนยัน] |
| State of the art on endogenous and exogenous factors for driver state and task demand, and monitoring technologies | 080166e5cc97a861 | อาจเป็นชื่อตามสัญญาของ D2.1 [ยังไม่ยืนยัน] |
| Overview of state of the art technology for safety interventions | 080166e5cc97c10f | |
| Report on survey of vehicle operator needs | 080166e5cab6b442 | |
| Toolbox of recommended interventions to assist drivers in maintaining the STZ | 080166e5d029f8af | |
| Standard protocol for the handling of Big Data | 080166e5d4187c70 | |
| Data Management Plan | 080166e5c8be9760 | |
| Report on activities of the User & Expert Advisory Boards | 080166e5f2c07706 | |
| Guide for driver/operator coaches and trainers | 080166e5d770539d | |

> **อัปเดต 1 พ.ย. 2026:** รายการเลข D ที่ครบและถูกต้องอยู่ในหัวข้อ "รายการ Deliverable จากเว็บโครงการ" ด้านล่าง (ตารางข้างบนที่จับคู่จากชื่อ CORDIS ให้ใช้เลข D จากตารางใหม่เป็นหลัก)

## อ่านฉบับไหนตอบคำถามอะไร (จากชื่อเรื่อง)

| อยากรู้ | อ่าน |
|---|---|
| level/threshold ของ 4 warning มาจากไหน | D3.6 |
| ข้อมูลถูกเก็บบนรถจริงยังไง | D5.3, D5.1 |
| ข้อมูลถูก fuse จากหลายเซนเซอร์ยังไง | D5.4, D4.1 |
| STZ คำนวณยังไงจริงๆ | D4.2 (ไม่เปิดสาธารณะ — ต้องถามผู้เขียน) |
| ทำไม Fatigue ผูกกับเวลาขับ | D3.6 §2.4.4 + Pilkington-Cheney et al. (2021) |
| โมเดลความเสี่ยงของโปรเจกต์ | D6.3 |

## Deliverable อื่นที่ผ่านตา

- D9.2–D9.4 เป็นงานสื่อสาร/เผยแพร่ ไม่เกี่ยวกับตัวข้อมูล
- CORDIS นับเอกสารทั้งหมด 31 รายการ (25 documents/reports, 3 other, 2 เว็บ/แพลตฟอร์ม, 1 DMP), publications 46 รายการ, datasets 0 รายการ (OpenAIRE search error ตอนดึง)

## รายการ Deliverable จากเว็บโครงการ (ครบ 37 รายการ) [ตรวจแล้ว 1 พ.ย. 2026]

ที่มา: <https://idreamsproject.eu/wp/deliverables/> — **ลิงก์ PDF โดยตรง ดาวน์โหลดได้ไม่ต้องผ่าน CORDIS** (หน้า download ของ CORDIS เป็น placeholder เปิดอ่านเนื้อหาผ่านเครื่องมือไม่ได้) ลิงก์ฐาน: `https://idreamsproject.eu/wp/wp-content/uploads/`

| D | ชื่อ | PDF (ต่อท้ายฐาน) | อ่านแล้ว? |
|---|---|---|---|
| D1.1, D1.3, D1.4, D4.2, D4.3, D10.1 | PMP, อัปเดต PMP/DMP, อัปเดต DMP ครั้งที่ 2, **อัลกอริทึม STZ**, **ฐานข้อมูล back-end**, POPD | **Confidential — ไม่มี PDF** | — |
| D1.2 | Data Management Plan | `2020/03/iDREAMS_814761_D1.2_28102019_V1.3-final.pdf` | ใช่ (ฉบับ v1.3 ปี 2019) |
| D2.1 | State of the art (endogenous/exogenous factors) | `2020/09/iDREAMS_814761_D2.1_28022020_Final.pdf` | ใช่ (ในเครื่อง) |
| D2.2 | Overview of state of the art technology for safety interventions | `2020/09/iDREAMS_814761_D2.2_28022020_Final.pdf` | ไม่ |
| D3.1 | Framework for operational design of experimental work | `2020/09/iDREAMS_814761_D3.1_30012020_Final.pdf` | ใช่ (ผลสำรวจผู้ปฏิบัติงาน, ภาพรวมแผน; อ่านผ่าน grep ไม่ใช่ทั้งฉบับ) |
| D3.2 | Toolbox of data collection tools and monitoring methods | `2020/09/iDREAMS_814761_D3.2_30042020_Final.pdf` | ใช่ (อ่านตาราง threshold §3.1.5, Table 8/10/11/14 จาก PDF โดยตรง; ส่วนอื่นอ่านผ่านสรุป) |
| D3.3 | Toolbox of recommended interventions | `2020/09/iDREAMS_814761_D3.3_09062020_Final.pdf` | ไม่ |
| D3.4 | Experimental protocol | `2022/05/iDREAMS_814761_D3.4_30082020_final.pdf` | ไม่ |
| D3.5 | Standard protocol for handling Big Data | `2022/05/iDREAMS_814761_D3.5_30092020_final.pdf` | ไม่ |
| D3.6 | Enhanced toolbox with thresholds for the STZ | `2022/09/iDREAMS_814761_D3.6_31082021_final.pdf` | ใช่ (ในเครื่อง) |
| D4.1 | Flexible modules for sensor data collection and real-time processing | `2022/09/iDREAMS_814761_D4.1_31012021_Final.pdf` | ใช่ |
| D4.4 | Flexible driver-machine interface for real-time warnings | `2022/09/iDREAMS_814761_D4.4_31122020_Final.pdf` | ไม่ |
| D4.5 | Android smartphone app for driving behavioural feedback | `2022/09/iDREAMS_814761_D4.5_31122020_Final.pdf` | ไม่ |
| D4.6 | Web platform for goal setting, tips, and social gamification | `2022/09/iDREAMS_814761_D4.6_31122020_final.pdf` | ไม่ |
| D4.7 | Guide for coaches and trainers on safety and ecological driving | `2022/09/iDREAMS_814761_D4.7_31122020_Final.pdf` | ไม่ |
| D5.1 | Organization of driving simulator and on-road trial experiments | `2022/09/iDREAMS_814761_D5.1_28022020_Final.pdf` | ใช่ (แผนจำนวนผู้เข้าร่วม/ขั้นตอน; อ่านผ่าน grep) |
| D5.2 | Driving simulator experiment description | `2022/09/iDREAMS_814761_D5.2_31102020_Final.pdf` | ไม่ |
| D5.3 | On-road driving trials description | `2022/09/iDREAMS_814761_D5.3_17062021-FINAL.pdf` | ใช่ (ส่วนแรก ~100,000 ตัวอักษรจาก ~129,000) |
| D5.4 | Unified Big Data fusion framework for driving performance data | `2022/09/iDREAMS_814761_D5.4_31122021_final.pdf` | ใช่ (ครบ รวม §4 และข้อสรุป) |
| D6.1 | Analysis of task complexity factors | `2019/05/iDREAMS_814761_D6.1_28042023_final_compressed-1.pdf` | ใช่ (Table 2 data dictionary, §2.4 การรวมข้อมูล, ผล SEM บางส่วน — อ่านจาก PDF) |
| D6.2 | Analysis of coping capacity factors: vehicle and operator state | `2019/05/iDREAMS_814761_D6.2_28042023_final-2_compressed.pdf` | ใช่ (ส่วนที่ดึงได้) |
| D6.3 | Integrated model of driver-vehicle-environment interaction and risk | `2019/05/iDREAMS_814761_D6.3_28042023_final-2_compressed-compressed-compressed-1.pdf` | ใช่ (ส่วนที่ดึงได้) |
| D7.1 | Methodology for the evaluation of interventions | `2022/05/iDREAMS_814761_D7.1_31102020_final.pdf` | ไม่ |
| D7.2 | Effectiveness evaluation of the interventions | `2019/05/iDREAMS_814761_D7.2_27042023_Final_compressed.pdf` | ใช่ (Executive summary, §4 Results – Trucks, ตาราง sample) |
| D8.1–D8.3 | Toolkit / Exploitation plans / Policy recommendations | `2019/05/iDREAMS_814761_D8.1_20042023_final_compressed.pdf`, `..._D8.2_24042023_Final.pdf`, `..._D8.3_27042023_Final.pdf` | ไม่ |
| D9.1–D9.5 | Survey of operator needs / website / dissemination plan (และ update) / UEAB report | `2020/01/..._D9.1_31122019_V2.1-final.pdf`, `2020/09/..._D9.2_31102019_Final.pdf`, `2020/03/..._D9.3_31102019_V2.0-final.pdf`, `2022/05/..._D9.4_31102020_final.pdf`, `2019/05/..._D9.5_20102022_final_compressed.pdf` | ไม่ |

หมายเหตุ: ชื่อ "Toolbox of recommended data collection tools ... + conceptual definition of the STZ" ที่ CORDIS ไม่ระบุเลข = **D3.2** (ยืนยันจากหน้าโครงการ); "Standard protocol for the handling of Big Data" = D3.5; "Report on survey of vehicle operator needs" = D9.1; "Report on activities of the User & Expert Advisory Boards" = D9.5; "Guide for driver/operator coaches and trainers" = D4.7; Data Management Plan = D1.2; ในตาราง CORDIS เดิม D9.2–D9.4 ตรงกับหน้าโครงการ

## เนื้อหาของฉบับที่อ่านแล้ว (สรุปเฉพาะที่เกี่ยวกับ dataset) [ตรวจแล้ว จากข้อความที่เครื่องมือดึงได้ — ส่วนท้ายของ D5.3, D5.4 ไม่ได้อ่าน และ D6.2/D6.3 ตัดมาบางส่วน]

### D6.3 — Integrated model of risk (อ้างอิงที่สำคัญที่สุดสำหรับชื่อคอลัมน์ของเรา)

**Table 2 ทำหน้าที่เป็น data dictionary และใช้ชื่อตัวแปรเดียวกับคอลัมน์ใน sample:**

| ตัวแปร | นิยามใน D6.3 Table 2 |
|---|---|
| `iDreams_Headway_Map_level` | **-1** ไม่พบรถข้างหน้า (Normal) · **0** พบรถ headway ≥ 2.5 วิ (Normal) · **1** พบรถ headway < 2.5 วิ แต่ยังเหนือ threshold เตือน (Normal) · **2** warning ขั้นแรก (Dangerous) · **3** warning ขั้นสอง (Avoidable accident) ค่าดิบ = `ME_AWS_hw_measurement` (วินาที). ตัวเลข 2.5 วิ เป็น threshold เดียวที่ระบุ |
| `ME_AWS_tsr_level` | **0** ไม่มี warning · **1** เกิน limit 0–5 หน่วย · **2** 5–10 · **3** 10–15 · **4** 15–20 · **5** 20–25 · **6** 25–30 · **7** 30+ หน่วย (km/h หรือ mph) |
| `iDreams_Speeding_Map_level` | **0** ไม่มี warning (Normal) · **1** แสดงสัญญาณภาพ (Normal) · **2** เตือนด้วยภาพ (Dangerous) · **3** ภาพ+เสียง (Avoidable) |
| `iDreams_Overtaking_Map_level` | **0** ไม่มี warning (Normal) · **1** เตือนภาพ (Normal) · **2** ภาพ+เสียง (Dangerous) · **3** เตือนถี่ (Avoidable) |
| `iDreams_Fatigue_Map_level` | **0** ไม่มี warning (Normal) · **1** เตือนภาพ · **2** ภาพ+เสียง · **3** เตือนถี่ — **ทั้ง 1–3 จัดเป็น Dangerous** (ไม่มี Avoidable) D6.3 ไม่ได้บอกว่า fatigue คำนวณจากอะไร (D3.6 บอกว่าเวลาขับ) |
| `DrivingEvents_Map_lvl` H/M/L และ ha/hb/hc | เป็น flag ของเหตุการณ์ระดับสูง/กลาง/ต่ำ แยกชนิด ha (เร่ง) hb (เบรก) hc (เข้าโค้ง); **ไม่มีเกณฑ์ g หรือ m/s²** |
| `IBI_value` | เวลาระหว่างการเต้นของหัวใจ (ms) จาก CardioID |

**ข้อเท็จจริงอื่นใน D6.3:**
- ข้อมูลรวมเป็นหน้าต่าง **30 หรือ 60 วินาที**; ตัวแปรแบบ level รวมเป็นทั้ง mean และ sum และมีการตรวจว่า **mean รวมกัน = 1 และ sum = 30 (ที่หน้าต่าง 30 วิ)** — ยืนยันความหมาย `_mean = _sum/หน้าต่าง` และ sum เป็นวินาที ตรงกับที่เราตรวจใน sample (หน้าต่าง 60 วิ)
- มีการตรวจว่า harsh L + M + H สอดคล้องกัน
- ตัดตัวแปรที่สหสัมพันธ์ |r| ≥ 0.6 ออกจากโมเดล
- **ไม่มีตัวแปร distraction / phone** ในตัวแปรที่วิเคราะห์ (มือถือมีแค่ในแบบสอบถามตอนเข้าร่วม)
- ผลวิเคราะห์ Belgian truck: SEM ของ speeding, harsh acceleration, headway; ตัวอย่าง **22–23 คนขับ, 6,346 trips, 590,356 นาที** (sample ของเรามี 10 คนขับ, 652 trips — **เอกสารไม่ได้ระบุว่า sample คือส่วนหนึ่งของชุด Belgian truck หรือไม่ [ยังไม่ยืนยัน]**)
- ไม่มีการกล่าวถึง Zenodo ในข้อความที่ดึงได้

### D6.2 — Coping capacity
- Fatigue ถูกอธิบายเป็นตัวแปรแบบ yes/no ในส่วนนิยาม; ไม่พูดถึง KSS, หาว, หลับตา ในข้อความที่ดึงได้
- ตัวแปร operator state (Table 3): IBI, headway, overtaking, fatigue, distance, duration, average speed, harsh acceleration/braking, FCW, PCW, LDW, เพศ, อายุ, การศึกษา; vehicle state: อายุรถ ยี่ห้อ เครื่องยนต์ ฯลฯ
- phone ไม่ได้วัดด้วยเซนเซอร์ มีแค่ในแบบสอบถาม

### D4.1 — Sensor modules และ real-time processing
- สถาปัตยกรรม: แต่ละโมดูลเป็น process แยก สื่อสารผ่าน ZeroMQ pub/sub (JSON + msgpack); โค้ด STZ เป็น Python (NumPy, SciPy, scikit-learn) รับ topic จากเซนเซอร์แล้วส่ง warning — **รายละเอียดอัลกอริทึมอยู่ใน D4.2 (ไม่เปิดสาธารณะ)**
- Mobileye ส่งข้อความ `ME_AWS`, `ME_TSR`, `TSR_Info`, `ME_Car` → ตรงกับคำนำหน้าคอลัมน์ `ME_AWS_*`, `ME_TSR_*`, `ME_Car_*` ใน sample
- Driving events (ha/hb/hc) มาจาก accelerometer + gyroscope ของ CardioGateway ผสมกับความเร็ว CAN ตรวจสอบกับ Geotab
- Fatigue/sleepiness: CardioWheel ใช้ HRV + มุมพวงมาลัย (SWA) ประมาณ **KSS**; IBI มาจาก PPG/ECG (สุ่มตัวอย่าง ECG 1000 Hz)
- **Distraction: แอปในมือถือตรวจช่วงที่ใช้มือถือและส่งเข้าอัลกอริทึม STZ** (และ CardioWheel รายงาน hands-on-wheel) — แปลว่าระบบจริงมีสัญญาณ phone แต่ **sample ที่ปล่อยไม่มีคอลัมน์นี้**
- กล้อง dash cam มี buffer ก่อน trigger 10 วิ; หลัง trigger: fatigue/FCW 10 วิ, harsh และ LDW 5 วิ, headway 20 วิ, overtaking 10 วิ

### D5.4 — Big Data fusion framework
- อัตราสุ่มตัวอย่าง: GPS 1 Hz, accelerometer 104 Hz, headway และ TSR 20 Hz, sensor มือถือ ≈ 10 Hz
- ข้อมูลที่ประมวลผลแล้วรวมเป็นช่วง **30 วินาที** สำหรับระบุ STZ แบบ real-time และหน้าต่าง 2 นาที/ทั้ง trip สำหรับวิเคราะห์หลัง trip; ฟังก์ชันรวมต่างกันตามตัวแปร (min/mean สำหรับ TTC, median สำหรับ KSS)
- การจัดระดับ STZ แบบ real-time ใช้ **Dynamic Bayesian Network** รับข้อมูล 30 วินาที — **ไม่ให้โครงสร้างหรือ threshold**
- ตรวจจับมือถือด้วย O7SDK (fusion ของเซนเซอร์มือถือ + classifier) มีคอลัมน์ "Mobile usage" ในตัวอย่างตาราง
- ไม่มี data dictionary แบบ `_mean`/`_sum`

### D5.3 — On-road trials
- 5 ประเทศ: เบลเยียม เยอรมนี กรีซ โปรตุเกส สหราชอาณาจักร; ยานพาหนะ: รถยนต์ รถบัส รถบรรทุก ราง
- จำนวนผู้เข้าร่วมไม่ตรงกันในเอกสาร (600 ในส่วน 1.1 กับ 490 ในส่วน 4.2)
- ขั้นตอนทดลอง: baseline 4 สัปดาห์ → stage 1 (เตือน real-time) 4 สัปดาห์ → stage 2 (+แอป) 4 สัปดาห์ → stage 3 (+เว็บ gamification) 6 สัปดาห์
- ไม่ระบุรูปแบบข้อมูลต่อ trip; ส่งต่อไป D3.2 และ D4.2

### D3.2 — Toolbox of data collection tools and monitoring methods
- **ตัวแปรตามเซนเซอร์:** Mobileye (headway วินาที + headway level, FCW, urban FCW, LDW, ป้ายจำกัดความเร็ว, ป้ายห้ามแซง, คนเดินเท้า, ที่ปัดน้ำฝน, ไฟเลี้ยว); CardioWheel (hands-on-wheel, เปลี่ยนคนขับ, fatigue event, IBI ≈ 1 Hz เป็น ms; ECG ดิบ 1000 Hz); **แอปมือถือ OSeven (นับ harsh acceleration/braking แบบ low/medium/high, speeding, การใช้มือถือ, ระยะที่ขับในชั่วโมงเสี่ยง ค่าเริ่มต้น 00:00–05:00)**
- **Fatigue/sleepiness:** ตัวชี้วัดตาที่แข็งแรงที่สุดคือ blink rate และ PERCLOS (แนะนำให้เสริมด้วยกล้อง ไม่ได้อยู่ใน CardioWheel); HRV ใช้ได้แต่แปรตามบุคคล; Table 3 ระบุเอาต์พุต KSS แบบหมวดหมู่ จาก CardioWheel/wristband; Table 4–5 ระบุระดับ attention/sleepiness 0–100
- **Distraction:** วัดด้วยการติดตามตา/ศีรษะ (PRC, PERLOOK) และการใช้มือถือผ่านแอป (ความแม่นยำ > 98% ในการทดลองที่มีการ annotate)
- **Threshold ใน Table 3:** headway, harsh events ฯลฯ ระบุเป็น "TBD" หรือ "ไม่มีค่าตายตัว (data-driven)"

**ตัวเลข threshold ที่เสนอใน D3.2 §3.1.5 (อ่านจาก PDF ตรงๆ — เป็นข้อเสนอจากวรรณกรรมปี 2020 ไม่ใช่ค่าที่ระบบใช้จริง; ค่าสุดท้ายอยู่ใน D3.6 ซึ่งแคบกว่า)**

| ตัวชี้วัด (Table 10) | รถบรรทุก/บัส Normal | Dangerous | Avoidable |
|---|---|---|---|
| Time headway (TH) | > 2.5 วิ | 2.5–1.26 วิ | < 1.26 วิ |
| ความเร่ง/เบรก | < 0.25 g (deceleration) | 0.25–0.3 g | > 0.3 g |
| TTC | > 4 วิ | — | — |
| BRT (brake reaction time) | 1.69/1.88 วิ | 1.69–1.5 วิ | < 1.0 วิ |

(รถยนต์: TH 1.8–2.8 / 0.6–1.4(1.8) / < 0.6 วิ; ความเร่ง < 0.31 g / 0.31–0.45 g / > 0.45 g)

| ตัวชี้วัด (Table 11 — ใช้ตัดสินว่า "ขับผิดปกติ") | รถบรรทุก/บัส | แหล่งเซนเซอร์ |
|---|---|---|
| Time headway | 2.5 วิ | Mobileye |
| Speed exceedance | 5% | Mobileye |
| Speed at turns | 5% | Mobileye |
| PCW / FCW / Urban FCW / LDW ซ้าย-ขวา | เกิดขึ้น (yes) | Mobileye |
| Long driving hours | **8 ชม.** (รถยนต์ 4–6 ชม.) | CardioID Gateway |
| ความเร่ง/ชะลอตามยาว | เกิน ±0.3 g | CardioID Gateway |
| Harsh acceleration | เกิดขึ้น (yes) | CardioID Gateway |
| Hands on wheel, มุมพวงมาลัย | yes / องศา | CardioWheel |

- **Table 8** (ระบบที่มีอยู่แล้ว): ความเร่ง 5–6 m/s² (Mazda, PATH, Stop Distance), ระยะต่ำสุด 5 ม., TTC 2.2 วิ (Honda), 3/2/1 วิ (Honda CMBS ขั้นตอนต่างๆ), 3 วิ (Hirst & Graham)
- **Table 14** (STZ ตาม task demand × coping capacity): High TD + Low CC และ Increased TD + Low CC = Avoidable accident; High/Increased TD + Decreased CC และ Low TD + Low CC = Dangerous; ที่เหลือ = Normal
- **เทียบกับ D3.6 (ค่าสุดท้าย):** headway Normal↔Dangerous 2.2–1.0 วิ, Dangerous↔Avoidable 1.2–0.6 วิ; fatigue คนขับอาชีพ 4.5 ชม. (D3.2 เสนอ 8 ชม.) → ใช้ตัวเลขของ D3.6 เป็นหลัก ค่า D3.2 ใช้อ้างเป็นที่มาจากวรรณกรรมเท่านั้น
- **สอดคล้องกับข้อมูล:** D6.3 กำหนด headway level 0 = ≥ 2.5 วิ ตรงกับ TH Normal ของรถบรรทุกใน D3.2 (> 2.5 วิ)
- **STZ:** นิยามเชิงแนวคิด 3 phase (Normal, Danger, Avoidable accident) เป็น safety envelope ที่รวมปัจจัยคนขับ + ตัวชี้วัดแบบ real-time; รายละเอียด Table 14 (ระดับ STZ ตาม task demand × coping capacity) ไม่อยู่ในส่วนที่อ่าน

### D1.2 — Data Management Plan (v1.3, ต.ค. 2019)
- **เผยแพร่:** ผ่าน Zenodo (DOI จาก DataCite), สัญญาอนุญาต CC BY 4.0 เป็นค่าเริ่มต้น, รูปแบบไฟล์ CSV หรือ JSON, **ข้อมูลต้องถูก aggregate ก่อนเผยแพร่**, ล้างข้อมูลเสียและตรวจความสมเหตุสมผลก่อน
- **ไม่ได้ระบุ:** ตัวแปรใดจะถูกเผยแพร่, ขนาดหน้าต่างเวลาที่ aggregate, และ **ไม่มีการกล่าวถึงฟอร์มขอข้อมูล/NDA** (ฟอร์มที่มากับชุด Zenodo จึงน่าจะเพิ่มทีหลัง [ยังไม่ยืนยัน])
- **ความเป็นส่วนตัว:** แทนที่ตัวระบุตรงๆ (ชื่อ อีเมล เบอร์ ID รถ) แบบสม่ำเสมอ; ตำแหน่ง GPS ที่จอดนานกว่า threshold (ตัวอย่าง 15 นาที) ถูกแทนด้วยโซนสี่เหลี่ยม — ตรงกับที่ sample ไม่มีพิกัดและรหัส driver/vehicle เป็น uuid
- **ชุดข้อมูลที่โครงการเก็บ:** ECG/IBI/hands-on-wheel (CardioWheel), CAN + warning ของ Mobileye, GPS, คลิป dashcam ที่ trigger โดยเหตุการณ์ (~50 คลิปต่อ 100 กม.), ข้อมูลเซนเซอร์มือถือ (GPS, accelerometer, gyroscope, screen state), แบบสอบถาม; trip = ignition on→off มี grace period 5 นาที
- **ข้อควรระวัง:** เอกสารเป็นแผนปี 2019 สถานะจริงหลังนั้นต้องเทียบกับฉบับอัปเดต (D1.3, D1.4 เป็น Confidential)

### D6.1 — Analysis of task complexity factors (**มี data dictionary ที่ตรงกับคอลัมน์ของเรามากที่สุด** — Table 2 หน้า 21–24) [ตรวจแล้ว จาก PDF ตรงๆ]

| คอลัมน์ | นิยามใน D6.1 Table 2 | หมายเหตุสำหรับ sample ของเรา |
|---|---|---|
| `ME_AWS_time_indicator` | สภาพแสง: **1 = กลางวัน, 2 = พลบค่ำ, 3 = กลางคืน** | **ยืนยันแล้ว** ว่า coding เป็น 1/2/3 (ที่เราตีความไว้) ปิดข้อสงสัยที่ค้างมา |
| `Phase` | เฟสการทดลอง: 1 = ไม่มี intervention/ monitoring, 2 = เตือนใน real-time, 3 = + post-trip feedback, 4 = + gamification | **sample ของเราไม่มีคอลัมน์ Phase** (ชุดเต็มมี) → บอกไม่ได้ว่า trip ไหนอยู่เฟสไหน ซึ่งอาจมีผลต่อพฤติกรรม |
| `*_level_N` (Headway/Overtaking/Speeding/Fatigue) | ค่า 0/1 ต่อ 1 แถวต้นทาง ("intervention level equal to N" = 1) | รวมเป็น `_sum` (วินาที) และ `_mean` ตอน aggregate |
| `DrivingEvents_Map_lvl_H/M/L`, `_evt_ha/hb/hc` | flag 0/1 ว่าตรวจพบระดับ/ชนิดนั้น | แหล่ง = Gateway IMU |
| `ME_AWS_hw_measurement` | headway เป็นวินาที (float) | |
| `ME_Car_wipers`, `ME_Car_high_beam`, `ME_AWS_fcw/ldw/pcw/pedestrian_dz` | Boolean; "0 = missing values", False = inactive, True = active | ตรวจใน sample ว่า 0 หมายถึงอะไรก่อนใช้ [ยังไม่ได้ตรวจ] |
| `GPS_distances` | ระบุหน่วย **km** ("Total trip distance") | ใน sample ค่าต่อนาทีที่รวมแล้วเป็นระยะทางสมเหตุสมผลถ้าตีเป็นเมตร (ทั้งไฟล์ ≈ 41,537 หน่วยเมตร→กม. ≈ 47 km/h เฉลี่ย) → น่าจะต่างหน่วยระหว่างเอกสารกับคอลัมน์ `_sum`; ยังไม่ยืนยัน |
| `vehicle_class` | Car, Bus, Truck, Train, Tram | sample มีแต่ Truck |

**การรวมข้อมูล (§2.4):** รวมเป็นหน้าต่าง 30 หรือ 60 วินาที; ตัวแปรระดับ (level) เก็บเป็นทั้ง mean และ sum โดยตรวจว่าในแต่ละแถว mean รวมกัน = 1 และ sum = 30 (ที่ 30 วิ); ค่า NA ถูกจัดการเฉพาะ (ระดับที่ไม่มีค่าเติมด้วย 0)

**ผลวิเคราะห์ที่เกี่ยวกับ field ของเรา:** `ME_AWS_time_indicator_median` สัมพันธ์เชิงบวกกับ speeding (speeding มากขึ้นตอนกลางคืน) และสัมพันธ์เชิงลบกับ headway (ตอนกลางคืนคนขับเว้นระยะปลอดภัยกว่า เพราะรถน้อย); `ME_Car_wipers_median` สัมพันธ์เชิงบวกกับ speeding; ตัวแปรเหล่านี้ใช้เป็นตัวแทนสภาพอากาศ/แสง (ฝน = ที่ปัดน้ำฝน, กลางคืน = time indicator)
**ข้อมูลเบลเยียม:** เฟส 1 ของ Belgian truck = 23 คนขับ 1,418 trips (117,160 นาที) — sample ของเรามี 10 คนขับ 652 trips 52,770 นาที จึงเล็กกว่าเฟสเดียวของชุดเต็ม; ยืนยันไม่ได้ว่าเป็นส่วนหนึ่งของชุดนั้นหรือไม่

### D5.4 — ส่วนข้อเสนอการแชร์ข้อมูลหลังโครงการ (§4) [ตรวจแล้ว]
- โครงการตั้งใจให้ข้อมูลถูก anonymize ตาม GDPR และควบคุมการเข้าถึงผ่าน API; การเปิดเป็น open access ขึ้นกับทุนสำหรับดูแลระบบหลังโครงการจบ และอาจให้บริการวิเคราะห์ต่อสำหรับนักวิจัยภายนอก
- เอกสารไม่ได้อธิบายชุดข้อมูลที่ปล่อยบน Zenodo หรือ variable ที่เปิดเผย → ที่มาของ sample ต้องดูที่หน้า Zenodo และ Data Description ในเครื่อง

### D7.2 — Effectiveness evaluation (ส่วนรถบรรทุกเบลเยียม) [ตรวจแล้ว จาก PDF ตรงๆ]

**ข้อมูลตัวอย่าง (Table 2, 37–39):**
- BE Trucks: **52 คนขับเข้าร่วม, เก็บข้อมูล 20/09/2021 – 25/10/2022**; ตัดออกจากการวิเคราะห์ผลลัพธ์ 15 คน; วิเคราะห์ผลลัพธ์ **n = 37**; แบบสอบถาม n = 40 (ชาย 100%, อายุเฉลี่ย 44.9 ปี, ประสบการณ์เฉลี่ย 20.2 ปี); **มาจาก 5 บริษัท**
- **12,761 trips, 900,155 กม.** ใน 4 เฟส (เฟสละ ~2,700–3,700 trips)
- *สอดคล้องกับ sample ของเรา* (ก.ย. 2021, ต.ค. 2021, มี.ค.–พ.ค. 2022 อยู่ในช่วงเก็บข้อมูล; vehicle_class = Truck; 10 คนขับ/652 trips เป็นส่วนย่อย) → **น่าจะเป็นข้อมูลรถบรรทุกเบลเยียม [สอดคล้อง ยังไม่ยืนยัน — เอกสารไม่ได้ระบุว่า sample คือชุดย่อยนี้]**

**ความหนาแน่นของ event ที่ใช้เป็นหลักยึดเชิงอ้างอิงได้ (Table 39–42, i-DREAMS events):**

| ตัวชี้วัด | ค่า (รถบรรทุกเบลเยียม, n = 37) |
|---|---|
| events ต่อ 100 กม. (ทุกชนิด) | ≈ 90.3–92.1 (เฟส 1 = 90.77) — ราวครึ่งหนึ่งของรถยนต์เบลเยียม |
| แบ่งเป็น vehicle control / speeding / road sharing (เฟส 1) | 50.2 / 4.1 / 36.1 ต่อ 100 กม. |
| fatigue events ต่อ 100 กม. | 0.41 (เฟส 1) → 0.35 (เฟส 4); ระดับกลาง ~0.21–0.26, ระดับสูง ~0.12–0.16 |
| คะแนนรวม (score) | ≈ 88–89 จาก 100 |

**ผลของการเตือน (สำหรับรถบรรทุก):** เปลี่ยนแปลงน้อยมาก — ผลที่มีนัยสำคัญทางสถิติมีแค่ (ก) total high-severity events ลดลงจากเฟส 1→2 (ข) medium speeding events *เพิ่มขึ้น* (ค) high road-sharing เพิ่มขึ้นจากเฟส 2→3; สรุปในเอกสารว่าระบบให้ผลบวกน้อยกว่ากับ **คนขับอาชีพ** เมื่อเทียบกับคนขับรถยนต์ส่วนบุคคล และสำหรับรถบรรทุก "สรุปแบบเบื้องต้น" ว่า real-time warning มีผลมากสุด
**Distraction/phone:** เอกสารระบุว่า **มีข้อมูล distraction ที่ใช้ได้เพียง 2 คนขับรถบรรทุก** จึงไม่รายงานผล → แม้ชุดเต็มของรถบรรทุกเบลเยียมก็แทบไม่มีข้อมูลมือถือ
**ข้อมูลแอป/แบบสอบถามออก:** คนขับรถบรรทุกส่วนน้อยตอบแบบสอบถามออก (n = 9) และมีการเข้าใช้แอปมากขึ้นหลังเพิ่ม gamification

### D5.1 และ D3.1 (แผนและผลสำรวจ)
- **D5.1 (ก.พ. 2020, แผน):** ขั้นสุดท้ายวางแผนผู้เข้าร่วม 515 คน: รถยนต์ 265, รถบัส 75 (โปรตุเกส), **รถบรรทุก 125 (เบลเยียม 75, โปรตุเกส 50)**, ราง 50; เบลเยียมมีการทดลองซิมูเลเตอร์รถบรรทุก 30 คน; ขั้นตอน baseline → intervention 7 เดือน แบ่ง 3 เฟส (4+4+6 สัปดาห์); **ผลจริงของเบลเยียมรถบรรทุก = 52 คน (D7.2) ต่างจากแผน 75** — ใช้ตัวเลขจาก D7.2 เป็นหลัก
- **D5.1 บทเรียน:** การสรรหาคนขับรถบรรทุกหญิงทำได้ยาก (สอดคล้องกับ 100% ชายใน D7.2)
- **D3.1 (ม.ค. 2020, สำรวจผู้ปฏิบัติงาน n = 103 โดยมีรถบรรทุกเพียง 10 คน):** "ขับตามชิดคันหน้า" ถูกเลือกเป็นความเสี่ยงสำคัญที่สุดของรถบรรทุก และเบรกกะทันหันก็สำคัญ — **สนับสนุนการใช้ tailgating เป็น feature หลักของเรา** (แต่ตัวอย่างเล็ก ใช้อ้างเป็นแนวโน้มเท่านั้น)

### D6.3 — เพิ่มเติม
- ตัวแปรในโมเดล SEM ใช้ **ชื่อคอลัมน์เดียวกับ sample** (`grpby_seconds`, `GPS_distances_sum`, `ME_AWS_time_indicator_median`, `DEM_evt_ha_lvl_H_mean`, `iDreams_Speeding_Map_level_N_mean`) ร่วมกับตัวแปรที่ **sample ไม่มี**: `Age`, `Gender`, `Fuel_type`, `VehicleAge`, `Gearbox` → ยืนยันว่า sample เป็นรูปแบบเดียวกับที่โครงการใช้วิเคราะห์ ตัดข้อมูลผู้ขับ/ยานพาหนะออก

## ผลต่อข้อสรุปของเรา (ตรวจแล้ว 1 พ.ย. 2026)

1. **ยืนยัน:** `_sum` = วินาที และ `_mean` = `_sum/หน้าต่าง` ตรงตามที่ D6.3 อธิบาย
2. **แก้ถ้อยคำ:** ค่า `Speeding/Overtaking/Fatigue_Map_level` คือ **ระดับของ warning (intervention level)** ที่ map เข้ากับ STZ phase ไม่ใช่ phase ตรงๆ — เฉพาะ Headway ที่ level แปลตรงเป็น phase (−1/0/1 Normal, 2 Dangerous, 3 Avoidable) Fatigue L1–3 ทั้งหมดอยู่ใน Dangerous ดังนั้นสูตร label แบบ Normal/Dangerous/Avoidable ของ Theodoraki ใช้ได้กับ headway เท่านั้น
3. **ใหม่ที่ใช้ได้:** `ME_AWS_tsr_level_mean` มีนิยามชัด (0–7 = เกิน limit กี่หน่วย) ใช้บอกขนาดการขับเร็วเกินได้ (ดูข้อควรระวังเรื่องค่าเฉลี่ยรายนาทีใน [[12-field-catalog]])
4. **ยืนยัน:** ไม่มี KSS, หาว/หลับตา ในชุดข้อมูลที่ปล่อยและในเอกสารฝั่งการวิเคราะห์; phone มีในระบบจริง (แอป O7SDK) แต่ไม่อยู่ใน sample
5. **หน้าต่างต่างกัน:** ระบบ real-time ของ i-DREAMS ใช้ 30 วิ ส่วน sample ของเราเป็น 60 วิ
6. **ยังไม่รู้:** วิธีที่ใช้คำนวณ level ภายใน (D4.2, DBN) และ threshold ของ harsh events ที่ระบบใช้จริง (D3.2 §3.1.5 ให้ค่าที่เสนอจากวรรณกรรม: ±0.3 g; ใน Table 3 ระบุว่าการตรวจของแอปเป็น data-driven)
7. **เหตุผลที่น่าจะอธิบายหน้าตา sample:** D1.2 ระบุว่าต้อง aggregate ก่อนเผยแพร่ และแทนตัวระบุ/พิกัดด้วยรหัสหรือโซน → sample จึงเป็นรายนาทีและไม่มีพิกัด [เป็นการตีความ ยังไม่ยืนยัน]
8. **phone:** D3.2 ยืนยันว่าแอป OSeven วัดการใช้มือถือได้ (> 98%) แต่ไม่มีคอลัมน์นี้ใน sample — ไม่พบคำอธิบายว่าทำไมถูกตัดออก
9. **ชั่วโมงเสี่ยง / กลางคืน:** D6.1 Table 2 ยืนยัน `ME_AWS_time_indicator` = 1 กลางวัน / 2 พลบค่ำ / 3 กลางคืน (D3.2 ใช้ 00:00–05:00 เป็นค่าเริ่มต้นของ "ชั่วโมงเสี่ยง" ซึ่งเป็นนิยามคนละแบบ) ใช้ `== 3` ทำ "ขับกลางคืน" ได้
10. **ไม่มี `Phase` ใน sample:** ชุดเต็มมีเฟสการทดลอง 1–4 (D6.1) แต่ sample ไม่มีคอลัมน์นี้
11. **sample น่าจะเป็นข้อมูลรถบรรทุกเบลเยียม** (ช่วงเวลา + ชนิดรถ สอดคล้องกับ D7.2) [ยังไม่ยืนยัน]
12. **phone:** แม้ชุดรถบรรทุกเบลเยียมเต็มก็มีข้อมูล distraction ที่ใช้ได้แค่ 2 คนขับ (D7.2) → ยืนยันว่า phone ต้องเป็น synthetic ต่อให้ขอชุดเต็มได้ (เสริม D-02/D-11/D-12)
13. **หลักยึดเชิงอ้างอิงใหม่:** รถบรรทุกเบลเยียมมี ≈ 91 events/100 กม. และ fatigue warning ≈ 0.4/100 กม. (i-DREAMS events ไม่ใช่ G7) ใช้เป็นเกณฑ์ตรวจความสมเหตุสมผลของอัตราที่เราสุ่มได้ (ดู R-08)
14. **อย่าอ้างว่าการเตือนช่วยลดพฤติกรรมเสี่ยงของรถบรรทุกได้จริง:** ผลใน D7.2 อ่อนและปะปน มีนัยสำคัญเฉพาะ high-severity events เฟส 1→2
