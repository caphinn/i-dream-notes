---
title: รายการแก้ POC (chatbot-with-idream) ให้ใช้ mapper v2
updated: 2026-11-14
status: ร่างรายการงาน — ยังไม่ได้แก้โค้ด POC (ตัดสินใจแล้วว่าให้ POC ใช้ mapper v2 เป็นแหล่ง event เดียวกับสไลด์; รายละเอียดจุดที่ต้องเลือกอยู่ในหัวข้อ 3)
---

# รายการแก้ POC ให้ใช้ mapper v2

กลับไป [[00-README]] · ที่มา: [[21-mapper-spec-v2]], [[22-advisor-brief-mapper-v2]], [[15-decision-log]] (D-25…D-30) · แผนแก้ POC เดิม: [[11-poc-fix-plan]]

## 1. ทำไมต้องแก้

POC (`work-space/chatbot-with-idream`) สร้าง event ใน `scripts/generate_data.py` ด้วยวิธีเดิม (แปลง `*_level_N_sum` ของ i-DREAMS เป็นหน้าต่างเหตุการณ์ 21 รหัส alert ตามระดับ L1–L3 และน้ำหนักต่อระดับ) ได้ราว 119,397 event
mapper v2 สร้าง event 5 ชนิดแบบ G7 ด้วยกฎตายตัว (ไม่สุ่ม ไม่มีน้ำหนัก) ได้ราว 2,800 event
ตัวเลขที่ chatbot ตอบจึงไม่ตรงกับตัวเลขในสไลด์และ brief จนกว่าจะเปลี่ยนแหล่งข้อมูล

ผลต่อแผนเดิม [[11-poc-fix-plan]]: ส่วนที่ผูกกับ event เดิมถูกแทนที่ด้วย D-25 เช่น WP1 (หน่วย harsh, `penalty`, `RISK_SCALE`) และน้ำหนักระดับ 1 ตาม D-22/D-23 ส่วน WP3–WP4 (FB-06, ที่มาข้อมูล, glossary) ยังใช้ได้ แต่ข้อความต้องปรับตามชนิด event ใหม่

## 2. ส่วนที่ไม่ต้องแก้ (ไม่ขึ้นกับชนิด event)

- LangGraph flow, RBAC, Input Guard, Pydantic validation, temporal normalizer, safety limit
- การดึงข้อมูลระดับทริป/คนขับ/เวลา

## 3. งานที่ต้องทำ

| # | ไฟล์ | สิ่งที่ต้องแก้ | หมายเหตุ |
|---|---|---|---|
| 1 | `scripts/generate_data.py` | เรียก mapper v2 (`mapper-v2/mapper.py`) แทนส่วนสร้าง event เดิม; เขียน `driver_events.csv` ด้วย event 5 ชนิด พร้อมป้าย `direct` / `derived-weak` / `proxy-weak` และ `rule_id` | ทำก่อน เพราะข้อ 2–6 ขึ้นกับรูปแบบข้อมูลใหม่ |
| 2 | `data/generated/alert_codes.csv` (สร้างจาก `build_alert_codes`) | เปลี่ยนรหัส `{event_type}_L{level}` (21 รหัส) เป็นรหัสของ event 5 ชนิด | ต้องตัดสินใจเรื่อง "ระดับ" (ดูหัวข้อ 4) |
| 3 | `app/governed_api.py` (`_tool_events`, การรวม episode) | ปัจจุบันถือว่า event มี `level` 1–3 (`max_level`) แล้วสรุปเป็น LOW/MEDIUM/HIGH และสร้างรหัส `{event_type}_L{max_level}` | ต้องปรับตามข้อ 4 |
| 4 | `app/knowledge.py` | เขียนใหม่ให้ตรงข้อมูลใหม่: "ระดับเตือน (level) หมายถึงอะไร", D-01 (Fatigue = เวลาขับ), D-22/D-23 (ระดับ 1 = ขับปกติ) | ข้อความเดิมจะผิดความหมาย |
| 5 | `app/llm.py` (`EVENT_KEYWORDS`) | แมปคำผู้ใช้ไปชนิด event ใหม่: "หาว"→yawn, "หลับตา"→eye_close มีอยู่แล้ว; เพิ่ม "มองนอกถนน"→eye_off_road, "โทรศัพท์/มือถือ"→phone, "ตามติด"→tailgating; คำถามที่เคยตอบ "ไม่มีสัญญาณนี้" (kind none) อาจตอบได้แล้ว | ตรวจ FB-06 ด้วย |
| 6 | `scripts/seed_mongo.py` | โหลดข้อมูลใหม่เข้า MongoDB (`driver_events`, `alert_codes`) | |
| 7 | `app/scenarios.py`, `tests/offline_test.py`, `tests/smoke_test.py` | ปรับค่าที่คาดหวังของ use-case ที่นับเหตุการณ์ (เช่น UC-03b) และ GL-03 | รันเทสต์ซ้ำหลังข้อ 1–6 |
| 8 | `driver_trip_histories.csv`, `risk_config.json` (คะแนนความเสี่ยงต่อทริป) | คำนวณ `risk_score` ใหม่จาก event ใหม่ | สูตรเดิมเป็นคะแนนชั่วคราว (D-16) ต้องเลือกสูตรใหม่ (หัวข้อ 4) |
| 9 | `README.md`, `docs/POC_DESIGN.md`, `docs/DATA_TRANSFORMATION_SUMMARY.md`, `docs/PRESENTATION_DATA_SUMMARY.md` | ปรับตัวเลข (119,397 event, 21 alert codes) และคำอธิบายแหล่ง event | |
| 10 | UI/คำตอบของ chatbot | บอกผู้ใช้ว่า yawn / eye_close / phone / eye_off_road เป็นค่าประมาณจากกฎ (ฟิลด์ weak) | ตาม D-15 (บอกที่มาข้อมูล) |

## 4. สิ่งที่ต้องตัดสินใจก่อนแก้

1. **"ระดับ" ของ event:** mapper v2 ไม่มีระดับต่อ event (เกิด/ไม่เกิด) มีแค่สถานะ 10 นาที (LOW/MEDIUM/HIGH). ทางเลือก: (ก) ให้ `level` ของแต่ละ event = สถานะ 10 นาที ณ เวลานั้น; (ข) ตัดแนวคิด level ออกจากคำตอบ ใช้ชนิด event + จำนวนครั้งอย่างเดียว
2. **สูตร risk score ต่อทริป:** คำนวณจากจำนวน event/ชม. ของ 5 ชนิด หรือจากสถานะ 10 นาที/alert ของรุ่นพี่; ต้องปรับ `RISK_SCALE` ให้มัธยฐานสมเหตุสมผล
3. **ชื่อรหัส alert:** ใช้ชื่อ event 5 ชนิดตรง ๆ หรือคงรูป `{event}_L{n}` ไว้เพื่อลดการแก้ UI

## 5. ขอบเขตที่ไม่ทำตอนนี้

- เชื่อมระบบ mock real-time (replayer + G7 emulator ไป Kafka) — ทำเป็นขั้นถัดไป และใช้ mapper v2 เป็นตัวสร้าง event เหมือนกัน
- เปลี่ยน LangGraph flow หรือชั้น Governed API ส่วนที่ไม่เกี่ยวกับชนิด event
