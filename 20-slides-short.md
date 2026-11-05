---
title: สไลด์ i-DREAMS ฉบับสั้น (9 หน้า)
updated: 2026-11-05
status: ร่าง — ย่อจาก 17-slide-content + 18-field-deep-dive
---

# สไลด์ฉบับสั้น (9 หน้า)

ต้นทาง: [[17-slide-content]], [[18-field-deep-dive]] · ตัวเลขยกมาจาก 2 ไฟล์นี้ (+03, 06)

| ช่วง | สไลด์ |
|---|---|
| S1 Dataset | 1–2 |
| S2 Usage | 3 |
| Fields (หน้าละ field) | 4 Fatigue · 5 Headway · 6 Phone + Eyes-off-road · 7 Speeding · 8 Harsh |
| สรุป + Limitations + Next step | 9 |

---

## Slide 1 — i-DREAMS Dataset: Data nature

- **52,770 แถว** · **52 วัน** (134 คัน-วัน) · **652 trips** · 10 คนขับ · 8 คัน (รถบรรทุก)
- **ไม่มี event ติดป้ายมาให้** · **1 แถว = 1 นาที** ไม่ใช่ 1 event → event เราต้องสร้างเองจาก level
- `*_level_N_sum` = จำนวน**วินาที**ในนาทีนั้นที่อยู่ระดับ N (รวมกันได้ 60 ต่อแถว) · Level 0–3 = ระดับเตือนที่ i-DREAMS คำนวณให้
- **ไม่มีข้อมูลเรื่อง:** มือถือ · หาว · หลับตา · มองนอกถนน · STZ label · `Phase` · อายุ/เพศ
- Zenodo **v1.0 (28 ก.พ. 2023)** · CC BY 4.0 → ใช้เป็น **mock data**

> 🎤 **โน้ตผู้พูด**
> - รถวิ่งจริง (ความเร็ว > 5 km/h) 42,869 นาที = 81% ของทั้งหมด ≈ 714 ชม.
> - 85 คอลัมน์ที่ใช้ได้ (ตัดคอลัมน์ว่าง 50) · ข้อมูลกระจาย 5 เดือน (ก.ย.–ต.ค. 2021 และ มี.ค.–พ.ค. 2022)
> - ช่อง event ใส่ 0 เพราะข้อมูลไม่มี label · POC ของเราสร้างเองได้ 94,066 — แก้เป็นตัวเลขอื่นได้

## Slide 2 — Deliverable

- **Deliverable (D)** = เอกสารส่งมอบของโครงการ EU · **D{WP}.{ลำดับ}** (D3.6 = ฉบับที่ 6 ของ WP3) · **ไม่ใช่เวอร์ชันของ dataset**
- โครงการมี 37 ฉบับ · ฉบับที่เราใช้:

| Number | Explain | Link |
|---|---|---|
| **D3.6** | threshold ของ Headway / Speeding / Fatigue (**ค่าสุดท้าย**) | [PDF](https://idreamsproject.eu/wp/wp-content/uploads/2022/09/iDREAMS_814761_D3.6_31082021_final.pdf) |
| **D6.1** | data dictionary (Table 2) — ชื่อตรงกับคอลัมน์ใน sample | [CORDIS](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb2f9dfc&appId=PPGMS) |
| **D6.3** | data dictionary + นิยาม level (Normal / Dangerous / Avoidable) | [CORDIS](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb4d7263&appId=PPGMS) |
| **D3.2** | ตัวแปรและเกณฑ์ที่ *เสนอ* จากวรรณกรรม (ก่อน D3.6) | [CORDIS](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5ceb0b2be&appId=PPGMS) *(ยังไม่ยืนยันว่าเป็น D3.2)* |
| **D2.1** | state of the art — วิธีวัดสภาพคนขับ | [PDF](https://documentserver.uhasselt.be/bitstream/1942/32592/1/iDREAMS_814761_D2.1_28022020_Final%20%281%29.pdf) |
| **D7.2** | ผลรถบรรทุกเบลเยียม (หลักยึดตรวจความสมเหตุสมผล) | [CORDIS](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb197147&appId=PPGMS) |
| **D4.2** | อัลกอริทึม STZ จริง | 🔒 Confidential (ไม่มีลิงก์) |

- ฉบับหลังมักปรับค่าของฉบับก่อน → ตัวเลขจึงไม่ตรงกันเสมอ · เรายึด **D3.6** (ฉบับสุดท้าย)
- ตัวอย่าง Fatigue: D2.1 ดูทั้งเวลาขับและอาการ (กะพริบตา, PERCLOS) → D3.2 เสนอเวลาขับ **8 ชม.** → D3.6 ปรับเป็น **4.5 ชม.** (คนขับอาชีพ · ขับ < 2 ชม. = ปกติ)

> 🎤 **โน้ตผู้พูด**
> - เลข D เรียงตาม Work Package ไม่ใช่ v1 → v2 ของเอกสารเดียว
> - ลิงก์ D6.1, D6.3, D3.2, D7.2 เป็นลิงก์ CORDIS ยังไม่ได้เปิดเช็กวันนี้ · D3.2 ยังไม่ยืนยันว่าเป็นฉบับนี้
> - ตัวอย่าง D2.1 มาจากสไลด์ของทีมผู้เขียน ยังไม่ได้ยืนยันในตัวเอกสาร

## Slide 3 — การใช้กับของรุ่นพี่: G7 vs i-DREAMS

- ข้อมูล G7 เดิมของรุ่นพี่เอามาใช้ไม่ได้ → ใช้ i-DREAMS เป็นข้อมูลจำลอง (mock) · เรา **ไม่ retrain** โมเดลของรุ่นพี่

| | G7 | i-DREAMS |
|---|---|---|
| หน่วย | event นับครั้ง | วินาทีใน level ต่อนาที |
| สัญญาณ | กล้อง AI คนขับ+ถนน | ADAS + GPS + ความเร่ง + เวลาขับ |
| สภาพคนขับ | มี | **ไม่มี** |

**5 feature ของรุ่นพี่:** ข้อมูลเรามีให้ **ตรงๆ 1** · **ทางอ้อม 2** · **สร้างเองโดยอิงสัญญาณจริง 2** · และเพิ่มอีก 2 field นอก G7

| กลุ่ม | Feature / Field | ที่มาในข้อมูลเรา | ป้าย | สไลด์ |
|---|---|---|---|---|
| **1 ตรง** | tailgating | Headway L3 + ≥ 50 km/h | `direct` (ตรง) | 5 |
| **2 อ้อม** | yawn | ระดับ Fatigue → สุ่ม | `derived-weak` (อ้อม) | 4 |
| | eye_close | ระดับ Fatigue → สุ่ม | `derived-weak` (อ้อม) | 4 |
| **2 อิงอ่อน** | phone | สุ่ม ผูก LDW + headway L2–3 | `synthetic-anchored` (อิงสัญญาณ) | 6 |
| | eye_off_road | สุ่ม ผูก LDW + headway L2–3 | `synthetic-anchored` (อิงสัญญาณ) | 6 |
| **เพิ่ม 2 field นอก G7** (ใช้ใน chatbot + scoring layer) | Speeding | `Speeding_Map_level` | `proxy` (ตัวแทน) | 7 |
| | Harsh events | `DEM_evt_{ ha, hb, hc }_lvl_*` | `proxy` (ตัวแทน) | 8 |

> 🎤 **โน้ตผู้พูด**
> - ยังไม่ได้ทดสอบกับระบบรุ่นพี่จริง ใช้ emulator ที่สร้างจากสไลด์ของรุ่นพี่
> - "อ้อม" และ "อิงอ่อน" ยังไม่ได้ validate → ห้ามอ้างความแม่นยำของโมเดล

## Slide 4 — Field: Fatigue

**คืออะไร:** i-DREAMS มีระบบเตือน "ความเหนื่อยล้า" ที่ดู **เวลาที่ขับมาแล้ว** (ไม่ได้ตรวจหน้า/ตาคนขับ) แล้วบันทึกเป็น **ระดับเตือน 0–3** ทุกวินาที

**Column:** `iDreams_Fatigue_Map_level_{ 0, 1, 2, 3 }_sum` (วินาทีในแต่ละระดับเตือน) · `grpby_seconds` (เวลาตั้งแต่เริ่ม trip)

| Level | Threshold | Explain | Ref |
|---|---|---|---|
| **L0** | ขับ < 2 ชม. | ยังไม่เตือน = **ปกติ (Normal)** | [D6.3](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb4d7263&appId=PPGMS) Table 2 (นิยาม level) · [D3.6](https://idreamsproject.eu/wp/wp-content/uploads/2022/09/iDREAMS_814761_D3.6_31082021_final.pdf) Table 6 (< 2 ชม.) |
| **L1** | ไม่เปิดเผย | เตือนด้วยภาพ · **Dangerous** | [D6.3](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb4d7263&appId=PPGMS) Table 2 · ตัวเลขถูกตัดจาก [D3.6](https://idreamsproject.eu/wp/wp-content/uploads/2022/09/iDREAMS_814761_D3.6_31082021_final.pdf) |
| **L2** | ไม่เปิดเผย | เตือนภาพ + เสียง · **Dangerous** | เหมือน L1 |
| **L3** | ไม่เปิดเผย | เตือนถี่ · **Dangerous** (Fatigue ไม่มีระดับ Avoidable) | เหมือน L1 |

- เพดานคนขับอาชีพ = **4.5 ชม.** · เส้นปรับตามอายุ/เพศ (ไม่มีในข้อมูลเรา) — [D3.6](https://idreamsproject.eu/wp/wp-content/uploads/2022/09/iDREAMS_814761_D3.6_31082021_final.pdf) §2.4.4 · ([D3.2](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5ceb0b2be&appId=PPGMS) เคยเสนอ 8 ชม.)
- "วัดจากเวลาขับ": ระบุใน [D3.6](https://idreamsproject.eu/wp/wp-content/uploads/2022/09/iDREAMS_814761_D3.6_31082021_final.pdf) · [D6.3](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb4d7263&appId=PPGMS) บอกแค่นิยาม level ไม่บอกวิธีคำนวณ

**Data nature**
- **99.4%** ของแถว (นาที) อยู่ระดับเดียวทั้งนาที เช่น L1 = 60 วินาที ส่วนอีก 3 ระดับ = 0 → ระดับเตือนไม่เปลี่ยนตลอดนาที
- อีก **0.6%** (304 แถว) ระดับเตือนเปลี่ยนกลางนาที จึงมี 2 คอลัมน์ที่ไม่เป็น 0 เช่น L0 = 4 และ L1 = 56 (4 วินาทีแรกยังไม่เตือน แล้วเปลี่ยนเป็นเตือนภาพ) · ไม่พบแถวที่เปลี่ยนถึง 3 ระดับในนาทีเดียว
- ช่วง 1.5 ชม.แรกของ trip: ส่วนใหญ่ยังไม่เตือน (L0 = **93–95%** ของเวลา)
- ขับเกิน 4 ชม.: L0 เหลือ **17%** ส่วน **69%** เป็น L2 → ยิ่งขับนาน ระดับเตือนยิ่งสูง

**เอาไปใช้:** ข้อมูลไม่มีการหาว/หลับตา → **สร้าง event หาว/หลับตาเอง** โดยให้ระดับเตือน Fatigue เป็นตัวกำหนดว่าจะเกิดถี่แค่ไหน

- **L0** = หาว/หลับตา 0.2 ครั้ง/ชม. (~ 1 ครั้งใน 5 ชม.)
- **L1** = 1 ครั้ง/ชม. (~ ชม.ละครั้ง)
- **L2** = 3 ครั้ง/ชม. (~ ทุก 20 นาที)
- **L3** = 30 ครั้ง/ชม. (~ ทุก 2 นาที)
- อัตราเหล่านี้เป็นค่า *สมมติ* ปรับได้
- ทำทุกนาทีที่รถวิ่ง ตามระดับของนาทีนั้น → รวมเฉลี่ย ≈ **5.8 ครั้ง ต่อรถ 1 คัน ต่อ 1 วัน** (คัน-วัน)
- ใช้เป็นข้อมูลเข้าให้ G7 เท่านั้น · ป้าย `derived-weak` (อ้อม)

> 🎤 **โน้ตผู้พูด**
> - ช่วงเวลา: 0–0.5 ชม. L0 = 94.9% · 1–1.5 ชม. = 92.8% · 1.5–2 ชม. = 58.6% · เกิน 4 ชม. L0 = 16.6%, L2 = 69.0%
> - วิธีคิด %: เอาวินาทีของระดับนั้นรวมทุกแถวในช่วง หารด้วยวินาทีทั้งหมดของช่วง
> - ตัวอย่างแถวที่ระดับเปลี่ยนกลางนาที: ที่ 7,200 วินาที (ครบ 2 ชม.พอดี) L0 = 4 วิ, L1 = 56 วิ
> - มี trip เดียวที่ระดับสลับแปลก (L0 1 วิ, L3 59 วิ) ยังไม่รู้สาเหตุ ถ้าถูกถามให้บอกตรงๆ
> - บอทห้ามพูดว่า "ตรวจพบการหาว" ให้พูดว่า "ประเมินจากระยะเวลาขับ"

## Slide 5 — Field: Headway → Tailgating

**คืออะไร:** Headway = ระยะห่างจากรถคันหน้า วัดเป็น**วินาที** (อีกกี่วินาทีรถเราจะถึงจุดที่คันหน้าอยู่ตอนนี้) · ที่ 60 km/h ห่าง 1 วินาที ≈ 16.7 เมตร

**Column:** `iDreams_Headway_Map_level_{ -1, 0, 1, 2, 3 }_sum` · `ME_Car_speed_mean` (ใช้เช็ก ≥ 50 km/h) · `ME_AWS_hw_measurement_mean` (headway เป็นวินาที ใช้ตรวจเท่านั้น)

| Level | Threshold | Explain | Ref |
|---|---|---|---|
| **L−1** | ไม่พบรถคันหน้า | **Normal** | [D6.1](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb2f9dfc&appId=PPGMS) / [D6.3](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb4d7263&appId=PPGMS) Table 2 |
| **L0** | ห่าง ≥ 2.5 วิ | **Normal** | [D6.3](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb4d7263&appId=PPGMS) Table 2 |
| **L1** | ห่าง < 2.5 วิ แต่ยังไม่ถึงเส้นเตือน | **Normal** · เริ่มใกล้ | [D6.3](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb4d7263&appId=PPGMS) Table 2 |
| **L2** | ข้ามเส้น 1: ห่าง 2.2–1.0 วิ *(ขยับตามความเร็ว อากาศ ฯลฯ)* | **Dangerous** · เตือนขั้นแรก | [D6.3](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb4d7263&appId=PPGMS) Table 2 (level) · [D3.6](https://idreamsproject.eu/wp/wp-content/uploads/2022/09/iDREAMS_814761_D3.6_31082021_final.pdf) Table 3 §2.4.1 (ตัวเลข) |
| **L3** | ข้ามเส้น 2: ห่าง 1.2–0.6 วิ | **Avoidable** · เตือนขั้นสอง | เหมือน L2 |

- [D3.2](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5ceb0b2be&appId=PPGMS) เสนอ Avoidable < 1.26 วิ แต่ [D3.6](https://idreamsproject.eu/wp/wp-content/uploads/2022/09/iDREAMS_814761_D3.6_31082021_final.pdf) แคบกว่า → ใช้ [D3.6](https://idreamsproject.eu/wp/wp-content/uploads/2022/09/iDREAMS_814761_D3.6_31082021_final.pdf)

**Data nature**
- **61%** ของแถว (นาที) อยู่ระดับเดียวทั้งนาที เช่น L−1 = 60 วินาที ส่วนระดับอื่น = 0 · อีก 39% เปลี่ยนระดับระหว่างนาที
- ตอนรถวิ่ง: **66%** ของเวลาไม่พบรถคันหน้า (L−1) · L0 16% · L1 12% · L2 5% · **L3 แค่ 0.5%**
- มีตัวเลขระยะห่างจริง (วินาที) แค่ราว **5%** ของแถว · ที่เหลือไม่มีรถคันหน้า จึงไม่มีค่า
- ระยะห่างกลาง (มัธยฐาน เฉพาะแถวที่มีค่าจริง): L1 1.70 · L2 1.09 · L3 0.67 วิ (อยู่ในช่วงของ [D3.6](https://idreamsproject.eu/wp/wp-content/uploads/2022/09/iDREAMS_814761_D3.6_31082021_final.pdf))

**เอาไปใช้ → tailgating (ขับตามชิด)**
- **กฎ:** นาทีที่ **L3 > 0** และความเร็ว **≥ 50 km/h** → นับ 1 event (นาทีติดกันรวมเป็น 1)
- ป้าย `direct` ที่สุด · เกณฑ์ ≥ 50 km/h และห่าง ≤ 20 ม. เป็นของ G7 / SCGJWD (รุ่นพี่)
- **เช็กกับรุ่นพี่:** แถวที่ L3 เป็นระดับหลักของนาที (มีวินาทีมากสุด) และมีค่าระยะจริง (60 แถว) มี **88%** ที่ห่าง ≤ 20 ม. แบบรุ่นพี่ · อีก 12% ห่างกว่านั้น ซึ่งยังรับได้ · ระยะห่างกลาง ≈ 14.9 ม.
- **ผลที่ได้:** ≈ **8.2 ครั้ง/คัน-วัน** · เกิดใน ≈ **3.4%** ของนาทีที่รถวิ่ง

> 🎤 **โน้ตผู้พูด**
> - แถวที่ขับ ≥ 50 km/h มี 30,090 แถว แต่ที่ L3 เด่นมีแค่ 110 แถว
> - ถ้านับทุกนาทีที่ L3 > 0 (กฎจริงของเรา) จะมี ≈ 51% ที่ห่าง ≤ 20 ม. เพราะหลายนาทีมี L3 แค่ไม่กี่วินาที · 88% คือเฉพาะนาทีที่ L3 เป็นหลัก
> - คนขับใน sample ขับชิดบ่อย เราไม่ปรับพารามิเตอร์ให้ผลดูดี
> - D3.2 เสนอ Avoidable < 1.26 วิ แต่ใช้ D3.6 เพราะเป็นค่าสุดท้าย

## Slide 6 — Field: Phone + Eyes-off-road

**ไม่มีสัญญาณในข้อมูล** (ไม่มีคอลัมน์มือถือ ไม่มี gaze/head pose) แต่เป็น 2 ใน 5 feature ของรุ่นพี่ → **สร้างเอง แต่ผูกกับสัญญาณจริง** (`synthetic-anchored` = อิงสัญญาณ)

**Column:** ไม่มีคอลัมน์ phone / eyes-off-road โดยตรง · จุดยึดที่ใช้: `ME_LDW_Map_type_{ L, R }_mean` (เฉพาะรถคันอื่น) · `iDreams_Headway_Map_level_{ 2, 3 }_sum`

| | **Phone** | **Eyes-off-road** |
|---|---|---|
| **Level** | ไม่มี level | ไม่มี level |
| **อัตราเกิด (ครั้ง/ชม.)** *สมมติ* | ปกติ **0.05**<br>มี LDW **0.45** (คูณ 9)<br>headway L2–3 **0.15** (คูณ 3)<br>มีทั้งคู่ **0.55** (คูณ 11) | ปกติ **0.3**<br>มี LDW **1.5** (คูณ 5)<br>headway L2–3 **1.2** (คูณ 4)<br>มีทั้งคู่ **2.4** (คูณ 8) |
| **เฉลี่ยทั้งหมด** | ≈ 0.4 ครั้ง/คัน-วัน | ≈ 2.6 ครั้ง/คัน-วัน |
| **Ref** (เหตุผลที่ผูก) | [D3.2](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5ceb0b2be&appId=PPGMS) Table 15 (หน้า 99) ผูก "เสียสมาธิ" กับ LDW | [D3.6](https://idreamsproject.eu/wp/wp-content/uploads/2022/09/iDREAMS_814761_D3.6_31082021_final.pdf) §2.4 ใช้ distraction ปรับเกณฑ์ headway |

**Data nature**
- ไม่มีคอลัมน์ phone / eyes-off-road ในข้อมูลเลย
- **LDW** (เตือนออกนอกเลน) ฝั่งขวามีค่า 10,828 แถว แต่ 10,569 แถวมาจากรถ **คันเดียว** ที่เตือนถึง 84% ของเวลา → น่าจะเป็นอาการของอุปกรณ์คันนั้น ไม่ใช่พฤติกรรมคนขับ จึงไม่ใช้รถคันนั้น
- ตัดรถคันนั้นออกแล้ว LDW เหลือ ≈ 181 นาที (**0.4%** ของนาทีที่รถวิ่ง)
- headway L2–L3 พบ ≈ **21%** ของนาทีที่รถวิ่ง → ใช้เป็นจุดยึดหลัก

**เอาไปใช้ → phone + eyes-off-road (สร้างเอง)**
- **กฎ:** ทุกนาทีที่รถวิ่ง (> 5 km/h) สุ่มว่าเกิด event ไหม ตามอัตราในตาราง · นาทีที่เสี่ยงกว่า (LDW หรือ headway L2–3) เกิดถี่ขึ้น
- LDW มีน้อยมาก (0.4%) → ตัวที่ดึงให้ event กระจุกคือ headway L2–3 ส่วน LDW เป็นแค่ส่วนเสริม
- **ทำไมเลือกค่าคูณนี้:** อัตราและตัวคูณเป็นค่าสมมติของเรา (ไม่มีเอกสารให้ตัวเลข) · ลองตัวคูณ 4 ชุด (ไม่มี / อ่อน / กลาง / แรง) แล้วเลือก **กลาง** เพราะ event ตกในนาทีที่มีสัญญาณราวครึ่งหนึ่ง (Phone ≈ 46% · Eyes-off-road ≈ 52%) · ทุกชุดได้สัดส่วนกองรถเท่ากัน จึงไม่ได้เลือกเพื่อให้ผลดูดี
- **ผลที่ได้:** Phone ≈ **0.4 ครั้ง/คัน-วัน** · Eyes-off-road ≈ **2.6 ครั้ง/คัน-วัน**

> 🎤 **โน้ตผู้พูด**
> - ตัวคูณ = 1 + น้ำหนัก เช่น Phone: มี LDW คูณ 9 (1+8) · มี headway L2–3 คูณ 3 (1+2) · มีทั้งคู่คูณ 11
> - เอกสาร i-DREAMS ไม่ได้ให้สูตรนี้ เราตั้งเอง
> - ถ้ากรรมการถามว่าตรวจมือถือได้ไหม: ตอบว่า sample ไม่มีคอลัมน์นี้ event ที่เห็นเราสร้างเอง ระบบจริงใช้ G7

## Slide 7 — Extra field: Speeding

**คืออะไร:** i-DREAMS เตือนเมื่อขับเร็วเกิน **ป้ายจำกัดความเร็วของถนนช่วงนั้น** แบ่งเป็นระดับ 0–3 ทุกวินาที (วัดเทียบ limit ของถนน ไม่ใช่ดูความเร็วตรงๆ)

**"เกินเส้น" คืออะไร:** ระบบไม่เตือนทันทีที่เกิน limit แต่เผื่อไว้นิดหน่อย **เส้น = ความเร็วที่ระบบเริ่มขยับไประดับเตือนถัดไป** = limit × ตัวคูณ (คูณ 1.10 = เกิน limit 10%)
- ตัวอย่าง limit 80 km/h → เส้น 1 อยู่ที่ ≈ 82.6–88 km/h · เส้น 2 อยู่ที่ ≈ 83.8–92 km/h
- ตัวคูณเป็นช่วง เพราะเส้นขยับตามสภาพ เช่น อากาศ ความเหนื่อย ช่วงเวลา — [D3.6](https://idreamsproject.eu/wp/wp-content/uploads/2022/09/iDREAMS_814761_D3.6_31082021_final.pdf) §2.4.3

**Column:** `iDreams_Speeding_Map_level_{ 0, 1, 2, 3 }_sum` · `ME_AWS_tsr_level_mean` (ขับเกินป้ายไปเท่าไร 0 ไม่เกิน → 7 เกิน 30+ หน่วย) · `ME_Car_speed_mean`, `GPS_spd_mean` (ความเร็ว)

| Level | Threshold | Explain | Ref |
|---|---|---|---|
| **L0** | ไม่เกินเส้น 1 | ไม่เตือน · Normal · ไม่นับเป็นความเสี่ยง | [D6.3](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb4d7263&appId=PPGMS) Table 2 |
| **L1** | ใกล้ถึงเส้น 1 | สัญญาณภาพ · Normal · ไม่นับ (น้ำหนัก ×0) | [D6.3](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb4d7263&appId=PPGMS) Table 2 |
| **L2** | เกินเส้น 1 (เกิน limit 3.25–10%) | เตือนภาพ · **Dangerous** · 1 วินาทีนับเป็น 3 (น้ำหนัก ×3) | [D6.3](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb4d7263&appId=PPGMS) Table 2 (level) · [D3.6](https://idreamsproject.eu/wp/wp-content/uploads/2022/09/iDREAMS_814761_D3.6_31082021_final.pdf) Table 5 §2.4.3 (ตัวเลข) |
| **L3** | เกินเส้น 2 (เกิน limit 4.75–15%) | ภาพ+เสียง · **Avoidable** · 1 วินาทีนับเป็น 10 (น้ำหนัก ×10) | เหมือน L2 |

**Data nature**
- **78%** ของแถว (นาที) อยู่ระดับเดียวทั้งนาที เช่น L0 = 60 วินาที ส่วนระดับอื่น = 0
- ตอนรถวิ่ง: L0 56% · L1 33% · L2 5% · L3 6% → เตือนจริง (L2 + L3) ≈ **11%** ของเวลา
- **ไม่มี speed limit ของถนน**ในข้อมูล → คำนวณ level เองย้อนหลังไม่ได้ ต้องใช้ level ที่ i-DREAMS ให้มา

**เอาไปใช้**
- **ใช้ทำอะไร:** เป็นส่วนหนึ่งของ risk score ใน chatbot · ไม่ส่งให้ G7 · ป้าย `proxy` (ตัวแทน)
- **วิธีนับ:** แต่ละแถว (1 นาที) ดูว่าอยู่ L2 กี่วินาที L3 กี่วินาที → L2 × 3 + L3 × 10 แล้วรวมทุกนาทีของ trip (น้ำหนักเราตั้งเอง ไม่ใช่ของ i-DREAMS)
  - ตัวอย่าง: นาทีที่ L2 = 20 วิ, L3 = 5 วิ → 20 × 3 + 5 × 10 = 110
- **ผลที่ได้:** speeding ≈ **20.8%** ของ penalty ทั้งหมด
- **เทียบของจริง:** รถบรรทุกเบลเยียมใน [D7.2](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb197147&appId=PPGMS) มี speeding ≈ 4 ครั้ง/100 กม.

> 🎤 **โน้ตผู้พูด**
> - ความเร็วเฉลี่ยตามระดับ: L0 45.7 · L1 60.4 · L2 83.2 · L3 78.0 km/h
> - L3 ต่ำกว่า L2 เพราะวัดเทียบ limit ของถนน ไม่ใช่ความเร็วตรงๆ
> - น้ำหนัก ×0 / ×3 / ×10 เราตั้งเอง ไม่ใช่ของ i-DREAMS

## Slide 8 — Extra field: Harsh events

**คืออะไร:** ตัวนับ "การขับรุนแรง" จากเซนเซอร์ความเร่งของรถ (IMU ใน Gateway — [D6.1](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb2f9dfc&appId=PPGMS) Table 2) มี 3 แบบ: `ha` **เร่งแรง** · `hb` **เบรกแรง** · `hc` **เข้าโค้งแรง** · แต่ละแบบมี 3 ความรุนแรง และค่าเป็น **วินาที** ในนาทีนั้น ไม่ใช่จำนวนครั้ง

**Column:** `DEM_evt_{ ha, hb, hc }_lvl_{ L, M, H }_sum` (รวม 9 คอลัมน์)

| Level        | Threshold              | Explain                                          | Ref                                                                                                                                                                                                                                                                         |
| ------------ | ---------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **L** (ต่ำ)  | โครงการไม่เปิดเผยค่า g | ความรุนแรงต่ำ · 1 วินาทีนับเป็น 1 (น้ำหนัก ×1)   | [D6.1](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb2f9dfc&appId=PPGMS) / [D6.3](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5fb4d7263&appId=PPGMS) Table 2 (ธง H/M/L ไม่มีเกณฑ์ g) |
| **M** (กลาง) | ไม่เปิดเผย             | ความรุนแรงกลาง · 1 วินาทีนับเป็น 3 (น้ำหนัก ×3)  | เหมือน L                                                                                                                                                                                                                                                                    |
| **H** (สูง)  | ไม่เปิดเผย             | ความรุนแรงสูง · 1 วินาทีนับเป็น 10 (น้ำหนัก ×10) | เหมือน L                                                                                                                                                                                                                                                                    |

- **ค่า g ที่พอมีอ้างอิง:** [D3.2](https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5ceb0b2be&appId=PPGMS) เสนอสำหรับรถบรรทุก (เร่ง/เบรก): ปกติ < **0.25 g** · Dangerous 0.25–0.3 g · Avoidable > **0.3 g** → เป็นแหล่งเดียวที่มี แต่ **ไม่ใช่เกณฑ์จริงของ i-DREAMS** และไม่รวมเข้าโค้ง

**Data nature**
- ค่าทั้ง 9 คอลัมน์เป็นวินาที รวมกันต่อแถวไม่เกิน 60
- **95%** ของแถว (นาที) มีการขับรุนแรงอย่างน้อย 1 แบบ → เกิดบ่อยมาก
- ระดับต่ำ (L) เจอบ่อยสุด: เข้าโค้ง **55%** · เบรก **31%** · เร่ง **19%** ของแถว
- ระดับสูง (H) เจอน้อยมาก: **0.4–1.3%** ของแถว
- เบรก (`hb`) ตรวจแล้วเป็นเบรกจริง (ความเร็วลด 6.6–7.6 km/h) · เร่ง (`ha`) ยืนยันไม่ได้

**เอาไปใช้**
- **ใช้ทำอะไร:** เป็นส่วนหนึ่งของ risk score ใน chatbot · ไม่ส่งให้ G7 · ป้าย `proxy` (ตัวแทน)
- **วิธีนับ:** แต่ละแถว (1 นาที) ดูว่าอยู่ L / M / H กี่วินาที → L × 1 + M × 3 + H × 10 แล้วรวมทุกนาทีของ trip (น้ำหนักเราตั้งเอง) · นับเป็น "ครั้ง" แบบ episode: เหตุการณ์ที่ห่างกัน ≤ 90 วินาทีรวมเป็น 1 ครั้ง
- **ผลที่ได้:** harsh รวม ≈ **50.7%** ของ penalty (เข้าโค้ง 33.2 · เร่ง 8.8 · เบรก 8.7)

> 🎤 **โน้ตผู้พูด**
> - ชื่อ ha / hb / hc ใน Data Description สลับกับตำแหน่งจริง ให้เชื่อชื่อคอลัมน์
> - ยังไม่ตัดสิน: ระดับต่ำของ cornering เกิดบ่อยมาก (55% ของแถว) จะนับ ×1 ไหม

## Slide 9 — สรุป + Limitations + Next step

| Field | ใช้ทำอะไร | ป้าย |
|---|---|---|
| Headway | tailgating | `direct` (ตรง) |
| Fatigue | yawn / eye_close | `derived-weak` (อ้อม) |
| Phone, Eyes-off-road | สร้างเอง ผูก headway/LDW | `synthetic-anchored` (อิงสัญญาณ) |
| Speeding, Harsh | risk score (นอก G7) | `proxy` (ตัวแทน) |
| IBI, FCW/PCW, Overtaking | ไม่ใช้ | – |

**Limitations**
- ข้อมูล mock จากยุโรป
- ตรงกับ G7 แค่ 1 จาก 5 feature (อ้อม 2 · อิงสัญญาณ 2) → อ้างความแม่นยำของโมเดลไม่ได้
- Fatigue วัดจากเวลาขับ ไม่ใช่อาการของคนขับ
- **ยังไม่ได้ทดสอบกับระบบรุ่นพี่จริง**
- ไม่รู้เกณฑ์ harsh และสูตร STZ (D4.2)

**พิสูจน์ได้:** pipeline real-time · tool calling ของ chatbot · วิธี scoring

**Next step → Mapper function:** อ่านข้อมูลรายนาที → สร้าง event แบบ G7 5 ชนิด (ติดป้ายที่มาทุก event · seed ต่อ trip รันซ้ำได้) แล้วค่อยคำนวณ label / K ใหม่

> 🎤 **โน้ตผู้พูด**
> - สเปกละเอียดอยู่ใน [[18-field-deep-dive]] §2 และบรีฟส่งต่อ [[19-handoff-mapper-weights]]
> - event ที่สร้างมาจากกฎที่เราเขียน ผลของ scoring และ chatbot จึงขึ้นกับกฎนั้น ต้องบอกในรายงาน
