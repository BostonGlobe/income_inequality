1970:
	csvgrep -c year -m 1970 csv/raw.csv > csv/raw_1970.csv

	csvgrep -c metname -m "Boston-Quincy, MA" csv/raw_1970.csv > csv/1970_boston-quincy.csv
	csvgrep -c metname -m "Cambridge-Newton-Framingham, MA" csv/raw_1970.csv > csv/1970_cambridge-newton-framingham.csv
	csvgrep -c metname -m "Essex County, MA" csv/raw_1970.csv > csv/1970_essex-county.csv
	
	# boston quincy
	bind-data-to-geojson \
	-d csv/1970_boston-quincy.csv \
	--dc gisjoin2 \
	-g shapefiles/US_tract_1970_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_1970_boston-quincy.json

	# mv noMatches.json noMatches_1970_boston-quincy.json

	# cambridge newton framingham
	bind-data-to-geojson \
	-d csv/1970_cambridge-newton-framingham.csv \
	--dc gisjoin2 \
	-g shapefiles/US_tract_1970_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_1970_cambridge-newton-framingham.json

	# mv noMatches.json noMatches_1970_cambridge-newton-framingham.json

	# essex county
	bind-data-to-geojson \
	-d csv/1970_essex-county.csv \
	--dc gisjoin2 \
	-g shapefiles/US_tract_1970_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_1970_essex-county.json

	# mv noMatches.json noMatches_1970_essex-county.json

1980:
	csvgrep -c year -m 1980 csv/raw.csv > csv/raw_1980.csv
	
	csvgrep -c metname -m "Boston-Quincy, MA" csv/raw_1980_modified.csv > csv/1980_boston-quincy.csv
	csvgrep -c metname -m "Cambridge-Newton-Framingham, MA" csv/raw_1980_modified.csv > csv/1980_cambridge-newton-framingham.csv
	csvgrep -c metname -m "Essex County, MA" csv/raw_1980_modified.csv > csv/1980_essex-county.csv

	python create_gisjoin_1980.py

	bind-data-to-geojson \
	-d csv/1980_boston-quincy.csv \
	--dc gisjoin_mod \
	-g shapefiles/US_tract_1980_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_1980_boston-quincy.json

	mv noMatches.json noMatches_1980_boston-quincy.json

	bind-data-to-geojson \
	-d csv/1980_cambridge-newton-framingham.csv \
	--dc gisjoin_mod \
	-g shapefiles/US_tract_1980_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_1980_cambridge-newton-framingham.json

	# mv noMatches.json noMatches_1980_cambridge-newton-framingham.json

	bind-data-to-geojson \
	-d csv/1980_essex-county.csv \
	--dc gisjoin_mod \
	-g shapefiles/US_tract_1980_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_1980_essex-county.json

	mv noMatches.json noMatches_1980_essex-county.json

1990:
	csvgrep -c year -m 1990 csv/raw.csv > csv/raw_1990.csv

	python create_gisjoin_1990.py

	csvgrep -c metname -m "Boston-Quincy, MA" csv/raw_1990_modified.csv > csv/1990_boston-quincy.csv
	csvgrep -c metname -m "Cambridge-Newton-Framingham, MA" csv/raw_1990_modified.csv > csv/1990_cambridge-newton-framingham.csv
	csvgrep -c metname -m "Essex County, MA" csv/raw_1990_modified.csv > csv/1990_essex-county.csv
	
	bind-data-to-geojson \
	-d csv/1990_boston-quincy.csv \
	--dc gisjoin_mod \
	-g shapefiles/US_tract_1990_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_1990_boston-quincy.json

	mv noMatches.json noMatches_1990_boston-quincy.json

	bind-data-to-geojson \
	-d csv/1990_cambridge-newton-framingham.csv \
	--dc gisjoin_mod \
	-g shapefiles/US_tract_1990_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_1990_cambridge-newton-framingham.json

	# mv noMatches.json noMatches_1990_cambridge-newton-framingham.json

	bind-data-to-geojson \
	-d csv/1990_essex-county.csv \
	--dc gisjoin_mod \
	-g shapefiles/US_tract_1990_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_1990_essex-county.json

	mv noMatches.json noMatches_1990_essex-county.json

2000:
	csvgrep -c year -m 2000 csv/raw.csv > csv/raw_2000.csv

	python create_gisjoin_2000.py

	csvgrep -c metname -m "Boston-Quincy, MA" csv/raw_2000_modified.csv > csv/2000_boston-quincy.csv
	csvgrep -c metname -m "Cambridge-Newton-Framingham, MA" csv/raw_2000_modified.csv > csv/2000_cambridge-newton-framingham.csv
	csvgrep -c metname -m "Essex County, MA" csv/raw_2000_modified.csv > csv/2000_essex-county.csv
	
	bind-data-to-geojson \
	-d csv/2000_boston-quincy.csv \
	--dc gisjoin2_mod \
	-g shapefiles/US_tract_2000_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_2000_boston-quincy.json

	mv noMatches.json noMatches_2000_boston-quincy.json

	bind-data-to-geojson \
	-d csv/2000_cambridge-newton-framingham.csv \
	--dc gisjoin2_mod \
	-g shapefiles/US_tract_2000_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_2000_cambridge-newton-framingham.json

	# mv noMatches.json noMatches_2000_cambridge-newton-framingham.json

	bind-data-to-geojson \
	-d csv/2000_essex-county.csv \
	--dc gisjoin2_mod \
	-g shapefiles/US_tract_2000_ma.json \
	--gc GISJOIN2 \
	-a false \
	-t csv \
	-o joined_2000_essex-county.json

	mv noMatches.json noMatches_2000_essex-county.json

2009:
	csvgrep -c year -m 2009 csv/raw.csv > csv/raw_2009.csv
	
	csvgrep -c metname -m "Boston-Quincy, MA" csv/raw_2009.csv > csv/2009_boston-quincy.csv
	csvgrep -c metname -m "Cambridge-Newton-Framingham, MA" csv/raw_2009.csv > csv/2009_cambridge-newton-framingham.csv
	csvgrep -c metname -m "Essex County, MA" csv/raw_2009.csv > csv/2009_essex-county.csv

	# python create_gisjoin_2009.py
	
	bind-data-to-geojson \
	-d csv/2009_boston-quincy.csv \
	--dc trnum \
	-g shapefiles/US_tract_2010_ma.json \
	--gc GEOID10 \
	-a false \
	-t csv \
	-o joined_2009_boston-quincy.json

	mv noMatches.json noMatches_2009_boston-quincy.json

	bind-data-to-geojson \
	-d csv/2009_cambridge-newton-framingham.csv \
	--dc trnum \
	-g shapefiles/US_tract_2010_ma.json \
	--gc GEOID10 \
	-a false \
	-t csv \
	-o joined_2009_cambridge-newton-framingham.json

	# mv noMatches.json noMatches_2009_cambridge-newton-framingham.json

	bind-data-to-geojson \
	-d csv/2009_essex-county.csv \
	--dc trnum \
	-g shapefiles/US_tract_2010_ma.json \
	--gc GEOID10 \
	-a false \
	-t csv \
	-o joined_2009_essex-county.json

	mv noMatches.json noMatches_2009_essex-county.json