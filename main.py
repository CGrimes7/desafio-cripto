from ingest import ingest_data
from export_bi import export_to_csv

if __name__ == "__main__":
    ingest_data()
    export_to_csv()
    print("Dados coletados e exportados para Power BI com sucesso.")
