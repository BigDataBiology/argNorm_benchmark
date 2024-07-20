# ResFinder Data
wget https://bitbucket.org/genomicepidemiology/resfinder_db/raw/e92560efcdcdf7aee0abc56e991f0a1132890273/phenotypes.txt
mv phenotypes.txt data/resfinder_antibiotic_classes.tsv

# SARG Data
wget https://smile.hku.hk/ARGs/dataset/indexingdownload/Short_subdatabase_V3.2.1.zip
unzip ./Short_subdatabase_V3.2.1.zip
rm -rf __MACOSX
rm -rf Short_subdatabase_V3.2.1.zip
mv Short_subdatabase/4.SARG_v3.2_20220917_Short_subdatabase_structure.txt data/SARG_structure.tsv
rm -rf Short_subdatabase

# ResFinderFG data
wget https://raw.githubusercontent.com/RemiGSC/ResFinder_FG_Construction/main/output/merged_data/o_merge.csv
mv o_merge.csv ./data/resfinderfg_antibiotic_classes.csv