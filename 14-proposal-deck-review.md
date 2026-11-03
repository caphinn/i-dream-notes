---
title: สรุป Canva deck "Research Slide Oct 2026 - Capstone" และผลทบทวน
updated: 2026-11-04
---

# สรุป Canva deck และผลทบทวน

> **สถานะ 4 พ.ย.:** เอกสารนี้เป็นภาพ ณ 31 ต.ค. (ตอนรีวิว deck) สิ่งที่ตัดสินแล้วดู [[15-decision-log]] (D-01…D-24) และข้อความที่ทีมต้องแก้ใน Canva ดู [[16-deck-patch-list]] ส่วนที่ขัดกับการตัดสินใจ เช่น Headway L2 เป็น tailgating, ใช้ FCW/IBI, LDW แทน eyes-off-road, phone ปิด/mock ถูกแก้ตาม patch list C1–C7 และ I1–I5
กลับไป [[00-README]] · การตัดสินใจทีละข้อ: [[15-decision-log]] · แผนเชื่อมระบบ: [[13-integration-with-seniors-system]]

## ที่มา

- Canva: "Research Slide Oct 2026 - Capstone" (design id `DAHYGXlAXzc`) ลิงก์ดู: <https://www.canva.com/d/eWViAv1JGw2wSnV>; ลิงก์ที่ให้มา: <https://canva.link/mfix85jk8e59ihn>
- metadata: 68 หน้า; แก้ไขล่าสุดราว 29 ต.ค. 2026 (คำนวณจาก timestamp)
- **ข้อจำกัด:** อ่านเฉพาะข้อความและ metadata — ไม่ได้ดูรูป กราฟผล POC และสมการที่เป็นภาพ [ตรวจแล้ว เฉพาะข้อความ]
- ตัวเลขผลการทดลอง (Flink/Redis) และตัวเลขตัวอย่างใน scoring layer ด้านล่าง **อ้างตามที่ deck เขียน ยังไม่ได้ตรวจซ้ำ**

## เนื้อหา deck

Weekly Report 29/10/2026 (และ 22/10/2026 ที่แนบรวม): ML Real-time (สมการ + POC Flink DataStream กับ Kafka), Chatbot mock data และ POC, Scoring Layer, Knowledge Management และ Proposal draft

### 1) Netradyne และ 3 add-on
- Real-time Notification (DBAS): เตือนพฤติกรรมเสี่ยงแบบเสียงในห้องโดยสาร จัดลำดับตามระดับ (แรงบันดาลใจ: Driver·i)
- Chatbot Add-on: natural-language event search เช่น "หาช่วงที่คนขับ A เล่นโทรศัพท์อาทิตย์ที่แล้ว" (แรงบันดาลใจ: Video LiveSearch)
- Strategic / Reward / Coaching Layer: tier/ดาว, gamification, coaching (แรงบันดาลใจ: GreenZone Score, DriverStars)

### 2) Scoring layer: Reward และ Alert
- **Feedback อาจารย์**: (1) แปลง label high=100 / medium=50 / low=0 ทั้ง 4 factor (G7, Fatigue, Truck, Route) (2) รวมด้วย w1–w4 ปรับได้ใน dashboard, เต็ม 400, ยิ่งสูงยิ่งเสี่ยง (3) 1 แถว = รถ 1 คัน 1 วัน ดูแค่ label ไม่ดูปริมาณข้อมูล; **reference ต้องตีพิมพ์แล้วหรือมาจากหน่วยงานทางการ** (Lee 2026 เป็นแค่ preprint); **แยก Reward กับ Alert**
- **ปัญหาสูตรเดิมของรุ่นพี่**: ไม่ normalize ตามปริมาณข้อมูล (คนข้อมูลน้อยได้คะแนนสุดโต่ง) และไม่มีนิยามรายเดือน/รายปี
- **Reward** (ระยะยาว คนนี้ขับดีแค่ไหน): ใช้ Empirical Bayes — E = จำนวนวัน; Z = E/(E+K), K = φ/λ̄ (Z = 0.5 เมื่อครบ K วัน); λ ผสมอัตราของตัวเองกับค่าเฉลี่ย fleet; medium/high คิดแยก (high ×2 ตาม FMCSA, ปรับได้); RR = λ เทียบ fleet; แปลงเป็นคะแนน 0–100 ยิ่งสูงยิ่งปลอดภัย; รวมช่วง daily/monthly/annual โดยรวม n และ E ก่อนคิด
- **Alert** (ตอนนี้/วันนี้ผิดปกติไหม): ใช้ข้อมูลล่าสุดตรงๆ ไม่ดึงเข้าค่าเฉลี่ย
- ตัวอย่าง (ค่า fleet และ φ สมมติ): K medium = 20 วัน, K high = 60 วัน; คนขับ A–D และ "คนใหม่" เทียบสูตรเดิม–สูตรใหม่ (C ข้อมูล 3 วัน low ทุกวัน ถูกดึงเข้าหา 50)
- **Threshold ขั้นต่ำ**: ต้องมีข้อมูล G7 ≥ K วันจึงได้อันดับและรางวัล ไม่ถึง = "ยังไม่จัดอันดับ" (ยังเห็นคะแนน) อ้าง Motive (Minimum Miles)
- **References**: Hauer et al. (2002) TRR 1784 (429 cite), FHWA (2016) Reliability of Safety Management Methods, Yanez–Guillen–Nielsen (2025) ASTIN Bulletin 55(1), Bühlmann (1967) credibility
- **Implementation**: `driver_risk_score` (ข้อมูลรายวันเดิม ไม่แก้ pipeline) → **Scoring API** (JWT เดียวกับ API เดิม) → ผู้ใช้: หน้า Leaderboard, ระบบ reward ของ SCG, Chatbot (use case Driver Ranking)
  - `GET /scoring/leaderboard` (period, date, page, limit, car_id) → rank, car_id, safety, days, z, low_data, rank_change, factors
  - `GET /scoring/drivers/:car_id` (period, from, to) → current + history
  - `GET, PUT /admin/scoring-config` → severity weight (medium 1, high 2), `low_data_z` = 0.6; w1–w4 ใช้ `/admin/weight` เดิม
- **Wireframe**: Leaderboard (เลือก period, ป้ายข้อมูลน้อย, คะแนน 4 factor, เทียบเดือนก่อน, กดไปหน้ารายคน) และหน้ารายละเอียดคนขับ
- **Feedback รอบก่อน → ตัดสินใจ**: ใช้ weight ทางการชุดเดียวทั้ง fleet (ล็อกรอบ มี version/log), admin ปรับบน dashboard ได้แต่เป็น "มุมมองที่ปรับเอง ไม่ใช่อันดับทางการ"; C ยังอยู่อันดับต้นเพราะ low ทุกวัน → แก้ด้วย threshold; "จำนวนวันที่ขับ" จัดการผ่าน Z + threshold แล้วจึงไม่ใส่เป็น weight เพิ่ม; "Work Quality weight" ไม่ใส่ในสูตร Safety (ถ้าหมายถึงผลงานให้ไปรวมฝั่ง Reward)

### 3) ML Real-time
- **สถาปัตยกรรม** (system diagram): iDREAM log → Kafka → (Python หรือ Apache Flink) risk score processing → Go backend → Next.js Admin Dashboard; MongoDB; MLflow (model version) + Airflow + Redis cache; Chatbot service (Python, LangGraph) + PostgreSQL (agent state machine) + LLM call
- **Track 1 Fast Safety Guard**: เช็ค edge case เฉพาะหน้า (อาจใช้ 4 cases ที่ดักให้ Admin Call)
- **Track 2 Near Real-Time ML Engine**: buffer ข้อมูล G7 ใน RAM (Redis ZSET), aggregate ย้อน 30 นาที, trigger predict ทุก 5 นาที, normalize จำนวน event ต่อเวลาขับจริง; HIGH risk → Admin Call; ส่งคะแนน G7 [0,100] ไปรวมกับ Fatigue + Truck + Route (static)
- **สมการ**: Sₜ = γ·rₜ + (1−γ)·Sₜ₋₁ (EMA) โดย r: LOW=0 / MEDIUM=50 / HIGH=100; ทดลองเทียบ EMA กับ Sliding-window Average (SWA ทำให้ความเสี่ยงที่กำลังเกิดจางลง) และ **Asymmetric EMA** (α ต่างกันขาขึ้น/ขาลง); อ้างอิง: Sensors 25(6):1769 (2025, MDPI) และ IEEE Access 14:12167 (2026, FastKAN) — ส่วนที่มาของ EMA อ้างบทความบล็อก (towardsdatascience)
- **Redis ZSET design**: key `g7:events:{vehicle_plate}`, score = Unix timestamp, member = event JSON + `_uid` (กันชนกัน); `g7:active_vehicles` (SET); ลบข้อมูลเก่ากว่า 24 ชม. ด้วย ZREMRANGEBYSCORE
- **Flink design**: 1 JobManager + 1 TaskManager (2 slots) อ่าน `ai_event_topic` เก็บ event ต่อทะเบียน, predict จาก 5 พฤติกรรมเสี่ยง (หาว, หลับตา, โทรศัพท์, ละสายตา, ขับชิด), normalize เป็น 24 ชม. ถ้า aggregate 30 นาที, ผ่าน EMA, ส่งผลไป `ml_realtime_risk_topic` ทุก 5 นาที → Go consumer ใหม่ → WebSocket → dashboard
- **POC**: 4 designs (Flink 24h, Flink 30m, Redis 24h, Redis 30m); โหมด 30m normalize ×16 (= 480/30); workload "Heavy" (100 คัน × ~500 event/คัน/วัน; 50,000 event/24h, 1,211/30m) และ "iDream-avg" (5 คัน × 204 event/คัน/วัน; 1,020/24h, 25/30m); ประมวลผลทุก 30 วินาที × 10 ครั้ง/รัน (ของจริงทุก 5 นาที), 5 รัน/design; วัดเวลา (agg_ms, tick_total_ms), RAM (peak/delta), CPU; ตรวจว่าจำนวน event ใน window ตรงเฉลย
- **สถิติ iDream ที่ deck ใช้**: 8 คัน, 52 วัน, 3–5 คัน/วัน, event ต่อคันต่อวัน mean 204 / median 178 / p95 519 / max 783
- **ผล (ตาม deck)**: Heavy — agg_ms Flink24h 26.5, Redis24h 1,157, Flink30m 4.52, Redis30m 46.0; RAM peak (MiB) 1,528 / 203 / 1,038 / 104. iDream-avg — agg_ms 1.42 / 41.2 / 0.31 / 8.8; RAM peak 1,018 / 102 / 1,005 / 101. สรุป: Flink เร็วกว่าทุกกรณี, Redis ใช้ RAM น้อยกว่า, 24h vs 30m ไม่ต่างมากใน iDream-avg แต่ต่างขึ้นเมื่อ heavy; **ข้อเสนอ** ใช้ Flink ถ้า memory พอ (ดูแล component เดียว), ถ้ากังวล memory ต้อง POC เพิ่มด้านความแม่นยำ
- **Mapping iDREAMS → G7** (สไลด์ "I-dream data & G7 mapper"): Headway L2/L3 (level_3_sum > 0 หรือ level_2_sum > 0) → ขับชิดท้าย เสริม `ME_AWS_fcw_mean`; Fatigue L2/L3 → "หาว/ตาปิด" ด้วย heuristic L2 = หาว, L3 = ตาปิด/หลับใน และอาจใช้ร่วมกับ `IBI_value_mean`; `ME_LDW_Map_type_L/R_mean` + `ME_AWS_pedestrian_dz_mean` → ละสายตาจากถนน (ทางอ้อม); โทรศัพท์ = mock หรือตัดออกแล้วระบุเป็นข้อจำกัด; ตัวอธิบาย: "FATIGUE Lv 1-2-3 = ระดับความง่วง" *[ณ 31 ต.ค. — ปัจจุบันใช้ Headway L3 + ≥ 50 km/h เท่านั้น ไม่ใช้ FCW/IBI; LDW ใช้เป็นจุดยึดอ่อนของ phone/eye_off_road ไม่ใช่สัญญาณ eyes-off-road ตรง (D-08, D-10, D-21)]*

### 4) AI Chatbot POC (รายงาน 22/10)
- ข้อมูลดิบ: 52,770 แถว × 135 คอลัมน์, 1 แถว = 1 นาที, 652 trips, 10 คนขับ, 8 คัน, ช่วงเดิม ก.ย. 2021–พ.ค. 2022 (52 วัน)
- 5 use case (UC-01 Risk Score … UC-05 Trip Timeline), 5 fallback (FB-01…FB-05), 2 guardrail (GR-01 Input Guard, GR-02 RBAC)
- Flow: หน้าเว็บปุ่มกด → LangGraph (Regex/Keyword สกัด intent ไม่ใช้ LLM) → Governed API Tool Service → LangGraph (Template string) → UI component; Postgres เก็บ checkpoint; Mongo เก็บ `driver_trip_histories` (652), `driver_events` (119,397), `alert_codes` (21)
- ระบุว่า **Risk score ปัจจุบันยังไม่ final** จะแก้หลัง scoring layer ได้สูตรแน่นอน และคำนวณตั้งแต่ขั้น data pipeline
- ตัวอย่างคำตอบในสไลด์: "รถ 1กก-9999 มีอาการหาวสะสม 2 ครั้ง เมื่อวานนี้ เวลา 14:02 น. และ 15:10 น."

### 5) ท้าย deck
Template "Weekly Report" ที่ยังเป็น placeholder และข้อความที่ไม่เกี่ยวกับโปรเจกต์ — ควรลบก่อนนำเสนอ

## ส่วนที่สอดคล้องกับที่เราคุยกัน (ไม่ต้องแก้)

- Kafka เป็นจุดเชื่อม + mapper iDREAMS→G7 (ตรงกับ G7 emulator ใน [[13-integration-with-seniors-system]])
- ประเมิน XGBoost บนหน้าต่าง 30 นาที normalize เป็นรายวัน (ตรงกับแนว "หน้าต่างเลื่อน" ที่เสนอ แต่ deck เลือก 30 นาที ×16 เทียบกับ 24 ชม.)
- Chatbot เรียก Scoring API ร่วมกับหน้า Leaderboard (ตรงกับหลัก "อ่านจาก layer กลาง ไม่อ่านคอลัมน์ i-DREAMS ตรง")
- แยก Reward ออกจาก Alert

## ประเด็นที่ควรตรวจ (เรียงตามผลกระทบ) — แต่ละข้อมีหลักฐานจากข้อมูลจริง [ตรวจแล้ว]

| # | ประเด็น | หลักฐาน | ข้อเสนอ | สถานะ |
|---|---|---|---|---|
| 1 | **Fatigue_Map ถูกใช้ซ้ำสองทาง** *(ตัดสินแล้ว: ใช้กับ G7 factor เท่านั้น — D-05)*: mapper ใช้สร้าง yawn/eye_close (G7 factor) ขณะที่ Scoring มี Fatigue factor แยก (ปัจจัยของ SCGJWD) | รายงานรุ่นพี่แยก G7 กับ Fatigue (สไลด์ 11; ตาราง 5.12.1) — [[09-g7-definitions-from-seniors]] | เลือกทางเดียวหรือนิยามให้ชัดว่าแต่ละ factor ใช้ส่วนไหน ไม่ให้นับซ้ำใน w1·G7 + w2·Fatigue | **ตัดสินแล้ว (ก)** |
| 2 | สไลด์เขียน "Fatigue Lv = ระดับความง่วง" | D3.6 §2.4.4: วัดจากเวลาขับ — [[03-fatigue-finding]] | แก้ข้อความเป็น "ความเหนื่อยล้าจากเวลาขับ" | **ตัดสินแล้ว (D-01)** — แก้ถ้อยคำตาม [[16-deck-patch-list]] C5 |
| 3 | **ความหนาแน่นของ event**: 204 event/คัน/วัน | ผมนับ Headway L1–3 + Fatigue L1–3 (1 event/แถว) ได้ mean 189 / median 168 / p95 441 / max 620; ขับเฉลี่ย 394 นาที/คัน/วัน → ~1 event ทุก 2 นาที; เกณฑ์ SCGJWD: หาว 1–2 ครั้ง/ชม. = กลาง | Calibrate generator ให้ใกล้เกณฑ์/การกระจายที่โมเดลเคยเห็น; ระวังว่า ×16 ขยาย noise (1 event/30 นาที → 16/วัน) | **ตัดสินแล้ว (D-08, D-21)** — ความหนาแน่นมาจาก mapper; ดู 18 §2.7 |
| 4 | **K ใน scoring ตัวอย่างเกินข้อมูล**: K medium 20, K high 60 วัน | active days ต่อคัน = 4, 7, 9, 13, 17, 17, 29, 38 (ต่อคนขับสูงสุด 34) → K high ไม่มีใครถึง, K=20 ผ่านแค่ 2 จาก 8 คัน | ประมาณ λ̄/φ จาก mock จริงแล้วเลือก K ให้อยู่ในช่วงที่ข้อมูลมี หรือใช้ช่วง 4–38 วันนี้เป็นกรณีทดสอบ shrinkage; และบอกว่าป้าย label มาจากฟีเจอร์ synthetic จึงเป็นการสาธิตวิธี ไม่ใช่การ validate | **ตัดสินแล้ว (D-09)** — ประมาณ K จาก mock; คำนวณใหม่หลัง D-21 (R-09) |
| 5 | `IBI_value_mean` ใช้เสริม Fatigue L3 | เป็น 0 ใน 99.3% (3 trips, คนขับ 1 คน) | ตัดออกจาก mapper | **ตัดสินแล้ว (D-10)** |
| 6 | FCW เสริม tailgating; LDW/pedestrian_dz แทน eyes-off-road | FCW 18 แถว (PCW 1); LDW ขวา 20.5% / ซ้าย 0.57% และกระจุกที่รถคันเดียว (10,569 จาก 10,828 แถว; คันนั้น 84% ของนาที); pedestrian_dz 0.8% | ตัด FCW/LDW/IBI (D-10) | **ตัดสินแล้ว (D-10)** |
| 7 | heuristic L2 = หาว, L3 = ตาปิด | L2 ≈ 69% ของเวลาหลัง 4 ชม.; ถ้า 1 event/แถว จะชน rule "หาว ≥ 2 ใน 2 นาที" ตลอดทริปยาว | ใช้อัตราสุ่มตามระดับ (ดู [[13-integration-with-seniors-system]] §4) | **ตัดสินแล้ว (D-06): อัตราสุ่มตามระดับ** |
| 8 | ตัวอย่าง "หาวสะสม 2 ครั้ง" และ "คนขับ A เล่นโทรศัพท์" | หาว = สร้างขึ้น, phone = mock | ติดป้าย synthetic หรือเปลี่ยนตัวอย่าง | **ตัดสินแล้ว (D-13)** |
| 9 | Risk score ใน POC chatbot ยังไม่ final | harsh นับผิดหน่วย (cornering ≈ 52% ของ penalty) — [[04-harsh-events-poc-issue]] | แก้ WP1 และกำหนดว่า risk_score ใน POC จะถูกแทนด้วยสูตร scoring layer เมื่อไร | **ตัดสินแล้ว (D-16)** — แก้ WP1 แล้ว (cornering 33.2%) ใช้สูตรเดิมชั่วคราวจน Scoring API พร้อม |
| 10 | "52 วัน ก.ย. 2021–พ.ค. 2022"; "3–5 คัน/วัน" | 52 = วันที่มีข้อมูล กระจายใน 5 เดือนปฏิทิน (ไม่มี พ.ย.–ก.พ.); ผมนับ 134 vehicle-day = 2.6 คัน/วัน | ตรวจวิธีนับ แล้วเขียนให้ชัด | รอตัดสินใจ |
| 11 | อ้างอิงที่มาของ EMA เป็นบล็อก | อาจารย์ให้ใช้ reference ที่ตีพิมพ์หรือเป็นทางการ | แทนด้วยแหล่งทางการ เช่น NIST e-Handbook (EWMA) หรือ Roberts (1959) — **ยังไม่ได้เปิดตรวจ** ต้องเช็กก่อนใส่ | รอตัดสินใจ (R-04) |
| 12 | สไลด์ท้ายมี placeholder/ข้อความไม่เกี่ยวข้อง | อ่านจากข้อความ deck | ลบก่อนนำเสนอ | รอตัดสินใจ |

## ข้อสังเกตเพิ่มเติม (ไม่ใช่ข้อผิดพลาด)

- Empirical Bayes ใช้จำนวนวัน medium/high ต่อคัน — ถ้า label มาจาก XGBoost บน feature ที่ 4 ใน 5 เป็น synthetic ผลจะเป็นการสาธิตคุณสมบัติทางคณิตศาสตร์ (shrinkage) ได้ แต่ไม่สะท้อนคุณภาพการขับ
- ข้อมูล iDREAMS มีความต่างของปริมาณข้อมูลต่อคันตามธรรมชาติ (4–38 วัน) ซึ่งเหมาะกับการสาธิต EB

## ภาคผนวก: ทดลองความหนาแน่นของ event (31 ต.ค. 2026) — ประเด็นที่ 3

**ข้อเท็จจริงที่ตรวจแล้ว:** เอกสารรุ่นพี่ (รายงานไทย, รายงานอังกฤษ, สไลด์ Final, Progress) **ไม่มีสถิติความถี่ event จริง** (จำนวนต่อคนต่อวัน ค่าเฉลี่ย ฯลฯ) — มีแค่ว่า feature ถูกจัดว่า "เบ้ขวา" และ risk score distribution ที่เป็นรูป จึงไม่มีความจริง (ground truth) ให้ calibrate [ตรวจแล้ว]

**สิ่งที่มีให้ยึดได้ (anchors จากเอกสาร):** สถานะ real-time 10 นาที — event ≥ 3 = กลาง, ≥ 6 = สูง (สไลด์ 56); priority alerts (สไลด์ 58); เกณฑ์ผู้เชี่ยวชาญ SCGJWD §5.1.8 (หาว/หลับตา 1–2 ครั้ง/ชม. = กลาง)

ผลจำลองบน sample (tailgating เฉพาะ ≥ 50 km/h; yawn/eye_close สุ่มตาม D-06 ที่ L0 0.2 / L1 1 / L2 3 / L3 30 ครั้ง/ชม. ต่อชนิด; seed 42; **อัตราเป็นสมมติฐาน**):

| ทางเลือก | tailgating ต่อนาที | event รวมต่อนาที | หน้าต่าง 10 นาที ≥ 3 (กลาง+) | ≥ 6 (สูง) | ต่อคัน-วัน mean / median / p95 |
|---|---|---|---|---|---|
| แมปตรงแบบ deck (Headway L1–3 + Fatigue L1–3, 1 event/แถว) | — | 0.55 | 59.5% | 49.4% | ~189 / 168 / 441 (นับเฉพาะ 2 ประเภท) |
| A: Headway L2\|L3 > 0 และ ≥ 50 km/h ทุกนาที | 0.153 | 0.195 | 30.8% | 13.4% | 77 / 50 / 233 |
| B: Headway L3 > 0 และ ≥ 50 km/h | 0.028 | 0.069 | 7.0% | 2.5% | 27 / 14 / 83 |
| C: (L2 ≥ 15 วินาที หรือ L3 > 0) และ ≥ 50 km/h | 0.067 | 0.109 | 14.9% | 5.6% | 43 / 26 / 138 |
| D: A + cooldown 3 นาที | 0.077 | 0.118 | 17.2% | 2.3% | 47 / 32 / 122 |

- ตัวขับความหนาแน่นหลักคือ **tailgating** (headway L2/L3 อยู่ใน 15% ของนาที) ไม่ใช่ fatigue: yawn และ eye_close อย่างละ ~0.02/นาที (~1.3 ครั้ง/ชม.)
- กฎ "หาว ≥ 2 ครั้งใน 2 นาที" ถูกยิงใน 0.67% ของหน้าต่าง 2 นาที ภายใต้การสุ่มตาม D-06 (ไม่ flood)
- แบบ deck ทำให้ครึ่งหนึ่งของเวลาเป็นสถานะ "สูง" ตามเกณฑ์ของรุ่นพี่เอง

## ภาคผนวก 2: ถ้าไม่ใช้ XGBoost บน mock (D-07) — ใช้ rule-based engine ของรุ่นพี่

**กฎที่ใช้ (โมเดลที่ 1 "Rule-Based" ของรุ่นพี่, SCGJWD-CP-Report §5.3.3; จัดคนขับรายวัน)** [ตรวจแล้ว จากรายงาน]

| ระดับ | เงื่อนไข |
|---|---|
| สูง | หาว > 2 ครั้งใน 2 นาที · หลับตา > 2 ครั้งใน 2 นาที · ละสายตา (event 3 โทรศัพท์ + 11 ละสายตา) > 1 ครั้งใน 3 วินาที |
| กลาง | หาว > 2 ครั้งใน 1 ชม. · หลับตา > 2 ครั้งใน 1 ชม. · ละสายตา > 1 ครั้งใน 1 ชม. · ขับกระชั้นชิด (event 9) ที่ ≥ 50 km/h และห่างคันหน้า ≤ 20 ม. |
| ต่ำ | นอกเหนือจากนั้น |

- ถ้อยคำของเกณฑ์ผู้เชี่ยวชาญ §5.3.2.1 บอกกลาง = "หาว 1–2 ครั้ง/ชม." ขณะที่ตัวโมเดลเขียน "> 2 ครั้ง/ชม." — ไม่ตรงกันเล็กน้อย ยังไม่ทราบว่าควรยึดข้อใด [ยังไม่ยืนยัน]
- ประสิทธิภาพบนข้อมูลจริงของรุ่นพี่: rule-based F1 สูงสุด 0.80 แล้วลดเหลือ 0.45 เมื่อข้อมูลมากขึ้น; ML (raw features) สูงสุด 0.90 (ก.ค.–พ.ย. → ธ.ค.) — ไม่เกี่ยวกับ mock เพราะไม่มีความจริงให้วัดความแม่น แต่ต้องไม่อ้างว่า engine นี้ "แม่น"
- หน้า real-time ของรุ่นพี่ใช้ rule-based อยู่แล้ว (สถานะ 10 นาที ≥3/≥6, priority alerts) — จึงสอดคล้องกันโดยตรง

**แปลงนิยาม tailgating ของ SCGJWD (≥ 50 km/h และ ≤ 20 ม.) ให้เข้ากับ Headway level** [ตรวจแล้ว กับแถวที่ headway สะอาด; ความเร็ว ≥ 50 km/h, n = 2,820]

ระยะ ≈ headway(วินาที) × ความเร็ว(m/s):

| Headway level (เด่น) | แถวสะอาด | สัดส่วนที่ระยะ ≤ 20 ม. | ระยะมัธยฐาน |
|---|---|---|---|
| L1 | 1,615 | 0% | 38.4 ม. |
| L2 | 1,145 | 21% | 24.1 ม. |
| L3 | 60 | 88% | 14.9 ม. |

→ นิยามที่ใกล้เอกสารที่สุด = **Headway L3 > 0 และ ≥ 50 km/h** (n ของ L3 น้อย: ข้อสรุปบอกแนวโน้มเท่านั้น). ใน sample มีแถวความเร็ว ≥ 50 ที่ L3 เด่นแค่ 110 จาก 30,090

**จำลองการจัดระดับรายวัน (134 คัน-วัน; yawn/eye_close สุ่มตาม D-06 ซ้ำ 200 รอบ; ละสายตา/โทรศัพท์ = ไม่มีเหตุการณ์)**

| สถานการณ์ | LOW | MEDIUM | HIGH |
|---|---|---|---|
| เฉพาะ fatigue (ไม่มี tailgating) | 63% | 30% | 6.9% |
| + tailgating (L3 > 0, ≥ 50 km/h), กลางเมื่อ ≥ 1 episode/วัน | 22% | 71% | 6.8% |
| ... กลางเมื่อ ≥ 2 episodes/วัน | 28% | 66% | 6.8% |
| ... กลางเมื่อ ≥ 3 episodes/วัน | 30% | 63% | 6.8% |

- tailgating episode (L3 ที่ ≥ 50 km/h) ต่อคัน-วัน: median 4, p75 13, max 37; มี ≥ 1 episode ใน 69% ของคัน-วัน
- ผลต่อ scoring layer: λ̄ medium ≈ 0.63–0.71 ต่อวัน, λ̄ high ≈ 0.07 ต่อวัน (deck สมมติ 0.15 / 0.05) → ถ้า φ = 3 ตามตัวอย่าง K medium ≈ 4–5 วัน (ทุกคันผ่าน) แต่ K high ≈ 43 วัน (> วันสูงสุดต่อคัน 38)
