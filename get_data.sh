#!/usr/bin/zsh
# use /usr/bin/sh for bash shell
kaggle datasets download gauravduttakiit/smoker-status-prediction --force 
unzip -d ./data smoker-status-prediction.zip 
mv *.csv ./data 
rm smoker-status-prediction.zip 
echo "Data Download Done"
