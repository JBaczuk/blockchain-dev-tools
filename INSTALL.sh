cp blockchain_fundamentals.py ../lib/python3.6/
cp *.py ../bin
cp -R coins ../lib/python3.6/
echo "export COIN='bitcoin'" >> ../bin/activate
cd ../bin

for file in *.py; do
    cp -- "$file" "${file%%.py}"
done

cd ../../
