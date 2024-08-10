import pandas as pd
import logging
from openpyxl import load_workbook

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.INFO)

#read csv file in a datafame
df = pd.read_csv('APP-ID-all.csv')

#Removing one unnamed column
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

#print(df.head())
#defining all the clusters
cluster_names = ['451Research-EKS-DEV', '451Research-EKS-Stage', 'MICAPIQ-EKS-DEV', 'MICIS-CONTENT-DEV', 'MIDVACIS-EKS-DEV', 'MIDVACIS-EKS-PROD', 'MIDVACIS-EKS-QA', 'MIGeneral-EKSCluster-DEV', 'MIGeneral-EKSCluster-PRD', 'MIGeneral-EKSCluster-STG', 'MIInternal-EKSCluster-DEV', 'MIInternal-EKSCluster-PRD', 'MIInternal-EKSCluster-STG', 'MIInternal-EKSGlobal-DEV', 'MIInternal-EKSGlobal-PRD', 'MIInternal-EKSGlobal-QA', 'MIInternal-EKSGlobal-STG', 'MIMP-EKSCluster-DEV', 'MIMP-EKSCluster-PRD', 'MIMP-EKSCluster-QA', 'MIMP-EKSCluster-STG', 'MIPlatform-EKSCluster-DEV', 'MIPlatform-EKSCluster-PRD', 'MIPlatform-EKSCluster-STG', 'MITC-EKSCluster-GLOBAL', 'MIINT-EKS-PILOT']

#defining the dev clusters
cluster_dev = ['451Research-EKS-DEV', 'MICAPIQ-EKS-DEV', 'MICIS-CONTENT-DEV', 'MIDVACIS-EKS-DEV', 'MIGeneral-EKSCluster-DEV', 'MIInternal-EKSCluster-DEV', 'MIInternal-EKSGlobal-DEV', 'MIMP-EKSCluster-DEV', 'MIPlatform-EKSCluster-DEV', 'MIINT-EKS-PILOT']

#defining the qa clusters
cluster_qa = ['MIDVACIS-EKS-QA', 'MIInternal-EKSGlobal-QA', 'MIMP-EKSCluster-QA']

#defining the stage clusters
cluster_stg = ['451Research-EKS-Stage', 'MIGeneral-EKSCluster-STG', 'MIInternal-EKSCluster-STG', 'MIInternal-EKSGlobal-STG', 'MIMP-EKSCluster-STG', 'MIPlatform-EKSCluster-STG']

#defining the prod clusters
cluster_prd = ['MIDVACIS-EKS-PROD', 'MIGeneral-EKSCluster-PRD', 'MIInternal-EKSCluster-PRD', 'MIInternal-EKSGlobal-PRD', 'MIMP-EKSCluster-PRD', 'MIPlatform-EKSCluster-PRD', 'MITC-EKSCluster-GLOBAL']

# seggragating all cluster in different dataframes
for cluster in cluster_names:
    try:
        # selecting rows based on condition
        name_df = (f"{cluster}_df")
        name_df = df[df['container_cluster_name'] == cluster]

        #naming each pivot differently
        #pivot = (f"{cluster}")
        #print(pivot)
        cluster = name_df.pivot_table(index=['k8\'s_appid'],
                       columns=['date'],
                       values=['unblended_cost'],
                       aggfunc='sum',
                       margins=True,
                       margins_name="Total")
    except Exception as e:
        print("Skipping due to error",e)
        logging.error(f"{e}")


for cluster in cluster_dev:
    with pd.ExcelWriter('dev.xlsx') as writer_dev:
        try:
            #sheet=(f"{cluster}_pivot")
            #print(sheet)
            # writing to the cluster sheet
            cluster.to_excel(writer_dev, sheet_name=cluster)
    
            logging.info(f'DataFrames are written to Excel File {cluster} successfully.')
        except Exception as e:
            print("Skipping due to error",e)
            logging.error(f"{e}")

for cluster in cluster_qa:
    with pd.ExcelWriter('qa.xlsx') as writer_qa:
        try:
            sheet=(f"{cluster}_pivot")
            # writing to the cluster sheet
            sheet.to_excel(writer_qa, sheet_name=cluster)
            logging.info(f'DataFrames are written to Excel File {cluster} successfully.')
        except Exception as e:
            print("Skipping due to error",e)
            logging.error(f"{e}")

for cluster in cluster_stg:
    with pd.ExcelWriter('stage.xlsx') as writer_stg:
        try:
            sheet=(f"{cluster}_pivot")
            # writing to the cluster sheet
            sheet.to_excel(writer_stg, sheet_name=cluster)
            logging.info(f'DataFrames are written to Excel File {cluster} successfully.')
        except Exception as e:
            print("Skipping due to error",e)
            logging.error(f"{e}")

for cluster in cluster_prd:
    with pd.ExcelWriter('prod.xlsx') as writer_prd:
        try:
            sheet=(f"{cluster}_pivot")
            # writing to the cluster sheet
            sheet.to_excel(writer_prd, sheet_name=cluster)
            logging.info(f'DataFrames are written to Excel File {cluster} successfully.')
        except Exception as e:
            print("Skipping due to error",e)
            logging.error(f"{e}")

#print("File read successfully")
logging.info("All files created successfully")