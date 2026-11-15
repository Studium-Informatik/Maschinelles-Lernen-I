for i in {01..14}
do
    if [ -f ./orgs/sheet${i}-programming.zip.gpg ]; then
        gpg -d ./orgs/sheet${i}-programming.zip.gpg > ./orgs/sheet${i}.zip
        if [ ! -d sheet${i} ]; then
            unzip ./orgs/sheet${i}.zip -d sheet${i}
        fi
        rm ./orgs/sheet${i}.zip
    fi
done
