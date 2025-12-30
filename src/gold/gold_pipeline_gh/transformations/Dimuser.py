import dlt

expectations= {

    "rule_1" : "user_id is not Null"
}

@dlt.table #Decorator
@dlt.expect_all_or_drop(expectations)
def dimuser_stg1():
    df = spark.readStream.table("spotify_cata.silver.DimUser")
    return df

dlt.create_streaming_table(name="dimuser", expect_all_or_drop = expectations) #creates an empty streaming table

dlt. create_auto_cdc_flow(
target = "dimuser",
source = "dimuser_stg1",
keys = ["user_id"],
sequence_by = "updated_at",
stored_as_scd_type = 2,
track_history_except_column_list = None,
name = None,
once = False
)