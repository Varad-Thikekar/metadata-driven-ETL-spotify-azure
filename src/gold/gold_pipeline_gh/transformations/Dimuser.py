import dlt

@dlt.table #Decorator
def dimuser_stg():
    df = spark.readStream.table("spotify_cata.silver.DimUser")
    return df

# dlt.create_streaming_table(name="dimuser") #creates an empty streaming table