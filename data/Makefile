1970:
	csvgrep -c year -m 1970 csv/raw.csv > csv/raw_1970.csv
	
	bind-data-to-geojson \
	-d csv/raw_1970.csv \
	--dc gisjoin2 \
	-g shapefiles/US_tract_1970_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_1970.json

	mv noMatches.json noMatches_1970.json

1980:
	csvgrep -c year -m 1980 csv/raw.csv > csv/raw_1980.csv
	
	bind-data-to-geojson \
	-d csv/raw_1980.csv \
	--dc gisjoin2 \
	-g shapefiles/US_tract_1980_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_1980.json

	mv noMatches.json noMatches_1980.json

1990:
	csvgrep -c year -m 1990 csv/raw.csv > csv/raw_1990.csv
	
	bind-data-to-geojson \
	-d csv/raw_1990.csv \
	--dc gisjoin2 \
	-g shapefiles/US_tract_1990_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_1990.json

	mv noMatches.json noMatches_1990.json

2000:
	csvgrep -c year -m 2000 csv/raw.csv > csv/raw_2000.csv
	
	python create_gisjoin_2000.py
	
	bind-data-to-geojson \
	-d csv/raw_2000_modified.csv \
	--dc gisjoin2_mod \
	-g shapefiles/US_tract_2000_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_2000.json

	mv noMatches.json noMatches_2000.json

2009:
	csvgrep -c year -m 2009 csv/raw.csv > csv/raw_2009.csv
	
	# python create_gisjoin_2009.py
	
	bind-data-to-geojson \
	-d csv/raw_2009.csv \
	--dc trnum \
	-g shapefiles/US_tract_2010_ma.json \
	--gc GEOID10 \
	-a false \
	-t csv \
	-o joined_2009.json

	mv noMatches.json noMatches_2009.json