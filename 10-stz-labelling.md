---
title: STZ label — นิยาม, ที่ sample ใช้, และทางเลือกเมื่อ D4.2 ไม่เปิด
updated: 2026-10-31
---

# STZ label — นิยาม, ที่ sample ใช้, และทางเลือกเมื่อ D4.2 ไม่เปิด

กลับไป [[00-README]] · deliverable: [[06-deliverables-catalog]]

## 1. STZ คืออะไร (D3.6 §2.2, Table 1) [ตรวจแล้ว]

Safety Tolerance Zone แบ่งสภาพการขับเป็น 3 phase:

| Phase | ความหมาย |
|---|---|
| **Normal** | โอกาสเกิดอุบัติเหตุต่ำ; คนขับปรับพฤติกรรมให้ตรงกับความต้องการของงานขับได้ |
| **Danger** | มีการเปลี่ยนจากการขับปกติที่บ่งชี้ว่าอาจเกิดอุบัติเหตุ; ความเสี่ยงเพิ่มขึ้น |
| **Avoidable accident** | สถานการณ์ชนเริ่มก่อตัวแต่ยังมีเวลาให้คนขับแก้ได้; ถ้าไม่ปรับตัว โอกาสชนสูงมาก |

เป้าหมายแพลตฟอร์ม: ให้คนขับอยู่ใน Normal นานที่สุด และกันไม่ให้ไหลจาก Danger ไป Avoidable accident. ระบบวัดผ่าน 4 performance objectives: **headway, illegal overtaking, speeding, fatigue**

## 2. ใน data sample มี label ไหม

**ไม่มีคอลัมน์ STZ label รวม** [ตรวจแล้ว — ตรงกับ note เดิม]. สิ่งที่มีคือ **level 0–3 ต่อหมวด** ซึ่งเป็นผลของ warning strategy ที่คำนวณแล้ว ([[01-dataset-overview]]) **ข้อควรระวัง (D6.1/D6.3 Table 2):** เฉพาะ Headway ที่ level แปลตรงเป็น phase; Speeding/Overtaking/Fatigue เป็นระดับ warning (Fatigue L1–3 ทั้งหมดเป็น Dangerous ไม่มี Avoidable) กฎ label ด้านล่างจึงใช้ได้กับ headway เท่านั้น ต้องไม่ขยายไปหมวดอื่นโดยไม่มีหลักฐาน

การแปลง level → phase ที่เปเปอร์ที่ใช้คอลัมน์ชุดเดียวกับเราใช้ (Theodoraki et al., *Infrastructures* 11(8):266, ข้อมูล BE+UK, ช่วงละ 30 วินาที) [ตรวจแล้ว จากเนื้อเปเปอร์ที่ดึงมา]:

| Phase | Headway intervention level |
|---|---|
| Normal | -1, 0 หรือ 1 |
| Dangerous | 2 |
| Avoidable accident | 3 |

- ช่วงเวลาถูก label ด้วย **level ที่แย่ที่สุด** ที่เกิดขึ้นในช่วงนั้น (ใช้ headway อย่างเดียว ไม่ใช้ความเร็ว)
- ช่วงที่ไม่มีรถข้างหน้าถูกระบุว่า "ไม่มี headway reading จึงไม่ได้ label" (ขัดกับการนับ level -1 เป็น Normal — เปเปอร์เล่าทั้งสองอย่าง; ยังไม่ชัดว่าตัดทิ้งหรือไม่ [ยังไม่ยืนยัน])
- Feature ที่ใช้ทำนาย 4 ตัว: `GPS_distances_sum`, `GPS_spd_mean`, `DEM_evt_ha_lvl_L_mean`, `DEM_evt_hb_lvl_L_mean` — **ทั้งหมดมีใน sample ของเรา**; headway ถูกตัดออกจาก input เพื่อไม่ให้ circular

→ ทำซ้ำได้ด้วยคอลัมน์ใน sample โดยตรง (ต่างแค่ความละเอียด: เปเปอร์ 30 วินาที, sample 60 วินาที)

### ตัวอย่างการกระจาย label บน sample ของเรา (กฎ "วินาทีที่แย่ที่สุดในนาที") [ตรวจแล้ว]

| ตัวชี้วัด | Normal | Dangerous | Avoidable |
|---|---|---|---|
| Headway (ทุกแถว 52,770) | 82.4% | 14.7% | 2.9% |
| Headway (ตัดแถวที่ไม่มีรถข้างหน้าทั้ง 60 วินาที: 22,968 แถว) | 59.7% | 33.7% | 6.6% |
| Speeding | 85.9% | 2.9% | 11.3% |
| Fatigue | 86.8% | 11.0% | 2.2% |
| รวม max(Headway, Speeding, Fatigue) | 59.5% | 24.6% | 15.9% |

กติกา: Dangerous = level 2 มีวินาที > 0 และ level 3 ไม่มี; Avoidable = level 3 มีวินาที > 0. (L1 นับเป็น Normal ตามกติกาของเปเปอร์ — คำอธิบาย level ใน Data Description เรียก L1 ของ Speeding/Overtaking ว่า "normal warning" เหมือนกัน)
แถวที่ไม่มีรถข้างหน้าทั้งนาที = 29,802 แถว (56%)

## 3. ถ้า D4.2 (อัลกอริทึมคำนวณ STZ) ไม่เปิด — ทางเลือกอื่น

D4.2 เป็นหนึ่งใน 2 deliverable ที่ไม่มีลิงก์ download ([[06-deliverables-catalog]]) และ D3.6 ตัดค่า threshold จริงออกเพราะ IP. ทางเลือกที่ **อ้างอิงเอกสารเปิดได้**:

| # | วิธี | แหล่ง | ข้อดี / ข้อเสีย |
|---|---|---|---|
| A | Rule-based จาก level ที่มีอยู่ (Normal = L ≤ 1, Dangerous = L2, Avoidable = L3) | Theodoraki 2026 (headway) | ทำซ้ำได้ทันที ตรงกับคอลัมน์ที่มี; ใช้ได้กับ Speeding/Fatigue ในแนวเดียวกัน (เป็นการขยายของเรา ไม่ใช่ของเปเปอร์) |
| B | Threshold จากช่วงที่ D3.6 เปิดเผย | D3.6 Tables 3, 5, 6 | headway 1.0–2.2 s / 1.2–0.6 s; speed เกินขีดจำกัด 3.25–10% ถึง 4.75–15%; fatigue < 2 ชม. ปกติ (ไม่มีตัวเลขเต็ม). ใช้กับ sample ไม่ได้ตรงๆ เพราะ headway ดิบสะอาดแค่ ~4% |
| C | Threshold บน `Headway_min` ต่อช่วง 30 วินาที: Normal > 2 s, Dangerous 1.4–2 s, Avoidable < 1.4 s | Garefalakis 2022 (simulator, 36 drivers) | ชัดเจน อ้างอิงง่าย; ต้องมี `Headway_min` ซึ่ง sample ไม่มี (มีแต่ค่าเฉลี่ยที่ปน sentinel) |
| D | Normalise แล้วใช้ CI: ใน 90% = Normal, 95% = Dangerous, ที่เหลือ = Avoidable | D3.6 §4.3 ข้อ 3 | ไม่ต้องมี threshold; ผลขึ้นกับการกระจายของข้อมูล |
| E | Clustering (PCA / k-means / t-SNE) 3 กลุ่ม แล้วตรวจด้วย silhouette หรือ Dunn index | D3.6 §4.3 ข้อ 4 | unsupervised; Garefalakis 2022 ลองแล้วพบว่า Avoidable กลายเป็นกลุ่มใหญ่สุด จึงปฏิเสธ |

- Garefalakis 2022 ยังทดลอง TTC และ mean speed เป็นกฎ label แล้วได้คลาสไม่สมดุลมาก จึงตัดทิ้ง [ตรวจแล้ว]
- Roussou 2024 (Sustainability 16(2):518) เปิดดูแล้ว **ไม่ระบุกติกา label** ชัดเจน (ไม่มี threshold หรือ window) [ตรวจแล้ว]
- ถ้ายังอยากได้ตัวจริง: D4.2 ต้องขอจากผู้เขียนโปรเจกต์ (UHasselt/NTUA/Loughborough/CardioID) — ไม่จำเป็นสำหรับ POC

## 4. ข้อเสนอสำหรับ discuss

- ใช้ **วิธี A** เป็น label มาตรฐานของงานเรา แล้วอ้างอิง Theodoraki 2026 + D3.6 §2.2/§4.3
- ระบุ limitation: 60 วินาทีต่อ 30 วินาที, ไม่ได้ตัดแถว no-lead (เลือกได้ 2 แบบ ดูตารางด้านบน), L1 นับเป็น Normal
- ใช้ label นี้ได้ใน (1) glossary ของ bot ("Dangerous หมายถึงอะไร") และ (2) ถ้าต้องการ ทำ benchmark RF/MLP ในรายงาน — ไม่จำเป็นกับ POC
