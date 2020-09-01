from azure.kusto.data.request import KustoClient, KustoConnectionStringBuilder
from azure.kusto.ingest import (KustoIngestClient,IngestionProperties,FileDescriptor,DataFormat,ReportLevel)

def authenticate_kusto(kusto_cluster):
    tenant_id = '72f988bf-86f1-41af-91ab-2d7cd011db47'
    KCSB = KustoConnectionStringBuilder.with_aad_device_authentication(kusto_cluster)
    KCSB.authority_id = tenant_id
    return KustoClient(KCSB),KCSB

# Query Kusto
cga_cluster = 'https://cgadataout.kusto.windows.net'
ingest_cluster = "https://ingest-cgadataout.kusto.windows.net"
cga_client = authenticate_kusto(cga_cluster)[0]
ingest_client = KustoIngestClient(authenticate_kusto(ingest_cluster)[1])
ls=[cga_client,ingest_client]

def Ingest(Tag):
    ingestion_props = IngestionProperties(
        database="DevRelWorkArea",
        table="ContributorCommits",
        dataFormat=DataFormat.CSV,
        ingestByTags=[Tag],
        dropByTags=[Tag],
        mappingReference="ContributorCommits_CSV_Mapping",
        reportLevel=ReportLevel.FailuresAndSuccesses,
        additionalProperties={'ignoreFirstRecord': 'true'}
    )

    file_descriptor = FileDescriptor(r"D:\test\merge.csv",3333)  # 3333 is the raw size of the data in bytes.
    ls[1].ingest_from_file(file_descriptor, ingestion_properties=ingestion_props)

    return 1

DROP_TABLE_IF_EXIST = """.drop extents <| .show table ContributorCommits extents where tags has 'drop-by:{}'""".format(StartTime)
RESPONSE = ls[0].execute_mgmt("DevRelWorkArea", DROP_TABLE_IF_EXIST)

Ingest("2020-07-01")