all:
	csvgrep -c year -m 1970 csv/raw.csv > csv/raw_1970.csv
	
	bind-data-to-geojson \
	-d csv/raw_1970.csv \
	--dc gisjoin2 \
	-g shapefiles/US_tract_1970_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_1970.json
