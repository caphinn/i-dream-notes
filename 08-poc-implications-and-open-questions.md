---
title: ผลต่อ POC และคำถามที่ต้อง discuss
updated: 2026-11-04
---

# ผลต่อ POC และคำถามที่ต้อง discuss

กลับไป [[00-README]] · แผนแก้เต็ม: [[11-poc-fix-plan]]

## POC ปัจจุบัน (สรุปจากเอกสารและโค้ดที่อ่านแล้ว)

`work-space/chatbot-with-idream` — LangGraph + Governed API + PostgreSQL (checkpoint) + MongoDB (fleet data); LLM เป็น mock; UI แบบกดปุ่ม

- Use case: UC-01 Driver Risk Score · UC-02 Warning History (level ≥ 2) · UC-03 AI Event Log "แนว G7" · UC-04 Driver Ranking · UC-05 Trip Timeline
- Fallback: FB-01 นอกขอบเขต · FB-02 กำกวม · FB-03 ขาด parameter · FB-04 ไม่พบข้อมูล · FB-05 ล้มเหลวซ้ำ · **FB-06 ไม่มีข้อมูลประเภทนี้** (เพิ่มแล้ว WP3) · **glossary** (GL-01…04: ถามความหมาย risk score / level / ข้อมูลที่รองรับ)
- Guardrail: GR-01 SQL/Prompt injection · GR-02 RBAC (manager/viewer)
- Governed API: RBAC, input guard, Pydantic, temporal normalizer, safety limit 20 แถว; event ถูกรวมเป็น episode (ห่าง ≤ 90 วินาที) ก่อนนับ "ครั้ง"
- **สถานะ 4 พ.ย.:** แก้ WP1–WP4 แล้ว (smoke test 27/27, offline test 45 เคส) รายการด้านล่างบางส่วนเป็นภาพตอนเริ่มตรวจ
- อ่านโค้ดแล้ว: `scripts/generate_data.py`, ส่วนที่เกี่ยวข้องของ `app/governed_api.py` และ `app/llm.py`; **ยังไม่ได้อ่านเต็ม**: `graph.py`, `static/index.html`, `seed_mongo.py`, `load_db.py`

### สิ่งที่ POC สร้างขึ้นเอง (ไม่ได้มาจาก i-DREAMS)

| รายการ | ที่มา |
|---|---|
| ทะเบียนรถ/ชื่อคนขับ | `mapping_drivers.csv`, `mapping_vehicles.csv` (ข้อมูลดิบมีแค่ UUID) |
| วันที่ | time re-basing โหมด `compress` ย่อเหลือ 52 วัน ให้ถามเช่น "52 วันล่าสุด" ได้ |
| `risk_score` 0–100 | สูตรของเราเอง: Σ(วินาทีเสี่ยง × น้ำหนัก) ต่อชั่วโมงขับ: ระดับ 1 = ×0, ระดับ 2 = ×3, ระดับ 3 = ×10 (D-22, D-23; harsh คงน้ำหนักเดิม), RISK_SCALE 14,600 (เดิม 60,000) |
| Alert code A0101–A0703 | ตั้งเอง ไม่ใช่ code ของ G7 ([[02-g7-mapping]]) |
| Episode ของ event | รวมแถวที่ห่าง ≤ 90 วินาทีเป็น 1 episode |

ตอน demo/รายงานควรบอกชัดว่าเป็นข้อมูล **derive/สังเคราะห์**

## ผลที่ต้องจัดการ → รายละเอียดใน [[11-poc-fix-plan]]

| # | เรื่อง | แผน |
|---|---|---|
| P1 | harsh event นับผิดหน่วย (ส่งผลต่อ penalty/risk_score และฟิลด์ `occurrences`) | WP1 — **ทำแล้ว** |
| P2 | ชื่อ `FATIGUE` — **ตัดสินแล้ว (อาจารย์): คงชื่อ Fatigue** แต่ต้องเปิดเผยว่าวัดจากเวลาขับ | WP2 (แก้ใหม่) — **ทำแล้ว** |
| P3 | ไม่มีเส้นทางตอบเมื่อถามเรื่องที่ข้อมูลไม่มี (มือถือ/หาว/หลับตา/…) | WP3 (FB-06) — **ทำแล้ว** |
| P4 | ยังไม่แจ้งว่าข้อมูลเป็นสังเคราะห์/คำนวณเอง | WP4 — **ทำแล้ว** |
| P9 | เอกสาร requirement ยังอ้าง G7 และตัวอย่างมือถือ | WP8 |
| P5–P7 | เอกสารไม่สอดคล้อง, exposure ของ trip, โหมด compress | WP1, WP6, WP7 |

## แนวทางใช้ data กับ chatbot

- **ข้อมูลตัวเลข** → structured query ผ่าน tool calling เข้า DB (สิ่งที่ POC ทำอยู่) ไม่ต้องทำ RAG กับ CSV
- **PDF + Data Description + สรุปในโฟลเดอร์นี้** → knowledge base เล็กๆ (glossary/RAG) ตอบ "level 2 คืออะไร / threshold มาจากไหน"
- **คำถามนอกข้อมูล** → ตอบว่าไม่มีข้อมูล ไม่ใช้ proxy แบบเงียบๆ
- i-DREAMS เป็น **stand-in** ที่ทดสอบโครงสร้าง; ถ้ามีข้อมูล G7 จริง ควรสลับ data source ได้โดยไม่แก้ส่วนอื่น (`driver_events` เป็นสัญญาของ Governed API)

## สถานะคำถามเดิม

| # | คำถาม | สถานะ |
|---|---|---|
| 1 | นิยาม `G7_continuous_work`, `G7_vehicle_fatigue` | **ตอบบางส่วน** — เอกสารรุ่นพี่มีแค่ชื่อ event ("ปฏิบัติงานต่อเนื่อง 4 ชม.", "การเตือนความเมื่อยล้าของยานพาหนะ") ไม่มีเงื่อนไข ([[09-g7-definitions-from-seniors]]); ไม่กระทบ POC เพราะเป็น mock |
| 2 | feature 5 ตัวของโมเดล production | **ตอบแล้ว** — yawn, eye_close, phone, tailgating, eye_off_road (ที่ข้อมูลรองรับ: 1 ตรง / 2 อ้อมอ่อน / 2 สร้างแบบอิงอ่อน — D-12, D-21) |
| 3 | map แบบรายวันหรือรายนาที | **เปิด** — ถ้าจะเทียบกับโมเดลรุ่นพี่ต้อง roll-up รายวัน; POC ใช้ระดับนาที/episode อยู่แล้ว |
| 4 | ขอชุดเต็มไหม | **ปิด** — อาจารย์ไม่อนุญาต; ใช้ sample นี้เป็น mock ([[05-zenodo-sample-version]]) |
| 5 | sample มาจากประเทศไหน | **ปิด** — ไม่สำคัญ (mock) |
| 6 | `ME_AWS_time_indicator_median` ไม่มีค่า 0 | **ปิด** — เป็น coding ต่างจากเอกสาร (1/2/3 = กลางวัน/พลบค่ำ/กลางคืน) ไม่ใช่ข้อมูลหาย ([[01-dataset-overview]]) |
| 7 | สร้าง STZ label เองไหม | **ตอบแล้ว (ข้อเสนอ)** — ใช้ headway-level rule; รายละเอียดใน [[10-stz-labelling]]; ยังต้องตัดสินว่าจะทำ benchmark ในรายงานหรือไม่ |
| 8 | D4.2 ไม่เปิด จะทำยังไง | **ตอบแล้ว** — มีวิธี A–E ที่อ้างอิงได้ ไม่ต้องใช้ D4.2 ([[10-stz-labelling]]) |
| 9 | harsh event แก้เป็นวินาทีหรือ episode | **ปิดแล้ว → D-14** (penalty เป็นวินาที; จำนวน "ครั้ง" = episode) |
| 10 | วาง i-DREAMS เป็นอะไรตอนนำเสนอ | **ปิดแล้ว → D-02, D-19** — "mock data เพื่อแสดงระบบ" ยังไม่ได้ทดสอบกับระบบรุ่นพี่จริง |
| 11 | เก็บตาราง G7 ↔ i-DREAMS ไว้ที่ไหนอีก | **เปิด** — Project "Capstone" ใน claude.ai หรือ Notion |

> คำถามที่ค้างทั้งหมดถูกรวมเป็นรายการตัดสินใจใน [[15-decision-log]] (Q-01…Q-12) — คุยทีละข้อ

## คำถามใหม่ที่ต้อง discuss

1. FB-06 (ไม่มีข้อมูลประเภทนี้) นับรวมกับตัวนับ FB-05 หรือไม่ → **ปิด (D-15): ไม่นับรวม**
2. ~~คงชื่อ FATIGUE หรือเปลี่ยน~~ → **ปิด** (อาจารย์: fatigue = fatigue); เหลือ: Fatigue ควรมีน้ำหนักในคะแนนเท่าไร (หลังแก้ harsh จะเป็น ~20%) และ trip ยาวถูกลงโทษจากเวลาโดยไม่เกี่ยวพฤติกรรม
3. ทำ WP5 (G7 catalog + adapter) และ WP6 (ความเสถียรของคะแนน) ตอนนี้หรือเลื่อน → **ปิด (D-24): WP5 เลื่อน; ส่วนตัดค่า GPS ของ WP6 ทำใน WP1**
4. ต้องเก็บ risk_score ชุดเดิมสำหรับสไลด์ที่เคยนำเสนอไหม → **ปิด (D-24): เก็บที่ `reports/before_fix/`**
5. ใช้ label STZ ใน glossary ของ bot อย่างเดียว หรือทำ benchmark RF/MLP ลงรายงาน
6. คำถามเรื่อง "หาว/หลับตา" จะให้ bot ตอบแบบ "ใกล้เคียงที่สุด (Fatigue)" หรือตอบว่าไม่มีข้อมูลตรงๆ → วันนี้ตอบ "ใกล้เคียง = Fatigue"; หลังทำ mapper (D-06, 18 §2.2–2.3) ตอบได้ พร้อมป้าย `derived-weak`
7. จะจัดการตัวอย่างคำถามมือถือใน `ChatBot use-case.md` อย่างไร (เก็บไว้เป็นกรณี FB-06 หรือเอาออก)
8. จะถามทีม SCGJWD เรื่องนิยาม `continuous_work`/`vehicle_fatigue` หรือปล่อยเป็น "ยังไม่ทราบนิยาม" ในรายงาน

## งานที่ยังไม่ได้ทำ (ตรวจสอบก่อนใช้)

- ~~ยังไม่ได้รัน `generate_data.py`~~ → **รันแล้ว (WP1)** ผลก่อน/หลังอยู่ที่ `reports/WP1_before_after.md`
- ~~ยังไม่ได้อ่าน `graph.py`, `static/index.html`~~ → **แก้ WP2–WP4 ไปแล้ว** (เหลือตรวจว่า `load_db.py`/Postgres fleet ยังใช้อยู่หรือไม่)
- ยังไม่ได้เปิดอ่านเนื้อหา deliverable อื่นนอกจาก D2.1 (ส่วนต้น) และ D3.6 (ส่วน STZ/threshold)
- ยังไม่ได้ตรวจ Table 5/Table 7 ของ D3.6 ละเอียด และข้อความที่อยู่ในรูปภาพของเอกสารรุ่นพี่
