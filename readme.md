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

## 📊 Key features

**World GDP** — overview, KPIs (total GDP, growth rates), world map and Top 20 countries comparison.

**GDP Dynamics** — time-series analysis: annual growth, changes across years, continent distribution.

**2025 GDP Forecast** — comparison of the independent forecast with the IMF (2025) using matrices and conditional formatting.

---

## ⚙️ DAX measures and metrics

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
│     Cont.CSV
│     Динаміка розподілу ВВП.csv
│     Порівняльний аналіз прогнозу МВФ на 2025 рік за континентами у %.csv
│     Порівняльний аналіз прогнозу МВФ на 2025 рік за країною у %.csv
│
├─ dashboard/               <- Exported dashboard images (PNG)
│     world_gdp.png
│     gdp_dynamics.png
│     forecast_2025.png
│
└─ scripts/                 <- Python scripts used for forecasting
      gdp_forecast.py
```

## 📬 Contact / Author

**BilogurO** — author
- Email: **biloguroleksij@gmail.com**
- LinkedIn: https://www.linkedin.com/in/oleksij-bilohur

---


# РЕТ-Проєкт: Аналіз та прогноз ВВП (2020–2025)

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

## 📊 Ключові сторінки дашборду

**ВВП країн світу** — огляд, KPI (сукупний ВВП, темпи зростання), карта та порівняння топ-20 країн.

**Динаміка ВВП** — часові ряди: річне зростання, зміни по роках, розподіл по континентах.

**Прогноз ВВП 2025** — порівняння незалежного прогнозу з прогнозом МВФ (2025), умовне форматування для відмінностей.

---

## 📂 Джерело даних

Дані взято з Kaggle: **"GDP per Country 2020–2025"** — https://www.kaggle.com/datasets/codebynadiia/gdp-per-country-20202025

---

## 📂 Структура репозиторію

```
GDP-Analysis-2025/
│  README.md                <- Опис проєкту (цей файл)
│  .gitignore               <- Правила ігнорування Git
│  requirements.txt         <- Залежності Python (опціонально)
│
├─ data/                    <- Дані та файл Power BI
│     2020-2025.csv
│     GDP.pbix
│     Cont.CSV
│     Динаміка розподілу ВВП.csv
│     Порівняльний аналіз прогнозу МВФ на 2025 рік за континентами у %.csv
│     Порівняльний аналіз прогнозу МВФ на 2025 рік за країною у %.csv
│
├─ dashboard/               <- Збережені зображення дашбордів (PNG)
│     world_gdp.png
│     gdp_dynamics.png
│     forecast_2025.png
│
└─ scripts/                 <- Python-скрипти для прогнозу
      gdp_forecast.py
```

## 📬 Контакти

- Email: **biloguroleksij@gmail.com**
- LinkedIn: https://www.linkedin.com/in/oleksij-bilohur

