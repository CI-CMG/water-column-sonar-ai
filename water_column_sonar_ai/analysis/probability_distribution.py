# pip install hvplot xarray[complete] s3fs
import random
import numpy as np
import pandas as pd
import xarray as xr
import hvplot.xarray
#from holoviews import opts

bucket_name = 'noaa-wcsd-zarr-pds'
ship_name = "Henry_B._Bigelow"
cruise_name = "HB0707"
sensor_name = "EK60"

zarr_store = f'{cruise_name}.zarr'
s3_zarr_store_path = f"{bucket_name}/level_2/{ship_name}/{cruise_name}/{sensor_name}/{zarr_store}"

cruise = xr.open_dataset(f"s3://{s3_zarr_store_path}", engine='zarr', storage_options={'anon': True}, chunks="auto")
cruise

start_time = "2007-07-12T05:00:00" # more than 10 minutes crashes Colab memory
end_time = "2007-07-12T05:10:00"
timeslice = slice(start_time, end_time)
drop=False

select = cruise.sel(time=timeslice, drop=drop).Sv
select.hvplot.kde('Sv', by='frequency', alpha=0.5, legend='top')

select_masked = cruise.where(cruise.depth < cruise.bottom).sel(time=timeslice, drop=drop).Sv
select_masked.hvplot.kde('Sv', by='frequency', alpha=0.5, legend='top')

# average depth over the interval
np.nanmean(cruise.sel(time=timeslice, drop=drop).bottom.values)

select_masked2 = cruise.where(cruise.depth < cruise.bottom).where(cruise.depth > 5, drop=True).sel(time=timeslice, drop=drop).Sv
select_masked2.hvplot.kde('Sv', by='frequency', alpha=0.5, legend='top')

select_masked2.sel(frequency=18_000).hvplot.hist("Sv", bins=100)

select_masked2.hvplot.hist("Sv", by="frequency", subplots=True, bins=100, width=400, height=300).cols(2)