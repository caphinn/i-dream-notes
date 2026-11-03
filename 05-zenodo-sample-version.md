---
title: Zenodo sample dataset — เวอร์ชันและชุดข้อมูลที่ตัวเลขต่างกัน
updated: 2026-10-31
---

# Zenodo sample dataset — เวอร์ชันและชุดข้อมูลที่ตัวเลขต่างกัน

กลับไป [[00-README]] · deliverable ที่เกี่ยวข้อง [[06-deliverables-catalog]]

## Record ที่เราใช้

ลิงก์: <https://zenodo.org/records/7684848> (ดึงหน้ามาตรวจเมื่อ 2026-10-31) [ตรวจแล้ว]

| รายการ | ค่า |
|---|---|
| ชื่อ | i-Dreams H2020 EU Project: Sample dataset |
| ผู้สร้าง | Tom Brijs (ORCID 0000-0003-2622-4398), Transportation Research Institute (IMOB), Hasselt University |
| **Version** | **1.0** |
| เผยแพร่ | 28 ก.พ. 2023 (สร้าง record 28 ก.พ. 2023, แก้ไขล่าสุด 1 มี.ค. 2023) |
| DOI | 10.5281/zenodo.7684848 |
| Concept DOI | ไม่แสดงในหน้า |
| License | CC BY 4.0 |
| ไฟล์ | `Sample_dataset.csv` 20.9 MB · `Data Description.docx` 19.3 kB · `Data access application form.docx` 30.7 kB |
| เวอร์ชันอื่น | หน้าที่ดึงมาไม่แสดงเวอร์ชันอื่น |
| Related identifiers | หน้าไม่แสดง (ลิงก์ที่มีมีแค่เว็บโปรเจกต์, grant CORDIS, OpenAIRE — ไม่ชี้ไป deliverable) |

- ขนาดไฟล์ในเครื่องตรงกับทั้ง 3 ไฟล์ (CSV = 20,851,771 ไบต์, Data Description = 19,315, ฟอร์ม = 30,723) — เทียบแค่ขนาด ไม่ได้เทียบ hash และ CSV ถูกเปลี่ยนชื่อเป็น `i-Dream-Sample_dataset.csv`
- **ชุดเต็มไม่เปิดสาธารณะ**: ต้องโหลด sample ศึกษา → กรอกฟอร์ม → ส่งอีเมลตามฟอร์ม → ผู้ประสานงานตรวจ → เซ็น NDA → ส่งข้อมูล; ผู้ใช้ต้องอ้างอิงข้อมูลตามเงื่อนไข
- หน้า Zenodo ระบุว่าข้อมูลมีทั้ง handheld phone และ driver characteristics (ตัวหลังไม่อยู่ใน sample) — ใน sample ของเราไม่พบคอลัมน์ phone [จาก note เดิม]

## ความสัมพันธ์กับ D2.1 / D3.6

"Version 1.0" เป็นเวอร์ชันของ record บน Zenodo ไม่เกี่ยวกับ "ver 2.x / 3.x" — ดู [[06-deliverables-catalog]]

| เวลา | เหตุการณ์ |
|---|---|
| ก.พ. 2020 | D2.1 (รีวิวงานวิจัย) |
| ส.ค. 2021 | D3.6 (นิยาม STZ และ threshold) |
| 28 ก.พ. 2023 | Zenodo sample v1.0 |
| 30 เม.ย. 2023 | โปรเจกต์สิ้นสุดตาม CORDIS (PDF ปี 2019–2021 เขียน 30/04/2022 — น่าจะขยายเวลา [ยังไม่ยืนยัน]) |

หน้า Zenodo ไม่มีลิงก์ไป deliverable; ที่เชื่อมกันเชิงเนื้อหาคือศัพท์ level (dangerous / avoidable accident) ซึ่งตรงกับ phase ของ STZ ใน D3.6

## ชุดข้อมูลที่มีตัวเลขต่างกัน (อย่าสับสน)

| ชุด | ขนาด | แหล่ง |
|---|---|---|
| โปรเจกต์ทั้งหมด | 600 ผู้เข้าร่วม 5 ประเทศ (รถยนต์ รถบัส รถบรรทุก รถไฟ) | Zenodo / เว็บโปรเจกต์ |
| ชุดในเปเปอร์ล่าสุด (Theodoraki et al., *Infrastructures* 11(8):266) | 69 drivers, 15,389 trips, 265,512 นาที — เบลเยียมและสหราชอาณาจักร | [MDPI](https://www.mdpi.com/2412-3811/11/8/266) |
| **sample ของเรา** | 10 drivers, 652 trips, 8 รถ, รถบรรทุก 100% | ไฟล์ CSV [ตรวจแล้ว] |

- Zenodo ไม่ระบุว่า sample มาจากประเทศไหน [ยังไม่ยืนยัน]
- ตัวเลข 26,908 trips / 500,000 นาที ใน `I-dream Index.md` (cite 1.1.3) ยังหาแหล่งยืนยันไม่เจอ ควรเช็กต้นทางก่อนอ้างในรายงาน [จาก note เดิม]
- Garefalakis et al. (2024) ใช้ risk factor รวม mobile phone use และ fatigue จากทั้ง simulator และ naturalistic driving → ชุดที่ใช้ในเปเปอร์มี phone แต่ sample ของเราไม่มี

## การตัดสินใจเรื่องการใช้ข้อมูล (30–31 ต.ค. 2026)

- อาจารย์ **ไม่อนุญาตให้ขอชุดเต็ม** (ฟอร์ม + NDA) → ใช้ได้เฉพาะ sample v1.0 ปัจจุบัน
- ใช้เป็น **mock data เพื่อแสดงระบบ** ไม่ใช่เพื่ออ้างผลเชิงวิจัยหรือเทียบกับถนนไทย → ประเทศต้นทางของ sample **ไม่สำคัญ** (คำถามข้อ 4–5 ใน [[08-poc-implications-and-open-questions]] ปิดแล้ว)
- ผลต่อรายงาน: เขียน limitation ว่า phone / KSS / driver characteristics ไม่มีในข้อมูลที่ใช้
