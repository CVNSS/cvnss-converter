# CVNSS 4.0 Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![JavaScript](https://img.shields.io/badge/JavaScript-Node.js-informational)
![Python](https://img.shields.io/badge/Python-package-informational)

> **VI:** Bộ chuyển đổi theo CVNSS 4.0 (**CQN → CVN → CVNSS**), có cơ chế **“P-guard”** để tránh nhập nhằng.  
> **EN:** CVNSS 4.0 conversion toolkit (**Quốc Ngữ → CVN → CVNSS**), featuring a **“P-guard”** mechanism to reduce ambiguity.

---

## Mục lục | Table of Contents

- [Giới thiệu | Overview](#giới-thiệu--overview)
- [Tính năng | Features](#tính-năng--features)
- [Cài đặt | Installation](#cài-đặt--installation)
  - [Cài từ GitHub](#cài-từ-github)
  - [Cài từ npm / PyPI](#cài-từ-npm--pypi)
- [Sử dụng | Usage](#sử-dụng--usage)
  - [JavaScript / Node.js](#javascript--nodejs)
  - [Python](#python)
- [Cấu hình & Mapping](#cấu-hình--mapping)
- [P-guard (chống nhập nhằng)](#p-guard-chống-nhập-nhằng)
- [Phát triển | Development](#phát-triển--development)
  - [Yêu cầu | Requirements](#yêu-cầu--requirements)
  - [Clone & Setup](#clone--setup)
- [Đóng góp | Contributing](#đóng-góp--contributing)
- [Giấy phép | License](#giấy-phép--license)
- [Ghi công | Acknowledgements](#ghi-công--acknowledgements)

---

## Giới thiệu | Overview

### VI

**CVNSS 4.0 Converter** là mô-đun chuyển đổi dựa trên **công thức CVNSS 4.0** do **Trần Tư Bình**, **Kiều Trường Lâm**  phát kiến và đề xuất. Thư viện hỗ trợ **JavaScript (Node.js)** và **Python** để chuyển đổi văn bản theo hướng:

- **CQN (Chữ Quốc Ngữ) → CVN → CVNSS**

Ngoài ra, module có cơ chế **“P-guard”** (ký tự/đánh dấu bảo vệ) nhằm giảm nhầm lẫn khi nhập liệu hoặc khi văn bản nguồn chứa các chuỗi dễ gây mơ hồ trong quá trình chuyển đổi.

### EN

**CVNSS 4.0 Converter** is a conversion module based on the **CVNSS 4.0 formula**, authored by **Trần Tư Bình**, **Kiều Trường Lâm**. It provides **JavaScript (Node.js)** and **Python** implementations to convert text in the following direction:

- **CQN (Vietnamese Quốc Ngữ) → CVN → CVNSS**

It also includes a **“P-guard”** mechanism to prevent unintended conversions and reduce ambiguity when the input contains potentially confusing patterns.

---

## Tính năng | Features

- **Song ngữ JS/Python** (cùng một logic mapping)
- **Chuyển đổi CQN → CVN → CVNSS** (theo mapping/spec)
- **P-guard** để chống nhập nhằng và bảo toàn chuỗi đặc biệt
- **Mapping tách rời** (dễ cập nhật, dễ kiểm thử)
- Phù hợp cho:
  - chuẩn hoá văn bản trước NLP/LLM/RAG
  - nhập liệu/hiển thị cần quy ước nhất quán
  - pipeline chuyển đổi hàng loạt

---

## Cài đặt | Installation

> Repo này hướng tới dùng như **thư viện** (JS/Python) và/hoặc nhúng vào dự án của bạn.

### Cài từ GitHub

#### JavaScript (Node.js)

```bash
npm install github:CVNSS/cvnss-converter
# hoặc
pnpm add github:CVNSS/cvnss-converter
# hoặc
yarn add github:CVNSS/cvnss-converter
```

#### Python

```bash
pip install git+https://github.com/CVNSS/cvnss-converter.git
```

### Cài từ npm / PyPI

Khi bạn publish lên npm/PyPI, chỉ cần thay `<package>` bằng tên gói thật:

#### JavaScript (Node.js)

```bash
npm install <package>
# hoặc
pnpm add <package>
# hoặc
yarn add <package>
```

#### Python

```bash
pip install <package>
```

---

## Sử dụng | Usage

> **Gợi ý API:** để các ví dụ dưới đây dùng được ngay, bạn nên export (hoặc alias) các hàm:
>
> - **JS:** `convertCqnToCvnss(text, options?)`
> - **Python:** `convert_cqn_to_cvnss(text, options=None)`

### JavaScript / Node.js

#### ESM

```js
import { convertCqnToCvnss } from "./src/cvnss4/converter.js"; // dùng trực tiếp từ source

const input = "Xin chào Việt Nam";
const output = convertCqnToCvnss(input);

console.log(output);
```

#### CommonJS

```js
const { convertCqnToCvnss } = require("./src/cvnss4/converter.js");

const input = "Xin chào Việt Nam";
const output = convertCqnToCvnss(input);

console.log(output);
```

### Python

```python
from cvnss4 import convert_cqn_to_cvnss

text = "Xin chào Việt Nam"
out = convert_cqn_to_cvnss(text)

print(out)
```

---

## Cấu hình & Mapping

### VI

Mapping/spec được tách rời để dễ cập nhật và kiểm thử. Thông thường nằm tại:

- `src/cvnss4/mapping.json`
- `spec/` (tài liệu đặc tả, bảng ánh xạ, ghi chú phiên bản)

Bạn có thể **phiên bản hoá mapping** để đảm bảo tương thích ngược (backward compatibility) khi phát hành.

### EN

The mapping/spec is separated from the core logic for easier versioning and testing. Typical locations:

- `src/cvnss4/mapping.json`
- `spec/` (spec docs, mapping tables, version notes)

You can **version the mapping** to preserve backward compatibility across releases.

---

## P-guard (chống nhập nhằng)

- **VI:** “P-guard” là cơ chế đánh dấu/escape giúp giảm mơ hồ và hạn chế chuyển đổi sai khi chuỗi nguồn có pattern dễ gây nhầm.
- **EN:** “P-guard” is an escape/guard mechanism to reduce ambiguity and avoid unintended conversions.

---

## Phát triển | Development

### Yêu cầu | Requirements

- Node.js (khuyến nghị bản LTS)
- Python 3.9+ (khuyến nghị 3.10+)

### Clone & Setup

```bash
git clone https://github.com/CVNSS/cvnss-converter.git
cd cvnss-converter
```

#### Python (editable)

```bash
pip install -e .
```

#### Node

```bash
npm install
```

> Gợi ý: thêm test (`pytest`/`jest`) để “khóa” hành vi chuyển đổi theo từng phiên bản mapping.

---

## Đóng góp | Contributing

### VI

1. Fork repo  
2. Tạo branch: `feat/...` hoặc `fix/...`  
3. Commit rõ ràng (ngắn gọn nhưng đủ ý)  
4. Mở Pull Request (PR), kèm ví dụ input/output (đặc biệt khi đổi mapping)

### EN

1. Fork the repository  
2. Create a `feat/...` or `fix/...` branch  
3. Commit with clear messages  
4. Open a PR with reproducible input/output examples (especially for mapping changes)

---

## Giấy phép | License

Phát hành theo giấy phép MIT. Xem [LICENSE](LICENSE).  
Released under the MIT License. See [LICENSE](LICENSE).

---

## Ghi công | Acknowledgements

- **Trần Tư Bình**, **Kiều Trường Lâm** — tác giả công thức/đặc tả CVNSS 4.0
- **Giấy tác quyền**số 1850/2020/QTG từ Cục Bản quyền tác giả thuộc Bộ Văn hóa, Thể thao và Du lịch cấp.
- **CVNSS Contributors** — đóng góp mã nguồn, mapping, kiểm thử, do **Long Ngo** - Trưởng team phát triển dự án phụ trách.
