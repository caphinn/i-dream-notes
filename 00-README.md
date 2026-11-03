---
title: i-DREAMS ↔ G7 — knowledge base (Capstone)
updated: 2026-11-01
status: ตัดสินใจ D-01…D-24; POC แก้ WP1–WP4 แล้ว (smoke test 27/27 ผ่าน); ถัดไป = mapper function
---

# i-DREAMS ↔ G7 — knowledge base

## เริ่มอ่านที่ไหนดี

1. **ส่วนที่ 1 ของไฟล์นี้ (สรุป 1 หน้า)** — 5 นาที
2. **[[18-field-deep-dive]]** — ไฟล์อธิบายทีละ field ล่าสุดและละเอียดสุด (ภาพรวม i-DREAMS, i-DREAMS ↔ G7 ทั้ง 5 feature พร้อมสเปก mapper, Speeding/Harsh, สิ่งที่ต้องเปลี่ยน)
3. **[[15-decision-log]]** — ตัดสินใจอะไรไปแล้ว (D-01…D-24) และเรื่องที่ยังเปิด (R-xx)
4. **[[17-slide-content]]** — ข้อความสไลด์ 16 หน้าพร้อมวาง (สไลด์ 16 = การกระจายของค่าที่ map ได้ ใช้พรีอาจารย์)
5. ไฟล์อื่นเปิดดูเมื่อสงสัยหลักฐานของข้อใดข้อหนึ่ง (ตาราง "อ่านต่อที่ไหน" ด้านล่าง)

## 1. สรุปทั้งหมดใน 1 หน้า

**โจทย์:** ใช้ i-DREAMS (ข้อมูลขับรถบรรทุกจากยุโรป) เป็น *mock data* ให้ chatbot POC และ real-time pipeline ของ DBAS โดยไม่ retrain โมเดลรุ่นพี่ (G7 / SCGJWD) งานใหม่ปีนี้มี 2 อย่าง: **scoring layer** (Empirical Bayes) และ **admin chatbot** ย้อนดู event

**i-DREAMS คืออะไร (ตรวจกับข้อมูลจริงแล้ว)**
- Sample = 52,770 แถว, 652 trip, 10 คนขับ, 8 คัน; **1 แถว = 1 นาทีของ 1 trip** ไม่ใช่ 1 event
- คอลัมน์ `*_level_N_sum` และ `DEM_*_sum` = *วินาทีที่อยู่ในสถานะนั้น* (รวมได้ 60) ไม่ใช่จำนวนครั้ง
- Level ที่ i-DREAMS คำนวณให้แล้ว: Headway แปลตรงเป็น phase ของ Safety Tolerance Zone ส่วน Speeding / Overtaking / Fatigue เป็นระดับ warning ที่จัดเข้า phase (D6.1/D6.3 Table 2)
- ข้อมูลอยู่ใน 5 เดือนปฏิทิน (ก.ย.–ต.ค. 2021, มี.ค.–พ.ค. 2022) 52 วันที่ขับ, 134 คัน-วัน (เฉลี่ย 2.6 คัน/วัน)
- Zenodo sample = v1.0 (28 ก.พ. 2023) ส่วน D2.1/D3.6 คือเลข deliverable ของ Work Package ไม่ใช่เวอร์ชัน

**i-DREAMS ↔ G7 ต่างกันกว่าที่คิด**
- i-DREAMS วัด *พฤติกรรมการขับ* (headway, speed, braking, เวลาขับ) ส่วน G7 วัด *สภาพคนขับ* (หาว, หลับตา, มือถือ, มองนอกถนน)
- จาก 5 feature ของโมเดลรุ่นพี่: **tailgating = ตรง (ผ่าน Headway L3 ที่ ≥ 50 km/h)**, **หาว/หลับตา = อ้อม (ผ่าน Fatigue)**, **phone และ eye_off_road = ไม่มีสัญญาณ ต้อง synthetic** → สัดส่วน **1 ตรง / 2 อ้อม / 2 mock**
- **Fatigue_Map วัดจากเวลาขับ ไม่ใช่การตรวจอาการ** อาจารย์ให้คงชื่อ Fatigue และเชื่อมกับหาว/หลับตาในระดับแนวคิด แต่ต้องเปิดเผยว่าเป็นค่าประมาณ
- ตัด IBI (0 ใน 99.3% ของแถว), FCW (18 แถว), LDW (เป็นผลของรถคันเดียว) ออกจาก mapper

**สิ่งที่ตัดสินแล้ว (D-01…D-24) แบบสั้น**
1. Fatigue_Map ใช้กับ G7 factor เท่านั้น (ไม่นับซ้ำกับ Fatigue factor)
2. หาว/หลับตา = event สุ่มตามระดับ Fatigue (Poisson, seed คงที่) ติดป้าย derived-weak
3. **ไม่ใช้ XGBoost บน mock** — ใช้ **Real-time risk engine แบบ rule-based + EMA** (Track 1: กฎ HIGH หน้าต่าง 2 นาที; Track 2: กฎ MEDIUM หน้าต่าง 60 นาที ประเมินทุก 5 นาที) ออกแบบให้เสียบ XGBoost ได้ภายหลัง
4. tailgating ตามนิยาม SCGJWD ตรงๆ → mock fleet ≈ LOW 22 / MEDIUM 71 / HIGH 7 (% คัน-วัน) คนขับใน sample ขับชิดบ่อย (หลังเปิด phone/eye_off_road ตาม D-21 ≈ LOW 18 / MEDIUM 75 / HIGH 7) ต้องบอกในรายงาน
5. K ใน scoring layer ประมาณจาก mock: K medium ≈ 4 วัน, K high ≈ 43 วัน; เกณฑ์ติดอันดับใช้ K medium
6. phone / eye_off_road เปิดแบบสร้างอิงข้อมูลจริงอ่อนๆ ผูก LDW + headway ระดับ 2–3 (D-21); **ติดป้าย provenance ทุก event** และตัวอย่างหลักใช้ tailgating
7. ไม่ขอชุดเต็ม (อาจารย์ไม่อนุญาต) และไม่ขอโค้ดรุ่นพี่ → สร้าง emulator จากสไลด์ (4 ฟิลด์ G7) เข้า Kafka ของเราเอง → **ยังไม่ได้ทดสอบกับระบบรุ่นพี่จริง** ต้องเขียนใน proposal
8. Canva deck: ไม่แก้ใน Canva ทำเป็นรายการแก้ markdown ให้ทีมแก้เอง
9. ระดับ 1 ของ Headway / Speeding / Overtaking = ×0 และซ่อนจากรายการเหตุการณ์ ตามนิยาม i-DREAMS (D-22, D-23); Harsh ยังไม่ตัดสิน (R-10)

**สถานะการแก้ POC chatbot (1 พ.ย. 2026)**
- **ทำแล้ว (WP1–WP4):** harsh เป็นวินาทีและตัด ×5, ระดับ 1 = ×0 และซ่อนจาก event, ตัดค่า GPS ผิดปกติ, ปรับสเกลคะแนน (trip มัธยฐาน ≈ 50), เปลี่ยนชื่อ Fatigue เป็น "ความเหนื่อยล้า" พร้อมบอกว่าประเมินจากเวลาขับ, เพิ่ม FB-06 และ glossary, แถบแจ้งว่าเป็นข้อมูลสังเคราะห์
- **ผลที่วัดได้:** event 119,397 → 94,066; สัดส่วน penalty ของ cornering 52.4% → 33.2%; อันดับคนขับ 3 อันดับบนเป็นชุดเดิม (Spearman รายทริป 0.867); **smoke test ผ่าน 27/27** (รายงานเต็ม `work-space/chatbot-with-idream/reports/WP1_before_after.md`)
- **ยังไม่ได้ทำ:** mapper function และป้ายที่มาต่อ event, ย้ายมือถือ/มองนอกถนนออกจาก FB-06 (ตอนนี้ยังตอบ "ไม่มี"), WP5–WP8, แก้ Canva (ทีมทำเอง)

**ขั้นต่อไป (เรียงตามลำดับที่ผมแนะนำ)**
1. **เขียน mapper function** (ขับชิด หาว หลับตา มือถือ มองนอกถนน) ตามสเปกใน [[18-field-deep-dive]] → สร้างสตรีมเหตุการณ์แบบ G7 ที่มีป้ายที่มา (`direct` / `derived-weak` / `synthetic-anchored`) + เทสต์ + รายงานการกระจายเทียบกับสไลด์ 16
2. **ต่อ mapper เข้า chatbot:** ย้ายมือถือ/มองนอกถนนออกจาก FB-06, แสดงป้ายที่มาในคำตอบและหน้าจอ
3. **คำนวณ label รายวัน, λ̄ และ K ใหม่** (R-09) แล้วสร้าง Scoring API (D-16)
4. **Real-time risk engine** (D-17, D-18) และวัด POC หน้าต่าง 60 นาที (R-05)
5. **ทีมแก้ Canva** ตาม [[16-deck-patch-list]] (ข้อ B7 reference EMA ต้องตรวจก่อนใส่) และ [[17-slide-content]]
6. **ยังเปิดให้คุยก่อนลงมือ:** น้ำหนัก Fatigue (R-06), ใช้หลักยึด D7.2 ตรวจอัตราสุ่ม (R-08), น้ำหนักของ Harsh (R-10), overtaking ไม่มี event เลย → จะซ่อนหมวดนี้จากบอทหรือตอบอย่างไร, ทำให้เทสต์ "3/7 วันที่ผ่านมา" ไม่ตกเมื่อข้อมูลเก่า (ตั้ง `POC_NOW`)

## 2. อ่านต่อที่ไหน

| อยากรู้ | อ่าน |
|---|---|
| ข้อมูลมีอะไร / ใช้อะไรได้ | [[01-dataset-overview]], [[12-field-catalog]] |
| G7 ↔ i-DREAMS ตัวไหน map ได้ | [[02-g7-mapping]], [[09-g7-definitions-from-seniors]] |
| ทำไม Fatigue ไม่ใช่อาการง่วง | [[03-fatigue-finding]] |
| บั๊ก harsh ใน POC | [[04-harsh-events-poc-issue]], [[11-poc-fix-plan]] |
| จะเชื่อมกับระบบรุ่นพี่ยังไง | [[13-integration-with-seniors-system]] |
| ตัดสินใจอะไรไปแล้ว เพราะอะไร | [[15-decision-log]] |
| ต้องแก้อะไรใน deck | [[16-deck-patch-list]] (เหตุผลดู [[14-proposal-deck-review]]) |
| ลงลึกทีละ field (เริ่มตรงนี้ถ้าจะอ่านเรื่อง field) | [[18-field-deep-dive]] |
| เนื้อหาสไลด์ใหม่ พร้อมวาง | [[17-slide-content]] |
| เวอร์ชัน / ลิงก์อ้างอิง | [[05-zenodo-sample-version]], [[06-deliverables-catalog]], [[07-references]] |

## 3. ป้ายความมั่นใจที่ใช้ทั้งโฟลเดอร์

| ป้าย | ความหมาย |
|---|---|
| **[ตรวจแล้ว]** | รันกับข้อมูลจริงในแชต หรืออ่านจากเอกสารต้นทางโดยตรง |
| **[จาก note เดิม]** | มาจาก `data-sample/I-dream sample.md` หรือ `I-dream Index.md` ยังไม่ได้ตรวจซ้ำ |
| **[ยังไม่ยืนยัน]** | เป็นการตีความ/เดา ต้องเช็กก่อนใช้อ้างอิง |

## 4. ข้อสรุปรายข้อ (16 ข้อ พร้อมลิงก์ไฟล์ละเอียด)

1. **1 แถว = 1 นาทีของ 1 trip** ไม่ใช่ 1 event คอลัมน์ `*_level_N_sum` คือ *วินาทีที่อยู่ใน level นั้น* (รวมกันได้ 60 ต่อแถว) ไม่ใช่จำนวนครั้ง → [[01-dataset-overview]]
2. Level 0–3 ที่ i-DREAMS คำนวณมาให้แล้ว ไม่ใช่เซนเซอร์ดิบ: Headway แปลตรงเป็น phase ของ STZ (−1/0/1 Normal, 2 Danger, 3 Avoidable) ส่วน Speeding/Overtaking/Fatigue เป็น *ระดับ warning* ที่จัดเข้า phase (D6.3 Table 2 → [[06-deliverables-catalog]])
3. i-DREAMS ครอบคลุมเฉพาะ **พฤติกรรมการขับ** (headway, speed, braking, เวลาขับ) ส่วน **สภาพคนขับ** (phone, หาว, หลับตา, มองนอกถนน, บุหรี่) ไม่มีในไฟล์ → [[02-g7-mapping]]
4. **Fatigue_Map วัดจากเวลาขับ** ไม่ใช่อาการง่วง จึงไม่ map กับ G7_yawn / eyes_closed (เป็น proxy ของ continuous_work ได้) → [[03-fatigue-finding]]
5. **DEM (harsh) ก็เป็นวินาทีเช่นกัน** แต่ POC นับเป็นจำนวนครั้ง ×5 วินาที → penalty/risk_score น่าจะสูงเกินจริง → [[04-harsh-events-poc-issue]]
6. Zenodo sample = **v1.0 (28 ก.พ. 2023)** ไม่เกี่ยวกับ "ver 2.x/3.x" — D2.1/D3.6 คือเลข Deliverable ของ Work Package → [[05-zenodo-sample-version]], [[06-deliverables-catalog]]
7. ใน POC `risk_score`, ทะเบียนรถ และวันที่ เป็นข้อมูลที่เรา derive/สังเคราะห์ ไม่ได้มาจาก i-DREAMS → [[08-poc-implications-and-open-questions]]
8. โมเดล production ของรุ่นพี่ใช้ feature 5 ตัว (yawn, eye_close, phone, tailgating, eye_off_road) — i-DREAMS ครอบคลุมแค่ **1 ใน 5** (tailgating); G7 event 11 ชนิด ไม่มีนิยามของ `continuous_work`/`vehicle_fatigue` นอกจากชื่อ → [[09-g7-definitions-from-seniors]]
9. **STZ label** ทำซ้ำได้จากคอลัมน์ Headway level ที่มีอยู่ (Normal = -1/0/1, Dangerous = 2, Avoidable = 3) ตามเปเปอร์ Theodoraki 2026; ไม่ต้องรอ D4.2 → [[10-stz-labelling]]
10. ตัวเลข "กี่ครั้ง" ในคำตอบ bot มาจากจำนวน episode (ไม่ผิดหน่วย) — ที่ผิดคือ penalty/risk_score และฟิลด์ `occurrences` ของ harsh → แผนแก้ใน [[11-poc-fix-plan]]
11. อาจารย์ไม่อนุญาตให้ขอชุดเต็ม → ใช้ sample นี้เป็น mock data เพื่อแสดงระบบเท่านั้น
12. ฟิลด์ที่ใช้ได้เต็มที่มีน้อยกว่าที่คิด: แกนคือ Headway/Speeding/ความเร็ว/harsh brake + ตัวระบุ; `IBI` เป็น 0 ใน 99.3% ของแถว, FCW/PCW/high beam แทบไม่มีข้อมูล, `GPS_distances_sum` มีค่าผิดปกติ 126 แถว → [[12-field-catalog]]
13. **อาจารย์ (31 ต.ค.): fatigue = fatigue และเชื่อมกับหาว/หลับตาของ G7 ได้ในระดับแนวคิด** → คงชื่อ Fatigue ใน POC แต่ต้องบอกว่าวัดจากเวลาขับ (ไม่ใช่ตรวจอาการ); ผลวัด: หลังแก้ harsh แล้ว Fatigue จะมีน้ำหนัก ~20% ของ penalty → [[03-fatigue-finding]], [[11-poc-fix-plan]]
14. **Real-time ของรุ่นพี่เป็น rule-based; XGBoost เป็น batch รายวัน** — (ข้อเสนอเดิมเรื่องหน้าต่าง 24 ชม. ถูกแทนด้วย D-17: rule engine หน้าต่าง 2/60 นาที); สัดส่วนการแปลง G7 feature ที่ข้อมูลรองรับคือ 1 ตรง / 2 อ้อม / 2 mock; จุดเชื่อมคือ G7 emulator ที่ Kafka → [[13-integration-with-seniors-system]]
15. **Deck proposal (Canva) มีสถาปัตยกรรม, scoring layer (Empirical Bayes) และ POC Flink/Redis อยู่แล้ว** — ที่เสนอเรื่อง Kafka mapper และหน้าต่างเวลาตรงกับ deck; ประเด็นที่ตรวจพบ (Fatigue ใช้ซ้ำ, event 204/คัน/วัน, K เกินข้อมูล, IBI ใช้ไม่ได้) ตัดสินครบแล้ว → [[14-proposal-deck-review]], ตัดสินทีละข้อใน [[15-decision-log]]
16. **ตัดสินใจครบแล้ว (D-01…D-20)**: Fatigue_Map → G7 factor เท่านั้น; event หาว/หลับตาสุ่มตามระดับ; **ไม่ใช้ XGBoost บน mock** (rule engine: Track 1 หน้าต่าง 2 นาที, Track 2 หน้าต่าง 60 นาที + EMA); tailgating ตามนิยาม SCGJWD (mock fleet ≈ LOW 22 / MED 71 / HIGH 7); K จาก mock (เกณฑ์อันดับใช้ K medium); ตัด IBI/FCW/LDW; สัดส่วน 1/2/2; ติดป้าย provenance ทุกที่; ไม่ขอโค้ดรุ่นพี่ → ยังไม่ได้ทดสอบกับระบบจริง → [[15-decision-log]], [[16-deck-patch-list]]

## 5. ลำดับที่เจอ (เพื่อไล่ตามบริบทตอน discuss)

1. อ่าน Data Description + CSV + note เดิม + POC docs → เข้าใจโครงสร้างข้อมูล
2. เทียบ G7 ↔ i-DREAMS ชั้น note เดิม กับชั้น alert code ใน POC
3. อาจารย์ชี้ว่า Fatigue วัดจากระยะ/เวลา → ตรวจ D3.6 §2.4.4 และข้อมูลจริง → ยืนยัน
4. ตรวจ mapping ตัวอื่นกับข้อมูล → เจอปัญหาหน่วยของ harsh event ใน POC
5. ตรวจ version ของ Zenodo, D2.1/D3.6 และรวบรวม deliverable ทั้งหมด
6. ค้นนิยาม G7 ในเอกสารรุ่นพี่ → เจอลิสต์ event 11 ชนิดและ feature 5 ตัว
7. ตรวจ `ME_AWS_time_indicator_median` → เป็นการ coding ต่างจากเอกสาร (ไม่ใช่ข้อมูลหาย)
8. หาวิธี label STZ ทางเลือกจากเปเปอร์ และทำแผนแก้ POC

## 6. ไฟล์ในโฟลเดอร์

| ไฟล์ | เนื้อหา |
|---|---|
| [[01-dataset-overview]] | โครงสร้างข้อมูล, ความหมายคอลัมน์/level, คุณภาพข้อมูล |
| [[02-g7-mapping]] | ตารางเทียบ G7 ↔ i-DREAMS พร้อมหลักฐาน |
| [[03-fatigue-finding]] | Fatigue = เวลาขับ (หลักฐานจาก D3.6 + ข้อมูล) |
| [[04-harsh-events-poc-issue]] | DEM เป็นวินาที + ปัญหาใน POC |
| [[05-zenodo-sample-version]] | Zenodo v1.0 และชุดข้อมูลที่ตัวเลขต่างกัน |
| [[06-deliverables-catalog]] | D2.1, D3.6 และ deliverable อื่นทั้งหมด |
| [[07-references]] | ลิงก์อ้างอิงทั้งหมด (ตรวจแล้ว / จาก note) |
| [[08-poc-implications-and-open-questions]] | ผลต่อ POC และคำถามที่ต้อง discuss (อัปเดตสถานะคำตอบแล้ว) |
| [[09-g7-definitions-from-seniors]] | G7 event 11 ชนิด, feature 5 ตัว, ผลค้นหา continuous_work/vehicle_fatigue |
| [[10-stz-labelling]] | นิยาม STZ, label ที่ sample ใช้ได้, ทางเลือกแทน D4.2 |
| [[11-poc-fix-plan]] | แผนแก้ POC (WP1–WP8), ปัญหา P1–P9, การตัดสินใจ |
| [[12-field-catalog]] | ทุกคอลัมน์ (85) พร้อมคุณภาพ ✅/⚠/❌ และสิ่งที่ derive ได้ |
| [[13-integration-with-seniors-system]] | แผนเชื่อม i-DREAMS mock real-time เข้ากับระบบรุ่นพี่ (G7 emulator ที่ Kafka), scoring layer, chatbot |
| [[14-proposal-deck-review]] | สรุป Canva deck (scoring layer, ML real-time, chatbot) + ประเด็นที่ควรตรวจ 12 ข้อ |
| [[15-decision-log]] | รายการตัดสินใจ D-01…D-20 (Q-01…Q-15 ปิดครบ) + งานค้าง R-01…R-05 |
| [[16-deck-patch-list]] | รายการแก้ Canva deck ตามการตัดสินใจ D-01…D-20 (ร่าง ให้ทีมแก้เอง) |
| [[18-field-deep-dive]] | เจาะลึกทีละ field: ภาพรวม i-DREAMS, i-DREAMS ↔ G7 ทั้ง 5 feature พร้อมสเปก mapper, Speeding/Harsh, สิ่งที่ต้องเปลี่ยนใน alert code/POC/scoring layer |
| [[17-slide-content]] | ข้อความพร้อมวางสำหรับสไลด์ใหม่ (i-DREAMS, แทน G7, แต่ละ field, งานแก้ POC/alert code/scoring layer, limitations) |

## 7. ไฟล์ต้นทางในเครื่อง (relative จาก `Capstone/`)

- `จากรุ่นพี่/` — `SCGJWD-CP-Report.pdf`, `Capstone Final Presentation SCGJWD2025.pptx`, `Progress presentation.pdf`, รายงานอังกฤษ `Final_Report_Capstone_2025__...pdf` (ใช้ใน [[09-g7-definitions-from-seniors]])
- `Idream/iDREAMS_814761_D2.1_28022020_Final.pdf`, `Idream/iDREAMS_814761_D3.6_31082021_final.pdf`
- `data-sample/i-Dreams/` → `i-Dream-Sample_dataset.csv`, `Data Description.docx`, `Data access application form.docx`
- `data-sample/I-dream sample.md` (วิเคราะห์ sample), `data-sample/I-dream Index.md` (รวม dataset/paper)
- `work-space/chatbot-with-idream/` (POC) — `README.md`, `docs/POC_DESIGN.md`, `docs/DATA_TRANSFORMATION_SUMMARY.md`, `scripts/generate_data.py`, `data/generated/alert_codes.csv`
- `work-space/AI-chatbot-Langgraph/ChatBot use-case.md` (use case/requirement ของ chatbot)
