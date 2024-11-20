# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://github.com/mousastech/dbdemos/blob/4824e1cd8e6896aff9a7fac133ef824340171e7d/files/dbdemos_en.png?raw=true">

# COMMAND ----------

# DBTITLE 1,Install library
# MAGIC %pip install dbdemos
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

# DBTITLE 1,Know available demos
import dbdemos
dbdemos.list_demos()

# COMMAND ----------

# DBTITLE 1,Example - Install System tables
import dbdemos
dbdemos.install('uc-04-system-tables')

# COMMAND ----------

# DBTITLE 1,Example - AI/BI Dashaboards
dbdemos.install('aibi-sales-pipeline-review')

# COMMAND ----------

# MAGIC %md
# MAGIC #Databricks Express trial
# MAGIC If you are using the trial version, don't forget to add the cluster parameter `warehouse_name = 'Serverless Starter Warehouse')`
# MAGIC
# MAGIC This way:
# MAGIC `dbdemos.install('aibi-sales-pipeline-review', catalog='main'. schema='default', warehouse_name = 'Serverless Starter Warehouse')`

# COMMAND ----------

dbdemos.install('aibi-sales-pipeline-review', catalog='main', schema='default', warehouse_name = 'Serverless Starter Warehouse')
