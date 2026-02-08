git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/perlov3301/haim251118_python.git
git push -u origin main

$python3.10 -m venv myvenv
$source myvenv/bin/activate
(myvenv)$pip install pip --upgrade
(myvenv)$pip install "fastapi[standard]"
#check python interpretaer is from myvenv
from fastapi import FastAPI
app=FastAPI()
@app.get("/")#root url for GET
def read_root():
  return {"Hello":"World}
(myvenv)$uvicorn main22:app --reload