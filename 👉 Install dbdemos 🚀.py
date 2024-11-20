# Databricks notebook source
# MAGIC %pip install dbdemos

# COMMAND ----------

dbutils.library.restartPython() 

# COMMAND ----------

import dbdemos
dbdemos.install('uc-04-system-tables')
