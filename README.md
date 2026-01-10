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
- [Sử dụng | Usage](#sử-dụng--usage)
  - [JavaScript / Node.js](#javascript--nodejs)
  - [Python](#python)
- [Cấu hình & Mapping](#cấu-hình--mapping)
- [Phát triển | Development](#phát-triển--development)
- [Đóng góp | Contributing](#đóng-góp--contributing)
- [Giấy phép | License](#giấy-phép--license)
- [Ghi công | Acknowledgements](#ghi-công--acknowledgements)

---

## Giới thiệu | Overview

### VI

**CVNSS 4.0 Converter** là mô-đun chuyển đổi dựa trên **công thức CVNSS 4.0** do **Trần Tư Bình** soạn thảo. Thư viện hỗ trợ **JavaScript (Node.js)** và **Python** để chuyển đổi văn bản theo hướng:

- **CQN (Chữ Quốc Ngữ) → CVN → CVNSS**

Ngoài ra, module có cơ chế **“P-guard”** (ký tự/đánh dấu bảo vệ) nhằm giảm nhầm lẫn khi nhập liệu hoặc khi văn bản nguồn chứa các chuỗi dễ gây mơ hồ trong quá trình chuyển đổi.

### EN

**CVNSS 4.0 Converter** is a conversion module based on the **CVNSS 4.0 formula**, authored by **Trần Tư Bình**. It provides **JavaScript (Node.js)** and **Python** implementations to convert text in the following direction:

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

> Repo này hiện hướng tới dùng như **thư viện** (JS/Python) và/hoặc nhúng vào dự án của bạn. Bạn có thể cài trực tiếp từ GitHub.

### Cài từ GitHub (khuyên dùng khi đang dev)

#### JavaScript (Node.js)

```bash
npm install github:CVNSS/cvnss-converter
# hoặc
pnpm add github:CVNSS/cvnss-converter
# hoặc
yarn add github:CVNSS/cvnss-converter
