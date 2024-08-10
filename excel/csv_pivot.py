import pandas as pd
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.INFO)

#read csv file in a datafame
df = pd.read_csv('course-sample-file.csv')
#print(df.head())
#Removing one unnamed column
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
#print(df.head())

#defining all the Owners
Transaction_Owner = ['Owner-A1', 'Owner-A2', 'Owner-A3', 'Owner-A4', 'Owner-A5', 'Owner-B1', 'Owner-B2', 'Owner-B3', 'Owner-C1', 'Owner-C2', 'Owner-C3', 'Owner-C4', 'Owner-C5', 'Owner-C6', 'Owner-D1', 'Owner-D2', 'Owner-D3', 'Owner-D4', 'Owner-D5', 'Owner-D6', 'Owner-D7', 'Owner-E1', 'Owner-E2', 'Owner-E3', 'Owner-E4', 'Owner-E5', 'Owner-E6', 'Owner-E7', 'Owner-F1', 'Owner-F2', 'Owner-F3', 'Owner-F4', 'Owner-F5', 'Owner-F6']

#defining the A Owners
Owner_A = ['Owner-A1', 'Owner-A2', 'Owner-A3', 'Owner-A4', 'Owner-A5']

#defining the B Owners
Owner_B = ['Owner-B1', 'Owner-B2', 'Owner-B3']

#defining the C Owner
Owner_C = ['Owner-C1', 'Owner-C2', 'Owner-C3', 'Owner-C4', 'Owner-C5', 'Owner-C6']

#defining the D Owners
Owner_D = ['Owner-D1', 'Owner-D2', 'Owner-D3', 'Owner-D4', 'Owner-D5', 'Owner-D6', 'Owner-D7']

#defining the E Owners
Owner_E = ['Owner-E1', 'Owner-E2', 'Owner-E3', 'Owner-E4', 'Owner-E5', 'Owner-E6', 'Owner-E7']

#defining the F Owners
Owner_F = ['Owner-F1', 'Owner-F2', 'Owner-F3', 'Owner-F4', 'Owner-F5', 'Owner-F6']

# seggragating all owner in different dataframes
for owner in Transaction_Owner:
    try:
        # selecting rows based on condition
        name_df = (f"{owner}_df")
        name_df = df[df['Transaction_Owner'] == owner]
        print(name_df.head())
        #naming each pivot differently
        pivot = (f"{owner}_pivot")
        print(pivot)
        pivot = name_df.pivot_table(index=['Transaction_ID'],
                       columns=['Date'],
                       values=['Cost_Per_Day'],
                       aggfunc='sum',
                       margins=True,
                       margins_name="Total")
        print("pivot done")    
        if owner in Owner_A:
            with pd.ExcelWriter('./result/a.xlsx', mode='a', engine="openpyxl", if_sheet_exists="replace") as writer_a:
            # writing to the owner sheet
                pivot.to_excel(writer_a, sheet_name=owner, index=True)
            logging.info(f'DataFrames are written to Excel File {owner} successfully.')
        elif owner in Owner_B:
            with pd.ExcelWriter('./result/b.xlsx', mode='a', engine="openpyxl", if_sheet_exists="replace") as writer_b:
            # writing to the owner sheet
                pivot.to_excel(writer_b, sheet_name=owner, index=True)
            logging.info(f'DataFrames are written to Excel File {owner} successfully.')
        elif owner in Owner_C:
            with pd.ExcelWriter('./result/c.xlsx', mode='a', engine="openpyxl", if_sheet_exists="replace") as writer_c:
            # writing to the owner sheet
                pivot.to_excel(writer_c, sheet_name=owner, index=True)
            logging.info(f'DataFrames are written to Excel File {owner} successfully.')
        elif owner in Owner_D:
            with pd.ExcelWriter('./result/d.xlsx', mode='a', engine="openpyxl", if_sheet_exists="replace") as writer_d:
            # writing to the owner sheet
                pivot.to_excel(writer_d, sheet_name=owner, index=True)
            logging.info(f'DataFrames are written to Excel File {owner} successfully.')
        elif owner in Owner_E:
            with pd.ExcelWriter('./result/e.xlsx', mode='a', engine="openpyxl", if_sheet_exists="replace") as writer_e:
            # writing to the owner sheet
                pivot.to_excel(writer_e, sheet_name=owner, index=True)
            logging.info(f'DataFrames are written to Excel File {owner} successfully.')
        elif owner in Owner_F:
            with pd.ExcelWriter('./result/f.xlsx', mode='a', engine="openpyxl", if_sheet_exists="replace") as writer_f:
            # writing to the owner sheet
                pivot.to_excel(writer_f, sheet_name=owner, index=True)
            logging.info(f'DataFrames are written to Excel File {owner} successfully.')
    except Exception as e:
        print("Skipping due to error",e)
        logging.error(f"{e}")

#print("File read successfully")
logging.info("All files created successfully")