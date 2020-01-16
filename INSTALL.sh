cp blockchain_fundamentals.py ../lib/python3.6/
cp *.py ../bin
cp coins/*.py ../bin

echo "export COIN='bitcoin'" >> ../bin/activate
cd ../bin

for file in *.py; do
    cp -- "$file" "${file%%.py}"
done

cd ../../
