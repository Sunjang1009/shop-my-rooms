pip3 install -r deps.txt

python3 manage.py migrate

python3 manage.py collectstatic --no-input
