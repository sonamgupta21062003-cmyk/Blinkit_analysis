#  Blinkit Business Analytics & Machine Learning Project

# 🟡 Blinkit Business Analytics & Machine Learning Project

<h3 align="center">
  <span style="color:#F7C948;">Turning Raw Data</span>
  <span style="color:#00C9A7;">Into Business Insights</span>
</h3>

<p align="center">
  An end-to-end analytics project exploring commercial performance, supply and supplier operations, inventory and quality, customer behaviour, and predictive analytics using SQL, Python, Power BI, and Machine Learning.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="SQL"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-learn"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
</p>

<p align="center">
  <b> Business Intelligence |  Data Analytics |  Machine Learning |  Data-Driven Decision Making</b>
</p>

\<p align="center">   \<b> Business Intelligence |  Data Analytics |  Machine Learning |  Data-Driven Decision Making\</b> \</p>



1. Overall understanding of the dataset
The project uses multiple related datasets rather than one flat file. They can be understood in these business groups:
Business area	Data involved	What it helps analyse
Orders & transactions	Orders, order items	Order volume, revenue, quantity, payment patterns and trends
Customer intelligence	Customers	Customer profiles, purchasing frequency and customer segments
Product & catalog	Products, catalog	Product availability, product mix, categories and pricing
Delivery operations	Delivery performance	Delivery time, on-time performance, delays and delay reasons
Customer experience	Customer feedback, rating icons	Ratings, feedback and customer satisfaction
Inventory	Inventory-related tables	Stock and product availability
Marketing	Marketing performance	Campaign performance and marketing effectiveness

The business value: combining these datasets makes it possible to study not only how much business was generated, but also what influenced that performance — customer behaviour, product mix, delivery experience and marketing activity.
2. How the data connects
The central relationship is the order. Orders connect to customers and order items; order items connect to products. Delivery and feedback records can be connected through the order identifier. Marketing and inventory provide additional business context.
3. Understanding the main business metrics
These are the important measurements the combined data can support:
Metric	Business meaning
Total revenue	Sales value generated from order items
Total orders	Number of distinct orders
Total quantity sold	Total units purchased
Average order value (AOV)	Average revenue per order
Average selling price	Average selling price per unit
Gross profit / estimated profit	Revenue less estimated product cost
On-time delivery rate	Percentage of deliveries completed on time
Average delivery time	Average time taken to deliver orders
Average customer rating	Overall customer feedback score
Repeat customer rate	Share of customers who placed multiple orders
Campaign performance	Performance of marketing campaigns using available campaign metrics
Inventory availability	Product stock and availability patterns, subject to the fields available

Important distinction: revenue is calculated from the order-item level using quantity × unit price. Estimated profit is a separate calculation that depends on the product cost or margin information. Revenue should not be described as profit.
4. What makes this dataset useful?
The strongest aspect is the ability to connect different business questions.
- Commercial performance: Which products and categories generate the most revenue? How do sales change over time?
- Customer intelligence: Who are the high-value customers? Which customers purchase repeatedly?
- Delivery performance: Which delivery statuses and delay reasons occur most often? Is delivery performance associated with customer ratings?
- Product performance: Which products contribute most to sales and quantity?
- Customer experience: Which sentiment groups and product categories receive lower ratings?
- Marketing performance: How do campaigns perform against their available spend, impressions, clicks or conversion metrics?
- Inventory analysis: Which products need attention based on stock and availability information?
This is more valuable than reporting revenue alone because it connects business outcomes with operational and customer-related factors.
5. Data quality and important considerations
There are a few points we should explain transparently in the README.
1. Uncategorized products: You previously found that the uncategorized group contains a substantial amount of data. Removing it could exclude meaningful sales and distort totals. It should remain in the analysis as an explicit category, with its data-quality limitation documented.
2. Multiple rows per order: An order can contain multiple products. Therefore, order counts must use distinct order IDs, while revenue and quantity should be calculated at the order-item level.
3. Table relationships: Related tables should be joined using their appropriate keys, such as order_id, customer_id and product_id. Avoid joins that multiply rows and inflate revenue.
4. Missing information: Missing customer, product, delivery or feedback fields should be assessed according to the analysis rather than automatically deleting records.
5. Estimated profit: This is a derived estimate, not necessarily the company's actual accounting profit.
6. Dataset authenticity: We should describe this as a Blinkit-focused analytics case study using the provided dataset, not claim that it is official internal Blinkit company data unless its source confirms that.
6. What the data analysis has already produced
Your completed analysis goes beyond descriptive dashboards:
Customer segmentation
4
Exploratory K-Means customer segments
- 590 customers in the segmentation report.
- Silhouette score: 0.4377.
- Segments are profiled using recency, frequency and monetary value.
  
  Delivery prediction
  68.9%
  Random Forest accuracy
- Macro F1: 27.2%.
- Class-wise performance is weak, so this should be presented as an experimental model, not a reliable production predictor.
  
  Demand forecasting
  71.77%
  WAPE
- MAE: 1.69
- RMSE: 2.15
- Forecasting accuracy is limited; missing calendar dates were treated as zero-demand days.

These are actual results from your saved model reports, not target or predicted performance claims.
7. My recommendation for the README
I would structure the dataset section around this story:
From raw business data to business intelligence
Multiple business datasets

Orders · Customers · Products · Delivery · Feedback · Inventory · Marketing


Data inspection, cleaning and validation


SQL joins, analytical views and feature engineering


Power BI

4 business dashboards


Python & ML

EDA, segmentation, prediction




Business insights and decision support


##  Power BI – Interactive Business Intelligence Dashboards

Developed an interactive Power BI solution featuring **three business-focused dashboards** to analyze commercial performance, supply chain operations, supplier performance, inventory management, and quality metrics.

###  Dashboard 1: Commercial Overview
- Analyzed overall revenue, order volume, and quantity sold.
- Evaluated sales trends and business performance over time.
- Compared revenue contribution across product categories.
- Examined key commercial KPIs to understand sales performance.
- Identified important trends to support business decision-making.

<img width="1163" height="646" alt="image" src="https://github.com/user-attachments/assets/6f16fdac-dc6d-4997-aa64-8034e963a1f3" />


###  Dashboard 2: Supply & Supplier Analysis
- Analyzed supply chain and supplier-related performance.
- Evaluated supplier contribution and operational trends.
- Examined supply availability and related performance indicators.
- Identified potential supply-side issues and areas for improvement.

<img width="1177" height="656" alt="image" src="https://github.com/user-attachments/assets/911e6c07-7a3e-43fd-a8dc-1fc46ca49357" />



###  Dashboard 3: Inventory & Quality Analysis
- Evaluated inventory levels and stock-related performance.
- Analyzed product quality and customer feedback indicators.
- Examined ratings and quality-related patterns.
- Identified potential inventory and quality management concerns.

<img width="1167" height="655" alt="image" src="https://github.com/user-attachments/assets/187a4740-78d4-4b1b-9267-65f1dc6f4800" />



###  Power BI Skills Applied
- Data modeling and table relationships
- Star schema and dimensional modeling
- Power Query data transformation
- Advanced DAX measures and calculations
- Filter context and context transition
- Interactive slicers and cross-filtering
- KPI cards and business-focused visualizations
- Dashboard design and performance optimization
- Data storytelling and business insights

**Outcome:** Built a three-dashboard business intelligence solution connecting commercial performance, supply operations, and inventory quality to support data-driven decisions.



##  SQL – Data Auditing, Cleaning & Analytical Query Development

Used **MySQL Workbench** to prepare and validate the Blinkit dataset through a structured SQL workflow. The process focused on data quality, consistency, relational integrity, and building a reliable foundation for business analysis.

###  1. Initial Data Auditing
Performed an initial audit of the source tables to understand the dataset structure and identify potential data quality issues.

**Key activities:**
- Checked table structures and column definitions.
- Verified row counts across the available tables.
- Examined duplicate records and missing values.
- Reviewed key fields and data consistency.

**SQL Query Screenshot:**

<img width="1087" height="596" alt="image" src="https://github.com/user-attachments/assets/b04897d9-3a28-4877-8ab1-5d1eeb669405" />


**Query Results:**

<img width="321" height="223" alt="image" src="https://github.com/user-attachments/assets/15c98343-d6fb-4a45-8c2c-f1bf260f4aea" />


---

###  2. Data Cleaning
Applied SQL-based cleaning operations to improve data reliability and prepare the tables for analysis.

**Key activities:**
- Handled missing and inconsistent values where appropriate.
- Reviewed duplicate records.
- Corrected data quality issues without unnecessarily removing valid business records.
- Prepared cleaned tables for subsequent analysis.

**SQL Query Screenshot:**

<img width="893" height="547" alt="image" src="https://github.com/user-attachments/assets/2fadda51-8702-450c-9e38-66640d6b3d46" />
<img width="1050" height="595" alt="image" src="https://github.com/user-attachments/assets/9a6ea57c-2d17-4cb3-9170-6c6e88fc3274" />
<img width="941" height="576" alt="image" src="https://github.com/user-attachments/assets/8f4219ca-83c9-41b6-962b-1120942a2c9d" />
<img width="1047" height="561" alt="image" src="https://github.com/user-attachments/assets/187e7600-bcbb-41c8-be55-ad24b075b254" />
<img width="882" height="467" alt="image" src="https://github.com/user-attachments/assets/8fd73798-008d-4b96-9c04-4f10e8459497" />
<img width="917" height="437" alt="image" src="https://github.com/user-attachments/assets/0154f6e5-5c8e-4796-92f0-b5f791a45603" />
<img width="870" height="422" alt="image" src="https://github.com/user-attachments/assets/85e30d34-ee86-4754-957d-3fbc94a3b48c" />



**Query Results:**

![Data Cleaning Results](screenshots/sql/02_cleaning_results.png)

---

###  3. Orphan Record Auditing
Validated relationships between related tables by identifying records that did not have matching parent records.

**Key activities:**
- Checked foreign-key relationships across relevant tables.
- Identified unmatched customer, order, product, and transaction references where applicable.
- Evaluated referential integrity before joining tables.

**SQL Query Screenshot:**

<img width="842" height="540" alt="image" src="https://github.com/user-attachments/assets/527f6407-3324-4cab-892c-6adfc08fdf06" />
<img width="1217" height="555" alt="image" src="https://github.com/user-attachments/assets/d32368b9-90c2-4719-a4a6-00737b48f7c6" />
<img width="1432" height="250" alt="image" src="https://github.com/user-attachments/assets/1222fc5e-787c-4ca6-bba4-5108350017ef" />


**Query Results:**

<img width="323" height="173" alt="image" src="https://github.com/user-attachments/assets/028a8f29-dc1a-45ae-afcb-79489030d1ce" />


---

###  4. Data Standardization
Improved consistency in data values and formats to make the dataset more reliable for reporting and analysis.

**Key activities:**
- Standardized text values and categorical fields where required.
- Reviewed inconsistent labels and formats.
- Improved consistency across relevant columns and tables.
- Preserved meaningful categories, including uncategorized records, rather than discarding potentially valuable data.

**SQL Query Screenshot:**

<img width="691" height="341" alt="image" src="https://github.com/user-attachments/assets/669e00f8-2994-4409-838d-d933b3e1629c" />


"This query creates a cleaned version of the raw blinkit_customers table. It removes duplicate records and entries missing a customer ID. It also standardizes text formatting, converts registration dates into a proper date format, and fills missing customer segments with a default 'Regular' label."

---

###  5. Table Joining & Analytical View Creation
Combined relevant cleaned tables using SQL joins to create a consolidated analytical dataset for downstream business analysis.

**Key activities:**
- Joined orders with customer and order-item information.
- Connected product, delivery, and feedback information through relevant keys.
- Applied calculated fields such as revenue using quantity and unit price.
- Created the analytical master view `vw_blinkit_master` for further analysis.

**SQL Query Screenshot:**
<img width="966" height="612" alt="image" src="https://github.com/user-attachments/assets/2e87bdf3-5888-4ce7-9187-54a5c6ba1d4e" />
<img width="712" height="480" alt="image" src="https://github.com/user-attachments/assets/cf85c34f-b96b-4fc5-bc55-20d2e2d0b85e" />


**Query Results:**

<img width="1465" height="277" alt="image" src="https://github.com/user-attachments/assets/c426a12e-a5e2-4280-a2a9-47305ed6815c" />


---

###  SQL Skills Demonstrated

MySQL and MySQL Workbench

Data exploration and auditing

Data cleaning and standardization

Duplicate and NULL value checks

Orphan record and referential integrity checks

INNER JOIN and LEFT JOIN

Data transformation and calculated fields

Analytical view creation

Relational database analysis

Outcome: Established a structured and validated SQL data preparation workflow, creating a consolidated analytical view to support Power BI reporting and Python-based analysis.




##  Python – Data Analysis, Feature Engineering & Machine Learning

Used Python to perform data analysis and develop exploratory machine learning models on the cleaned Blinkit analytical dataset. Connected Python with MySQL to access the consolidated `vw_blinkit_master` view and carry out customer analysis, delivery prediction, and demand forecasting.

###  1. MySQL Database Connection & Data Loading

Connected Python to the MySQL database using `mysql-connector-python` / SQLAlchemy and loaded the consolidated analytical data.

**Key activities:**
- Established a Python–MySQL database connection.
- Retrieved data from `vw_blinkit_master`.
- Loaded the dataset into Pandas DataFrames.
- Parsed date fields and prepared the dataset for analysis.
- Checked the structure and availability of analytical fields.

**Code Screenshot:**

![Python MySQL Connection](screenshots/python/01_mysql_connection.png)

**Execution Output:**

![MySQL Data Loading Output](screenshots/python/01_mysql_output.png)

---

###  2. Data Preparation & Feature Engineering

Prepared the analytical dataset for machine learning while preserving meaningful records, including products classified as `Uncategorized`.

**Key activities:**
- Converted date columns into appropriate datetime formats.
- Created time-based features such as month, weekday, and day.
- Created an `is_uncategorized` indicator.
- Added `product_match_status` to distinguish matched and unmatched product records.
- Prepared relevant numerical and categorical features for modeling.

**Code Screenshot:**

![Python Feature Engineering](screenshots/python/02_feature_engineering.png)

**Execution Output:**

![Feature Engineering Output](screenshots/python/02_feature_output.png)

---

###  3. Customer Segmentation – RFM Analysis & K-Means

Applied RFM (Recency, Frequency, Monetary) analysis to understand customer purchasing patterns and identify exploratory customer segments using K-Means clustering.

**Key activities:**
- Calculated customer-level Recency, Frequency, and Monetary values.
- Prepared RFM features for clustering.
- Applied K-Means clustering.
- Evaluated clustering quality using the Silhouette Score.
- Analyzed customer distribution and revenue contribution across four exploratory segments.

**Model Results:**

| Metric | Result |
|---|---:|
| Customers analyzed | 590 |
| Number of clusters | 4 |
| Silhouette Score | 0.4377 |

**Business value:** Helped distinguish customer groups based on purchasing activity and spending patterns, supporting exploratory customer targeting and retention analysis.

**Code Screenshot:**

![Customer Segmentation Code](screenshots/python/03_customer_segmentation.png)

**Results & Segment Analysis:**

![Customer Segmentation Results](screenshots/python/03_segmentation_results.png)

---

###  4. Delivery Performance Prediction

Developed classification models to explore whether delivery outcomes could be predicted using available order and operational features.

**Key activities:**
- Prepared features and target variables for classification.
- Applied preprocessing for numerical and categorical variables.
- Trained and evaluated classification algorithms.
- Compared model performance using Accuracy and Macro F1-score.
- Examined class-wise performance to identify prediction weaknesses.

**Selected Random Forest Results:**

| Evaluation Metric | Score |
|---|---:|
| Accuracy | 68.9% |
| Macro F1-score | 27.2% |

**Observation:** The model showed weak class-wise performance, indicating difficulty predicting underrepresented delivery classes. Accuracy alone was therefore not sufficient to judge its effectiveness.

**Code Screenshot:**

![Delivery Prediction Code](screenshots/python/04_delivery_prediction.png)

**Model Evaluation:**

![Delivery Prediction Results](screenshots/python/04_delivery_results.png)

---

###  5. Demand Forecasting

Developed an exploratory demand forecasting model using historical daily demand patterns and time-based features.

**Key activities:**
- Aggregated historical demand at the daily level.
- Created lag-based features using `Lag_1` and `Lag_7`.
- Created a `Rolling_7` feature to capture recent demand patterns.
- Trained and compared forecasting approaches.
- Evaluated prediction errors using MAE, RMSE, and WAPE.
- Analyzed feature importance to understand which variables contributed most to predictions.

**Selected Random Forest Results:**

| Evaluation Metric | Score |
|---|---:|
| MAE | 1.69 |
| RMSE | 2.15 |
| WAPE | 71.77% |

**Important observation:** The forecasting model had limited accuracy, with a WAPE of 71.77%. It should be treated as an exploratory model rather than a reliable production forecasting solution.

**Code Screenshot:**

![Demand Forecasting Code](screenshots/python/05_demand_forecasting.png)

**Forecasting Results:**

![Demand Forecasting Results](screenshots/python/05_forecasting_results.png)

---

###  6. Feature Importance Analysis

Used Random Forest feature importance to examine which engineered features contributed most to the demand forecasting model.

**Top contributing features:**

| Feature | Importance |
|---|---:|
| Rolling_7 | 27.24% |
| Day_of_Month | 26.38% |
| Lag_1 | 15.90% |

**Observation:** Recent rolling demand and calendar-related patterns were among the most influential features in the trained model.

**Code Screenshot:**

![Feature Importance Code](screenshots/python/06_feature_importance.png)

**Feature Importance Results:**

![Feature Importance Results](screenshots/python/06_feature_importance_results.png)

---

###  7. Exported Python Analysis Results

Saved important analytical outputs as CSV files for reuse, reporting, and further project integration.

| Output File | Description |
|---|---|
| `blinkit_customer_segments.csv` | Customer-level cluster assignments |
| `blinkit_customer_segment_report.csv` | Customer segment summaries and revenue contribution |
| `blinkit_demand_feature_importance.csv` | Demand model feature importance |
| `blinkit_ml_model_comparison.csv` | Machine learning evaluation summary |

###  Python Skills Demonstrated

- Python and Jupyter Notebook
- Pandas and NumPy
- MySQL database connectivity
- Data preprocessing and feature engineering
- RFM analysis and customer segmentation
- K-Means clustering
- Classification with Random Forest and other evaluated algorithms
- Demand forecasting
- Model evaluation and comparison
- Silhouette Score, Accuracy, Macro F1, MAE, RMSE, and WAPE
- Feature importance analysis
- CSV-based analytical output generation

**Outcome:** Developed an end-to-end Python analytics and exploratory machine learning workflow covering customer segmentation, delivery prediction, and demand forecasting, with evaluation results and documented model limitations.



##  Machine Learning – Predictive Modeling & Customer Intelligence

Implemented exploratory machine learning solutions to investigate customer behaviour, delivery outcomes, and demand patterns using the prepared Blinkit analytical dataset.

The project explores three machine learning use cases:

###  1. Customer Segmentation – K-Means Clustering

**Objective:** Identify distinct customer groups based on their purchasing behaviour and spending patterns.

**Methodology:**
- Applied RFM (Recency, Frequency, Monetary) analysis.
- Prepared and scaled customer-level features.
- Used the K-Means clustering algorithm.
- Evaluated clustering quality using the Silhouette Score.
- Analyzed segment size, average spending, and revenue contribution.

**Model Configuration & Results:**

| Parameter | Result |
|---|---:|
| Algorithm | K-Means |
| Number of clusters | 4 |
| Customers analyzed | 590 |
| Silhouette Score | 0.4377 |

**Business Insights:**
- Identified four exploratory customer segments.
- Compared customer spending and purchasing frequency.
- Examined revenue contribution across customer groups.
- Generated insights that can support customer targeting and retention strategies.

**Model Screenshot:**

![K-Means Clustering](screenshots/ml/01_customer_segmentation.png)

**Cluster Evaluation & Results:**

![Customer Segmentation Results](screenshots/ml/01_clustering_results.png)

---

###  2. Delivery Outcome Prediction – Classification

**Objective:** Explore whether delivery outcomes can be predicted using available order and operational features.

**Methodology:**
- Prepared relevant numerical and categorical features.
- Applied preprocessing to the input variables.
- Trained and evaluated classification algorithms.
- Compared model performance using Accuracy and Macro F1-score.
- Examined class-wise performance to understand prediction limitations.

**Selected Model:**

| Parameter | Result |
|---|---|
| Algorithm | Random Forest |
| Accuracy | 68.9% |
| Macro F1-score | 27.2% |
| Evaluation | Weak class-wise performance |

**Model Interpretation:**

The model achieved 68.9% accuracy but only 27.2% Macro F1-score. This indicates that the model did not perform consistently across delivery classes, potentially due to class imbalance and limited data.

**Business Relevance:**
- Explores factors associated with delivery outcomes.
- Demonstrates the challenges of predicting operational performance.
- Highlights the importance of class-wise evaluation rather than relying only on accuracy.

**Model Screenshot:**

![Delivery Classification Model](screenshots/ml/02_delivery_prediction.png)

**Model Evaluation:**

![Delivery Model Evaluation](screenshots/ml/02_delivery_results.png)

---

###  3. Demand Forecasting – Regression

**Objective:** Develop an exploratory model to estimate future demand using historical demand patterns and time-based features.

**Methodology:**
- Aggregated demand at the daily level.
- Engineered lag-based features such as `Lag_1` and `Lag_7`.
- Created a rolling seven-day demand feature.
- Trained and evaluated forecasting models.
- Compared predictions using regression error metrics.
- Examined feature importance to understand model behaviour.

**Selected Model:**

| Parameter | Result |
|---|---:|
| Algorithm | Random Forest |
| MAE | 1.69 |
| RMSE | 2.15 |
| WAPE | 71.77% |

**Model Interpretation:**

The model produced a WAPE of 71.77%, indicating limited forecasting accuracy relative to actual demand. The results are exploratory and require further improvement before operational use.

**Business Relevance:**
- Explores historical demand patterns.
- Demonstrates the use of lag and rolling-window features.
- Provides a foundation for further inventory and demand planning experiments.

**Model Screenshot:**

![Demand Forecasting Model](screenshots/ml/03_demand_forecasting.png)

**Forecasting Evaluation:**

![Demand Forecasting Results](screenshots/ml/03_forecasting_results.png)

---

###  Machine Learning Model Comparison

| Use Case | Algorithm | Evaluation Metric | Result |
|---|---|---|---|
| Customer Segmentation | K-Means | Silhouette Score | 0.4377 |
| Delivery Prediction | Random Forest | Accuracy / Macro F1 | 68.9% / 27.2% |
| Demand Forecasting | Random Forest | MAE / RMSE / WAPE | 1.69 / 2.15 / 71.77% |

###  Machine Learning Skills Demonstrated

- Supervised and unsupervised learning
- K-Means clustering
- Random Forest classification and regression
- RFM-based customer segmentation
- Feature engineering and preprocessing
- Numerical and categorical data handling
- Model evaluation and comparison
- Classification metrics and regression error metrics
- Silhouette analysis
- Feature importance interpretation
- Model limitations and performance assessment

###  Model Limitations & Future Improvements

- **Customer Segmentation:** Explore alternative cluster counts and validate segment stability and business usefulness.
- **Delivery Prediction:** Address class imbalance and improve minority-class prediction performance.
- **Demand Forecasting:** Improve forecasting accuracy through additional features, stronger time-series validation, and alternative forecasting approaches.
- **Data Limitations:** Missing calendar dates were treated as zero-demand days, which is an assumption that may influence forecasting performance.

**Overall Outcome:** Built three exploratory machine learning solutions connecting customer intelligence, delivery operations, and demand forecasting. The project emphasizes model evaluation, business interpretation, and honest assessment of predictive limitations rather than relying on model scores alone.
