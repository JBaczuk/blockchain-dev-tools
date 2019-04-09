mv blockchain_fundamentals.py ../lib/python3.7/
cp *.py ../bin
cp -R coins ../lib/python3.7/
echo "export COIN='bitcoin'" >> ../bin/activate
cd ../bin

for file in *.py; do
    mv -- "$file" "${file%%.py}"
done

cd ../../
