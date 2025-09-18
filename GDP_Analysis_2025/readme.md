# GDP Analysis and Forecast Project (2020–2025)

**Interactive Power BI dashboard + Python forecasting**

This repository contains an interactive Power BI report and supporting files for analyzing and forecasting world GDP per country for the period **2020–2025**.

---

## 📌 Project overview

This project demonstrates:
- data processing and forecasting with Python (scikit-learn),
- DAX calculations and measures in Power BI,
- data visualization best practices in Power BI.

The main deliverable is a Power BI report (`GDP.pbix`) with three main dashboard pages and an attached Python script used for model training / prediction.

---

## 📊 Key features (English)

**World GDP** — overview, KPIs (total GDP, growth rates), world map and Top 20 countries comparison.

**GDP Dynamics** — time-series analysis: annual growth, changes across years, continent distribution.

**2025 GDP Forecast** — comparison of the independent forecast with the IMF (2025) using matrices and conditional formatting.

---

## ⚙️ DAX measures and metrics (English)

- **Average Annual Growth** — average % and absolute growth over 2020–2025.
- **Years of Growth** — count of years with positive GDP growth per country.
- **Year-over-Year Growth** — annual growth rate.
- **Total Period Growth** — overall growth from 2020 to 2025.

---

## 📂 Data source

Data taken from [Kaggle — GDP per Country 2020–2025](https://www.kaggle.com/datasets/codebynadiia/gdp-per-country-20202025)

Dataset title: **"GDP per Country 2020–2025"**

---

## 📂 Repository structure

```
GDP-Analysis-2025/
│  README.md                <- Project description (this file)
│  .gitignore               <- Git ignore rules for Python & Power BI
│  requirements.txt         <- Python dependencies (optional)
│
├─ data/                    <- Data and Power BI file(s)
│     2020-2025.csv
│     GDP.pbix
│
├─ dashboard/               <- Exported dashboard images (PNG)
│     world_gdp.png
│     gdp_dynamics.png
│     forecast_2025.png
│
└─ scripts/                 <- Python scripts used for forecasting
      gdp_forecast.py
```

**Notes:**
- `GDP.pbix` (4.3 MB) is safe to keep in the repo. If you prefer not to store large binary files in Git, use Git LFS.
- Keep `data/2020-2025.csv` tracked if it’s not sensitive.

---

## 🚀 How to use (quick)

1. Open `data/GDP.pbix` in Power BI Desktop.
2. Inspect visuals on the three pages (World GDP, GDP Dynamics, 2025 Forecast).
3. If you want to reproduce forecasting locally, open `scripts/gdp_forecast.py` and install dependencies from `requirements.txt`.

---

## 🧾 How to upload this README to GitHub (Web UI)

If you prefer to add the file using GitHub web interface (recommended to preserve formatting):

1. Go to your repository page on GitHub: `https://github.com/<your-username>/GDP-Analysis-2025`.
2. Click **Add file → Upload files**.
3. Drag and drop the prepared `README.md` (or a ZIP with the whole folder) into the upload area.
4. In **Commit changes** write: `Add README and initial project files` and click **Commit changes**.

Alternatively, you can click **Add file → Create new file**, name it `README.md` and paste the contents of this file, then commit — but uploading the file directly avoids formatting issues.

---

## 📌 Branches & folders note

- Folders on GitHub are *not* the same as branches. Keep the folder structure on the **main** branch for simplicity.
- Use branches for feature work, not for representing folders. If you already created branches named `scripts`, `dashboard`, `data`, it’s OK, but you can keep everything on `main` until you need collaborative branching.

---

## 📬 Contact / Author

**BilogurO** — author
- Email: **biloguroleksij@gmail.com**
- LinkedIn: https://www.linkedin.com/in/oleksij-bilohur

---

# --- УКРАЇНСЬКА ВЕРСІЯ / УКРАЇНСЬКИЙ ТЕКСТ ---

# Проєкт: Аналіз та прогноз ВВП (2020–2025)

**Інтерактивний дашборд Power BI + прогнозування на Python**

Цей репозиторій містить Power BI звіт та допоміжні файли для аналізу й прогнозування ВВП країн за період **2020–2025**.

---

## 📌 Опис проєкту

Проєкт демонструє:
- підготовку даних та прогнозування на Python (scikit-learn),
- DAX-обчислення у Power BI,
- принципи візуалізації даних у Power BI.

Основний результат — файл Power BI (`GDP.pbix`) з трьома сторінками дашборду та Python-скриптом для навчання моделі та прогнозів.

---

## 📊 Ключові сторінки дашборду (укр.)

**ВВП країн світу** — огляд, KPI (сукупний ВВП, темпи зростання), карта та порівняння топ-20 країн.

**Динаміка ВВП** — часові ряди: річне зростання, зміни по роках, розподіл по континентах.

**Прогноз ВВП 2025** — порівняння незалежного прогнозу з прогнозом МВФ (2025), умовне форматування для відмінностей.

---

## 📂 Джерело даних

Дані взято з Kaggle: **"GDP per Country 2020–2025"** — https://www.kaggle.com/datasets/codebynadiia/gdp-per-country-20202025

---

## 📂 Структура репозиторію (укр.)

```
GDP-Analysis-2025/
│  README.md                <- Опис проєкту (цей файл)
│  .gitignore               <- Правила ігнорування Git
│  requirements.txt         <- Залежності Python (опціонально)
│
├─ data/                    <- Дані та файл Power BI
│     2020-2025.csv
│     GDP.pbix
│
├─ dashboard/               <- Збережені зображення дашбордів (PNG)
│     world_gdp.png
│     gdp_dynamics.png
│     forecast_2025.png
│
└─ scripts/                 <- Python-скрипти для прогнозу
      gdp_forecast.py
```

---

## 🚀 Як користуватися (коротко)

1. Відкрий `data/GDP.pbix` у Power BI Desktop.
2. Переглянь сторінки дашборду: World GDP, GDP Dynamics, 2025 Forecast.
3. Для відтворення прогнозу локально — відкрий `scripts/gdp_forecast.py` та встанови залежності з `requirements.txt`.

---

## 📌 Примітка щодо .gitignore і `.pbix`

- `GDP.pbix` (4.3 MB) можна тримати у репозиторії. Якщо хочеш уникнути зберігання бінарних великих файлів у Git — використай Git LFS.
- Якщо `README.md` в минулому ламався при вставці — завантаж його як файл через **Upload files** у GitHub (це збереже форматування).

---

## 📬 Контакти

- Email: **biloguroleksij@gmail.com**
- LinkedIn: https://www.linkedin.com/in/oleksij-bilohur


---

*README.md згенеровано для репозиторію **GDP-Analysis-2025**. Якщо треба — можу підготувати ZIP-архів із файлами-заглушками для швидкого завантаження через веб-інтерфейс GitHub.*

