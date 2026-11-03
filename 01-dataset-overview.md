---
title: Dataset overview — i-DREAMS sample
updated: 2026-10-31
---

# Dataset overview — i-DREAMS sample

กลับไป [[00-README]]

## ตัวไฟล์

- ไฟล์: `data-sample/i-Dreams/i-Dream-Sample_dataset.csv` (20,851,771 ไบต์) — ชื่อบน Zenodo คือ `Sample_dataset.csv` [ตรวจแล้ว: ขนาดตรงกับหน้า Zenodo ที่ปัดเป็น 20.9 MB]
- 52,770 แถว × 135 คอลัมน์ดิบ → ตัด `Unnamed` ว่างท้ายไฟล์ 50 คอลัมน์ เหลือ **85 คอลัมน์** [ตรวจแล้ว]
- 652 trips, 10 drivers, 8 vehicles [ตรวจแล้ว]; รถบรรทุก 100%, ช่วง 2021-09-20 ถึง 2022-05-17 (239 วัน) [จาก note เดิม] — **แต่มีข้อมูลแค่ 5 เดือนปฏิทิน** จำนวน trip ต่อเดือน: ก.ย. 2021 = 47, ต.ค. 2021 = 5, มี.ค. 2022 = 83, เม.ย. 2022 = 369, พ.ค. 2022 = 148 (ไม่มีข้อมูล พ.ย. 2021–ก.พ. 2022) [ตรวจแล้ว]
- จำนวน trip ต่อ driver: 8, 8, 19, 25, 28, 76, 90, 100, 110, 188 (รวม 652) [ตรวจแล้ว]
- แถวต่อ trip: มัธยฐาน 54, เฉลี่ย 80.9, สูงสุด 459 [ตรวจแล้ว]
- ไม่มีทะเบียนรถหรือชื่อคนขับ มีแค่ UUID (`trip_uuid_`, `driver_uuid_`, `vehicle_uuid_`)

## 1 แถว = ?

**1 แถว = หน้าต่าง 60 วินาทีของ 1 trip** (aggregate จากหลายเซนเซอร์ที่ fuse แล้ว)

- `grpby_seconds` = วินาทีสะสมตั้งแต่เริ่ม trip (60, 120, 180, …)
- `trip_start_` = **วันที่อย่างเดียว** (DD/MM/YYYY) ไม่ใช่ timestamp
- `tirp_start_time` (สะกดผิดในไฟล์ดิบ) = เวลาเริ่ม trip เช่น `08:53:05+00:00`
- `trip_end_` = ISO timestamp
- เวลาจริงของแถว = วันที่ `trip_start_` + `tirp_start_time` + offset ตาม `grpby_seconds` [จาก note เดิม]

## หน่วยของคอลัมน์ `*_level_N_sum` — **วินาที ไม่ใช่จำนวนครั้ง**

Data Description เขียนว่า "number of events" แต่ข้อมูลจริงบอกเป็นอย่างอื่น [ตรวจแล้ว]:

- ผลรวมทุก level ของ Headway = 60 ในทุกแถว (52,765 จาก 52,770 แถว) ส่วน Speeding = 52,768 แถว, Fatigue = 52,769 แถว
- `_mean = _sum / 60` (ตรวจแล้วว่าตรงกัน) = สัดส่วนของนาทีนั้น
- ข้อสรุป "เป็นวินาทีที่อยู่ใน state" เป็นการตีความจากตัวเลข เอกสารไม่ได้เขียนตรงๆ [ยังไม่ยืนยัน กับผู้เขียนเอกสาร]

> รายการคอลัมน์ครบทุกตัวพร้อมระดับการใช้ได้: [[12-field-catalog]]

## กลุ่มคอลัมน์

| กลุ่ม | คอลัมน์ตัวอย่าง | หมายเหตุ |
|---|---|---|
| ตัวระบุ/เวลา | `trip_uuid_`, `driver_uuid_`, `vehicle_uuid_`, `vehicle_class_`, `grpby_seconds`, `trip_start_`, `tirp_start_time`, `trip_end_` | ดูหัวข้อด้านบน |
| i-DREAMS risk maps | `iDreams_{Headway,Overtaking,Speeding,Fatigue}_Map_level_N_{mean,sum}` | คำนวณมาจาก pipeline ของ i-DREAMS ไม่ใช่เซนเซอร์ดิบ |
| Mobileye (ADAS) | `ME_Car_speed_mean`, `ME_AWS_hw_measurement_mean`, `ME_AWS_fcw_mean`, `ME_AWS_pcw_mean`, `ME_AWS_pedestrian_dz_mean`, `ME_AWS_tsr_level_mean`, `ME_TSR_tsr_1_speed_median` | ดูเรื่อง sentinel ด้านล่าง |
| GPS | `GPS_spd_mean`, `GPS_distances_sum` | ว่าง 15.4%; `GPS_distances_sum` มี **126 แถวที่เกิน 3,000 ม./นาที** (max 132 กม.) [ตรวจแล้ว] |
| Harsh driving (DEM) | `DEM_evt_{ha,hb,hc}_lvl_{L,M,H}_{mean,sum}`, `DrivingEvents_Map_*` | ha/hb/hc = เร่ง/เบรก/เข้าโค้ง; **เป็นวินาที** — ดู [[04-harsh-events-poc-issue]] |
| Lane departure | `ME_LDW_Map_type_L_mean`, `ME_LDW_Map_type_R_mean` | ด้านขวา 20.5% ของแถว ด้านซ้าย 0.57% |
| หัวใจ | `IBI_value_mean` | **เป็น 0 ใน 99.3% ของแถว** — มีค่าแค่ 378 แถว / 3 trips / คนขับ 1 คน (ช่วง 1,716–7,712) → แทบไม่มีข้อมูล [ตรวจแล้ว] |
| บริบท | `ME_Car_wipers_median`, `ME_Car_high_beam_median`, `ME_AWS_time_indicator_median` | ฝน/ไฟสูง/กลางวัน-คืน — ดู "การ coding ของ time indicator" ด้านล่าง; wipers เปิด 1.6% ของแถว, high beam 5 แถว [ตรวจแล้ว] |
| ขยะ | `check` ×4 (ค่าคงที่ 1), `Unnamed` ×50 (ว่าง) | ตัดทิ้งได้ |

## ความหมายของ level (จาก Data Description)

| หมวด | Level และความหมาย |
|---|---|
| Headway | **-1** ไม่มีรถข้างหน้า · **0** มีรถแต่ headway > 2.5 วินาที · **1** < 2.5 วินาที แต่ยังไม่ถึง threshold ของ i-DREAMS · **2** อยู่ระหว่าง threshold กับ 0.6 วินาที · **3** < 0.6 วินาที |
| Overtaking | **0** ไม่เตือน (Normal) · **1** เตือนภาพ (Normal) · **2** ภาพ+เสียง (Dangerous) · **3** เตือนถี่ (Avoidable) — นิยามจาก D6.1/D6.3 Table 2 |
| Speeding | **0** ไม่เตือน (Normal) · **1** สัญญาณภาพ (Normal) · **2** เตือนภาพ (Dangerous) · **3** ภาพ+เสียง (Avoidable) |
| Fatigue | **0** ไม่เตือน (Normal) · **1** เตือนภาพ · **2** ภาพ+เสียง · **3** เตือนถี่ — **ทั้ง 1–3 เป็น Dangerous** (ไม่ใช่การพิมพ์ซ้ำ และ **ไม่มี Avoidable**) |

> **แก้ 1 พ.ย. 2026:** ตัวเลขที่ผมเคยเขียนว่า "3 = เกือบเกิดอุบัติเหตุ" ของ Fatigue/Speeding/Overtaking เป็นการอ่านจากคำอธิบายใน Data Description ซึ่งไม่ตรงกับ D6.1/D6.3 Table 2 ที่เป็นแหล่งหลัก: level ของสามหมวดนี้คือ **ระดับ warning** ที่จัดเข้า phase (Fatigue L3 ยังเป็น Dangerous); เฉพาะ Headway ที่แปลตรงเป็น phase

ศัพท์ "dangerous / avoidable accident" ตรงกับ 3 phase ของ STZ ใน D3.6 และตาราง level ข้างบนยืนยันโดย D6.1/D6.3 Table 2 [ตรวจแล้ว — ดู [[06-deliverables-catalog]]]

ตรวจ threshold จริงของ Headway: ค่า headway สะอาด (< 10 วินาที) ที่ level เด่นของแต่ละนาที [ตรวจแล้ว]

| Level เด่น | แถว | min | Q1 | มัธยฐาน | Q3 | max |
|---|---|---|---|---|---|---|
| 1 | 1,628 | 0.96 | 1.50 | 1.70 | 1.92 | 2.50 |
| 2 | 1,168 | 0.65 | 0.94 | 1.09 | 1.22 | 1.70 |
| 3 | 60 | 0.41 | 0.61 | 0.67 | 0.74 | 1.16 |

ช่วงของ level ซ้อนกัน ซึ่งเข้ากับ threshold แบบปรับตามเงื่อนไข (D3.6 Table 3) — ไม่ใช่เส้นตัดคงที่

## จำนวนแถวที่มีวินาที > 0 ในแต่ละ level [ตรวจแล้ว]

| หมวด | level: จำนวนแถว |
|---|---|
| Headway | -1: 45,715 · 0: 18,897 · 1: 15,439 · 2: 9,190 · 3: 1,527 |
| Speeding | 0: 36,374 · 1: 19,727 · 2: 6,406 · 3: 5,944 |
| Fatigue | 0: 40,461 · 1: 5,665 · 2: 5,811 · 3: 1,136 |
| Overtaking | 0: 52,770 · 1: 2,365 · **2: 0 · 3: 0** (ตายทั้ง 4 คอลัมน์) |

## ปัญหาคุณภาพข้อมูลที่ต้องรู้

- `ME_AWS_hw_measurement_mean`: **70.24% เป็น sentinel 99999** และส่วนที่เหลือปนค่าเฉลี่ยกับ sentinel; มีแถวสะอาดจริง ~2,856 แถว [จาก note เดิม; ผมนับ L1+L2+L3 ที่ headway < 10 วินาที ได้ 2,856 เท่ากัน] → ใช้ `Headway_Map_level_*` แทน
- มี trip ที่ timeline ขาดหาย อย่างน้อย 10 trips ขาดเกิน 100 นาที (แย่สุดขาด 217 จาก ~503 นาที = 43%) [จาก note เดิม]
- `grpby_seconds` ช่วงจริง 60–30,180 [จาก note เดิม]
- `IBI_value_mean` มี artifact (ดูตารางกลุ่มคอลัมน์)
- `ME_TSR_tsr_1_speed_median` เป็น **รหัสป้าย** (ค่าเช่น 254, 9, 6, 8, 171) ไม่ใช่ km/h → คำนวณ speed limit เองไม่ได้ [ตรวจแล้ว]; ว่าง ~23.8% [จาก note เดิม]
- `ME_AWS_time_indicator_median`: **ไม่ใช่ข้อมูลหาย แต่ coding ต่างจาก Data Description** — เอกสารบอก 1 = กลางวัน/พลบค่ำ และ 0 = กลางคืน แต่ค่าจริงคือ 3.0 (25,549 แถว), 1.0 (25,206), 2.0 (935), 2.5/1.5 (รวม 9), ว่าง 1,071 และไม่มี 0 เลย. ตรวจกับชั่วโมงเริ่มขับ (UTC): ค่า 3 กระจุกช่วง ~19:00–03:00, ค่า 1 ช่วง ~05:00–17:00, ค่า 2 อยู่ช่วงเปลี่ยนผ่านเช้า/เย็น → **1 = กลางวัน, 2 = พลบค่ำ, 3 = กลางคืน** [ตรวจแล้ว ว่ารูปแบบเป็นเช่นนี้ และ **ยืนยันโดย D6.1 Table 2** ("1 - day, 2 - dusk, 3 - night")]. คำเตือนก่อนหน้า ("ไม่มีกลางคืน") เป็นการอ่านผิดจากเอกสาร

## สิ่งที่ Data Description / Zenodo บอกว่ามี แต่ไฟล์ไม่มี

- `Distraction_Map_mean` (handheld phone) และ `Drowsiness` (KSS) — ตาม note เดิม grep header แล้วไม่พบ [จาก note เดิม] ขณะที่หน้า Zenodo ระบุว่าโปรเจกต์บันทึก handheld phone
- ไม่มีคอลัมน์ label แบบ STZ (Normal / Dangerous / Avoidable) ต้องสร้างเอง → ดู D3.6 §4.3 "STZ labelling and preparation of training datasets" ใน [[06-deliverables-catalog]]
- ไม่มี event ที่มี timestamp ระดับวินาที ไม่มีทะเบียน/ชื่อ
- `DEM_evt_hc_lvl_H_mean` กับ `DEM_evt_hb_lvl_H_mean` อยู่ผิดกลุ่มในลำดับคอลัมน์ แต่จับคู่กับ `_sum` ตามชื่อได้ถูกต้อง — ดู [[04-harsh-events-poc-issue]]
