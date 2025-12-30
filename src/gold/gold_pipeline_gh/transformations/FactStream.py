import dlt

@dlt.table #Decorator
def factstream_stg1():
    df = spark.readStream.table("spotify_cata.silver.FactStream")
    return df

dlt.create_streaming_table(name="factstream") #creates an empty streaming table

dlt. create_auto_cdc_flow(
target = "factstream",
source = "factstream_stg1",
keys = ["stream_id"],
sequence_by = "stream_timestamp",
stored_as_scd_type = 1,
track_history_except_column_list = None,
name = None,
once = False
)