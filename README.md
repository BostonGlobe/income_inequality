# Income inequality

## Steps

* open year shape file
* query builder reduce to State
* save as state shp
* open year data
* convert category value to int `to_int(medcat)`
* join data to shp file (double check in attr table)
* save as esri
* query builder on things with value `"raw_1970_v" > -1`
* save as `joined_reduced`
* delete unecessary attributes