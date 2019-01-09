mv blockchain_fundamentals.py ../lib/python3.6
cp *.py ../bin
cp sample.env ../lib/python3.6
cp coins -r ../lib/python3.6
echo "COIN='bitcoin'" >> ../bin/activate
cd ../bin

for file in *.py; do
    mv -- "$file" "${file%%.py}"
done

cd ../../
