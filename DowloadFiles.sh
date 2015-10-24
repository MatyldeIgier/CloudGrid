ACTUL_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

mkdir Programme
cd Programme

echo "Download"
echo ""

#Download le tout
curl -L https://rawgit.com/MatyldeIgier/CloudGrid/master/clustering.py > clustering.py
curl -L https://rawgit.com/MatyldeIgier/CloudGrid/master/data.csv > data.csv
curl -L https://rawgit.com/MatyldeIgier/CloudGrid/master/main.py > main.py
curl -L https://rawgit.com/MatyldeIgier/CloudGrid/master/point.py > point.py

echo "Wait"
echo ""

sleep 1

#Run main.py
python main.py > results.csv
cd ..
mv Programme/results.csv "${ACTUL_DIR}"
sleep 1
rm -r Programme

echo "Sucess!"