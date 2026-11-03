---
title: G7 ↔ i-DREAMS mapping
updated: 2026-10-31
---

# G7 ↔ i-DREAMS mapping

กลับไป [[00-README]] · ข้อมูลพื้นฐาน [[01-dataset-overview]]

## ความต่างระดับ "ธรรมชาติของข้อมูล" (สำคัญกว่าการ map ทีละ feature)

| | G7 (production) | i-DREAMS sample |
|---|---|---|
| หน่วย | event ที่ตรวจจับแล้ว นับต่อวัน/ต่อรถ | วินาทีที่อยู่ใน level ต่อนาที |
| แหล่งสัญญาณ | กล้อง AI มองคนขับ + ถนน | ADAS หน้ารถ (Mobileye) + GPS + ความเร่ง + เวลาขับ + HRV |
| สภาพคนขับ | มี (phone, หาว, หลับตา, มองนอกถนน, บุหรี่) | **ไม่มี** |
| บริบท | กองรถ SCGJWD (ไทย) | รถบรรทุก 10 คน threshold แบบยุโรป |

G7 event ที่ระบบจริงส่งออก (รายงานเหตุการณ์ SCGJWD) มี **11 ชนิด** และโมเดล production ของรุ่นพี่ใช้ **5 feature**: `G7_yawn`, `G7_eye_close`, `G7_phone`, `G7_tailgating`, `G7_eye_off_road` (จำนวนครั้งรายวัน) [ตรวจแล้ว จากเอกสารรุ่นพี่ — รายละเอียดใน [[09-g7-definitions-from-seniors]]]. ชื่อ `G7_brake`, `G7_sudden_acceleration`, `G7_front_crash`, `G7_cigarette`, `G7_continuous_work`, `G7_vehicle_fatigue` ในตารางด้านล่างมาจาก note เดิม; เทียบกับลิสต์ 11 ชนิดของรุ่นพี่ ไม่พบ event "เบรก" (มี "คำเตือนความเร่ง") [ยังไม่ยืนยัน].

**การครอบคลุมของ feature โมเดล production (5 ตัว):**

| ระดับ | ครอบคลุม | ตัวที่ครอบคลุม |
|---|---|---|
| event-level (ตรวจจับสิ่งเดียวกัน) | **1 ใน 5** | tailgating |
| construct-level (เรื่องเดียวกัน ต่างวิธีวัด — ตามอาจารย์) | **3 ใน 5** | tailgating + yawn + eye_close ผ่าน Fatigue |
| ไม่มี (synthetic ฉีดเอง, D-11/D-12) | 2 ใน 5 | phone, eye_off_road *[อัปเดต 1 พ.ย.: D-21 — phone/eye_off_road เปิดแบบสร้างอิงข้อมูลจริงอ่อนๆ แทนปิด/ฉีดเอง ดู [[18-field-deep-dive]]]* |

การนับ construct-level เป็นสมมติฐานทดแทนที่ยังไม่ได้ validate

## ตารางเทียบ (สถานะปัจจุบัน)

| G7 event | i-DREAMS ที่ใกล้สุด | ระดับ | หลักฐาน |
|---|---|---|---|
| tailgating | `Headway_Map` L1–3 | **proxy ดี** | ค่า headway สะอาดมัธยฐาน 1.70 / 1.09 / 0.67 วินาที ตาม L1/L2/L3 สอดคล้อง D3.6 Table 3 (อันตราย 1.0–2.2 วินาที, วิกฤต 1.2–0.6 วินาที). ข้อจำกัด: แถวสะอาดแค่ ~4% และ L3 มี 60 แถว [ตรวจแล้ว] |
| speed_limit / speed_warning | `Speeding_Map` L1–3 | proxy | level วัดเทียบ speed limit (D3.6 Table 5: เกินขีดจำกัดราว 3.25–10% ถึง 4.75–15%) ไม่ใช่ความเร็วสัมบูรณ์. ความเร็วเฉลี่ยตาม level เด่น = 45.7 / 60.4 / 83.2 / 78.0 km/h (L3 ต่ำกว่า L2); L3 เด่นที่ < 30 km/h มี 170 จาก 2,193 นาที [ตรวจแล้ว] |
| brake | `DEM_evt_hb_*` | proxy | ตอนมี event ความเร็วลดจากนาทีก่อนหน้า 6.58 km/h (M) และ 7.58 km/h (H) เทียบกับค่าเฉลี่ยทั้งไฟล์ +0.09 [ตรวจแล้ว]. หมายเหตุ: ลิสต์ G7 11 ชนิดของรุ่นพี่ไม่มี event เบรก ([[09-g7-definitions-from-seniors]]) |
| sudden_acceleration | `DEM_evt_ha_*` | ยืนยันไม่ได้ | ความเร็วเปลี่ยน −1.03 (M) / −2.19 (H) ไม่เหมือนการเร่ง แต่ข้อมูลรายนาทีหยาบเกินจะตัดสิน [ตรวจแล้ว] |
| front_crash | `ME_AWS_fcw_mean`, `ME_AWS_pcw_mean` | ใช้ไม่ได้จริง | FCW > 0 แค่ 18 แถว (0.03%), PCW 1 แถว; 11 จาก 18 แถว FCW อยู่ในนาทีที่ Headway map บอกว่าไม่มีรถข้างหน้า → สองแหล่งไม่ตรงกัน [ตรวจแล้ว] |
| continuous_work ("ปฏิบัติงานต่อเนื่อง 4 ชม.") | `Fatigue_Map` L1–3 หรือคำนวณเองจาก `grpby_seconds ≥ 14,400` | proxy | Fatigue วัดจากเวลาขับ — ดู [[03-fatigue-finding]]. เอกสารรุ่นพี่มีแค่ชื่อ event ไม่มีนิยามเงื่อนไข ([[09-g7-definitions-from-seniors]]); ใน sample มี 2,634 แถว / 36 trips ที่ถึง 4 ชม. (เวลา trip ≠ เวลาทำงานต่อเนื่องเสมอไป) [ตรวจแล้ว; นิยามจริง ยังไม่ยืนยัน] |
| yawn / eyes_closed | `Fatigue_Map` (ตามคำแนะนำอาจารย์ 31 ต.ค.: fatigue = fatigue) | **ระดับ construct เท่านั้น — ไม่ใช่ event** | เรื่องเดียวกัน (ความเหนื่อยล้า) แต่ i-DREAMS วัดจากเวลาขับ ไม่ใช่อาการหาว/หลับตา; ไม่มีสัญญาณหน้า/ตา, KSS ไม่อยู่ในไฟล์, IBI มีค่าแค่ 0.7% ของแถว ([[03-fatigue-finding]]) |
| eyes_off_road | — (LDW/pedestrian_dz ตัดแล้ว: D-10) | **ไม่มี → synthetic ฉีดเอง (D-12)** | LDW ด้านขวา 20.5% ของแถว แต่ 10,569 จาก 10,828 แถวมาจากรถคันเดียว (84% ของนาทีของคันนั้น; คันอื่น 0–2.2%) และเป็น flag 0/60 วินาที → ผลของอุปกรณ์ ไม่ใช่พฤติกรรมคนขับ; pedestrian_dz บอกว่ามีคนเดินใกล้ ไม่ใช่การมองของคนขับ; ไม่มี gaze/head-pose [ตรวจแล้ว] |
| phone | — | **ไม่มีในไฟล์นี้** | หน้า Zenodo/Data Description พูดถึง handheld phone แต่ไฟล์ตัวอย่างไม่มีคอลัมน์ [จาก note เดิม]. ชุดเต็มอาจมี — ต้องยื่นฟอร์มขอ ([[05-zenodo-sample-version]]) |
| cigarette | — | **ไม่มี** | ไม่มีสัญญาณที่เกี่ยวข้อง |
| vehicle_fatigue ("การเตือนความเมื่อยล้าของยานพาหนะ") | — | ไม่มี | เอกสารรุ่นพี่ไม่นิยามว่ามาจากตัวรถหรือคนขับ; i-DREAMS ไม่มีสัญญาณจากอุปกรณ์ [ยังไม่ยืนยัน นิยาม] |
| *(ไม่มีใน G7)* | Overtaking L1, harsh cornering (`hc`), wipers/high beam, IBI | — | Overtaking L2/L3 เป็น 0 ทั้งไฟล์ |

## มี mapping 2 ชั้น (อย่าสับสน)

1. **ชั้น note เดิม** (`I-dream sample.md` หัวข้อ 4): เป็นเอกสารเชิงแนวคิด map ไปยังชื่อ event ของ G7 จริง พร้อมระดับความมั่นใจ — ไม่มีไฟล์/โค้ดที่เป็น mapping table จริง และ POC ไม่ได้อ้างอิงมัน
2. **ชั้น POC** (`data/generated/alert_codes.csv`): สร้าง **alert code ของเราเอง 21 ตัว (A0101–A0703)** ตั้งชื่อให้ดูแนว G7 แต่ **ไม่ใช่ code ของ G7 จริง**

| event_type ใน POC | codes | source ใน alert_codes.csv |
|---|---|---|
| HEADWAY | A0101–A0103 | iDreams map |
| OVERTAKING | A0201–A0203 | iDreams map |
| SPEEDING | A0301–A0303 | iDreams map |
| FATIGUE | A0401–A0403 | iDreams map |
| HARSH_ACCEL | A0501–A0503 | Driving events (DEM) |
| HARSH_BRAKE | A0601–A0603 | Driving events (DEM) |
| HARSH_CORNER | A0701–A0703 | Driving events (DEM) |

ผลที่ตามมา: ถ้า user ถามว่า "G7 ตรวจจับอะไรได้บ้าง" แล้ว bot ตอบจากตารางนี้ จะตอบผิด

## สรุปความแตกต่าง

i-DREAMS ใช้เป็น **ข้อมูลทดสอบโครงสร้าง** ของ chatbot (query, ranking, timeline, guardrail) ได้ แต่ไม่ใช่ตัวแทนของ G7:

- ทำได้: คำถามแนว headway, speeding, braking, เวลาขับต่อเนื่อง, ranking
- ต้องตอบว่าไม่มีข้อมูล: phone, cigarette, หาว, หลับตา, มองนอกถนน

เก็บคำถามที่ต้อง discuss ต่อใน [[08-poc-implications-and-open-questions]]
